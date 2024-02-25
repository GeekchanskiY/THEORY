

DB.Close is not available in GORM 1.2+ because it's policy refers that you should share one db instance through all of the files. 
But if it's required, you can still do:
```go
dbInstance, _ := db.DB()
_ = dbInstance.Close()
```

### Field-level permission
```go
type User struct {  
  Name string `gorm:"<-:create"` // allow read and create  
  Name string `gorm:"<-:update"` // allow read and update  
  Name string `gorm:"<-"`        // allow read and write (create and update)  
  Name string `gorm:"<-:false"`  // allow read, disable write permission  
  Name string `gorm:"->"`        // readonly (disable write permission unless it configured)  
  Name string `gorm:"->;<-:create"` // allow read and create  
  Name string `gorm:"->:false;<-:create"` // createonly (disabled read from db)  
  Name string `gorm:"-"`            // ignore this field when write and read with struct  
  Name string `gorm:"-:all"`        // ignore this field when write, read and migrate with struct  
  Name string `gorm:"-:migration"`  // ignore this field when migrate with struct  
}
```
