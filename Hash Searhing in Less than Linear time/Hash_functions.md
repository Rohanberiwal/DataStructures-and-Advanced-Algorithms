# Hash Functions

A hash function is a function that converts an input (or 'message') into a fixed-size string of bytes. The output is typically a "digest" that uniquely represents the data input. 

## Characteristics
- **Deterministic**: The same input will always produce the same output.
- **Uniform Distribution**: Ideally, it produces an even distribution of hash values for varying inputs.
- **Fast Computation**: The function should compute the hash value quickly.
- **Pre-image Resistance**: It should be infeasible to retrieve the original input from the hash value.

## Common Hash Functions
- SHA-256
- MD5
- SHA-1

## Applications
- Data integrity verification
- Digital signatures
- Cryptographic applications

## References
1. [Wikipedia on Hash Functions](https://en.wikipedia.org/wiki/Hash_function)
2. [GeeksforGeeks Hash Functions](https://www.geeksforgeeks.org/hashing-set-1-introduction/)
