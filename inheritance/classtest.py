class personclass:
    name: str
    age: int

    def summary(self) -> str:
        return f"{self.name}, {self.age} years old"
    
    def greet():
        print(f"Hello, your name is {self.name} and you are {self.age} years old.")

def main():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    person = personclass(name, age)
    person.greet()

main()