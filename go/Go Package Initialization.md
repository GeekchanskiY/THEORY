Order of initialization: var -> init -> main
```go
var x = func(){
	println("var")
	
	return 1
}()

func init(){
	println("init")
}

func main(){
	println("main")
}
// stdout:
// var
// init
// main
```

If package A requires package B, and both of them have `init` functions - then first will be executed function that has no dependencies (A -> B).

Multiple `init` functions may be defined per package, even within a single source file. In the package block, the init identifier can be used only to declare init functions, yet the identifier itself is not declared. Thus init functions cannot be referred to from anywhere in a program. Order of calling these functions will be alphabetical:  a.go will be executed first, b.go will be executed second, etc.