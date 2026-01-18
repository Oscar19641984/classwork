#class
class Addition:
    def calculate(self, a, b):
        return a + b

class Subtraction:
    def calculate(self, a, b):
        return a - b
    
class Multiplication:
    def calculate(self, a, b):
        return a * b

class Division:
    def calculate(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"

#main
def main():
    def input_data():
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        return a, b

    a, b = input_data()

    add = Addition()
    sub = Subtraction()
    mul = Multiplication()
    div = Division()

    print(f"Addition: {add.calculate(a, b)}")
    print(f"Subtraction: {sub.calculate(a, b)}")
    print(f"Multiplication: {mul.calculate(a, b)}")
    print(f"Division: {div.calculate(a, b)}")

main()