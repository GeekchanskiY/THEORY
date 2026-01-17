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

The name of each explicitly specified method must be unique and not blank.

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
### Type parameter declarations
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

A parsing ambiguity arises when the type parameter list for a generic type declares a single type parameter P with a constraint C such that the text P C forms a valid expression.

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


# Sources
[The Go Programming Language Specification](https://go.dev/ref/spec) (go version: 1.25)
[Wirth syntax notation](https://en.wikipedia.org/wiki/Wirth_syntax_notation)
[Extended Backus–Naur form](https://en.wikipedia.org/wiki/Extended_Backus–Naur_form)
[Codecademy go strings](https://www.codecademy.com/resources/docs/go/strings)
[Go blog: slices usage and internals](https://go.dev/blog/slices-intro)
[Boldlygo: universal and package identifiers](https://boldlygo.tech/archive/2023-06-22-the-universe-and-package-blocks/)
[Getting started with the generics](https://go.dev/doc/tutorial/generics)