# Article
A goroutine is a lightweight thread managed by the Go runtime. Actually, goroutine solves the concurrency problem, and involves a new way to manage parallel tasks. It doesn't mean that it does it parallel at CPU level. It would also work on a single-core CPU, as an older machines managed to create an illusion of parallelism. The flow of parallel jobs 'A' & 'B' can be described as:
 - Job A runs a single CPU operation (which takes nanoseconds for 1Ghz CPU)
 - Job A finishes operation, and gives the wheel to job B
 - Job B runs it's operation
 - Job B returns priority to A
 Note: it's not necessary for job to finish only one operation to switch priority, sometimes job can have a background task, for example http response, and while it waits, other jobs can do everything on a single "thread", without switching to waiting job, because it has nothing to do. Or it may happen that task two will require priority for several operations, which can't be disturbed, and then switch mechanism will be waiting for it to finish all high-priority operations.
 Tasks are sharing the processors in order to run some computations. Well the truth is, tasks don’t even have access to the processors or use them directly. They make use of Threads, which have access to the processors.
 TODO: finish