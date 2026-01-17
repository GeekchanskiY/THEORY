### `new(T)` vs `&T{}`
Their behavior is almost same, despite the fact that `new` will automatically put variable into heap, and `&T{}` have a chance to leave in stack. That leads to 2 facts: new is faster for runtime, it does not need to move variable into different scopes, but &T may be a bit faster for gc and be deleted with scope of it's creation.

### Chan initialization
It's not a invalid chan usage, but a deadlock of all goroutines
```go
func test(x chan int) {
	_, ok := <-x
	fmt.Println(ok)
}

func main() {
	var x chan int
	go test(x)
	x = make(chan int, 1)
	x <- 3

	z := make(chan int)
	z <- 1
	<-z

}
```

