https://redis.io/docs/management/persistence/
Persistence refers to the writing of data to durable storage, such as a solid-state disk (SSD). Redis provides a range of persistence options. These include:

- **RDB** (Redis Database): RDB persistence performs point-in-time snapshots of your dataset at specified intervals.
- **AOF** (Append Only File): AOF persistence logs every write operation received by the server. These operations can then be replayed again at server startup, reconstructing the original dataset. Commands are logged using the same format as the Redis protocol itself.
- **No persistence**: You can disable persistence completely. This is sometimes used when caching.
- **RDB + AOF**: You can also combine both AOF and RDB in the same instance.


## Snapshotting

By default Redis saves snapshots of the dataset on disk, in a binary file called `dump.rdb`. You can configure Redis to have it save the dataset every N seconds if there are at least M changes in the dataset, or you can manually call the [`SAVE`](https://redis.io/commands/save) or [`BGSAVE`](https://redis.io/commands/bgsave) commands.

For example, this configuration will make Redis automatically dump the dataset to disk every 60 seconds if at least 1000 keys changed:

```redis cli
save 60 1000
```

### How it works

Whenever Redis needs to dump the dataset to disk, this is what happens:

- Redis [forks](http://linux.die.net/man/2/fork). We now have a child and a parent process.
- The child starts to write the dataset to a temporary RDB file.
- When the child is done writing the new RDB file, it replaces the old one.

This method allows Redis to benefit from copy-on-write semantics.

## Append-only file

Snapshotting is not very durable. If your computer running Redis stops, your power line fails, or you accidentally `kill -9` your instance, the latest data written to Redis will be lost. While this may not be a big deal for some applications, there are use cases for full durability, and in these cases Redis snapshotting alone is not a viable option.

The _append-only file_ is an alternative, fully-durable strategy for Redis. It became available in version 1.1.

You can turn on the AOF in your configuration file:

```
appendonly yes
```

From now on, every time Redis receives a command that changes the dataset (e.g. [`SET`](https://redis.io/commands/set)) it will append it to the AOF. When you restart Redis it will re-play the AOF to rebuild the state.

### How durable is the append only file?

You can configure how many times Redis will [`fsync`](http://linux.die.net/man/2/fsync) data on disk. There are three options:

- `appendfsync always`: `fsync` every time new commands are appended to the AOF. Very very slow, very safe. Note that the commands are appended to the AOF after a batch of commands from multiple clients or a pipeline are executed, so it means a single write and a single fsync (before sending the replies).
- `appendfsync everysec`: `fsync` every second. Fast enough (since version 2.4 likely to be as fast as snapshotting), and you may lose 1 second of data if there is a disaster.
- `appendfsync no`: Never `fsync`, just put your data in the hands of the Operating System. The faster and less safe method. Normally Linux will flush data every 30 seconds with this configuration, but it's up to the kernel's exact tuning.

The suggested (and default) policy is to `fsync` every second. It is both fast and relatively safe. The `always` policy is very slow in practice, but it supports group commit, so if there are multiple parallel writes Redis will try to perform a single `fsync` operation