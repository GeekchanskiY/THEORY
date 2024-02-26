
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