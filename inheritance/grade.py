class Student_Scores:
    def __init__(self, fname, lname, subject):
        self.fname = fname
        self.lname = lname
        self.subject = subject

class Total_grade(Student_Scores):
    def __init__(self, fname, lname, subject, hw_gr, cw_gr, test_gr):
        super().__init__(fname, lname, subject)
        self.hw_gr = hw_gr
        self.cw_gr = cw_gr
        self.test_gr = test_gr

    # Method to calculate total
    def calc_total(self):
        return self.hw_gr + self.cw_gr + self.test_gr

class AverageGrade:
    @staticmethod
    def compute_average(total, number_of_components):
        return total / number_of_components

def display_student_score(student_obj):
    total = student_obj.calc_total()
    print(f"Student: {student_obj.fname} {student_obj.lname}")
    print(f"Subject: {student_obj.subject}")
    print(f"Total Score: {total}")

student1 = Total_grade("John", "Doe", "Maths", 30, 25, 40)
display_student_score(student1)

total = student1.calc_total()
avg = AverageGrade.compute_average(total, 3)
print(f"Average Grade: {avg}")