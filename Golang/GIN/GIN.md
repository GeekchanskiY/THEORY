Gin is a web framework written in Go (Golang). It features a martini-like API with much better performance, up to 40 times faster thanks to [httprouter](https://github.com/julienschmidt/httprouter). If you need performance and good productivity, you will love Gin.

#### Advantages:
Fast by radix tree based routing & small memo foot print
Middleware support
Crash-free, and availability to report 'panic' to sentry
Json validation
Routes grouping
Error management
Rendering built-in
Extendable


### Quickstart

Hello world app with a logging middleware
```go
package main

import (
	"github.com/gin-gonic/gin"
	"log"
	"time"
)

func LoggerMiddleware() gin.HandlerFunc {
	return func(c *gin.Context) {
		start := time.Now()
		c.Next()
		duration := time.Since(start)
		log.Printf("Request - Method: %s | Status: %d | Duration: %v", c.Request.Method, c.Writer.Status(), duration)
	}
}

func main() {
	router := gin.Default()

	// Use our custom logger middleware
	router.Use(LoggerMiddleware())

	router.GET("/", func(c *gin.Context) {
		c.String(200, "Hello, World!")
	})

	router.Run(":8080")
}
```

[[GIN Routing]]

