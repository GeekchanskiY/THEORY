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
- _literals_.  (==Literals are representations of values within the text of a program==. For example, in the following line of code, 10 is a literal, but x and y are not: `x = y * 10`. ==Literals have data types just as variables do==.)

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
### Constants
Types of constants:
- Numeric
	- Rune
	- Integer
	- Floating-point
	- Complex
- Boolean
- String

Constant is represented by literal (rune, integer, floating-point, imaginary, or string), an identifier denoting a constant, a constant expression, a conversion with a result that is a constant, or the result value of some built-in functions such as min or max applied to constant arguments, unsafe.Sizeof applied to certain values, cap or len applied to some expressions, real and imag applied to a complex constant and complex applied to numeric constants. The boolean values are represented by the predeclared constants `true` and `false`. Predeclared identifier `iota` denotes an integer constant.

Numeric constants represent exact values of arbitrary precision and do not overflow. There are no negative zero, infinity, and not-a-number values constants.

Constants may be typed or untyped. Literal constants, true, false, iota, and certain constant expressions containing only untyped constant operands are untyped.

A constant may be given a type explicitly by a constant declaration or conversion, or implicitly when used in a variable declaration or an assignment statement or as an operand in an expression. It is an error if the constant value cannot be represented as a value of the respective type. If the type is a type parameter, the constant is converted into a non-constant value of the type parameter.

An untyped constant has a default type which is the type to which the constant is implicitly converted in contexts where a typed value is required. The default type of an untyped constant is bool, rune, int, float64, complex128, or string respectively.

Implementation restriction: Although numeric constants have arbitrary precision in the language, a compiler may implement them using an internal representation with limited precision. That said, every implementation must:
- Represent integer constants with at least 256 bits.
- Represent floating-point constants, including the parts of a complex constant, with a mantissa of at least 256 bits and a signed binary exponent of at least 16 bits.
- Give an error if unable to represent an integer constant precisely.
- Give an error if unable to represent a floating-point or complex constant due to overflow.
- Round to the nearest representable constant if unable to represent a floating-point or complex constant due to limits on precision.

```go
const x = 2 + 3.0
const x = 15 / 4
const x float64 = 3/2
const h = "foo" > "bar" // true
```

### Variables
==A variable is a storage location for holding a value==. The set of permissible values is determined by the variable's type. ==Static and dynamic type is the way how this type is obtained==.

A variable declaration or, for function parameters and results, the signature of a function declaration or function literal reserves storage for a named variable. Calling the built-in function new or taking the address of a composite literal allocates storage for a variable at run time. Such an anonymous variable is referred to via a (possibly implicit) pointer indirection.

Structured variables of array, slice, and struct types have elements and fields that may be addressed individually. ==Each such element acts like a variable==.

The ==static type== (or just type) of a variable is the type given in its declaration, the type provided in the new call or composite literal, or the type of an element of a structured variable. Variables of interface type also have a distinct ==dynamic type==, which is the (non-interface) type of the value assigned to the variable at run time (unless the value is the predeclared identifier nil, which has no type). The dynamic type may vary during execution but values stored in interface variables are always assignable to the static type of the variable.
```go
var x interface{}  // x is nil and has static type interface{}
var v *T           // v has value nil, static type *T
x = 42             // x has value 42 and dynamic type int
x = v              // x has value (*T)(nil) and dynamic type *T
```

A variable's value is retrieved by referring to the variable in an expression; it is the most recent value assigned to the variable. If a variable has ==not yet been assigned a value, its value is the zero value for its type==.
## Types
A type determines a ==set of values together with operations and methods specific to those values==. A type may be denoted by a type name, if it has one, which must be followed by type arguments if the type is generic. A type may also be specified using a type literal, which composes a type from existing types.

The language predeclares certain type names. Others are introduced with type declarations or type parameter lists. Composite types—array, struct, pointer, function, interface, slice, map, and channel types—may be constructed using type literals.

