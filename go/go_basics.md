### Functions

All cases of go functions here:
```go
func name(args) return_type {
	return args
}

// multiple return values
func swap(x, y string) (string, string) {
	return y, x
}

// Named return values
func split(sum int) (x, y int) {
	x = sum * 4 / 9
	y = sum - x
	return
}

```

### Logic

if statement
```go
if err != nil {
	return err
}

// Scope of 'area' is inside of if statement
if area := math.Pow(x, n); area > limit {
	return errors.New("area is too big")
}
```

for-loop
```go
for i := 0; i < 10; i++ {
	sum += i
}

// init and post statements are optional
sum := 1
for ; sum < 1000; {
	sum += sum
}
// same as
for sum < 1000 {
	sum += sum
}

// Range returns iter num and value from iterable
var pow = []int{1, 2, 4, 8, 16, 32, 64, 128}
for i, v := range pow {
	fmt.Printf("2**%d = %d\n", i, v)
}
```

Switch-case example
```go
// Just a nice example, really like this use-case
package main

import (
	"fmt"
	"runtime"
)

func main() {
	fmt.Print("Go runs on ")
	switch os := runtime.GOOS; os {
	case "darwin":
		fmt.Println("OS X.")
	case "linux":
		fmt.Println("Linux.")
	default:
		// freebsd, openbsd,
		// plan9, windows...
		fmt.Printf("%s.\n", os)
	}
}

```

### defer statement
A defer statement defers the execution of a function until the surrounding function returns.
**Note: defers are stacked**

```go
func main() {
  defer fmt.Println(1)
  defer fmt.Println(2)
  defer fmt.Println(3)
}

// Output:
// 3
// 2
// 1
```

