Package rand implements pseudo-random number generators suitable for tasks such as simulation, but it should not be used for security-sensitive work.

Top-level functions like `Float64` and `Int` are safe for concurrent use by multiple goroutines

This package's outputs might be easily predictable regardless of how it's seeded. For random numbers suitable for security-sensitive work, see the `crypto/rand` package.

[[Go math-rand package types]]
[[Go math-rand package functions]]