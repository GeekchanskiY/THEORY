
https://pkg.go.dev/sync

Sync package is about working with goroutines. It allows us to create mutex (default and rwmutes), wait groups,  etc. From the original description: "provides basic synchronization primitives such as mutual exclusion locks. Other than the Once and WaitGroup types, most are intended for use by low-level library routines. Higher-level synchronization is better done via channels and communication."

### OnceFunc

```go
func OnceFunc(f func()) func()

// OnceFunc returns a function that invokes f only once. The returned function may be called concurrently.

// If f panics, the returned function will panic with the same value on every call.
```

### OnceValue

func OnceValue

OnceValue returns a function that invokes f only once and returns the value returned by f. The returned function may be called concurrently.

If f panics, the returned function will panic with the same value on every call.

### [[Go WaitGroup]]