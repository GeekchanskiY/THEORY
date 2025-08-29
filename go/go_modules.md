A module is a collection of Go packages stored in a file tree with a `go.mod` file at its root. The `go.mod` file defines the module’s `module path`, which is also the import path used for the root directory, and its `dependency requirements`, which are the other modules needed for a successful build. Each dependency requirement is written as a module path and a specific semantic version.

## Creating a new module

To create a new module you could use cli command:
```bash
go mod init example.com/hello
```

## Go mod
structure of a go.mod
```go.mod
module github.com/GeekchanskiY/THEORY // module name
go 1.23.1 // go version
require (
	"package"
)

require (
	"dependency"
)
```

# Links
[[go_CLI]]
[[go_packages]]