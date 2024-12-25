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

**You can't use `:=` outside of `funcs`. It's because, outside a func, a statement should start with a keyword.**

**You can use `:=` for multi-variable declarations and assignments**

**You can use them twice in "multi-variable" declarations, _if one of the variables is new_:**

```go
foo, bar  := someFunc()
foo, jazz := someFunc()  // <-- jazz is new
baz, foo  := someFunc()  // <-- baz is new
```

**You can use the short declaration to declare a variable in a newer scope even if that variable is already declared with the same name before**
```go
var foo int = 34

func some() {
  // because foo here is scoped to some func
  foo := 42  // <-- legal
  foo = 314  // <-- legal
}
```

**You can declare the same name in short statement blocks like: if, for, switch 


## Pointers
Go has pointers. A pointer holds the memory address of a value.

The type `*T` is a pointer to a `T` value. Its zero value is `nil`.
```go
var p *int
```

The `&` operator generates a pointer to its operand.

```go
i := 42
p = &i
```

The `*` operator denotes the pointer's underlying value.
```go
fmt.Println(*p) // read i through the pointer p
*p = 21         // set i through the pointer p
```
This is known as "dereferencing" or "indirecting".

Unlike C, Go has no pointer arithmetic.

[[Go slices]]