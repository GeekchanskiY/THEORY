Golang makes error handling a way better than lots of other languages, because go forces and error to be **not an exception, but a part of a workflow**. 
```go
func foo() err {
	return errors.New("I wish to be useful")	
}

func bar() {
	var err error 
	err = foo()
	if err != nil { 
		fmt.Fprintln("An error occured: %v", err) // error is not skipped
	}
}
```
In several cases, error could just be ignored:
```go
_ = foo()
// or
foo()
```
which is not a good practice, but sometimes there is no point to process each error. For example, `defer resp.Body.Close()` can be written as 
```go
defer func(){
	err := resp.Body.Close()
	if err != nil {
		...
	}
}
```
but it makes the code less readable, but lots of IDE's and linter's require to not silence errors.

In Go, all errors are manipulated with `errors` package.

**Creating an error** could be implemented with `errors.New` function, or `fmt.Errorf`, which can also wrap an error inside.

**Unwrapping errors** allows to detect if there's an wrapped error using `%w` verb inside `fmt.Errorf` function. With `errors.Unwrap(err) == ...` you can see if your error is wrapped inside different error. According to wrapping errors, it's behavior is described in `fmt.Errorf` function documentation:
```
If the format specifier includes a %w verb with an error operand, the returned error will implement an Unwrap method returning the operand. If there is more than one %w verb, the returned error will implement an Unwrap method returning a []error containing all the %w operands in the order they appear in the arguments. It is invalid to supply the %w verb with an operand that does not implement the error interface. The %w verb is otherwise a synonym for %v.
```
Also wrapping could be implemented with `errors.Join(errs ...error) error` function, which returns an error that wraps all the given errors and could be unwrapped later. Nil error are discarded, and if all errors equal to nil, function also returns nil. The error formats as the concatenation of the strings obtained by calling the Error method of each element of errs, with a newline between each string.