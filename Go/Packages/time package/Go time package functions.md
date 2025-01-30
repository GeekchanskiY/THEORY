### Sleep
```go
func Sleep(d Duration)
```
`Sleep` pauses the current goroutine for at least the duration d. A negative or zero duration causes `Sleep` to return immediately.

#### Tick
```go
func Tick(d Duration) <-chan Time
```

Tick is a convenience wrapper for `NewTicker` providing access to the ticking channel only. Unlike `NewTicker`, `Tick` will return nil if d <= 0.

### After
```go
func After(d Duration) <- chan Time
```
After waits for the duration to elapse and then sends the current time on the returned channel. Equals to `NewTimer(d).C`