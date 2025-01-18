
`Uber.go/fx` is a dependency injection framework
It allows to automatically build dependency graph inside, increases code reusability, and reduces boilerplates . Also it simplifies code writing process a lot.

## Concepts
### Container
Container is the abstraction responsible for holding all constructors and values. It’s the primary means by which an application interacts with Fx. You teach the container about the needs of your application, how to perform certain operations, and then you let it handle actually running your application.
Fx does not provide direct access to the container. Instead, you specify operations to perform on the container by providing `fx.Option`s to the `fx.New` constructor.
### Providing values
You can provide values to the container in 2 ways: `fx.Supply` and `fx.Provide`
`fx.Supply` is used for simple and non-interface types without using a constructor

```go
fx.Provide( 
	func(cfg *Config) *Logger {
		/* ... */
	},
)
```

```go
fx.Supply(&Config{Name: "my-app"})
```

Also, values can be decorated via `fx.Decorate`:
```go
func NewModule() fx.Option {  
    return fx.Module(  
       "sample",
	    fx.Decorate(func(s SampleA) SampleA {  
			return SampleA{Id: "test"}  
		}),
       fx.Invoke(CallSampleA), // Uses new variable 
    )  
}
```
### Invoking values
Invoking values is being achieved via `fx.Invoke`:

```go
fx.New(
  fx.Provide(newHTTPServer),
  fx.Invoke(startHTTPServer),
).Run()
```

`fx.Invoke` is typically used for root-level invocations, like starting a server or running a main loop. It's also useful for invoking functions that have side effects.

Examples of cases where you might use `fx.Invoke`:
- Starting a background worker
- Configuring a global logger

## Lifecycle

The lifecycle of an Fx application has two high-level phases: initialization and execution
During **initialization**, Fx will,

- register all constructors passed to `fx.Provide`
- register all decorators passed to `fx.Decorate`
- run all functions passed to `fx.Invoke`, calling constructors and decorators as needed

During **execution**, Fx will,

- run all startup hooks appended to the application by providers, decorators, and invoked functions
- wait for a signal to stop running
- run all shutdown hooks appended to the application


### Rules of Fx Hooks:
Lifecycle hooks provide the ability to schedule work to be executed by Fx, when the application starts up or shuts down. Fx provides two kinds of hooks:

- _Startup hooks_, also referred to as `OnStart` hooks. These run in the order they were appended.
- _Shutdown hooks_, also referred to as `OnStop` hooks. These run in the **reverse** of the order they were appended.

Typically, components that provide a startup hook also provide a corresponding shutdown hook to release the resources they acquired at startup.

Fx runs both kinds of hooks with a hard timeout enforcement. Therefore, hooks are expected to block only as long as they need to _schedule_ work. In other words,

- hooks **must not** block to run long-running tasks synchronously
- hooks **should** schedule long-running tasks in background goroutines
- shutdown hooks **should** stop the background work started by startup hooks


## Example code of fx usage

```go
package main  
  
import (  
    "context"  
    "fmt"    "strconv"  
    "go.uber.org/fx")  
  
type Config struct {  
    Id int  
}  
  
type SampleA struct {  
    Id string  
}  
  
type SampleB struct {  
    Id string  
}  
  
func NewB(s string) SampleB {  
    return SampleB{Id: s}  
}  
  
func NewAFromConfig(c Config) SampleA {  
    return SampleA{Id: strconv.Itoa(c.Id)}  
}  
  
func CallSampleA(i SampleA) {  
    fmt.Println(i.Id)  
}  
  
func CallSampleB(i SampleB) {  
    fmt.Println(i.Id)  
}  
  
func NewConfig(lc fx.Lifecycle) Config {  
    lc.Append(fx.Hook{  
       OnStart: func(context.Context) error {  
          fmt.Println("start hook")  
          return nil  
       },  
       OnStop: func(context.Context) error {  
          fmt.Println("stop hook")  
          return nil  
       },  
    })  
    return Config{Id: 1}  
}  
  
func main() {  
    fx.New(  
       fx.Supply("example B"), // Provides bare string which will be used for B constructor  
       fx.Provide(  
          NewB,  
          NewConfig,  
          NewAFromConfig,  
       ),  
       fx.Invoke(  
          CallSampleA,  
          CallSampleB,  
       ),  
       Submodule(),  
       SecondSubmodule(),  
    ).Run()  
}  
  
func Submodule() fx.Option {  
    return fx.Module(  
       "sampleMod",  
       fx.Decorate(func() SampleA {  
          return SampleA{Id: "2"} // Just updates the dependency  
       }),  
       fx.Invoke(CallSampleA), // Gets it from parent module, and decorates  
       SubSubmodule(),         // Gets decorated dependencies  
    )  
}  
  
func SubSubmodule() fx.Option {  
    return fx.Module(  
       "sampleMod",  
       fx.Decorate(func(s SampleA) SampleA {  
          return SampleA{Id: "submodule_call: " + s.Id}  
       }),  
       fx.Invoke(CallSampleA),  
    )  
}  
  
func SecondSubmodule() fx.Option {  
    return fx.Module(  
       "sampleMod2",  
       fx.Invoke(CallSampleA), // Gets it from parent module  
       SubSubmodule(),  
    )  
}
```