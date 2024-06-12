from sympy import symbols, Piecewise, limit
x = symbols('x')
p = Piecewise((x2, x < 2), (22, x == 2), (5*x - 7, x > 2))
result = [
limit(p, x, 2, '+'), # --> 3 (Corrected result)
limit(p, x, 2, '-') # --> 4
]
print(result)
