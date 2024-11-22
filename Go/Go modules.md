# Description

A module is a collection of [Go packages](https://go.dev/ref/spec#Packages) stored in a file tree with a `go.mod` file at its root. The `go.mod` file defines the module’s _module path_, which is also the import path used for the root directory, and its _dependency requirements_, which are the other modules needed for a successful build. Each dependency requirement is written as a module path and a specific [semantic version](http://semver.org/).

# Article
## Creating a new module

To create a new module you could use cli command:
```bash
go mod init example.com/hello
```

## 

# Article

# Links
[[Go packages]]