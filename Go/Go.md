Go is an open source programming language that makes it simple to build secure, scalable systems. Designed at Google by Robert Griesemer, Rob Pike, and Ken Thompson. It is syntactically similar to C, but also has memory safety, garbage collection, structural typing, and CSP-style concurrency

Most popular frameworks:
[[GIN]]
[[Gorm]]

### Hints and reminders
When your code imports packages contained in other modules, you manage those dependencies through your code's own module. That module is defined by a go.mod file that tracks the modules that provide those packages. That go.mod file stays with your code, including in your source code repository.


### Project structure
https://github.com/golang-standards/project-layout

```
- app
	- bin // binaries
	- cmd // main.go usually, entrypoints
	- pkg // package
	- internal // package that cant be imported from other packages
```

# Links

[[go packages]]
[[Go community packages]]

[[Go standard library]]

[[Go Asynchronous programming]]

[[Go variables and data types]]

[[Go basics]]

[[Go useful stuff]]

[[Go generics]]

[[Go garbage collector]]

[[Go CLI]]

[[Go mod and go work]]

[[Go errors]]