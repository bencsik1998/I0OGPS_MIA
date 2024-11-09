class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y

    def power(self, x, y):
        return x ** y

    def square_root(self, x):
        if x < 0:
            raise ValueError("Nem lehet negatív számból négyzetgyököt vonni")
        return x ** 0.5

    def modulo(self, x, y):
        return x % y
