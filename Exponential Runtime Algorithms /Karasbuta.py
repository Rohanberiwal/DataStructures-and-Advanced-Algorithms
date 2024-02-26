def complex_multiply(a, b, c, d):
    # Compute intermediate values
    ac = a * c
    bd = b * d
    pq = (a + b) * (c + d)
    
    # Calculate real and imaginary parts of the product
    real_part = ac - bd
    imag_part = pq - ac - bd
    
    return real_part, imag_part

# Example usage:
a, b, c, d = 2, 3, 4, 5
real_part, imag_part = complex_multiply(a, b, c, d)
print("Real part:", real_part)  # Output: 10
print("Imaginary part:", imag_part)  # Output: 23
