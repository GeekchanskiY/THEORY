1. What types of comments exists in GO?
	Line and block comments. [[Go Specification]]
2. Does go uses ;?
	 No, but formal syntax may use it. [[Go Specification]]
3. What's the difference between raw string literal, and interpreted string literal?
	 Raw string literal is a raw utf-8 string, which is not processed in compile time like a interpreted string, so the backslash sequences will have no effect, also raw string may contain a newline character. [[Go Specification]]