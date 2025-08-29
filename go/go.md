Go is an open source programming language that makes it simple to build secure, scalable systems. Designed at Google by Robert Griesemer, Rob Pike, and Ken Thompson. It is syntactically similar to C, but also has memory safety, garbage collection, structural typing, and CSP-style concurrency
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

[[go_packages]]
[[go_community_packages]]

[[go_standard_library]]

[[go_asynchronous_programming]]

[[go_variables_and_data_types]]

[[go_basics]]
[[go_tags]]

[[go_useful_stuff]]

[[go_generics]]

[[go_garbage_collector]]

[[go_CLI]]

[[go_mod and go_work]]

[[go_errors]]