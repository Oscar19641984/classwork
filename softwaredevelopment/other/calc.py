#class
class Calculator:
    def __init__(self, num1, num2): #initialises the numbers that will be used in calculations and will have alues assigned by the user when the object for the calculation is created
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 != 0:#valisates if the numbers can be divided
            return self.num1 / self.num2
        else:
            return "Error: Division by zero"

#main
def main():
    print("Welcome to the Calculator!")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")#takes the user numbers and operation

    calculator = Calculator(num1, num2)#asigns the inputted numbers to the object 'calculator'

    #validates th eoperation and calls th method to do that calculation
    if operation == '+':
        result = calculator.add()
    elif operation == '-':
        result = calculator.subtract()
    elif operation == '*':
        result = calculator.multiply()
    elif operation == '/':
        result = calculator.divide()
    else:
        result = "Error: Invalid operation"

    print(f"The result is: {result}")#prints the reul of the calculation

main()