#class
class Dog:
    def make_sound(self):
        return "Bark"  
    
class Cat:
    def make_sound(self):
        return "Meow"

class Cow:
    def make_sound(self):
        return "Moo"

class Duck:
    def make_sound(self):
        return "Quack"

#main
def main():
    dog = Dog()
    cat = Cat()
    cow = Cow()
    duck = Duck()

    print(f"Dog: {dog.make_sound()}")
    print(f"Cat: {cat.make_sound()}")
    print(f"Cow: {cow.make_sound()}")
    print(f"Duck: {duck.make_sound()}")

main()