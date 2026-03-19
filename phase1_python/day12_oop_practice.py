class NoGrades(Exception):
    def __init__(self, grades):
        self.grades = grades
        super().__init__(f"No grades available" )

class Student:
    def __init__(self, name, grades = None):
        self.name = name
        self.grades = grades if grades is not None else[]

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            raise ValueError("Grade cannot be less than 0 or more than 100")
    
    def average(self):
        if not self.grades:
            raise NoGrades(self.grades)
        return sum(self.grades)/len(self.grades)
        
    def __str__ (self):
        return f"Student: {self.name}| {self.average():.2f}"
        
    def __repr__(self):
        return f"Student(name={self.name}, Average={self.average():.2f})"
        
class Classroom():
    def __init__(self, students= None):
        self.students = students if students is not None else []
    
    def add_student(self,student):
        return self.students.append(student)
        
    def top_student(self):
        averages = []
        for student in self.students:
            averages.append(student.average())
        max_average = max(averages)
        for student in self.students:
            if student.average() == max_average:
                return student

    def students_list(self):
        return self.students
        
    def __len__(self):
        return len(self.students)
            
a = Student("Alice", [85, 90, 81])
b = Student("Bob", [86, 91, 82])
print(a.average())
std1 = Classroom()
std1.add_student(a)
std1.add_student(b)
print(std1.students_list())
print(std1.top_student())
# Test ValueError
try:
    a.add_grade(150)
except ValueError as e:
    print(e)

# Test NoGrades
try:
    empty = Student("Empty")
    empty.average()
except NoGrades as e:
    print(e)

# Test __len__
print(len(std1))