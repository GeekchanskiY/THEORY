Just a log implementation

Implements a Logger type


Logger methods:
 - Default - constructor
 - New(out i.o, prefix, flag) - advanced constructor
 - Fatal - logs on fatal level and call os.Exit(1)
 - Fatalf - fatal + printf
 - Fatalln - fatal + println
 - Flags - returns output flags ( The flag bits are Ldate, Ltime, and so on.)
 - Output - Output writes the output for a logging event. The string s contains the text to print after the prefix specified by the flags of the Logger.
 - Panic - Print + panic
 - Panicln, Panicf - same as in Fatalf, Fatalln
 - Prefix - returns prefix
 - Print - prints to logger
 - Prints, Println - same as Fatalf, Fatalln
 - SetFlags, SetOutput, SetPrefix
 - Writer - returns writer



### Slog
Package slog provides structured logging, in which log records include a message, a severity level, and various other attributes expressed as key-value pairs.


Default attributes for slog logger
```go
const (
	// TimeKey is the key used by the built-in handlers for the time
	// when the log method is called. The associated Value is a [time.Time].
	TimeKey = "time"
	// LevelKey is the key used by the built-in handlers for the level
	// of the log call. The associated value is a [Level].
	LevelKey = "level"
	// MessageKey is the key used by the built-in handlers for the
	// message of the log call. The associated value is a string.
	MessageKey = "msg"
	// SourceKey is the key used by the built-in handlers for the source file
	// and line of the log call. The associated value is a *[Source].
	SourceKey = "source"
)
```

all info on the doc: https://pkg.go.dev/log/slog@go1.22.3

A log record consists of a time, a level, a message, and a set of key-value pairs, where the keys are strings and the values may be of any type. 
The default handler formats the log record's message, time, level, and attributes as a string and passes it to the log package.

For more control over the output format, create a logger with a different handler. This statement uses New to create a new logger with a TextHandler that writes structured records in text form to standard error

The package also provides JSONHandler, whose output is line-delimited

Both TextHandler and JSONHandler can be configured with HandlerOptions. There are options for setting the minimum level, displaying the source file and line of the log call, and modifying attributes before they are logged.


#### Groups
Attributes can be collected into groups. A group has a name that is used to qualify the names of its attributes. How this qualification is displayed depends on the handler. TextHandler separates the group and attribute names with a dot. JSONHandler treats each group as a separate JSON object, with the group name as the key.

```go
slog.Group("request",
    "method", r.Method,
    "url", r.URL)
```

#### Contexts
Some handlers may wish to include information from the context.Context that is available at the call site. One example of such information is the identifier for the current span when tracing is enabled.


#### Attrs and values

An Attr is a key-value pair. The Logger output methods accept Attrs as well as alternating keys and values.

```go
slog.Info("hello", slog.Int("count", 3)) 
slog.Info("hello", "count", 3) // Shorten syntax. I dont like it actually
```
