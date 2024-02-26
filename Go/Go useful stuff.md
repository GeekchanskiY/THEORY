
### Defer statement
A defer statement defers the execution of a function until the surrounding function returns.


### Naming conventions

*Very important here*
```go
func writeToDB(){} // unexported, only visible within the 
func packageWriteToDB() {} // exported, visible within the package
```

**All functions should be named in camel case, but only functions starting with uppercase will be exported!**


### File I/O
https://www.honeybadger.io/blog/comprehensive-guide-to-file-operations-in-go/
