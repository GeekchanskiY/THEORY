Original info source
https://tip.golang.org/doc/gc-guide

Here are most important points from this huge statement.

For instance, non-pointer Go values stored in local variables will likely not be managed by the Go GC at all, and Go will instead arrange for memory to be allocated that's tied to the lexical scope in which it's created. In general, this is more efficient than relying on the GC, because the Go compiler is able to predetermine when that memory may be freed and emit machine instructions that clean up. Typically, we refer to allocating memory for Go values this way as "stack allocation," because the space is stored on the goroutine stack.


Together, objects and pointers to other objects form the **object graph**. To identify live memory, the GC walks the object graph starting at the program's **roots**, pointers that identify objects that are definitely in-use by the program. Two examples of roots are local variables and global variables. The process of walking the object graph is referred to as **scanning**.

This basic algorithm is common to all tracing GCs. Where tracing GCs differ is what they do once they discover memory is live. Go's GC uses the mark-sweep technique, which means that in order to keep track of its progress, the GC also **marks** the values it encounters as live. Once tracing is complete, the GC then walks over all memory in the heap and makes all memory that is _not_ marked available for allocation. This process is called **sweeping**.

Because the Go GC is a mark-sweep GC, it broadly operates in two phases: the mark phase, and the sweep phase. While this statement might seem tautological, it contains an important insight: it's not possible to release memory back to be allocated until _all_ memory has been traced, because there may still be an un-scanned pointer keeping an object alive. As a result, the act of sweeping must be entirely separated from the act of marking. Furthermore, the GC may also not be active at all, when there's no GC-related work to do. The GC continuously rotates through these three phases of sweeping, off, and marking in what's known as the **GC cycle**. For the purposes of this document, consider the GC cycle starting with sweeping, turning off, then marking.

To begin with, consider this model of GC cost based on three simple axioms.

1. The GC involves only two resources: CPU time, and physical memory.

2. The GC's memory costs consist of live heap memory, new heap memory allocated before the mark phase, and space for metadata that, even if proportional to the previous costs, are small in comparison.
    _Note: live heap memory is memory that was determined to be live by the previous GC cycle, while new heap memory is any memory allocated in the current cycle, which may or may not be live by the end._

1. The GC's CPU costs are modeled as a fixed cost per cycle, and a marginal cost that scales proportionally with the size of the live heap.
    _Note: Asymptotically speaking, sweeping scales worse than marking and scanning, as it must perform work proportional to the size of the whole heap, including memory that is determined to be not live (i.e. "dead"). However, in the current implementation sweeping is so much faster than marking and scanning that its associated costs can be ignored in this discussion._

The rate at which the application allocates new memory (in bytes per second) is constant.
The application's object graph looks roughly the same each time (objects are similarly sized, there's a roughly constant number of pointers, the maximum depth of the graph is roughly constant).

At a high level, **GOGC** determines the trade-off between GC CPU and memory.

It works by determining the target heap size after each GC cycle, a target value for the total heap size in the next cycle. The GC's goal is to finish a collection cycle before the total heap size exceeds the target heap size. Total heap size is defined as the live heap size at the end of the previous cycle, plus any new heap memory allocated by the application since the previous cycle. Meanwhile, target heap memory is defined as:

Target heap memory = Live heap + (Live heap + GC roots) * GOGC / 100
// Note: GOGC includes the root set only as of Go 1.18. Previously, it would only count the live heap.
**doubling GOGC will double heap memory overheads and roughly halve GC CPU cost**, and vice versa
Calculator with example of gc cpu and peak memory usage depending on gogc presents in gc-guide (link in top)

Useful stuff:
Escape analysis:
go run -cflags=-m main.go

array < 10mb => stack
array > 10 mb => heap

slice < 64kb => does not escape
slice > 64kb => escape to heap

! Important
Stop the world: GC stops the whole application while collecting data (almost fully, on prepearing before mark stage, and after mark stage, but not during mark stage)

New heap equals to 100% to live heap

In general words, GOGC is a percent of new unprocessed heap to a live heap, achieving which GC will be called.
GOGC = 100 => GC starts when live heap = new heap 

GoMemLimit - env var, limit for go runtime memory
GoMemLimit is not set by default to avoid memory leaks