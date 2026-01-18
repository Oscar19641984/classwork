class StudentData:
    def __init__(self, name, hw_gr, test_gr):
        self.name = name
        self.hw_gr = hw_gr
        self.test_gr = test_gr
        self.__Term_gr = (hw_gr + test_gr) / 2

    def Student1(self):
        return self.__Term_gr
    
    def set_Student1(self, grade):
        self.__Term_gr = grade


def main():
    student1 = StudentData("Oscar", 67, 69)
    print(student1.Student1())
    student1.set_Student1(99)
    print(student1.Student1())

main()