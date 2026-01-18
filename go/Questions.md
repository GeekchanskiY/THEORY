1. What types of comments exists in GO?
	Line and block comments. [[Go Specification]]
2. Does go uses ;?
	 No, but formal syntax may use it. [[Go Specification]]
3. What's the difference between raw string literal, and interpreted string literal?
	 Raw string literal is a raw utf-8 string, which is not processed in compile time like a interpreted string, so the backslash sequences will have no effect, also raw string may contain a newline character. [[Go Specification]]
 4.  What are the channel types?
	 Buffered and unbuffered, directional and bidirectional. [[Go Specification]]
5. What is a variadic function?
	It is a function with a `...` in the last parameter. [[Go Specification]]
6. What is comparable?
	TODO
7. Type declarations vs type parameter declarations?
	TODO
8. May method receiver be blank?
	Yes, `func (_ Type) f()` is valid. [[Go Specification]]
9. What's the difference between var and := (full and short) variable declarations?
	Short variable declaration may assign a new value to an declared variable in multi-value assignment, but it will not re-declare it.
10. How to define an empty int array with len 10 and 4th element equal 5?
	`[10]int{3: 5}` [[Go Specification#Composite literals]]
11. Selectors vs qualified identifiers?
	Qualified identifiers are selectors for the package [[Go Specification]].
	