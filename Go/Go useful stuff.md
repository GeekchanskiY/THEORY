
### Defer statement
A defer statement defers the execution of a function until the surrounding function returns.


### Naming conventions

*Very important here*
```go
func writeToDB(){} // unexported, only visible within the 
func packageWriteToDB() {} // exported, visible within the package
```

**All functions should be named in camel case, but only functions starting with uppercase will be exported!**

### Errors
error creation can be achieved with package `errors`

To define a custom error type, you must satisfy the predeclared error interface
```go
type error interface {
	Error() string
}
```

Example of custom error with additional data inside:
```go
type SyntaxError struct {
	Line int
	Col  int
}

func (e *SyntaxError) Error() string {
	return fmt.Sprintf("%d:%d: syntax error", e.Line, e.Col)
}
```
### File I/O
https://www.honeybadger.io/blog/comprehensive-guide-to-file-operations-in-go/
