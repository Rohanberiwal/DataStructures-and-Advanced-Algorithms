from sympy import Quaternion

class NotImplQuaternion:
    def __init__(self, operation):
        self.operation = operation
    
    def __str__(self):
        return f"One of the quaternions is not implemented for {self.operation}"

class MyQuaternion:
    Blacklist = []

    def __init__(self, a=0, b=0, c=0, d=0):
        try:
            self.quaternion = Quaternion(a, b, c, d)
        except Exception as e:
            print("An error occurred while initializing MyQuaternion:", e)

    def __add__(self, other):
        try:
            if type(other) in MyQuaternion.Blacklist:
                return NotImplemented
            elif isinstance(other, (int, float)):
                return NotImplQuaternion("addition")
            else:
                result = self.quaternion + other.quaternion
                return MyQuaternion(*result.args)
        except Exception as e:
            print("An error occurred during addition:", e)

    def __sub__(self, other):
        try:
            if type(other) in MyQuaternion.Blacklist:
                return NotImplemented
            elif isinstance(other, (int, float)):
                return NotImplQuaternion("subtraction")
            else:
                result = self.quaternion - other.quaternion
                return MyQuaternion(*result.args)
        except Exception as e:
            print("An error occurred during subtraction:", e)

    def __mul__(self, other):
        try:
            if type(other) in MyQuaternion.Blacklist:
                return NotImplemented
            elif isinstance(other, (int, float)):
                return NotImplQuaternion("multiplication")
            else:
                result = self.quaternion * other.quaternion
                return MyQuaternion(*result.args)
        except Exception as e:
            print("An error occurred during multiplication:", e)

    def __truediv__(self, other):
        try:
            if type(other) in MyQuaternion.Blacklist:
                return NotImplemented
            elif isinstance(other, (int, float)):
                return NotImplQuaternion("division")
            else:
                result = self.quaternion / other.quaternion
                return MyQuaternion(*result.args)
        except Exception as e:
            print("An error occurred during division:", e)

    def __str__(self):
        real, imag_i, imag_j, imag_k = self.quaternion.args
        return f"Result of operation: ({real} + {imag_i}*i + {imag_j}*j + {imag_k}*k)"

q1 = MyQuaternion(1, 2, 3, 4)
q2 = MyQuaternion(5, 6, 7, 8)
result_add = q1 + q2
print("Result of addition:", result_add)
result_sub = q1 - q2
print("Result of subtraction:", result_sub)
result_mul = q1 * q2
print("Result of multiplication:", result_mul)
result_div = q1 / q2
print("Result of division:", result_div)

print("Below are the test cases the returns Not implemented")
regular_number = 5
result_add = q1 + regular_number
print("Result of addition:", result_add)
result_sub = q1 - regular_number
print("Result of subtraction:", result_sub)
result_mul = q1 * regular_number
print("Result of multiplication:", result_mul)
result_div = q1 / regular_number
print("Result of division:", result_div)

