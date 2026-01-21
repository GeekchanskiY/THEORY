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

Identifiers name program entities such as variables and types. An identifier is a sequence of one or more letters and digits. The first character in an identifier must be a letter. Also go has [[#pre-declared identifiers]]

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
A struct is a ==sequence of named elements, called fields==, each of which has a name and a type. Field names may be specified explicitly (==IdentifierList==) or implicitly (==EmbeddedField==). Within a struct, ==non-blank field names must be unique==.

A field declared with a type but no explicit field name is called an embedded field. An embedded field must be specified as a type name or as a pointer to a non-interface type name, and type name itself may not be a pointer type or type parameter. The ==unqualified type name acts as the field name==.

```go
// An empty struct.
struct {}

// A struct with 6 fields.
struct {
	x, y int
	u float32
	_ float32  // padding
	A *[]int
	F func()
}

// A struct with four embedded fields of types T1, *T2, P.T3 and *P.T4
struct {
	T1        // field name is T1
	*T2       // field name is T2
	P.T3      // field name is T3
	*P.T4     // field name is T4
	x, y int  // field names are x and y
}
```

A field or method f of an embedded field in a struct x is called ==promoted if x.f is a legal selector that denotes that field or method f==. (if you can do x.f when f is a part of an embedded struct => field is promoted)

Promoted fields act like ordinary fields of a struct except that they cannot be used as field names in composite literals of the struct. (you cant do `struct{a: 10}` if a is a field of an embedded struct).

Given a struct type `S` and a type name `T`. promoted methods are included in the method set of the struct as follows:
 - If `S` contains an embedded field `T`, the method sets of `S` and `*S` both include promoted methods with receiver `T`. The method set of `*S` also includes promoted methods with receiver `*T`.
- If `S` contains an embedded field `*T`, the method sets of `S` and `*S` both include promoted methods with receiver `T` or `*T`.

A field declaration may be followed by an ==optional string literal tag==, which becomes an attribute for all the fields in the corresponding field declaration. The tags are made ==visible through a reflection interface== and take part in type identity for structs but are otherwise ignored.
### Pointer types
A pointer type denotes the set of all pointers to variables of a given type, called the base type of the pointer. The value of an uninitialized pointer is nil. 
```go
var x *int
var x *[4]int
```
### Function types
A function type denotes the set of all functions with the same parameter and result types. The value of an uninitialized variable of function type is nil.

All non-blank names in signature (parameter and result) must be unique.

Th ==final incoming parameter== in a function signature may have a type prefixed with `...`. A function with such a parameter is called ==variadic== and may be invoked with zero or more arguments for that parameter.
### Interface types
An interface type ==defines a type set==. A variable of interface type can store a value of any type that is in the type set of the interface. Such a type is said to implement the interface. The value of an uninitialized variable of interface type is nil.

An interface type is specified by a list of methods or types.
#### Basic interface
In its most basic form an interface specifies a (possibly empty) list of methods. The type set defined by such an interface is the set of types which implement all of those methods, and the corresponding method set consists exactly of the methods specified by the interface. Interfaces whose type sets can be ==defined entirely by a list of methods are called basic interfaces==.

The name of each explicitly specified method ==must be unique and not blank==.

More than one type may implement an interface. Every type that is a member of the type set of an interface implements that interface. Any given type may implement several distinct interfaces. 

All types implement the empty interface (`interface{}` or it's alias `any`) which stands for the set of all (non-interface) types.
#### Embedded interfaces
In a slightly more general form an interface `T` may use a (possibly qualified) interface type name `E` as an interface element. This is called embedding interface `E` in `T`. The type set of `T` is the intersection of the type sets defined by `T` explicitly declared methods and the type sets of `T` embedded interfaces. In other words, the type set of `T` is the ==set of all types that implement all the explicitly declared methods of T and also all the methods of E==.

When embedding interfaces, ==methods with the same names must have identical signatures==.
#### General interfaces
In their most general form, an interface element may also be an arbitrary type term `T`, or a term of the form `~T` ==specifying the underlying type== `T` (which is the type and aliases), or a union of terms `t1|t2|…|tn`. Together with method specifications, these elements enable the precise definition of an interface's type set as follows:
- The type set of the empty interface is the set of all non-interface types.
- The type set of a non-empty interface is the intersection of the type sets of its interface elements.
- The type set of a method specification is the set of all non-interface types whose method sets include that method.
- The type set of a non-interface type term is the set consisting of just that type.
- The type set of a term of the form `~T` is the ==set of all types whose underlying type is T==.
- The type set of a union of terms `t1|t2|…|tn` is the union of the type sets of the terms.

By construction, an ==interface's type set never contains an interface type==.
In a term of the form `~T`, the underlying type of `T` must be itself, and `T` cannot be an interface.

Implementation restriction: A union (with more than one term) cannot contain the predeclared identifier `comparable` or interfaces that specify methods, or embed `comparable` or interfaces that specify methods.

The type `T` in a term of the form `T` or `~T` ==cannot be a type parameter==, and the type sets of all non-interface terms must be pairwise disjoint (the pairwise intersection of the type sets must be empty).

Interfaces that are ==not basic may only be used as type constraints, or as elements of other interfaces used as constraints==. They cannot be the types of values or variables, or components of other, non-interface types.

An interface type `T` may not embed a type element that is, contains, or embeds `T`, directly or indirectly.

```go
type A int

type IntAlike interface {
	~int
}

var x IntAlike = A(4) // valid
var x IntAlike = int(3) // valid
```
#### Implementing an interface
A type T implements an interface I if
- `T` is not an interface and is an element of the type set of `I`
- `T` is an interface and the type set of T is a subset of the type set of `I`.
A value of type T implements an interface if T implements the interface.
### Map types
A map is an ==unordered group of elements of one type==, called the element type, ==indexed by a set of unique keys of another type==, called the key type. The value of an ==uninitialized map is nil==.

The comparison operators `==` and `!=` must be fully defined for operands of the key type
Thus ==the key type must not be a function, map, or slice==. 

If the key type is an interface type, these comparison operators must be defined for the dynamic key values; failure will cause a run-time panic.

The number of map elements is called its length. For a `map m`, it can be discovered using the built-in function `len` and may change during execution. Elements may be added during execution using assignments and retrieved with index expressions

Elements may be removed with the `delete` and `clear` built-in function.

A new, empty map value is made using the built-in function make, which takes the map type and an optional capacity hint as argument. The initial capacity does not bound its size: maps grow to accommodate the number of items stored in them, with the exception of `nil` maps. ==A `nil` map is equivalent to an empty map except that no elements may be added==.
### Channel types
A channel provides a mechanism for concurrently executing functions to communicate by sending and receiving values of a specified element type. The value of an uninitialized channel is nil.
`ChannelType = ( "chan" | "chan" "<-" | "<-" "chan" ) ElementType .`

The optional `<-` operator specifies the channel direction, send or receive. ==If a direction is given, the channel is directional, otherwise it is bidirectional==. A channel may be constrained only to send or only to receive by ==assignment or explicit conversion==.

The `<-` operator associates with the leftmost chan possible:
```go
chan<- chan int    // same as chan<- (chan int)
chan<- <-chan int  // same as chan<- (<-chan int)
<-chan <-chan int  // same as <-chan (<-chan int)
chan (<-chan int)
```

A new, initialized channel value can be made using the built-in function make, which takes the channel type and an optional capacity as argument.

The capacity, in number of elements, ==sets the size of the buffer in the channel==. If the capacity is zero or absent, the channel is ==unbuffered== and ==communication succeeds only when both a sender and receiver are ready==. Otherwise, the channel is ==buffered== and ==communication succeeds without blocking if the buffer is not full (sends) or not empty (receives)==. A `nil` channel is ==never ready for communication==.

A channel may be closed with the built-in function close. The multi-valued assignment form of the receive operator reports whether a received value was sent before the channel was closed.

A single channel may be used in send statements, receive operations, and calls to the built-in functions `cap` and `len` by any number of `goroutines` without further synchronization. ==Channels act as first-in-first-out queues==.
## Properties of types and values
### Representation of values
Values of predeclared types (see below for the interfaces any and error), arrays, and structs are self-contained: Each such ==value contains a complete copy of all its data==, and variables of such types ==store the entire value==. For instance, an array variable provides the storage (the variables) for all elements of the array. The respective zero values are specific to the value's types, and they are never nil.

`Non-nil pointer`, `function`, `slice`, `map`, and `channel` values ==contain references to underlying data== which may be shared by multiple values:
- A pointer value is a reference to the variable holding the pointer base type value.
- A function value contains references to the (possibly anonymous) function and enclosed variables.
- A slice value contains the slice length, capacity, and a reference to its underlying array.
- A map or channel value is a reference to the implementation-specific data structure of the map or channel.

An interface value may be self-contained or contain references to underlying data depending on the interface's dynamic type. The predeclared identifier nil is the zero value for types whose values can contain references.

When multiple values share underlying data, ==changing one value may change another==. For instance, ==changing an element of a slice will change that element in the underlying array for all slices that share the array==.
### Underlying type
Each type `T` has an underlying type: If `T` is one of the predeclared boolean, numeric, or string types, or a type literal, the corresponding ==underlying type is T itself==. Otherwise, `T`'s underlying type is the underlying type of the type to which `T` refers in its declaration. For a type parameter that is the underlying type of its type constraint, which is always an `interface`.
```go
type (
	A1 = string // underlying: string
	A2 = A1 // underlying: string
)

type (
	B1 string // underlying: string
	B2 B1 // underlying: string
	B3 []B1 // underlying: []B1 (both for []B1 and B3)
	B4 B3 // underlying: []B1
)

func f[P any](x P) { … } // underlying of P is interface{}
```
### Type identity
Two types are either identical or different.

A ==named type is always different from any other type==. Otherwise, two types are ==identical if their underlying type literals are structurally equivalent==

That is, they have the same literal structure and corresponding components have identical types. In detail:
- Two array types are identical if they have identical element types and the same array length.
- Two slice types are identical if they have identical element types.
- Two struct types are identical if they have the same sequence of fields, and if corresponding pairs of fields have the same names, identical types, and identical tags, and are either both embedded or both not embedded. ==Non-exported field names from different packages are always different==.
- Two pointer types are identical if they have identical base types.
- Two function types are identical if they have the same number of parameters and result values, corresponding parameter and result types are identical, and either both functions are variadic or neither is. ==Parameter and result names are not required to match==.
- Two interface types are identical if they define the same type set.
- Two map types are identical if they have identical key and element types.
- Two channel types are identical if they have identical element types and the same direction.
- Two instantiated types are identical if their defined types and all type arguments are identical.
### Assignability
A value `x` of type `V` is assignable to a variable of type `T` if one of the following conditions applies:
- `V` and `T` are identical.
- `V` and `T` have identical underlying types but are not type parameters and at least one of `V` or `T` is not a named type.
- `V` and `T` are channel types with identical element types, `V` is a bidirectional channel, and at least one of `V` or `T` is not a named type.
- `T` is an interface type, but not a type parameter, and x implements `T`. 
- `x` is the predeclared identifier nil and `T` is a pointer, function, slice, map, channel, or interface type, but not a type parameter.
- `x` is an untyped constant representable by a value of type `T`.

Additionally, if `x`'s type `V` or `T` are type parameters, `x` is assignable to a variable of type `T` if one of the following conditions applies:
- `x` is the predeclared identifier `nil`, `T` is a type parameter, and `x` is assignable to each type in `T`'s type set.
- `V` is not a named type, `T` is a type parameter, and `x` is assignable to each type in `T`'s type set.
- `V` is a type parameter and `T` is not a named type, and values of each type in `V`'s type set are assignable to `T`.
### Representability
A constant `x` is representable by a value of type `T`, where `T` is not a type parameter, if one of the following conditions applies:
- `x` is in the set of values determined by `T`.
- `T` is a floating-point type and x can be rounded to `T`'s precision without overflow. Rounding uses IEEE 754 round-to-even rules but with an IEEE negative zero further simplified to an unsigned zero. Note that constant values never result in an IEEE negative zero, NaN, or infinity.
- `T` is a complex type, and `x`'s components `real(x)` and `imag(x)` are representable by values of `T`'s component type (float32 or float64).
If `T` is a type parameter, `x` is representable by a value of type `T` if `x` is representable by a value of each type in `T`'s type set.
### Method sets
The method set of a type determines the methods that can be called on an operand of that type. Every type has a (possibly empty) method set associated with it:
- The method set of a defined type `T` consists of all methods declared with receiver type `T` (not `*T`).
- The method set of a pointer to a defined type `T` (where `T` is ==neither a pointer nor an interface==) is the set of all methods declared with receiver `*T` or `T`.
- The method set of an interface type is the ==intersection of the method sets of each type in the interface's type set==.
Further rules apply to structs (and pointer to structs) containing embedded fields, as described in the section on struct types. Any other type has an empty method set.

In a method set, each method must have a unique non-blank method name.
## Block
A block is a possibly empty sequence of declarations and statements within matching brace brackets.

In addition to explicit blocks in the source code, there are implicit blocks:
 - The universe block encompasses all Go source text.
 - Each package has a package block containing all Go source text for that package.
 - Each file has a file block containing all Go source text in that file.
 - Each "if", "for", and "switch" statement is considered to be in its own implicit block.
 - Each clause in a "switch" or "select" statement ==acts as an implicit block==.
 
 Blocks nest and ==influence scoping==.
## Declarations and scope
A declaration binds a non-blank identifier to a `constant`, `type`, `type parameter`, `variable`, `function`, `label`, or `package`. Every identifier in a program must be declared. ==No identifier may be declared twice in the same block==, and ==no identifier may be declared in both the file and package block==.

The blank identifier may be used like any other identifier in a declaration, but it does not introduce a binding and thus is not declared. In the package block, the identifier init may only be used for init function declarations, and like the blank identifier it does not introduce a new binding.

The _scope_ of a declared identifier is the extent of source text in which the identifier denotes the specified constant, type, variable, function, label, or package.

Go is lexically scoped using blocks:
 - The scope of a predeclared identifier is the universe block.
 - The scope of an identifier denoting a constant, type, variable, or function (==but not method==) declared at top level (outside any function) is the package block.
 - The scope of the package name of an imported package is the file block of the file containing the import declaration.
 - The scope of an identifier denoting a method receiver, function parameter, or result variable is the function body.
 - The scope of an identifier denoting a type parameter of a function or declared by a method receiver begins after the name of the function and ends at the end of the function body.
 - The scope of an identifier denoting a type parameter of a type begins after the name of the type and ends at the end of the TypeSpec.
 - The scope of a constant or variable identifier declared inside a function begins at the end of the ConstSpec or VarSpec (ShortVarDecl for short variable declarations) and ends at the end of the innermost containing block.
 - The scope of a type identifier declared inside a function begins at the identifier in the TypeSpec and ends at the end of the innermost containing block.

An identifier declared in a block may be redeclared in an inner block. While the identifier of the inner declaration is in scope, it denotes the entity declared by the inner declaration.

The package clause is not a declaration; the package name does not appear in any scope. Its purpose is to identify the files belonging to the same package and to specify the default package name for import declarations.
### Label scopes
Labels are declared by labeled statements and are used in the "break", "continue", and "goto" statements. It is illegal to define a label that is never used. In contrast to other identifiers, labels are not block scoped and do not conflict with identifiers that are not labels. The scope of a label is the body of the function in which it is declared and excludes the body of any nested function.

```go
Error: log.Panic("error encountered")

goto Error
```
### Blank identifier
The blank identifier is represented by the underscore character `_`. It serves as an anonymous placeholder instead of a regular (non-blank) identifier and has special meaning in declarations, as an operand, and in assignment statements.
### Predeclared identifiers
The following identifiers are implicitly declared in the universe block.
```
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
### Exported identifiers
An identifier may be exported to permit access to it from another package. An identifier is exported if both:
 - the first character of the identifier's name is a Unicode uppercase letter (Unicode character category Lu); and
 - the identifier is declared in the package block or it is a field name or method name.
 
All other identifiers are not exported.
### Uniqueness of identifiers
Given a set of identifiers, an identifier is called unique if it is different from every other in the set. Two identifiers are different if they are spelled differently, or if they appear in different packages and are not exported. Otherwise, they are the same.
### Constant declarations
A constant declaration binds a ==list of identifiers== to the values of a list of constant expressions. The ==number of identifiers must be equal to the number of expressions==, and the nth identifier on the left is bound to the value of the nth expression on the right.

If the type is present, all constants take the type specified, and the expressions must be assignable to that type, which must not be a type parameter. If the type is omitted, the constants take the individual types of the corresponding expressions. If the expression values are ==untyped constants==, the declared constants remain untyped and the constant identifiers denote the constant values.

Within a parenthesized const declaration list the expression list may be omitted from any but the first ConstSpec. Such an empty list is equivalent to the textual substitution of the first preceding non-empty expression list and its type if any. ==Omitting the list of expressions is therefore equivalent to repeating the previous list==. The number of identifiers must be equal to the number of expressions in the previous list.
```go
const (
	a = "test"
	b // also equals test
)
```
### Iota
Within a constant declaration, the predeclared identifier iota represents successive untyped integer constants. Its value is the index of the respective ConstSpec in that constant declaration, starting at zero. It can be used to construct a set of related constants.

By definition, ==multiple uses of iota in the same ConstSpec all have the same value==.
```go
const (
	bit0, mask0 = 1 << iota, 1<<iota - 1  // bit0 == 1, mask0 == 0  (iota == 0)
	bit1, mask1                           // bit1 == 2, mask1 == 1  (iota == 1)
	_, _                                  //                        (iota == 2, unused)
	bit3, mask3                           // bit3 == 8, mask3 == 7  (iota == 3)
)
```
### Type declarations
A type declaration binds an identifier, the type name, to a type. Type declarations come in two forms: alias declarations and type definitions.
#### Alias declarations
An alias declaration binds an identifier to the given type.
#### Type definitions
A type definition creates a new, distinct type with the same underlying type and operations as the given type and binds an identifier, the type name, to it.

The new type is called a defined type. ==It is different from any other type, including the type it is created from==.

A defined type may have methods associated with it. It does not inherit any methods bound to the given type, but the method set of an interface type or of elements of a composite type remains unchanged.
```go
// A Mutex is a data type with two methods, Lock and Unlock.
type Mutex struct         { /* Mutex fields */ }
func (m *Mutex) Lock()    { /* Lock implementation */ }
func (m *Mutex) Unlock()  { /* Unlock implementation */ }

// NewMutex has the same composition as Mutex but its method set is empty.
type NewMutex Mutex

// The method set of PtrMutex's underlying type *Mutex remains unchanged,
// but the method set of PtrMutex is empty.
type PtrMutex *Mutex

// The method set of *PrintableMutex contains the methods
// Lock and Unlock bound to its embedded field Mutex.
type PrintableMutex struct {
	Mutex
}

// MyBlock is an interface type that has the same method set as Block.
type MyBlock Block
```

Type definitions may be used to define different boolean, numeric, or string types and associate methods with them:
```go
type Enum int
```

If the type definition specifies type parameters, the type name denotes a generic type. Generic types must be instantiated when they are used.
```go
type List[T any] struct {
	next  *List[T]
	value T
}
```
In a type definition the given type ==cannot be a type parameter==.

A generic type may also have methods associated with it. In this case, the method receivers must declare the same number of type parameters as present in the generic type definition.
```go
// The method Len returns the number of elements in the linked list l.
func (l *List[T]) Len() int  { … }
```
#### Type parameter declarations
A type parameter list declares the type parameters of a generic function or type declaration. The type parameter list looks like an ordinary function parameter list except that the type parameter names must all be present and the list is enclosed in square brackets rather than parentheses.

All non-blank names in the list must be unique. Each name declares a type parameter, which is a new and ==different named type== that acts as a placeholder for an (as of yet) unknown type in the declaration. The type parameter is replaced with a type argument upon instantiation of the generic function or type.
```
[P any]
[S interface{ ~[]byte|string }]
[S ~[]E, E any]
[P Constraint[int]]
[_ any]
```
Just as each ordinary function parameter has a parameter type, each type parameter has a corresponding (meta-)type which is called its type constraint.

A parsing ambiguity arises when the type parameter list for a generic type declares a single type parameter P with a constraint C such that the text P C forms a valid expression:
```go
type T[P *C] …
type T[P (C)] …
type T[P *C|Q] …
```

In these rare cases, the type parameter list is indistinguishable from an expression and the type declaration is parsed as an array type declaration. To resolve the ambiguity, embed the constraint in an interface or use a trailing comma:
```go
type T[P interface{*C}] …
type T[P *C,] …
```

Type parameters may also be declared by the receiver specification of a method declaration associated with a generic type.

Within a type parameter list of a generic type T, a type constraint may not (directly, or indirectly through the type parameter list of another generic type) refer to T.

#### Type constraints
A type constraint is an interface that defines the set of permissible type arguments for the respective type parameter and controls the operations supported by values of that type parameter

If the constraint is an interface literal of the form interface{E} where E is an embedded type element (not a method), in a type parameter list the enclosing interface{ … } may be omitted for convenience.
```go
[T []P]                      // = [T interface{[]P}]
[T ~int]                     // = [T interface{~int}]
[T int|string]               // = [T interface{int|string}]
type Constraint ~int         // illegal: ~int is not in a type parameter list
```

The predeclared interface type comparable denotes the set of all non-interface types that are strictly comparable. Even though interfaces that are not type parameters are comparable, they are not strictly comparable and therefore they do not implement comparable. However, they satisfy comparable. The ==comparable interface and interfaces that (directly or indirectly) embed comparable may only be used as type constraints==. They cannot be the types of values or variables, or components of other, non-interface types.
#### Satisfying a type constraint
A type argument T satisfies a type constraint C if T is an element of the type set defined by C; in other words, if T implements C. As an exception, a strictly comparable type constraint may also be satisfied by a comparable (not necessarily strictly comparable) type argument. More precisely `type T satisfies a constraint C` if:
 - T implements C
 - C can be written in the form interface{ comparable; E }, where E is a basic interface and T is comparable and implements E.

Because of the exception in the constraint satisfaction rule, ==comparing operands of type parameter type may panic at run-time== (even though comparable type parameters are always strictly comparable).
### Variable declarations
A variable declaration creates one or more variables, binds corresponding identifiers to them, and gives each a type and an initial value.
```go
var i int
var U, V, W float64
var a = testFunc(x)
var (
	b int
	z, x, c = "asdasd", 2, 2.0
)
var _, x = lookup(123)
```
If a list of expressions is given, the variables are initialized with the expressions following the rules for assignment statements. Otherwise, ==each variable is initialized to its zero value==.

If a type is present, each variable is given that type. Otherwise, each variable is given the type of the corresponding initialization value in the assignment. If that value is an untyped constant, it is first implicitly converted to its default type; if it is an untyped boolean value, it is first implicitly converted to type bool. The ==predeclared identifier nil cannot be used to initialize a variable with no explicit type==.

> [!warning] Implementation restriction
> A compiler may make it illegal to declare a variable inside a function body if the variable is never used.

In these rare cases, the type parameter list is indistinguishable from an expression and the type declaration is parsed as an array type declaration. To resolve the ambiguity, embed the constraint in an interface or use a trailing comma:
```go
type T[P interface{*C}] …
type T[P *C,] …
```

Type parameters may also be declared by the receiver specification of a method declaration associated with a generic type.

Within a type parameter list of a generic type T, a type constraint may not (directly, or indirectly through the type parameter list of another generic type) refer to T. 

TODO: return here and refactor it.

#### Type constraints
A ==type constraint is an interface that defines the set of permissible type arguments for the respective type parameter== and controls the operations supported by values of that type parameter.

If the constraint is an interface literal of the form interface{E} where E is an embedded type element (not a method), in a type parameter list the enclosing interface{ … } may be omitted for convenience
```go
[T []P]                      // = [T interface{[]P}]
[T ~int]                     // = [T interface{~int}]
[T int|string]               // = [T interface{int|string}]
type Constraint ~int         // illegal: ~int is not in a type parameter list
```

The predeclared interface type `comparable` denotes the set of all non-interface types that are ==strictly comparable==.

Even though interfaces that are not type parameters are comparable, they are ==not strictly comparable and therefore they do not implement comparable==. However, they satisfy comparable.

The comparable interface and interfaces that (directly or indirectly) embed comparable may only be used as type constraints. They cannot be the types of values or variables, or components of other, non-interface types.
#### Satisfying a type constraint
A type T satisfies a constraint C if:
 - ==T implements C==
 - C can be written in the form `interface{ comparable; E }`, where `E` is a basic interface and `T` is `comparable` and implements `E`.

### Variable declarations
```go
var x, y = 1, 2
```

A variable declaration creates one or more variables, binds corresponding identifiers to them, and ==gives each a type and an initial value==.

If a list of expressions is given, the variables are ==initialized with the expressions== following the rules for assignment statements. Otherwise, ==each variable is initialized to its zero value==.
If a type is present, each variable is given that type. Otherwise, each variable is given the type of the corresponding initialization value in the assignment. If that value is an untyped constant, it is ==first implicitly converted to its default type==. If it is an untyped boolean value, it is first implicitly converted to type bool. ==The predeclared identifier nil cannot be used to initialize a variable with no explicit type==.

>[!warning] Unused variable implementation restriction
> A compiler may make it illegal to declare a variable inside a function body if the variable is never used.

### Short variable declarations
It is shorthand for a regular variable declaration with initializer expressions but no types.

Unlike regular variable declarations, a short variable declaration ==may redeclare variables== provided they were originally declared earlier in the same block (or the parameter lists if the block is the function body) with the same type, and ==at least one of the non-blank variables is new==. As a consequence, ==redeclaration can only appear in a multi-variable short declaration==. Redeclaration ==does not introduce a new variable; it just assigns a new value to the original==. The non-blank variable names on the left side of := must be unique.
```go
x := 10
var z *int

if true {
	x := 10
	z = &x
}

&x == z // false

// TODO: provide more examples here
```

Short variable declarations may appear only inside functions. In some contexts such as the initializers for `if`, `for`, or `switch` statements, they ==can be used to declare local temporary variables==.

### Function declarations
A function declaration ==binds an identifier, the function name, to a function==.

If the function's signature declares result parameters, the function body's statement list ==must end in a terminating statement==.

If the function declaration specifies type parameters, the function name denotes a `generic function`. A `generic function` ==must be instantiated before it can be called or used as a value==.

A function declaration ==without type parameters may omit the body==. Such a declaration provides the signature ==for a function implemented outside Go==, such as an assembly routine. Example:
```go
func flushICache(begin, end uintptr)
```

### Method declarations
A method is a ==function with a receiver==. A method declaration ==binds an identifier, the method name, to a method==, and ==associates the method with the receiver's base type==.

The receiver is specified via an extra parameter section preceding the method name. That parameter section must ==declare a single non-variadic parameter, the receiver==. Its type must be a ==defined type T or a pointer to a defined type T==, possibly followed by a list of type parameter names `[P1, P2, …]` enclosed in square brackets. `T` is called the ==receiver base type==. A receiver base type ==cannot be a pointer or interface type== and it ==must be defined in the same package as the method==. The method is said to be bound to its receiver base type and the method name is visible only within selectors for type `T` or `*T`.

A ==non-blank receiver identifier must be unique== in the method signature. If the receiver's value is not referenced inside the body of the method, ==its identifier may be omitted in the declaration==. The same applies in general to parameters of functions and methods.

For a base type, the non-blank names of methods bound to it must be unique. If the ==base type is a `struct` type==, the ==non-blank method and field names must be distinct==.

In the following example receiver type is `*Point`, and the base type is `Point`, and it binds `Length` to it.
```go
func (p *Point) Length() float64 {
	return math.Sqrt(p.x * p.x + p.y * p.y)
}
```

If the receiver base type is a generic type, the receiver specification ==must declare corresponding type parameters for the method== to use. This makes the receiver type parameters available to the method. Syntactically, this type parameter declaration looks like an instantiation of the receiver base type: the type arguments must be identifiers denoting the type parameters being declared, one for each type parameter of the receiver base type. ==The type parameter names do not need to match their corresponding parameter names in the receiver base type definition==, and ==all non-blank parameter names must be unique== in the receiver parameter section ==and the method signature==. The ==receiver type parameter constraints are implied by the receiver base type definition==: corresponding type parameters have corresponding constraints.

> [!warning] Generic alias method restriction
> If the receiver type is denoted by (a pointer to) an alias, the alias must not be generic and it must not denote an instantiated generic type, neither directly nor indirectly via another alias, and irrespective of pointer indirections.
> ```go
>type GPoint[P any] = Point
>type IPair         = Pair[int, int]
>
>func (*GPoint[P]) Draw(P)   { … }  // illegal: alias must not be generic
>func (*IPair) Second() int  { … }  // illegal: alias must not denote instantiated type Pair[int, int]
>```
## Expressions
An expression specifies the computation of a value by applying operators and functions to operands.
### Operands
Operands denote the elementary values in an expression. An operand may be: 
 - literal
 - (possibly qualified) non-blank identifier denoting a constant
 - variable
 - function
 - parenthesized expression.

An operand name denoting a generic function may be followed by a list of type arguments. The resulting operand is an instantiated function.

The `blank identifier` may appear as an operand only on the ==left-hand side of an assignment statement==.

A compiler ==will not report an error if an operand's type is a type parameter with an empty type set==. Functions with such type parameters cannot be instantiated; any attempt will lead to an error at the instantiation site:
```go
type Empty interface {
	~int
	~string
}

func f[T Empty](x T) // will not return an error
```

### Qualified identifier
A qualified identifier is an ==identifier qualified with a package name prefix==. Both the package name and the identifier must not be blank.

A qualified identifier accesses an identifier in a different package, which must be imported. The identifier must be exported and declared in the package block of that package.

### Composite literals
Composite literals construct new values for structs, arrays, slices, and maps each time they are evaluated. They consist of the type of the literal followed by a brace-bound list of elements. Each element may optionally be preceded by a corresponding key. 

Unless the LiteralType is a type parameter, its underlying type must be a struct, array, slice, or map type (the syntax enforces this constraint except when the type is given as a TypeName). If the LiteralType is a type parameter, ==all types in its type set must have the same underlying type== which must be a valid composite literal type. The types of the elements and keys must be assignable to the respective field, element, and key types of type `T`. There is no additional conversion. The key is interpreted as a field name for struct literals, an index for array and slice literals, and a key for map literals. For ==map literals, all elements must have a key==. ==It is an error to specify multiple elements with the same field name or constant key value==. For non-constant map keys, see the section on evaluation order.

For struct literals the following rules apply:
 - A key must be a field name declared in the struct type.
 - An element list that does not contain any keys must list an element for each struct field in the order in which the fields are declared.
 - If any element has a key, every element must have a key.
 - An element list that contains keys does not need to have an element for each struct field. Omitted fields get the zero value for that field.
 - A literal ==may omit the element list==; such a literal evaluates to the zero value for its type.
 - It is an error to specify an element for a non-exported field of a struct belonging to a different package.

For array and slice literals the following rules apply:
 - Each element has an associated integer index marking its position in the array.
 - An element with a key uses the key as its index. The key must be a non-negative constant representable by a value of type int; and if it is typed it must be of integer type.
 - An ==element without a key uses the previous element's index plus one. If the first element has no key, its index is zero==.

Taking the address of a composite literal ==generates a pointer to a unique variable initialized with the literal's value==. `var pointer *Point3D = &Point3D{y: 1000}`

Note that the zero value for a slice or map type is not the same as an initialized but empty value of the same type. Consequently, taking the address of an empty slice or map composite literal does not have the same effect as allocating a new slice or map value with `new`.
```go
p1 := &[]int{}    // p1 points to an initialized, empty slice with value []int{} and length 0
p2 := new([]int)  // p2 points to an uninitialized slice with value nil and length 0
```

The length of an array literal is the length specified in the literal type. If fewer elements than the length are provided in the literal, the ==missing elements are set to the zero value for the array element type==. It is an ==error to provide elements with index values outside the index range of the array==. 

The notation `...` specifies an array length equal to the maximum element index plus one (equals to the amount of elements): `[...]string{"", ""}  // len = 2`

A slice literal describes the entire underlying array literal. Thus the ==length and capacity of a slice literal are the maximum element index plus one==. A slice literal has the form `[]T{x1, x2, … xn}` and is shorthand for a slice operation applied to an array:
```go
tmp := [n]T{x1, x2, … xn}
tmp[0 : n]
```

Within a composite literal of array, slice, or map type `T`, elements or map keys that are themselves composite literals may elide the respective literal type if it is identical to the element or key type of `T`. Similarly, elements or keys that are addresses of composite literals may elide the `&T` when the element or key type is `*T`.
```go
[2]Point{{1.5, -3.5}, {}} // same as [2]Point{Point{1.5, -3.5}, Point{}}
[2]*Point{{1.5, -3.5}, {}} // same as [2]*Point{&Point{1.5, -3.5}, &Point{}}
```

A parsing ambiguity arises when a composite literal using the `TypeName` form of the `LiteralType` appears as an operand between the keyword and the opening brace of the block of an `if`, `for`, or `switch` statement, and the composite literal is not enclosed in parentheses, square brackets, or curly braces. In this rare case, the opening brace of the literal is erroneously parsed as the one introducing the block of statements. To resolve the ambiguity, the composite literal must appear within parentheses.
```go
if x == (T{a,b,c}[i]) { … }
if (x == T{a,b,c}[i]) { … }
```

Some examples of literals:
```go
// list of prime numbers
primes := []int{2, 3, 5, 7, 9, 2147483647}

// vowels[ch] is true if ch is a vowel
vowels := [128]bool{'a': true, 'e': true, 'i': true, 'o': true, 'u': true, 'y': true}


// the array [10]float32{-1, 0, 0, 0, -0.1, -0.1, 0, 0, 0, -1}
filter := [10]float32{-1, 4: -0.1, -0.1, 9: -1}

// frequencies in Hz for equal-tempered scale (A4 = 440Hz)
noteFrequency := map[string]float32{
	"C0": 16.35, "D0": 18.35, "E0": 20.60, "F0": 21.83,
	"G0": 24.50, "A0": 27.50, "B0": 30.87,
}
```

### Function literals
A function literal ==represents an anonymous function==. Function literals cannot declare type parameters (may not be generic).

A function literal can be assigned to a variable or invoked directly.
```go
f := func(x, y int) int { return x + y }
func(ch chan int) { ch <- ACK }(replyChan)
```

==Function literals are closures==: they may refer to variables defined in a surrounding function. Those variables are then shared between the surrounding function and the function literal, and they survive as long as they are accessible.
### Primary expressions
Primary expressions are the ==operands for unary and binary expressions==.
```go
x
2
(s + ".txt")
f(3.1415, true)
Point{1, 2}
m["foo"]
s[i : j + 1]
obj.color
f.p[i].x()
```
### Selectors
For a primary expression `x` that is not a package name, the selector expression `x.f` denotes the field or method `f` of the value `x` or `*x`. The identifier `f` is called the (field or method) selector; it must not be the blank identifier. The type of the selector expression is the type of `f`. If `x` is a package name, then it's a qualified identifiers.

A selector f may denote a field or method `f` of a type `T`, or it may refer to a field or method `f` of a nested embedded field of `T`. The number of embedded fields traversed to reach `f` is called its ==depth in `T`==. The depth of a field or method `f` declared in `T` is zero. The depth of a field or method `f` declared in an embedded field `A` in `T` is the depth of `f` in `A` plus one.

The following rules apply to selectors:
 - For a value `x` of type `T` or `*T` where `T` is not a pointer or interface type, `x.f` denotes the field or method at the shallowest depth in `T` where there is such an `f`. ==If there is not exactly one `f` with shallowest depth, the selector expression is illegal==.
 - For a value `x` of type `I` where `I` is an interface type, `x.f` denotes the actual method with name `f` of the dynamic value of `x`. If there is no method with name `f` in the method set of `I`, the selector expression is illegal.
 - As an exception, if the type of `x` is a defined pointer type and `(*x).f` is a valid selector expression denoting a field (but not a method), `x.f` is shorthand for `(*x).f`.
 - In all other cases, `x.f` is illegal.
 - If `x` is of pointer type and has the value nil and `x.f` denotes a struct field, assigning to or evaluating `x.f` ==causes a run-time panic==.
 - If `x` is of interface type and has the value `nil`, calling or evaluating the method `x.f` ==causes a run-time panic==.

### Method expressions
If `M` is in the method set of type `T`, `T.M` is a function that is ==callable as a regular function== with the same arguments as `M` prefixed by an additional argument that is the receiver of the method.

`T` is a type, `Mv` is a value receiver method, `Mp` is a pointer receiver method.
```go
func (tv  T) Mv(a int) int // equals to func(tv T, a int) int
func (tp *T) Mp(f float32) float32 // equals to func(tp *T, f float32) float32
```

A value-receiver function for a pointer-receiver method is illegal because pointer-receiver methods are not in the method set of the value type.

It is legal to derive a function value from a method of an interface type. The resulting function takes an explicit receiver of that interface type.

You can get struct method and use it in the code:
```go
type Greeter interface {
	Greet(name string) string
}

var g Greeter = englishGreeter{}

// Derive a function value from an interface method
f := Greeter.Greet

// The receiver is now an explicit parameter of type Greeter
fmt.Println(f(g, "Alice"))
```
### Method values
If the expression `x` has static type `T` and `M` is in the method set of type `T`, `x.M` is called a method value. The method value `x.M` is a function value that is callable with the same arguments as a method call of `x.M`. The expression `x` is evaluated and saved during the evaluation of the method value; the saved copy is then used as the receiver in any calls, which may be executed later.

The type `T` may be an interface or non-interface type.

As with selectors, a reference to a non-interface method with a value receiver using a pointer will ==automatically dereference that pointer==: `pt.Mv` is equivalent to `(*pt).Mv`.

As with method calls, a reference to a non-interface method with a pointer receiver using an addressable value will automatically take the address of that value: `t.Mp` is equivalent to `(&t).Mp`.

Although the examples above use non-interface types, it is also ==legal to create a method value from a value of interface type==.
```go
var i interface { M(int) } = myVal
f := i.M; f(7)  // like i.M(7)
```
### Index expressions
A primary expression of the form `a[x]` ==denotes the element of the array, pointer to array, slice, string or map a indexed by x==. The value `x` is called the ==index or map key==, respectively. 

If a is neither a map nor a type parameter:
 - the index x must be an untyped constant, or its type must be an integer or a type parameter whose type set contains only integer types
 - a constant index must be non-negative and representable by a value of type int
 - a constant index that is untyped is given type int
 - the index x is in range `if 0 <= x < len(a)`, otherwise it is out of range

For a of array type `A`:
 - a constant index must be in range
 - if x is out of range at run time, a ==run-time panic occurs==.
 - `a[x]` is the array element at index `x` and the type of `a[x]` is the element type of `A`.

For a of pointer to array type:
 - `a[x]` is shorthand for `(*a)[x]`

For a of slice type `S`:
 - if `x` is out of range at run time, a ==run-time panic occurs==
 - `a[x]` is the slice element at index `x` and the type of `a[x]` is the element type of `S`

For a of string type:
 - a constant index must be in range if the string `a` is also constant
 - if `x` is out of range at run time, a ==run-time panic occurs==
 - `a[x]` is the non-constant byte value at index x and the type of `a[x]` is `byte`
 - `a[x]` ==may not be assigned to==

For a of map type `M`:
 - `x`'s type must be assignable to the key type of `M`
 - if the map contains an entry with key `x`, `a[x]` is the map element with key x and the type of `a[x]` is the element type of `M`
 - if the map is nil or does not contain such an entry, `a[x]` is the ==zero value for the element type of M==

For a of type parameter type `P`:
 - The index expression `a[x]` must be valid for values of all types in `P`'s type set.
 - The element types of all types in `P`'s type set must be identical. In this context, the element type of a string type is byte.
 - If there is a map type in the type set of `P`, all types in that type set must be map types, and the respective key types must be all identical.
 - `a[x]` is the array, slice, or string element at index x, or the map element with key `x` of the type argument that `P` is instantiated with, and the type of `a[x]` is the type of the (identical) element types.
 - `a[x]` may not be assigned to if `P`'s type set includes string types.

==Otherwise `a[x]` is illegal==.

An index expression on a map a of type `map[K]V` used in an assignment statement or initialization of the special form ==yields an additional untyped boolean value==. The value of ok is `true` if the key `x` is present in the map, and `false` otherwise.
```go
v, ok = a[x]
v, ok := a[x]
var v, ok = a[x]
```

==Assigning to an element of a nil map causes a run-time panic==.
### Slice expressions
Slice expressions ==construct a substring or slice from a string, array, pointer to array, or slice operand==. There are two variants: a ==simple form that specifies a low and high bound==, and a ==full form that also specifies a bound on the capacity==.

If the operand type is a type parameter, unless its type set contains string types, all types in the type set must have the same underlying type, and the slice expression must be valid for an operand of that type. If the type set contains string types it may also contain byte slices with underlying type `[]byte`. In this case, the slice expression must be valid for an operand of `string` type.
#### Simple slice expressions
For a string, array, pointer to array, or slice a, the primary expression `a[low : high]` ==constructs a substring or slice==. The indices `low` and `high` select which elements of operand a appear in the result. The result has indices starting at `0` and length equal to `high - low`. After slicing the array `a := [5]int{1, 2, 3, 4, 5}` using `s := a[1:4]` the slice `s` has type `[]int`, length 3, capacity 4, and elements `2, 3, 4` with indexes `0, 1, 2`.

For convenience, ==any of the indices may be omitted==. A missing low index defaults to zero; a missing high index defaults to the length of the sliced operand.

If `a` is a pointer to an array, `a[low : high]` is shorthand for `(*a)[low : high]`.

For arrays or strings, the indices are in range if `0 <= low <= high <= len(a)`, otherwise they are out of range. ==For slices, the upper index bound is the slice capacity== rather than the length. A constant index must be non-negative and representable by a ==value of type int==; for arrays or constant strings, constant indices must also be in range. If both indices are constant, they must satisfy `low <= high`. If the indices are out of range at run time, a run-time panic occurs.

Except for untyped strings, if the sliced operand is a string or slice, the result of the slice operation ==is a non-constant value of the same type as the operand==. For untyped string operands the result is a non-constant value of type string. If the sliced operand is an array, it must be addressable and the result of the slice operation is a ==slice with the same element type as the array==.

If the sliced operand of a valid slice expression is a `nil` slice, the result is a `nil` slice. Otherwise, if the result is a slice, it ==shares its underlying array with the operand==. (underlying type of slice is an array).

#### Full slice expressions
For an array, pointer to array, or slice a (but not a string), the primary expression `a[low : high : max]` constructs a slice of the same type, and with the same length and elements as the simple slice expression `a[low : high]`. Additionally, it ==controls the resulting slice's capacity by setting it to max - low==. Only the first index may be omitted; it defaults to 0. 

### Type assertions
For an expression `x` of interface type, but not a type parameter, and a type `T`, the primary expression `x.(T)` ==asserts that x is not nil and that the value stored in x is of type T==. The notation `x.(T)` is called a type assertion.

More precisely, if `T` is not an interface type, `x.(T)` asserts that the dynamic type of `x` is identical to the type `T`. In this case, `T` must implement the (interface) type of `x`; otherwise the type assertion is invalid since it is not possible for `x` to store a value of type `T`. If `T` is an interface type, `x.(T)` asserts that the dynamic type of `x` implements the interface `T`.

==If it's not, then run-time panic occurs.==

A type assertion used in an assignment statement or initialization of the special form `v, ok := x.(T)` or `var v, ok interface{} = x.(T) // dynamic types of v and ok are T and bool` yields an additional untyped boolean value. The value of `ok` is `true` if the assertion holds. Otherwise it is false and the value of `v` is the zero value for type `T`. ==No run-time panic occurs in this case==.

### Calls
Given an expression `f` of function type `F` `f(a1, a2, … an)` calls `f` with arguments `a1, a2, … an`. Except for one special case, arguments must be single-valued expressions assignable to the parameter types of `F` and are evaluated before the function is called. The type of the expression is the result type of `F`. A method invocation is similar but the method itself is specified as a selector upon a value of the receiver type for the method.

If `f` denotes a generic function, it ==must be instantiated before it can be called or used as a function value==.

If the type of `f` is a type parameter, all types in its type set must have the same underlying type, which must be a function type, and the function call must be valid for that type.

In a function call, the function value and arguments are evaluated in the usual order. After they are evaluated, new storage is allocated for the function's variables, which includes its parameters and results. Then, the arguments of the call are passed to the function, which means that they are assigned to their corresponding function parameters, and the called function begins execution. The return parameters of the function are passed back to the caller when the function returns.

==Calling a nil function value causes a run-time panic==.

As a special case, if the return values of a function or method `g` are equal in number and individually assignable to the parameters of another function or method `f`, then the call `f(g(parameters_of_g))` will invoke `f` after passing the return values of `g` to the parameters of `f` in order. The call of `f` must contain no parameters other than the call of `g`, and `g` must have at least one return value. If `f` has a final `...` parameter, it is assigned the return values of `g` that remain after assignment of regular parameters.
```go
func Split(s string, pos int) (string, string) {
	return s[0:pos], s[pos:]
}

func Join(s, t string) string {
	return s + t
}

res := Join(Split(value, len(value)/2))
```

A method call `x.m()` is valid if the method set of (the type of) `x` contains `m` and the argument list can be assigned to the parameter list of `m`. If `x` is addressable and `&x`'s method set contains `m`, `x.m()` is shorthand for `(&x).m()`.

==There is no distinct method type and there are no method literals==.
### Passing arguments to ... parameters
If `f` is variadic with a final parameter p of type `...T`, then within `f` the type of `p` is equivalent to type `[]T`. ==If `f` is invoked with no actual arguments for `p`, the value passed to `p` is `nil`==. Otherwise, the value passed is a new slice of type `[]T` with a new underlying array whose successive elements are the actual arguments, which all must be assignable to `T`. The ==length and capacity of the slice is therefore the number of arguments== bound to `p` and may differ for each call site.
### Instantiations
A generic function or type is instantiated by substituting type arguments for the type parameters. Instantiation proceeds in two steps:
 - Each type argument is substituted for its corresponding type parameter in the generic declaration. This substitution happens across the entire function or type declaration, including the type parameter list itself and any types in that list.
 - After substitution, each type argument must satisfy the constraint (instantiated, if necessary) of the corresponding type parameter. Otherwise instantiation fails.

Instantiating a type results in a new non-generic named type; instantiating a function produces a new non-generic function.

==Type argument lists may be omitted entirely if the function is==:
 - called with ordinary arguments,
 - assigned to a variable with a known type
 - passed as an argument to another function, or
 - returned as a result.

In all other cases, a (possibly partial) type argument list must be present. If a type argument list is absent or partial, ==all missing type arguments must be inferrable from the context== in which the function is used.
```go
// sum returns the sum (concatenation, for strings) of its arguments.
func sum[T ~int | ~float64 | ~string](x... T) T { … }

x := sum                       // illegal: the type of x is unknown
intSum := sum[int]             // intSum has type func(x... int) int
a := intSum(2, 3)              // a has value 5 of type int
b := sum[float64](2.0, 3)      // b has value 5.0 of type float64
c := sum(b, -1)                // c has value 4.0 of type float64

type sumFunc func(x... string) string
var f sumFunc = sum            // same as var f sumFunc = sum[string]
f = sum                        // same as f = sum[string]
```

==A partial type argument list cannot be empty==; at least the first argument must be present. The list is a prefix of the full list of type arguments, leaving the remaining arguments to be inferred.
```go
func apply[S ~[]E, E any](s S, f func(E) E) S { … }

f0 := apply[]                  // illegal: type argument list cannot be empty
f1 := apply[[]int]             // type argument for S explicitly provided, type argument for E inferred
f2 := apply[[]string, string]  // both type arguments explicitly provided

var bytes []byte
r := apply(bytes, func(byte) byte { … })  // both type arguments inferred from the function arguments
```

==For a generic type, all type arguments must always be provided explicitly==.
### Type inference
A use of a generic function may omit some or all type arguments if they can be inferred from the context within which the function is used, including the constraints of the function's type parameters. Type inference succeeds if it can infer the missing type arguments and instantiation succeeds with the inferred type arguments. Otherwise, type inference fails and the program is invalid.

Type inference uses the type relationships between pairs of types for inference: For instance, a function argument must be assignable to its respective function parameter; this establishes a relationship between the type of the argument and the type of the parameter. If either of these two types contains type parameters, type inference looks for the type arguments to substitute the type parameters with such that the assignability relationship is satisfied. Similarly, type inference uses the fact that a type argument must satisfy the constraint of its respective type parameter.

Each such pair of matched types corresponds to a type equation containing one or multiple type parameters, from one or possibly multiple generic functions. Inferring the missing type arguments means solving the resulting set of type equations for the respective type parameters.

Given a set of type equations, the type parameters to solve for are the type parameters of the functions that need to be instantiated and for which no explicit type arguments is provided. ==These type parameters are called bound type parameters==. An ==argument to a generic function call may be a generic function itself==. The type parameters of that function are included in the set of bound type parameters. The types of function arguments may contain type parameters from other functions (such as a generic function enclosing a function call). Those type parameters may also appear in type equations but they are not bound in that context. Type equations are always solved for the bound type parameters only.

Type inference supports calls of generic functions and assignments of generic functions to (explicitly function-typed) variables. This includes passing generic functions as arguments to other (possibly also generic) functions, and returning generic functions as results. Type inference operates on a set of equations specific to each of these cases. The equations are as follows (type argument lists are omitted for clarity):
 - For a function call `f(a0, a1, …)` where `f` or a function argument `ai` is a generic function:
 - Each pair `(ai, pi)` of corresponding function arguments and parameters where `ai` is not an untyped constant yields an equation `typeof(pi) ≡A typeof(ai)`.
 - If `ai` is an untyped constant `cj`, and `typeof(pi)` is a bound type parameter `Pk`, the pair `(cj, Pk)` is collected separately from the type equations.
 - For an assignment `v` = `f` of a generic function `f` to a (non-generic) variable `v` of function type: `typeof(v) ≡A typeof(f)`.
 - For a return statement return `…,` `f`, `…` where `f` is a generic function returned as a result to a (non-generic) result variable `r` of function type: `typeof(r) ≡A typeof(f)`.

Type inference gives precedence to type information obtained from typed operands before considering untyped constants. Therefore, ==inference proceeds in two phases==:
- The type equations are solved for the bound type parameters using type unification. If unification fails, type inference fails.
- For each bound type parameter `Pk` for which no type argument has been inferred yet and for which one or more pairs `(cj, Pk)` with that same type parameter were collected, determine the constant kind of the constants `cj` in all those pairs the same way as for constant expressions. The type argument for `Pk` is the default type for the determined constant kind. If a constant kind cannot be determined due to conflicting constant kinds, type inference fails.

If not all type arguments have been found after these two phases, type inference fails.

If type arguments contain cyclic references to themselves through bound type parameters, simplification and thus type inference fails. Otherwise, type inference succeeds.
### Type unification
Type inference solves type equations through type unification. Type unification recursively compares the `LHS` and `RHS` (left and right hand size) types of an equation, where either or both types may be or contain bound type parameters, and looks for type arguments for those type parameters such that the `LHS` and `RHS` match (become identical or assignment-compatible, depending on context). To that effect, ==type inference maintains a map of bound type parameters to inferred type arguments; this map is consulted and updated during type unification==. Initially, the bound type parameters are known but the map is empty. During type unification, if a new type argument `A` is inferred, the respective mapping `P ➞ A` from type parameter to argument is added to the map. Conversely, when comparing types, a known type argument (a type argument for which a map entry already exists) takes the place of its corresponding type parameter. As type inference progresses, the map is populated more and more until all equations have been considered, or until unification fails. Type inference succeeds if no unification step fails and the map has an entry for each type parameter.

For example, type unification solves the problem when 2 function args have generic type `T`, and provided arguments have different from `T` types, which is incorrect.
### Operators
Operators combine operands into expressions. For different from comparison binary operators (they are discussed below), the operand types must be identical unless the operation involves shifts or untyped constants. For operations involving constants only, see the section on constant expressions.

Except for shift operations, if one operand is an untyped constant and the other operand is not, the ==constant is implicitly converted to the type of the other operand==.

The right operand in a shift expression must have integer type or be an untyped constant representable by a value of type uint. If the left operand of a non-constant shift expression is an untyped constant, it is first implicitly converted to the type it would assume if the shift expression were replaced by its left operand alone.
#### Operator precedence
Unary operators have the ==highest precedence==. As the `++` and `--` operators form statements, not expressions, they fall outside the operator hierarchy. As a consequence, statement `*p++` is the same as `(*p)++`.

There are five precedence levels for binary operators (higher = more important):
```
Precedence    Operator
    5             *  /  %  <<  >>  &  &^
    4             +  -  |  ^
    3             ==  !=  <  <=  >  >=
    2             &&
    1             ||
```
Binary operators of the same precedence associate from left to right. For instance, `x / y * z` is the same as `(x / y) * z`.
#### Arithmetic operators
Arithmetic operators apply to numeric values and yield a result of the same type as the first operand. The four standard arithmetic operators `(+, -, *, /)` ==apply to integer, floating-point, and complex types; + also applies to strings==. The ==bitwise logical and shift operators apply to integers only==.
```
+    sum                    integers, floats, complex values, strings
-    difference             integers, floats, complex values
*    product                integers, floats, complex values
/    quotient               integers, floats, complex values
%    remainder              integers

&    bitwise AND            integers
|    bitwise OR             integers
^    bitwise XOR            integers
&^   bit clear (AND NOT)    integers

<<   left shift             integer << integer >= 0
>>   right shift            integer >> integer >= 0
```

If the operand type is a type parameter, the ==operator must apply to each type in that type set==. The operands are represented as values of the type argument that the type parameter is instantiated with, and the operation is computed with the precision of that type argument.
#### Integer operations
If the divisor is a constant, it must not be zero. If the divisor is zero at run time, a run-time panic occurs.

If the dividend x is the most negative value for the int type of x, the quotient q = x / -1 is equal to x (and r = 0) due to two's-complement integer overflow

The shift operators shift the left operand by the shift count specified by the right operand, which must be non-negative. If the shift count is negative at run time, a run-time panic occurs.
#### Integer overflow
For signed integers, the operations `+, -, *, /, <<` may legally overflow and the resulting value exists and is deterministically defined by the signed integer representation, the operation, and its operands. ==Overflow does not cause a run-time panic==. A compiler may not optimize code under the assumption that overflow does not occur. For instance, it may not assume that `x < x + 1` is always true.
#### Floating-point operations
For floating-point and complex numbers, `+x` is the same as `x`, while `-x` is the negation of `x`. The result of a floating-point or complex division by zero is not specified beyond the `IEEE 754` standard; whether a run-time panic occurs is implementation-specific.
#### Strings concatenation
Strings can be concatenated using the `+` operator or the `+=` assignment operator. String addition creates a new string by concatenating the operands.
#### Comparison operators
Comparison operators compare two operands and yield an untyped boolean value.
```
==    equal
!=    not equal
<     less
<=    less or equal
>     greater
>=    greater or equal
```
In any comparison, the first operand ==must be assignable to the type of the second operand==, or vice versa.

The equality operators `==` and `!=` ==apply to operands of comparable types==. The ordering operators `<, <=, >, >=` apply to operands of ==ordered types==. These terms and the result of the comparisons are defined as follows:
- Boolean types are comparable.
- Integer types are comparable and ordered. 
- Floating-point types are comparable and ordered. Two floating-point values are compared as defined by the IEEE 754 standard.
- Complex types are comparable. Two complex values `u` and `v` are equal if both` real(u) == real(v) && imag(u) == imag(v)`.
- String types are comparable and ordered. Two string values are compared lexically byte-wise.
- Pointer types are comparable. Two pointer values are equal if they point to the same variable or if both have value nil. Pointers to ==distinct zero-size variables may or may not be equal==.
- Channel types are comparable. Two channel values are equal if they were created by the same call to make or if both have value nil.
- ==Interface types that are not type parameters are comparable==. Two interface values are equal if they have identical dynamic types and equal dynamic values or if both have value nil.
- A value `x` of non-interface type `X` and a value `t` of interface type `T` can be compared if type `X` is comparable and `X` implements `T`. They are equal if t's dynamic type is identical to `X` and `t`'s dynamic value is equal to `x`.
- ==Struct types are comparable if all their field types are comparable==. Two struct values are equal if their corresponding non-blank field values are equal. The fields are compared in source order.
- ==Array types are comparable if their array element types are comparable==. Two array values are equal if their corresponding element values are equal. The elements are compared in ascending index order.
 - Type parameters are comparable if they are strictly comparable (see below).

A comparison of two interface values with ==identical dynamic types causes a run-time panic== if that type is not comparable. This behavior applies not only to direct interface value comparisons but also when comparing arrays of interface values or structs with interface-valued fields.

As a special case, a `slice`, `map`, or `function` value may be compared to the predeclared identifier `nil`. Comparison of `pointer`, `channel`, and `interface` values to `nil` is also allowed and follows from the general rules above.

A type is `strictly comparable` if it is comparable and not an interface type nor composed of interface types. Specifically:
- Boolean, numeric, string, pointer, and channel types are strictly comparable.
- Struct types are strictly comparable if all their field types are strictly comparable.
- Array types are strictly comparable if their array element types are strictly comparable.
- Type parameters are strictly comparable if all types in their type set are strictly comparable.
#### Logical operators
Logical operators ==apply to boolean values and yield a result of the same type as the operands==. The left operand is evaluated, and then the right if the condition requires it.
```
&&    conditional AND    p && q  is  "if p then q else false"
||    conditional OR     p || q  is  "if p then true else q"
!     NOT                !p      is  "not p"
```
#### Adress operators
For an operand `x` of type `T`, the address operation `&x` generates a pointer of type `*T` to `x`. The operand must be `addressable`, that is, either a variable, pointer indirection, or slice indexing operation; or a field selector of an addressable struct operand; or an array indexing operation of an addressable array. As an exception to the addressability requirement, `x` may also be a (possibly parenthesized) composite literal. If the evaluation of `x` would cause a run-time panic, then the evaluation of `&x` does too.

==If `x` is `nil`, an attempt to evaluate `*x` will cause a run-time panic==.
#### Receive operators
For an operand `ch` of `channel type`, the value of the receive operation `<-ch` is the value received from the channel `ch`. The channel direction must permit receive operations, and the type of the receive operation is the element type of the channel. The ==expression blocks until a value is available==. ==Receiving from a nil channel blocks forever==. ==A receive operation on a closed channel can always proceed immediately==, yielding the element type's zero value after any previously sent values have been received.

If the operand type is a type parameter, all types in its type set must be channel types that permit receive operations, and they must all have the same element type, which is the type of the receive operation.

A receive expression used in an assignment statement or initialization of the special form `x, ok := <-ch` yields an additional untyped boolean result reporting whether the communication succeeded. The value of `ok` is `true` if the value received was delivered by a successful send operation to the channel, or `false` if it is a zero value generated because the channel is closed and empty.

### Conversions
A conversion changes the type of an expression to the type specified by the conversion. A conversion may appear literally in the source, or it may be implied by the context in which an expression appears.

An explicit conversion is an expression of the form `T(x)` where `T` is a type and `x` is an expression that can be converted to type `T`.

If the type starts with the operator `*` or `<-`, or if the type starts with the keyword func and has no result list, it must be parenthesized when necessary to avoid ambiguity:
```go
*Point(p)        // same as *(Point(p))
(*Point)(p)      // p is converted to *Point
<-chan int(c)    // same as <-(chan int(c))
(<-chan int)(c)  // c is converted to <-chan int
func()(x)        // function signature func() x
(func())(x)      // x is converted to func()
(func() int)(x)  // x is converted to func() int
func() int(x)    // x is converted to func() int (unambiguous)
```

A constant value x can be converted to type `T` if `x` is representable by a value of `T`. As a special case, an integer constant `x` can be explicitly converted to a string type using the same rule as for non-constant `x`.

Converting a constant to a type that is not a type parameter yields a typed constant.
```
uint(iota)               // iota value of type uint
float32(2.718281828)     // 2.718281828 of type float32
```

Converting a constant to a type parameter ==yields a non-constant value of that type==, with the value represented as a value of the type argument that the type parameter is instantiated with. For example, given the function:
```go
func f[P ~float32|~float64]() {
	… P(1.1) …
}
```
the conversion `P(1.1)` results in a non-constant value of type `P` and the value `1.1` is represented as a `float32` or a `float64` depending on the type argument for `f`.

A non-constant value `x` can be converted to type `T` in any of these cases:
- x is assignable to T.
- ignoring struct tags (see below), x's type and T are not type parameters but have identical underlying types.
- ignoring struct tags (see below), x's type and T are pointer types that are not named types, and their pointer base types are not type parameters but have identical underlying types.
- x's type and T are both integer or floating point types.
- x's type and T are both complex types.
- x is an integer or a slice of bytes or runes and T is a string type.
- x is a string and T is a slice of bytes or runes.
- x is a slice, T is an array or a pointer to an array, and the slice and array types have identical element types.

Additionally, if T or x's type V are type parameters, x can also be converted to type T if one of the following conditions applies:
- Both V and T are type parameters and a value of each type in V's type set can be converted to each type in T's type set.
- Only V is a type parameter and a value of each type in V's type set can be converted to T.
- Only T is a type parameter and x can be converted to each type in T's type set.

==Struct tags are ignored when comparing struct types for identity for the purpose of conversion==.

Specific rules apply to (non-constant) conversions between numeric types or to and from a string type. ==These conversions may change the representation of x and incur a run-time cost==. ==All other conversions only change the type but not the representation of x==.

There is no linguistic mechanism to convert between pointers and integers. The package unsafe implements this functionality under restricted circumstances.
#### Conversion between numeric types
For the conversion of non-constant numeric values, the following rules apply:
- When converting between integer types, if the value is a signed integer, it is sign extended to implicit infinite precision; otherwise it is zero extended. It is then truncated to fit in the result type's size. There is no indication of overflow.
- When converting a floating-point number to an integer, the ==fraction is discarded== (truncation towards zero).
- When converting an integer or floating-point number to a floating-point type, or a complex number to another complex type, the result value is rounded to the precision specified by the destination type.
#### Conversions to and from a string type
Converting a slice of bytes to a string type yields a string whose successive bytes are the elements of the slice.

Converting a slice of runes to a string type yields a string that is the concatenation of the individual rune values converted to strings.

Converting a value of a string type to a slice of bytes type yields a non-nil slice whose successive elements are the bytes of the string. The ==capacity of the resulting slice is implementation-specific and may be larger than the slice length==.

Converting a value of a string type to a slice of runes type yields a ==slice containing the individual Unicode code points of the string==. The ==capacity of the resulting slice is implementation-specific and may be larger than the slice length==.

 for historical reasons, an integer value may be converted to a string type. This form of conversion yields a string containing the (possibly multi-byte) UTF-8 representation of the Unicode code point with the given integer value. Values outside the range of valid Unicode code points are converted to "\uFFFD".
#### Conversions from slice to array or array pointer
Converting a slice to an array yields an array containing the elements of the underlying array of the slice. Similarly, converting a slice to an array pointer yields a pointer to the underlying array of the slice. In both cases, ==if the length of the slice is less than the length of the array, a run-time panic occurs==.
### Constant expressions
Constant expressions ==may contain only constant operands and are evaluated at compile time==.

Untyped boolean, numeric, and string constants may be used as operands wherever it is legal to use an operand of boolean, numeric, or string type, respectively.

A constant comparison always yields an untyped boolean constant. If the left operand of a constant shift expression is an untyped constant, the result is an integer constant; otherwise it is a constant of the same type as the left operand, which must be of integer type.

Any other operation on untyped constants results in an untyped constant of the same kind. If the untyped operands of a binary operation (other than a shift) are of different kinds, the result is of the operand's kind that appears later in this list.

Applying the built-in function complex to untyped integer, rune, or floating-point constants yields an untyped complex constant.

The values of typed constants must always be accurately representable by values of the constant type.

Implementation restriction: ==A compiler may use rounding while computing untyped floating-point or complex constant expressions==; see the implementation restriction in the section on constants. This rounding may cause a floating-point constant expression to be invalid in an integer context, even if it would be integral when calculated using infinite precision, and vice versa.
### Order of evaluation
At package level, initialization dependencies determine the evaluation order of individual initialization expressions in variable declarations. Otherwise, when evaluating the operands of an expression, assignment, or return statement, all function calls, method calls, receive operations, and binary logical operations are evaluated in ==lexical left-to-right order==.

At package level, initialization dependencies override the left-to-right rule for individual initialization expressions, but not for operands within each expression.
### Statements
Statements control execution.
#### Terminating statements
A terminating statement interrupts the regular flow of control in a block. The following statements are terminating:
- `return` and `goto`
- `panic` call
- A block in which the statement list ends in a terminating statement.
- An "if" statement in which the "else" branch is present, and both branches are terminating statements.
- A "for" statement in which there are no "break" statements referring to the "for" statement, and the loop condition is absent, and it does not use a range clause.
- A "switch" statement in which there are no "break" statements referring to the "switch" statement, there is a default case, and the statement lists in each case, including the default, end in a terminating statement, or a possibly labeled `fallthrough` statement.
- A "select" statement in which there are no "break" statements referring to the "select" statement, and the statement lists in each case, including the default if present, end in a terminating statement.
- A labeled statement labeling a terminating statement.
All other statements are not terminating.
#### Empty statement
Does nothing
#### Labeled statement
A labeled statement may be the target of a `goto`, `break` or `continue` statement.
`Error: log.Panic("error encountered")`
#### Expression statements
With the exception of specific built-in functions, function and method calls and receive operations can appear in statement context. Such statements may be parenthesized.

The following built-in functions are not permitted in statement context: `append cap complex imag len make new real unsafe.Add unsafe.Alignof unsafe.Offsetof unsafe.Sizeof unsafe.Slice unsafe.SliceData unsafe.String unsafe.StringData`
#### Send statements
A send statement sends a value on a channel. The channel expression must be of channel type, the channel direction must permit send operations, and the type of the value to be sent must be assignable to the channel's element type.

Both the channel and the value expression are evaluated before communication begins. Communication blocks until the send can proceed. ==A send on an unbuffered channel can proceed if a receiver is ready==. A ==send on a buffered channel can proceed if there is room in the buffer==. A send on a closed channel proceeds by causing a run-time panic. A send on a nil channel blocks forever.

If the type of the channel expression is a type parameter, all types in its type set must be channel types that permit send operations, they must all have the same element type, and the type of the value to be sent must be assignable to that element type.
#### IncDec statements
The `++` and `--` statements increment or decrement their operands by the untyped constant 1. As with an assignment, the operand must be addressable or a map index expression. `+= 1` and `++`, `-= 1` and `--` are equivalent.
#### Assignment statements
An assignment replaces the current value stored in a variable with a new value specified by an expression. An assignment statement may assign a single value to a single variable, or multiple values to a matching number of variables.

Each left-hand side operand must be addressable, a map index expression, or ==`for =` assignments only it may be the blank identifier==. Operands may be parenthesized.

An assignment operation `x op=` y where `op` is a binary arithmetic operator is equivalent to `x = x op (y)` but evaluates `x` only once. ==The `op=` construct is a single token==. In assignment operations, both the left- and right-hand expression lists must contain exactly one single-valued expression, and the left-hand expression must not be the blank identifier. `a[i] <<= 2`

A tuple assignment assigns the individual elements of a multi-valued operation to a list of variables. There are two forms. In the first, the right hand operand is a single multi-valued expression such as a `function call`, a `channel` or `map` operation, or a `type assertion`. The number of operands on the left hand side must match the number of values. `x, y = f()`

In the second form, the number of operands on the left must equal the number of expressions on the right, each of which must be single-valued, and the nth expression on the right is assigned to the nth operand on the left: `one, two, three = '一', '二', '三'`

The blank identifier provides a way to ignore right-hand side values in an assignment.

The assignment proceeds in two phases. ==First, the operands of index expressions and pointer indirections (including implicit pointer indirections in selectors) on the left and the expressions on the right are all evaluated in the usual order==. Second, the assignments are carried out in ==left-to-right== order.

In assignments, each value must be assignable to the type of the operand to which it is assigned, with the following special cases:
- Any typed value may be assigned to the blank identifier.
- If an untyped constant is assigned to a variable of interface type or the blank identifier, the constant is first implicitly converted to its default type.
- If an untyped boolean value is assigned to a variable of interface type or the blank identifier, it is first implicitly converted to type bool.

When a value is assigned to a variable, only the data that is stored in the variable is replaced. If the value contains a reference, the assignment copies the reference but does not make a copy of the referenced data (such as the underlying array of a slice).
#### if statements
`If` statements specify the conditional execution of two branches according to the value of a boolean expression. If the expression evaluates to true, the `if` branch is executed, otherwise, if present, the `else` branch is executed. The expression may be preceded by a simple statement, which executes before the expression is evaluated.
```go
if x := f(); x < y {
	return x
} else if x > z {
	return z
} else {
	return y
}
```
#### Switch statements
`Switch` statements provide multi-way execution. An expression or type is compared to the `cases` inside the `switch` to determine which branch to execute.

There are two forms: ==expression switches== and ==type switches==. In an expression switch, the cases contain expressions that are compared against the value of the switch expression. In a type switch, the cases contain types that are compared against the type of a specially annotated switch expression. The ==switch expression is evaluated exactly once in a switch statement==.

##### Expression switches
In an expression switch, the switch expression is evaluated and the case expressions, which need not be constants, are evaluated left-to-right and top-to-bottom; ==the first one that equals the switch expression triggers execution of the statements of the associated case==; ==the other cases are skipped==. If no case matches and there is a `default` case, its statements are executed. There can be at most one default case and it may appear anywhere in the `switch` statement. A missing switch expression is equivalent to the boolean value `true`.

If the switch expression evaluates to an untyped constant, it is first implicitly converted to its default type. The predeclared untyped value nil cannot be used as a switch expression. The ==switch expression type must be comparable==.

If a case expression is untyped, it is first implicitly converted to the type of the switch expression. For each (possibly converted) case expression `x` and the value `t` of the switch expression, `x == t` must be a valid comparison.

In a case or default clause, the last non-empty statement may be a (possibly labeled) `fallthrough` statement to indicate that control should flow from the end of this clause to the first statement of the next clause. Otherwise control flows to the end of the `switch` statement. A `fallthrough` statement may appear as the last statement of all but the last clause of an expression switch.
```go
switch tag {
default: s3()
case 0, 1, 2, 3: s1()
case 4, 5, 6, 7: s2()
}

switch x := f(); {  // missing switch expression means "true"
case x < 0: return -x
default: return x
}

switch {
case x < y: f1()
case x < z: f2()
case x == 4: f3()
}
```

Implementation restriction: A compiler may disallow multiple case expressions evaluating to the same constant. For instance, the ==current compilers disallow duplicate integer, floating point, or string constants in case expressions==.
##### Type switches
A type switch ==compares types rather than values==. It is otherwise similar to an expression switch. It is marked by a special switch expression that has the form of a type assertion using the keyword type rather than an actual type:
```go
switch x.(type) {
// cases
}
```

Cases then match actual types `T` against the dynamic type of the expression `x`. As with type assertions, `x` must be of interface type, but not a type parameter, and each non-interface type `T` listed in a case must implement the type of `x`. The types listed in the cases of a type switch must all be different.

The `TypeSwitchGuard` (expression to store type) may include a short variable declaration. When that form is used, the variable is declared at the end of the `TypeSwitchCase` in the implicit block of each clause. In clauses with a case listing exactly one type, the variable has that type; otherwise, the variable has the type of the expression in the `TypeSwitchGuard`.

Instead of a type, a case may use the predeclared identifier `nil`; that case is selected when the expression in the TypeSwitchGuard is a `nil` interface value. There may be at most one `nil` case.
```go
switch i := x.(type) {
case nil:
	printString("x is nil")                // type of i is type of x (interface{})
case int:
	printInt(i)                            // type of i is int
case float64:
	printFloat64(i)                        // type of i is float64
case func(int) float64:
	printFunction(i)                       // type of i is func(int) float64
case bool, string:
	printString("type is bool or string")  // type of i is type of x (interface{})
default:
	printString("don't know the type")     // type of i is type of x (interface{})
}
```

A type parameter or a generic type may be used as a type in a case. If upon instantiation that type turns out to duplicate another entry in the switch, the first matching case is chosen.

The type switch guard may be preceded by a simple statement, which executes before the guard is evaluated.

==The "fallthrough" statement is not permitted in a type switch.==
#### For statements
A "for" statement specifies repeated execution of a block. There are three forms: The iteration may be controlled by a single condition, a `for` clause, or a `range` clause.
##### For statements with single condition
In its simplest form, a "for" statement specifies the repeated execution of a block as long as a boolean condition evaluates to true. ==The condition is evaluated before each iteration==. If the condition is absent, it is equivalent to the boolean value true.
```go
for a < b {
	a *= 2
}
```
##### For statements with for clause
A `for` statement with a `ForClause` is also controlled by its condition, but additionally it may specify an `init` and a `post` statement, such as an assignment, an increment or decrement statement. The init statement may be a short variable declaration, but the post statement must not.

If non-empty, the init statement is executed once before evaluating the condition for the first iteration; the post statement is executed after each execution of the block (and only if the block was executed). ==Any element of the ForClause may be empty but the semicolons are required unless there is only a condition==. If the condition is absent, it is equivalent to the boolean value true.
```go
for i := 0; i < 10; i++ {
	f(i)
}
for cond { S() }    is the same as    for ; cond ; { S() }
for      { S() }    is the same as    for true     { S() }
```

==Each iteration has its own separate declared variable (or variables)==. The variable used by the first iteration is declared by the init statement. The variable used by each subsequent iteration is declared implicitly before executing the post statement and ==initialized to the value of the previous iteration's variable at that moment==.
```go
for i := 0; i < 5; i++ {
	fmt.Println(i)
	i++
}
// prints 0 2 4
```
##### For statements with range clause
A `for` statement with a `range` clause ==iterates through all entries of an array, slice, string or map, values received on a channel, integer values from zero to an upper limit, or values passed to an iterator function's yield function==. For each entry it assigns iteration values to corresponding iteration variables if present and then executes the block.

The expression on the right in the "range" clause is called the range expression, which may be an array, pointer to an array, slice, string, map, channel permitting receive operations, an integer, or a function with specific signature (see below). As with an assignment, if present the operands on the left must be addressable or map index expressions; they denote the iteration variables. If the range expression is a function, the maximum number of iteration variables depends on the function signature. If the range expression is a channel or integer, at most one iteration variable is permitted; otherwise there may be up to two. If the last iteration variable is the blank identifier, the range clause is equivalent to the same clause without that identifier.

The range expression `x` is evaluated before beginning the loop, with one exception: ==if at most one iteration variable is present and `x` or `len(x)` is constant, the range expression is not evaluated==.

Function calls on the left are evaluated once per iteration. For each iteration, iteration values are produced as follows if the respective iteration variables are present:
```go
Range expression                                       1st value                2nd value

array or slice      a  [n]E, *[n]E, or []E             index    i  int          a[i]       E
string              s  string type                     index    i  int          see below  rune
map                 m  map[K]V                         key      k  K            m[k]       V
channel             c  chan E, <-chan E                element  e  E
integer value       n  integer type, or untyped int    value    i  see below
function, 0 values  f  func(func() bool)
function, 1 value   f  func(func(V) bool)              value    v  V
function, 2 values  f  func(func(K, V) bool)           key      k  K            v          V
```

- For an array, pointer to array, or slice value a, the index iteration values are produced in increasing order, starting at element index 0. If at most one iteration variable is present, the range loop produces iteration values from 0 up to len(a)-1 and does not index into the array or slice itself. For a nil slice, the number of iterations is 0.
- For a string value, the "range" clause ==iterates over the Unicode code points in the string== starting at byte index 0. On successive iterations, the index value will be the index of the first byte of successive UTF-8-encoded code points in the string, and the second value, ==of type rune==, will be the value of the corresponding code point. If the iteration encounters an ==invalid UTF-8 sequence, the second value will be 0xFFFD==, the Unicode replacement character, and the next iteration will advance a single byte in the string.
- The ==iteration order over maps is not specified and is not guaranteed to be the same from one iteration to the next==. If a map entry that has not yet been reached is removed during iteration, the ==corresponding iteration value will not be produced==. If a ==map entry is created during iteration, that entry may be produced during the iteration or may be skipped==. The choice may vary for each entry created and from one iteration to the next. If the map is nil, the number of iterations is 0.
- For channels, the iteration values produced are the successive values sent on the channel until the channel is closed. ==If the channel is nil, the range expression blocks forever==.
- For an integer value n, where n is of integer type or an untyped integer constant, the iteration values ==0 through n-1 are produced in increasing order==. If n is of integer type, the iteration values have that same type. Otherwise, the type of ==n is determined as if it were assigned to the iteration variable==. Specifically: if the iteration variable is preexisting, the type of the iteration values is the type of the iteration variable, which must be of integer type. Otherwise, if the iteration variable is declared by the "range" clause or is absent, the type of the iteration values is the default type for n. If n <= 0, the loop does not run any iterations.
- For a function f, the iteration proceeds by calling f with a new, synthesized yield function as its argument. If yield is called before f returns, the arguments to yield become the iteration values for executing the loop body once. After each successive loop iteration, yield returns true and may be called again to continue the loop. As long as the loop body does not terminate, the "range" clause will continue to generate iteration values this way for each yield call until f returns. If the loop body terminates (such as by a break statement), yield returns false and must not be called again.

The iteration variables may be declared by the `range` clause using a form of short variable declaration (`:=`). In this case their scope is the block of the `for` statement and each iteration has its own new variables. The variables have the types of their respective iteration values.

If the iteration variables are not explicitly declared by the "range" clause, they must be preexisting. In this case, the iteration values are assigned to the respective variables as in an assignment statement.

If the type of the range expression is a type parameter, all types in its type set must have the same underlying type and the range expression must be valid for that type.
#### Go statements
A `go` statement starts the execution of a function call as an ==independent concurrent thread of control==, or `goroutine`, within the same address space.

The expression must be a function or method call; it cannot be parenthesized. ==Calls of built-in functions are restricted as for expression statements==.

The function value and parameters are evaluated as usual in the calling `goroutine`, but unlike with a regular call, program execution does not wait for the invoked function to complete. Instead, ==the function begins executing independently in a new `goroutine`==. ==When the function terminates, its `goroutine` also terminates==. ==If the function has any return values, they are discarded when the function completes==.
#### Select statements
A `select` statement chooses which of a set of possible send or receive operations will proceed. It looks similar to a `switch` statement but with the cases all referring to communication operations.

A case with a `RecvStmt` may assign the result of a `RecvExpr` to one or two variables, which may be declared using a short variable declaration. The `RecvExpr` must be a (possibly parenthesized) receive operation. There can be at most one default case and it may appear anywhere in the list of cases.

Execution of a "select" statement proceeds in several steps:

- For all the cases in the statement, the channel operands of receive operations and the channel and right-hand-side expressions of send statements are ==evaluated exactly once==, in source order, upon entering the "select" statement. The result is a set of channels to receive from or send to, and the corresponding values to send. Any side effects in that evaluation will occur irrespective of which (if any) communication operation is selected to proceed. Expressions on the left-hand side of a RecvStmt with a short variable declaration or assignment are not yet evaluated.
- If one or more of the communications can proceed, a single one that can proceed is chosen via a uniform pseudo-random selection. Otherwise, if there is a default case, that case is chosen. If there is no default case, the "select" statement blocks until at least one of the communications can proceed.
- Unless the selected case is the default case, the respective communication operation is executed.
- If the selected case is a RecvStmt with a short variable declaration or an assignment, the left-hand side expressions are evaluated and the received value (or values) are assigned.
- The statement list of the selected case is executed.



# Sources
[The Go Programming Language Specification](https://go.dev/ref/spec) (go version: 1.25)
[Wirth syntax notation](https://en.wikipedia.org/wiki/Wirth_syntax_notation)
[Extended Backus–Naur form](https://en.wikipedia.org/wiki/Extended_Backus–Naur_form)
[Codecademy go strings](https://www.codecademy.com/resources/docs/go/strings)
[Go blog: slices usage and internals](https://go.dev/blog/slices-intro)
[Boldlygo: universal and package identifiers](https://boldlygo.tech/archive/2023-06-22-the-universe-and-package-blocks/)
[Getting started with the generics](https://go.dev/doc/tutorial/generics)
