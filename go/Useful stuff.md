### `new(T)` vs `&T{}`
Their behavior is almost same, despite the fact that `new` will automatically put variable into heap, and `&T{}` have a chance to leave in stack. That leads to 2 facts: new is faster for runtime, it does not need to move variable into different scopes, but &T may be a bit faster for gc and be deleted with scope of it's creation.
