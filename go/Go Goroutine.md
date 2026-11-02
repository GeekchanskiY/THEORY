A goroutine is a lightweight thread of execution managed entirely by the Go runtime rather than the operating system. It's a main unit of concurrent programming in go. A Go program execution is modeled as a set of goroutine executions, together with a mapping that specifies the write-like operation that each read-like operation reads from. (Multiple executions of the same program can have different program executions.)

Goroutine vs OS Thread

| Feature        | Goroutine            | OS Thread    |
| -------------- | -------------------- | ------------ |
| Managed by     | Go Runtime Scheduler | OS Kernel    |
| Initial memory | ~2Kb (Dynamic)       | ~1Mb (Fixed) |
| Creation cost  | Cheap                | High         |
| Context switch | Fast                 | Slow         |

A _memory operation_ is modeled by four details:
- its kind, indicating whether it is an ordinary data read, an ordinary data write, or a _synchronizing operation_ such as an atomic data access, a mutex operation, or a channel operation,
- its location in the program,
- the memory location or variable being accessed
- the values read or written by the operation.
A goroutine execution is modeled as a set of memory operations executed by a single goroutine.
Goroutine doesn't guarantee to be finished before application stops


## Goroutine lifecycle
Program initialization runs in a single goroutine, but that goroutine may create other goroutines, which run concurrently.

If a package imports another package, the completion of imported `init` functions happens before the start of any of parent package.

The completion of all `init` functions is synchronized before the start of the function `main.main`.
## Sources
[The Go memory model](https://go.dev/ref/mem)