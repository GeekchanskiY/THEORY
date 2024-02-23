

DB.Close is not available in GORM 1.2+ because it's policy refers that you should share one db instance through all of the files. 
But if it's required, you can still do:
```go
dbInstance, _ := db.DB()
_ = dbInstance.Close()
```
