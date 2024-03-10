import math

def is_integer(value):
    return value == int(value)

class Expression:
    """Base class for all expression operations."""
    def evaluate(self):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError

class BinaryOperation(Expression):
    """Base class for binary operations."""
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f'{self.__class__.__name__}({repr(self.left)}, {repr(self.right)})'

class UnaryOperation(Expression):
    """Base class for unary operations."""
    def __init__(self, value: Expression):
        self.value = value
    
    def __repr__(self):
        return f'{self.__class__.__name__}({repr(self.value)})'

class Number(Expression):
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f'Number({self.value})'

class Add(BinaryOperation):
    def evaluate(self):
        return self.left.evaluate() + self.right.evaluate()

    def __str__(self):
        return f'({self.left} + {self.right})'

class Subtract(BinaryOperation):
    def evaluate(self):
        return self.left.evaluate() - self.right.evaluate()

    def __str__(self):
        return f'({self.left} - {self.right})'

class Multiply(BinaryOperation):
    def evaluate(self):
        return self.left.evaluate() * self.right.evaluate()

    def __str__(self):
        return f'({self.left} * {self.right})'

class Divide(BinaryOperation):
    def evaluate(self):
        if self.right.evaluate() == 0:
            raise ZeroDivisionError
        
        result = self.left.evaluate() / self.right.evaluate()
        if not is_integer(result):
            raise ValueError(f"Division operation not supported for non-integer value {result}")
        return result

    def __str__(self):
        return f'({self.left} / {self.right})'

class Power(BinaryOperation):
    def evaluate(self):
        base = self.left.evaluate()
        exponent = self.right.evaluate()

        if abs(exponent) > 1E3:
            raise OverflowError(f"Exponent too large: {exponent}")

        if base < 0 and not is_integer(exponent):
            raise ValueError("Negative base with non-integer exponent would result in a complex number")

        return base ** exponent

    def __str__(self):
        return f'({self.left} ^ {self.right})'

class SquareRoot(UnaryOperation):
    def evaluate(self):
        value = self.value.evaluate()
        if value < 0:
            raise ValueError(f"Square root operation not defined for negative value {value}")
        
        if value > 1E6:
            raise OverflowError(f"Square root operation not defined for large numbers {value}")

        result = math.sqrt(value)
        return result
        
    def __str__(self):
        return f'√{self.value}'

class Factorial(UnaryOperation):
    def evaluate(self):
        value = self.value.evaluate()
        if not is_integer(value):
            raise ValueError(f"Factorial operation not defined for non-integer value {value}")
        
        if value < 0:
            raise ValueError(f"Factorial operation not defined for negative value {value}")
        
        if value > 1E3:
            raise OverflowError(f"Factorial operation not calculated for large numbers {value}")
        
        return math.factorial(int(value))

    def __str__(self):
        return f'{self.value}!'

class DoubleFactorial(UnaryOperation):
    def evaluate(self):
        value = self.value.evaluate()
        if value < 0:
            raise ValueError(f"Double Factorial operation not defined for negative value {value}")
        
        if value > 1E3:
            raise OverflowError(f"Double Factorial operation wont be calculated for large numbers {value}")

        result = 1
        while value > 0:
            result *= value
            value -= 2
        return result

    def __str__(self):
        return f'{self.value}!!'
    
binary_operations = [Add, Subtract, Multiply, Divide, Power]
unary_operations = [SquareRoot, Factorial, DoubleFactorial]