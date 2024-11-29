
### Functions

All cases of go functions here:
```go
func name(args) return_type {
	return args
}

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
if v.Method == "get" {
	res, err = http.Get(v.Adress)
	if err != nil {
	fmt.Printf("error making http request: %s\n", err)
	} else {}
}

// Scope of 'v' is inside of if statement
if v := math.Pow(x, n); v < lim {
	return v
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

// While analog
for sum < 1000 {
	sum += sum
}

// Forever
for sum < 1000 {
	sum += sum
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

### Structures

additionally, there is a Tag feature. Read more: [[Go tags]]

#[ 

#[Go tags]]