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

### Literals
 An integer literal is a sequence of digits representing an integer constant.
 An optional prefix sets a non-decimal base: 0b or 0B for binary, 0, 0o, or 0O for octal, and 0x or 0X for hexadecimal
 For readability, an underscore character _ may appear after a base prefix or between successive digits
```go
var x = 123
var x = 123_000
var x = 0_123
```
---
Floating-point literal is a decimal or hexadecimal representation of a floating-point constant, consists of an integer part, a decimal point, a fractional part , and an exponent part. One of the integer part or the fractional part may be elided; one of the decimal point or the exponent part may be elided. An exponent value exp scales the mantissa (integer and fractional part) by 10exp.
```go
var x = 0.
var x = 72.40
var x = 1.e+0
var x = 6.67428e-11
var x = .25
var x = .12345E+5
var x = 1_5.         // == 15.0
var x = 0.15e+0_2    // == 15.0
```
---
An imaginary literal represents the imaginary part of a complex constant. It consists of an integer or floating-point literal followed by the lowercase letter i. The value of an imaginary literal is the value of the respective integer or floating-point literal multiplied by the imaginary unit.
```go
var x = 0i
var x = 0123i         // == 123i for backward-compatibility
var x = 0o123i        // == 0o123 * 1i == 83i
var x = 0xabci        // == 0xabc * 1i == 2748i
```
---
A rune literal represents a rune constant, an integer value identifying a Unicode code point. A rune literal is expressed as one or more characters enclosed in single quotes, as in 'x' or '\n'. Within the quotes, any character may appear except newline and unescaped single quote. A single quoted character represents the Unicode value of the character itself, while multi-character sequences beginning with a backslash encode values in various formats. Go source code is UTF-8 encoded => single character may represent several bytes
```go
var x = 'a'
var x = 'ä'
var x = '本'
var x = '\t'
```
---
A string literal represents a string constant obtained from concatenating a sequence of characters. There are two forms: raw string literals and interpreted string literals.

Raw string literals use \` symbol and within the quotes, any character may appear except back quote. Raw string means backslash has no meaning, and will be 'as is' utf-8 encoded string.

Interpreted string literals are character sequences between " symbols. Within the quotes, any character may appear except newline and unescaped double quote. The text between the quotes forms the value of the literal, with backslash escapes interpreted as they are in rune literals (except that \' is illegal and \" is legal), with the same restrictions. All escapes (except \nnn and \xnn) represent the (possibly multi-byte) UTF-8 encoding of individual characters.

```go
var x = `I am raw,
and I can have a newline`
var x = "I am interpreted, \n and newline uses backslash escape."
```
# Sources
[The Go Programming Language Specification](https://go.dev/ref/spec) (go version: 1.25)
[Wirth syntax notation](https://en.wikipedia.org/wiki/Wirth_syntax_notation)
[Extended Backus–Naur form](https://en.wikipedia.org/wiki/Extended_Backus–Naur_form)
[Codecademy go strings](https://www.codecademy.com/resources/docs/go/strings)