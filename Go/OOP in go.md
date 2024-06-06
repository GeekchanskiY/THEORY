
Go has a naming convention, that a lowercase is private visibility, and uppercase is public

```go
type Message struct {
	Data      []byte
	MimeType  string
	Timestamp time.Time
}

type TwitterSource struct {
    Username string
}

type SkypeSource struct {
	Login         string
	MSBackdoorKey string
}
```

Interfaces:
```go
type Finder interface {
    Find(word string) ([]Message, error)
}
```

Go does not support traditional inheritance, but it uses composition instead

### Type aliases
`type A = string` creates an alias for `string`. Whenever you use `A` in your code, it works just like `string`. So for example, you can't define methods on it.

```go
type Hint string
```