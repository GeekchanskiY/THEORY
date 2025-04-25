Cli tools can be written in go with high effectivity.
For writing cli tools we can use [cobra](https://github.com/spf13/cobra ) library, or do everything with the standard library

To get args, we can use `os` package and `os.Args`  to get raw command-line arguments (type = `slice`). First argument is a path to the executable, as always.

To get flags there is a `flag` package

Example: 
```go
var wordPtr = flag.String("word", "foo", "a string")

func main() {
	flag.Parse()
	fmt.Println(*wordPtr)
}
```

Running go run main.