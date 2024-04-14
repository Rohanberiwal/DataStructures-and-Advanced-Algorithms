# Bit Masking

## What is a Bit Mask?

A bit mask is a binary number used to manipulate individual bits or groups of bits within a larger binary data structure. It is commonly used in computer science and programming for tasks such as setting, clearing, or toggling specific bits within binary data.

## How Does Bit Masking Work?

Bit masking involves performing bitwise operations with the bit mask and the target data. Common bitwise operations used in bit masking include:

- **AND (`&`):** Performs a bitwise AND operation. It sets a bit to 1 only if both corresponding bits in the operands are 1.
- **OR (`|`):** Performs a bitwise OR operation. It sets a bit to 1 if at least one of the corresponding bits in the operands is 1.
- **XOR (`^`):** Performs a bitwise XOR (exclusive OR) operation. It sets a bit to 1 if the corresponding bits in the operands are different.
- **NOT (`~`):** Performs a bitwise NOT operation. It flips each bit, changing 0 to 1 and 1 to 0.
- **Shift (`<<`, `>>`):** Shifts the bits in the operand to the left or right by a specified number of positions.

By combining these bitwise operations with appropriate bit masks, programmers can achieve various tasks such as:

- Setting specific bits to 1.
- Clearing specific bits (setting them to 0).
- Toggling (flipping) specific bits.
- Extracting specific bits or groups of bits.
- Checking the status of specific bits.

## Example

```python
# Setting the 3rd bit to 1 using a bit mask
num = 5  # Binary: 101
mask = 1 << 2  # Shift 1 to the left by 2 positions: 100
result = num | mask  # Bitwise OR operation: 101 | 100 = 101
print(result)  # Output: 5 (binary: 101)

# Clearing the 2nd bit (setting it to 0) using a bit mask
num = 6  # Binary: 110
mask = ~(1 << 1)  # Shift 1 to the left by 1 position, then negate: 1111101
result = num & mask  # Bitwise AND operation: 110 & 1111101 = 100
print(result)  # Output: 4 (binary: 100)
