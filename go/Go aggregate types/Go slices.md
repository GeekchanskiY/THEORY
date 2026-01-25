
```go
package main

import "fmt"

func foo(src []int) {
	src = append(src, 5)
}

func main(){
	arr := []int{1, 2, 3}
	src := arr[:1] // pointer to 1st element of arr. it's data type is slice
	
	foo(src)
	
	fmt.Println(src)
	fmt.Println(arr)
}

// result:
// 1
// 1, 5, 3

// to avoid editing arr you can make() a new slice, and create a copy

```