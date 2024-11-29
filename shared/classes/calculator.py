# common/calculator.py
import math

class Calculator:
    @staticmethod
    def add(a, b):
        Calculator.validate_numbers(a, b)
        return a + b

    @staticmethod
    def subtract(a, b):
        Calculator.validate_numbers(a, b)
        return a - b

    @staticmethod
    def multiply(a, b):
        Calculator.validate_numbers(a, b)
        return a * b

    @staticmethod
    def divide(a, b):
        Calculator.validate_numbers(a, b)
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    @staticmethod
    def calculate(num1, num2, operator):
        # Додаємо логіку для обчислень
        operations = {
            "+": Calculator.add,
            "-": Calculator.subtract,
            "*": Calculator.multiply,
            "/": Calculator.divide,
        }
        return operations.get(operator, lambda x, y: None)(num1, num2)

    @staticmethod
    def validate_numbers(a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise ValueError("Invalid number")
