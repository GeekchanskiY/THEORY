The syntax  is specified using a variant of Extended Backus-Naur Form (EBNF). // TODO

Source code is Unicode text encoded in UTF-8. It disallows NUL character (U+0000) and ignores BOM's (Byte-order mask) if it is the first Unicode code point in the source text. A byte order mark may be disallowed anywhere else in the source.

## Lexical elements

### Comments
Comments exists in 2 forms: Line comments and General comments

Line comment example:
```go
// Line comment 1
var a = 123 // Line comment 2
```
General comment example
```go
/* Some general comment example. Often used  */
var a = 123
```

### Tokens
Tokens form the vocabulary of the Go language. 
There are four classes: 
- _identifiers_
- _keywords_
- _operators and punctuation_,
- _literals_.  

_White space_, formed from spaces, horizontal tabs, carriage returns, and newlines, is ignored except as it separates tokens that would otherwise combine into a single token. Also, a newline or end of file may trigger the insertion of a semicolon. While breaking the input into tokens, the next token is the longest sequence of characters that form a valid token.

Formal syntax uses semicolons (;), which are automatically omitted after the lines final token if that token is:
 - an identifier
 - an integer, floating-point, imaginary, rune, or string literal
 - one of the keywords break, continue, fallthrough, or return
 - one of the operators and punctuation ++, --, ), ], or }
 and to allow complex statements to occupy a single line, a semicolon may be omitted before a closing ")" or "}".


Identifiers name program entities such as variables and types. An identifier is a sequence of one or more letters and digits. The first character in an identifier must be a letter. Also go has pre-declared identifiers:
```identifiers
Types:
	any bool byte comparable
	complex64 complex128 error float32 float64
	int int8 int16 int32 int64 rune string
	uint uint8 uint16 uint32 uint64 uintptr

Constants:
	true false iota

Zero value:
	nil

Functions:
	append cap clear close complex copy delete imag len
	make max min new panic print println real recover
```


The following keywords are reserved and may not be used as identifiers.
```keywords
break        default      func         interface    select
case         defer        go           map          struct
chan         else         goto         package      switch
const        fallthrough  if           range        type
continue     for          import       return       var
```


The following character sequences represent operators (including assignment operators) and punctuation
```operators
+    &     +=    &=     &&    ==    !=    (    )
-    |     -=    |=     ||    <     <=    [    ]
*    ^     *=    ^=     <-    >     >=    {    }
/    <<    /=    <<=    ++    =     :=    ,    ;
%    >>    %=    >>=    --    !     ...   .    :
     &^          &^=          ~
```


 An integer literal is a sequence of digits representing an integer constant.
 An optional prefix sets a non-decimal base: 0b or 0B for binary, 0, 0o, or 0O for octal, and 0x or 0X for hexadecimal
 For readability, an underscore character _ may appear after a base prefix or between successive digits
```go
var x = 123
var x = 123_000
var x = 0_123
```


# Sources
[The Go Programming Language Specification](https://go.dev/ref/spec) (go version: 1.25)
[Wirth syntax notation](https://en.wikipedia.org/wiki/Wirth_syntax_notation)
[Extended Backus–Naur form](https://en.wikipedia.org/wiki/Extended_Backus–Naur_form)