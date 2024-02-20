Go has several built-in data types, including:

- Basic types: bool, int, float64, complex128, string
- Aggregate types: array, slice, struct
- Reference types: pointer, channel, map, interface

```go
var b bool = true
var i int = 42
var f float64 = 3.14
var c complex128 = 1 + 2i
var s string = "hello"

var arr [3]int = [3]int{1, 2, 3}
var sl []int = []int{1, 2, 3}
var st struct { x int; y int } = struct { x int; y int }{1, 2}

var p *int = &i
var ch chan int = make(chan int)
var m map[string]int = make(map[string]int)
var iface interface{} = "text"
```

 := is declaration and assignment
 = is assignment
