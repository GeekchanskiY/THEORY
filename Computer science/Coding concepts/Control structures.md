Control structure is a structure that can change the application flow direction. It can be a loop, if statement, and some of it's analogs. Historically, loops started from `goto`, which allows to continue execution of a code from different line/label/etc. But now there is plenty of possibilities to achieve this behavior. For example, a single `goto` statement was able to cause a conditional transfer of control:
`IF condition THEN goto label`
Usages of `goto` looked like this:
 - To make the code more readable and easier to follow
 - To make smaller programs, and get rid of code duplication
 - Implement a finite-state machine, using a state transition table and `goto` to switch between states (in absence of tail call elimination), particularly in automatically generated C code. For example, `goto` in the canonical LR parser.
 - Implementing multi-level break and continue if not directly supported in the language; this is a common idiom in C.
 - Surrogates for single-level break or continue (retry) statements when the potential introduction of additional loops could incorrectly affect the control flow.
 - Error handling (in absence of exceptions), particularly cleanup code such as resource deallocation.
 - Popping the stack in, e.g., Algol, PL/I.
 - Specialized scripting languages that operate in a linear manner, such as a dialogue system for video games.
Now everything is fixed by different paradigms, and `goto` statement is no longer supported in lots of languages. Loops are typically being like:
 - `FOR` loop, which is usually works as an iterator for an array
```python
for i in ["some", "random", "objects"]:
	print(i)
``` 
 - `WHILE DO` loop, which runs while condition is correct
 - `DO WHILE` loop, which runs, and then re-runs if condition is correct
 - Some of programming languages uses `WHILE` only, which works as `WHILE DO`. `DO WHILE` may be implemented with additional if statement and changed condition.
 If statement also has different variations, usually they are:
  - `IF condition THEN`, `ELSE THEN`, `ELSEIF condition THEN`
  - `SWITCH condition CASE value THEN` allows to replace lots of if and else-if statements, and also supports default value in lots of implementations.