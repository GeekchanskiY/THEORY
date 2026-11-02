V8 engine is a JavaScript interpreter. While usual interpreters translate code into machine instructions line by line, V8 was originally developed by Google to improve JavaScript execution performance in browsers.

V8 is one of many engines like Rhino (Java-based mozilla engine), SpiderMonkey(NetScape Navigator), JavaScriptCore (Safari), etc.

V8 is written in c++, and used in google chrome and server environment NodeJS. V8 translates Js code into more effective machine code, not using interpreter. Engine compiles code into machine instructions while code execution using dynamic compilation mechanism. V8's difference is that it does not use byte-code or any intermediate code.

V8 changed after 5.9 version, which was released in 2017. Before it was using two compilers: 
1) full-codegen, which is simple and fast compiler which creates slow machine code.
2) Crankshaft - optimizing JIT-compiler, which generates well-optimized machine code.

Inside engine has several threads: 
1) Main thread, which reads, compiles and executes js code.
2) Compilation thread, which is optimizes code alongside with the main thread.
3) Profiling thread, which tells about the most non-optimized code parts.
4) Several threads for Garbage Collection.

V8 does not create byte-code while execution, so there is no need in interpreter.

While execution when profiler understands which code is the least optimized it tells the Crankshaft. Crankshaft converts Abstract Syntax Tree (AST) into high-level presentation via static single-assignment SSA, which is called Hydrogen. Crankshaft then optimizes it, and most of JS optimizations are happening using Hydrogen.

---

Most popular optimization is embedding, when function is placed directly in the caller code instead of calling it.

---

JS is a prototype-based language without classes, and objects are creating using cloning processes. Also JS is a dynamic programming language, so after object is created it could be modified by adding or removing new parameters.

Most of js interpreters use structures using dictionaries for storing and finding object properties in memory, so getting these properties is harder than in c# and Java.
Unlike other interpreters - V8 uses hidden classes. Hidden classes are like regular classes in classic object-oriented languages, but these hidden classes are created while runtime.

Hidden classes example:
```js
function Point(x, y) {
    this.x = x;
    this.y = y;
}
var p1 = new Point(1, 2);
```
When `new` is called - V8 creates hidden class `C0`.

Before constructor is called - `Point` object has no properties, so `C0` is empty.

When `x` is added - `V8` creates `C1` from `C0` with this property.

When `y` is added - `V8` created `C2` from `C1` with `y` property inside. 

This hidden class creation differs when class has different initialization order:
```js
function Point(x, y) {
    this.x = x;
    this.y = y;
}
var p1 = new Point(1, 2);
p1.a = 5;
p1.b = 6;
var p2 = new Point(3, 4);
p2.b = 7;
p2.a = 8;
```

Here `p1` and `p2` will have different hidden class hierarchy.

---

V8 has caching mechanism, supporting object type cache for faster getting object properties. It is tightly connected with hidden classes. And that's why these object must have same hidden classes: correct caching hits.

---

After Hydrogen graph is optimized - Crankshaft translates is to a low-level interpretation called Lithium, which has lots of implementation for different operational systems. 

Lithium presentation is the one that compiles into the machine code.