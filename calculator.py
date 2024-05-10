# Define a class called Calculator to perform basic arithmetic operations
class Calculator:
    # Define a method for addition that takes two arguments and returns their sum
    def add(self, x, y):
        return x + y

    # Define a method for subtraction that takes two arguments and returns their difference
    def subtract(self, x, y):
        return x - y

    # Define a method for multiplication that takes two arguments and returns their product
    def multiply(self, x, y):
        return x * y

    # Define a method for division that takes two arguments and returns the result if the denominator is not zero,
    # or an error message if the denominator is zero
    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return ("Cannot divide by zero.")