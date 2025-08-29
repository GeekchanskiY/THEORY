

```go
package main

import (
    "fmt"
    "reflect"
)

type User struct {
    Username string `ankit:"required,min=5,max=20"`
    Email    string `ankit:"required,email"`
    Test     string
}

func main() {
    user := User{
        Username: "john_doe",
        Email:    "john.doe@example.com",
        Test:     "test value",
    }

    validateStruct(user)
}

func validateStruct(data interface{}) {
    val := reflect.ValueOf(data)
    for i := 0; i < val.NumField(); i++ {
        tag := val.Type().Field(i).Tag.Get("ankit")
        fmt.Printf("Field: %s, Tag: %s\n", val.Type().Field(i).Name, tag)
        // Implement your validation logic here based on the tag value.
    }
}
```