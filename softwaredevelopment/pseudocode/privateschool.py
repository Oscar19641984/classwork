class Student:
    def __init__(self, age):
        self.age = age
        self.key_stage = None
        self.fee = 0

    def determine_key_stage_and_fee(self):
        if 11 <= self.age <= 14:
            self.key_stage = "Key Stage 3"
            self.fee = 2000 * self.age
        elif 15 <= self.age <= 16:
            self.key_stage = "Key Stage 4"
            self.fee = 3000 * self.age
        else:
            self.key_stage = "Not eligible for Key Stage 3 or 4"
            self.fee = 0

    def display_info(self):
        print(f"Age: {self.age}")
        print(f"Key Stage: {self.key_stage}")
        print(f"Fee: £{self.fee}")

def main():
    age = int(input("Enter your age: "))
    student1 = Student(age)
    student1.determine_key_stage_and_fee()
    student1.display_info()

main()