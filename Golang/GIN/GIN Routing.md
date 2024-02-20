### Groups and use cases

Groups can be used to manage middlewares 
```go
authGroup := router.Group("/api")
authGroup.Use(AuthMiddleware())
{
	authGroup.GET("/data", func)
}
```

Group can create a different group, i.e. group layers

### Graceful restart
[fvbock/endless](https://github.com/fvbock/endless) solves this problem
instead of run, we can use 
```go
endless.ListenAndServe(":4242", router)
```
