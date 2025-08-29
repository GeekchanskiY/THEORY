### Locker
```go
type Locker interface {
	Lock()
	Unlock()
}
```
Further this interface will be used frequently to explain other structures behavior.
### WaitGroup
```go
type WaitGroup struct {
	// contains filtered or unexported fields
}
```
A `WaitGroup` waits for a collection of `goroutines` to finish. The main goroutine calls `WaitGroup.Add` to set the number of `goroutines` to wait for. Then each of the `goroutines` runs and calls `WaitGroup.Done` when finished. At the same time, `WaitGroup.Wait` can be used to block until all `goroutines` have finished.

A `WaitGroup` must not be copied after first use.

In the terminology of the Go memory model, a call to `WaitGroup.Done` “synchronizes before” the return of any Wait call that it unblocks.

[[go_waitgroup_examples]]

#### Methods
```go
func (wg *WaitGroup) Add(delta int)
```
Adds delta, which may be negative. If the counter becomes zero, all goroutines blocked in `Wait` will be released

```go
func (wg *WaitGroup) Done()
```
Decrements `WaitGroup` by one

```go
func (wg *WaitGroup) Wait()
```
Blocks until the `wg` counter is 0.

### Cond
```go
type Cond struct {
	// L is held while observing or changing the condition
	L Locker
	// contains filtered or unexported fields
}
```
`Cond` implements a condition variable, a rendezvous point for goroutines waiting for or announcing the occurrence of an event.

Each `Cond` has an associated `Locker L` (often a `*Mutex` or `*RWMutex`, which must be held when changing the condition and when calling the `Cond.Wait` method.

A `Cond` must not be copied after first use.

In the terminology of the Go memory model, `Cond` arranges that a call to `Cond.Broadcast` or `Cond.Signal` “synchronizes before” any Wait call that it unblocks.

For many simple use cases, users will be better off using channels than a `Cond` (Broadcast corresponds to closing a channel, and Signal corresponds to sending on a channel).

#### Methods
```go
func NewCond(l Locker) *Cond
```
Initializes a new `Cond`

```go
func (c *Cond) Broadcast()
```
Broadcast wakes all goroutines waiting on c
It is allowed but not required for the caller to hold c.L during the call.

```go
func (c *Cond) Signal() 
```
Signal wakes one goroutine waiting on c, if there is any

It is allowed but not required for the caller to hold c.L during the call.

Signal() does not affect goroutine scheduling priority; if other goroutines are attempting to lock c.L, they may be awoken before a "waiting" goroutine.

```go
func (c *Cond) Wait()
```
Wait atomically unlocks `c.L` and suspends execution of the calling goroutine. After later resuming execution, Wait locks `c.L` before returning. Unlike in other systems, Wait cannot return unless awoken by `Cond.Broadcast` or `Cond.Signal`.

Because c.L is not locked while Wait is waiting, the caller typically cannot assume that the condition is true when Wait returns. Instead, the caller should Wait in a loop:
```go
c.L.Lock()
for !condition() {
    c.Wait()
}
// make use of condition 
c.L.Unlock()
```

### Map
```go
type Map struct {
	// contains filtered or unexported fields
}
```
Map is like a Go `map[any]any` but is safe for concurrent use by multiple goroutines without additional locking or coordination. Loads, stores, and deletes run in amortized constant time.

The Map type is specialized. Most code should use a plain Go map instead, with separate locking or coordination, for better type safety and to make it easier to maintain other invariants along with the map content.

The Map type is optimized for two common use cases: (1) when the entry for a given key is only ever written once but read many times, as in caches that only grow, or (2) when multiple goroutines read, write, and overwrite entries for disjoint sets of keys. In these two cases, use of a Map may significantly reduce lock contention compared to a Go map paired with a separate `Mutex` or `RWMutex`.

The zero Map is empty and ready for use. A Map must not be copied after first use.

#### Methods
```go
func (m *Map) Clear()
```
Clears all map contents.

```go
func (m *Map) CompareAndDelete(key, old any) (deleted bool)
```
Deletes the entry key if it's value is equal to old

```go
func (m *Map) CompareAndSwap(key, old any) (swapped bool)
```
Swap the old and new values for key if the value stored in the map is equal to old. The old value must be of a comparable type.

```go
func (m *Map) Delete(key any)
```
Deletes the value for a key

```go
func (m *Map) Load(key any) (value any, ok bool)
```
Returns the value stored in the map for a key, or nil if no value is present. The ok result indicates whether value was found in the map.

```go
func (m *Map) LoadAnddelete(key any) (value any, loaded bool)
```
Deletes the value for a key, returning the previous value if any. The loaded result reports whether the key was present.

```go
func (m *Map) LoadOrStore(key, value any) (actual any, loaded bool)
```
 Returns the existing value for the key if present. Otherwise, it stores and returns the given value. The loaded result is true if the value was loaded, false if stored.

```go
func (m *Map) Range(f func(key, value any) bool)
```
Calls f sequentially for each key and value present in the map. If f returns false, range stops the iteration.

Range does not necessarily correspond to any consistent snapshot of the Map's contents: no key will be visited more than once, but if the value for any key is stored or deleted concurrently (including by f), Range may reflect any mapping for that key from any point during the Range call. Range does not block other methods on the receiver; even f itself may call any method on m.

Range may be O(N) with the number of elements in the map even if f returns false after a constant number of calls.

```go
func (m *Map) Store(key, value any)
```
Sets a value for key

```go
func (m *Map) Swap(key, value any) (previous any, loaded bool)
```
Swaps the value for a key and returns the previous value if any. The loaded result reports whether the key was present.

### Mutex
```go
type Mutex struct {
	// contains filtered or unexported fields
}
```
A `Mutex` is a mutual exclusion lock. The zero value for a `Mutex` is an unlocked mutex.

A `Mutex` must not be copied after first use.
#### Methods
```go
func (m *Mutex) Lock()
func (m *Mutex) TryLock() bool
func (m *Mutex) UnLock()
```
`Lock` locks m. If the lock is already in use, the calling goroutine blocks until the mutex is available.
`TryLock` tries to lock m and reports whether it succeeded. Note that while correct uses of `TryLock` do exist, they are rare, and use of `TryLock` is often a sign of a deeper problem in a particular use of mutexes.
`Unlock` unlocks m. It is a `run-time error` if m is not locked on entry to `Unlock`.

### Once
```go
type Once struct {
	// contains filtered or unexported fields
}
```
Once is an object that will perform exactly one action.

A Once must not be copied after first use.

```go
func (o *Once) Do(f func())
```
`Do` calls the function f if and only if Do is being called for the first time for this instance of `Once`
if `once.Do(f) `is called multiple times, only the first call will invoke f, even if f has a different value in each invocation. A new instance of Once is required for each function to execute.

### Pool
// TODO: add

### RWMutex
// TODO: add