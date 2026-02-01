
Diagnostics solutions can be categorized into the following groups:
- ==Profiling==: Profiling tools analyze the complexity and costs of a Go program such as its memory usage and frequently called functions to identify the expensive sections of a Go program.
- ==Tracing==: Tracing is a way to instrument code to analyze latency throughout the lifecycle of a call or user request. Traces provide an overview of how much latency each component contributes to the overall latency in a system. Traces can span multiple Go processes.
- ==Debugging==: Debugging allows us to pause a Go program and examine its execution. Program state and flow can be verified with debugging.
- ==Runtime statistics and events==: Collection and analysis of runtime stats and events provides a high-level overview of the health of Go programs. Spikes/dips of metrics helps us to identify changes in throughput, utilization, and performance.

## Profiling
Profiling is useful for identifying expensive or frequently called sections of code. The Go runtime provides profiling data in the format expected by the ==`pprof` visualization tool==. The profiling data can be collected during testing via go test or endpoints made available from the `net/http/pprof` package. Users need to collect the profiling data and use `pprof` tools to filter and visualize the top code paths.

Predefined profiles provided by the `runtime/pprof` package:
- `cpu`: CPU profile determines where a program spends its time while actively consuming CPU cycles (as opposed to while sleeping or waiting for I/O).
- `heap`: Heap profile reports memory allocation samples; used to monitor current and historical memory usage, and to ==check for memory leaks==.
- `threadcreate`: Thread creation profile reports the sections of the program that ==lead the creation of new OS threads==.
- `goroutine`: Goroutine profile reports the ==stack traces of all current goroutines==.
- `block`: Block profile shows where ==goroutines block waiting on synchronization primitives== (including timer channels). Block profile is not enabled by default; ==use runtime.SetBlockProfileRate to enable it==.
- `mutex`: Mutex profile ==reports the lock contentions==. When you think your CPU is not fully utilized due to a mutex contention, use this profile. Mutex profile is not enabled by default, see ==runtime.SetMutexProfileFraction to enable it==.

On Linux, [perf tools](https://perf.wiki.kernel.org/index.php/Tutorial) can be used for profiling Go programs. Perf can profile and unwind cgo/SWIG code and kernel, so it can be useful to get insights into native/kernel performance bottlenecks. On macOS, [Instruments](https://developer.apple.com/library/content/documentation/DeveloperTools/Conceptual/InstrumentsUserGuide/) suite can be used profile Go programs.

Enabling some profiles (e.g. the CPU profile) adds cost.

You may want to periodically profile your production services. Especially in a system with many replicas of a single process, selecting a random replica periodically is a safe option. Select a production process, profile it for X seconds for every Y seconds and save the results for visualization and analysis; then repeat periodically. Results may be manually and/or automatically reviewed to find problems. Collection of profiles can interfere with each other, so it is recommended to collect only a single profile at a time.

Additionally to what is provided by the runtime, ==Go users can create their custom profiles via `pprof.Profile`==  and use the existing tools to examine them.
## Tracing
## Debugging

## Runtime statistics and events
# Sources
[Diagnostics](https://go.dev/doc/diagnostics)