### Generation functions
```go
func Float32() float32
func Float64() float64
func Int() int
func Int31() int32 
func Int63() int64
func Uint32() uint32
func Uint64() uint64
```
Generates preudo-random values for provided types. `Int31` and `Int64` are called so because they generate 31 and 63 bit integers, represented as `int32` and `int64`.

```go
func Intn(n int) int
func Int31n(n int32) int32
func Int63n(n int64) int64
```
`IntXn` returns, as an `intX`, a non-negative pseudo-random number in the half-open interval (0,n) from the default source. Panics if n < 0.

