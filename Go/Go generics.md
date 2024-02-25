
After 1.18 release go has generics


```go
type Unsigned interface (
	uint8 | uint16 | uint32 | uint64
)

func testFunc[T int32 | int64, V Unsigned] (t T, v V) (T, V){
 // Code here...
}
```