Predeclared types, defined types, and type parameters are called ==named types==. ==An alias denotes a named type== if the type given in the alias declaration is a named type.
### Boolean type (bool)
A boolean type represents the set of Boolean truth values denoted by the predeclared constants true and false.
### Numeric types
An integer, floating-point, or complex type represents the set of integer, floating-point, or complex values, respectively. They are collectively called numeric types. The predeclared architecture-independent numeric types are:
```
uint8       the set of all unsigned  8-bit integers (0 to 255)
uint16      the set of all unsigned 16-bit integers (0 to 65535)
uint32      the set of all unsigned 32-bit integers (0 to 4294967295)
uint64      the set of all unsigned 64-bit integers (0 to 18446744073709551615)

int8        the set of all signed  8-bit integers (-128 to 127)
int16       the set of all signed 16-bit integers (-32768 to 32767)
int32       the set of all signed 32-bit integers (-2147483648 to 2147483647)
int64       the set of all signed 64-bit integers (-9223372036854775808 to 9223372036854775807)

float32     the set of all IEEE 754 32-bit floating-point numbers
float64     the set of all IEEE 754 64-bit floating-point numbers

complex64   the set of all complex numbers with float32 real and imaginary parts
complex128  the set of all complex numbers with float64 real and imaginary parts

byte        alias for uint8
rune        alias for int32

uint     either 32 or 64 bits
int      same size as uint
uintptr  an unsigned integer large enough to store the uninterpreted bits of a pointer value
```

To avoid portability issues all numeric types are defined types and thus distinct except byte, which is an alias for uint8, and rune, which is an alias for int32. Explicit conversions are required when different numeric types are mixed in an expression or assignment (int != int32 != int64).

### String type (string)
A string type represents the set of string values. A string value is a (possibly empty) sequence of bytes. The number of bytes is called the length,  number of bytes != number of characters. ==Strings are immutable==.

The length of a string s can be discovered using the built-in function `len`. The length is a compile-time constant if the string is a constant. A string's bytes can be accessed by integer indices 0 through `len(s)-1`. It is illegal to take the address of such an element.
### Array types
An array is a numbered sequence of elements of a single type, called the element type. 

The number of elements is called the ==length of the array== and is never negative. The ==length is part of the array's type==, it must evaluate to a ==non-negative constant== representable by a ==value of type int==. The length of array a can be discovered using the built-in function `len`. The elements can be addressed by integer indices 0 through `len(a)-1`. 

Distinct arrays always represent distinct storage

Array types are always one-dimensional but ==may be composed to form multi-dimensional types==.

Array type can not contain itself, or contain element containing it.

```go
[2]int
[5]*float64
[2][5]int
```
### Slice types
A slice is a ==descriptor for a contiguous segment of an underlying array== and provides ==access to a numbered sequence of elements from that array==. A slice type denotes the set of all slices of arrays of its element type. The number of elements is called the length of the slice and is never negative. The value of an ==uninitialized slice is nil==.

The length of a slice s can be discovered by the built-in function `len`. Unlike with arrays ==it may change during execution==. The elements can be addressed by integer indices 0 through `len(s)-1`. The ==slice index of a given element may be less than the index of the same element in the underlying array==.

A slice, once initialized, is ==always associated with an underlying array== that holds its elements. A ==slice therefore shares storage with its array and with other slices of the same array== (distinct arrays always represent distinct storage)

The ==array underlying a slice may extend past the end of the slice==. The ==capacity== is a measure of that extent: it is the ==sum of the length of the slice and the length of the array beyond the slice==; a slice of length up to that capacity can be created by slicing a new one from the original slice. The capacity of a slice a can be discovered using the built-in function `cap(a)`.

A new, initialized slice value for a given element type T may be made using the built-in function `make`, which takes a slice type and parameters specifying the length and optionally the capacity. A slice created with make always allocates a new, hidden array to which the returned slice value refers.

Like arrays, slices are ==always one-dimensional== but ==may be composed== to construct higher-dimensional objects. With arrays of arrays, the inner arrays are, by construction, always the same length; however with slices of slices (or arrays of slices), the ==inner lengths may vary dynamically==. Moreover, the ==inner slices must be initialized individually== (because their default value is nil).
### Struct types

### Pointer types
### Function types
### Interface types
### Map types
### Channel types


# Sources
[The Go Programming Language Specification](https://go.dev/ref/spec) (go version: 1.25)
[Wirth syntax notation](https://en.wikipedia.org/wiki/Wirth_syntax_notation)
[Extended Backus–Naur form](https://en.wikipedia.org/wiki/Extended_Backus–Naur_form)
[Codecademy go strings](https://www.codecademy.com/resources/docs/go/strings)
[Go blog: slices usage and internals](https://go.dev/blog/slices-intro)