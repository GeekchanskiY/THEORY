
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