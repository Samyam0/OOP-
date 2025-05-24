class student:
    def __init__(self,name,id,email):
        self.name = name
        self.id = id
        self.email = email  
        self.registered_courses = []
    
    def register_course(self,course):
        if course not in self.registered_courses:
            self.registered_courses.append(course)
            return True
        return False
    
    def drop_course(self,course):
        if course in self.registered_courses:
            self.registered_courses.remove(course)
            return True
        return False
    
    def display_course(self):
        print(f"student- {self.name} has registered in:")
        for course in self.registered_courses:
            print(f"{course.title}({course.course_code})")
        
class Course:
    def __init__(self,course_code,title,max_students):
        self.course_code = course_code
        self.title =title
        self.max_students = max_students
        self.students_enrolled = []

    def add_students(self,students):
        if len (self.students_enrolled)<self.max_students:
            self.students_enrolled.append(students)
            return True
        return False
    
    def remove_students(self,students):
        if student in self.students_enrolled:
            self.students_enrolled.remove(students)
            return True
        return False
    
    def display_info(self):
        print(f"students enrolled in{self.title}({self.course_code}):")
        for students in self.students_enrolled:
            print(f"{students.name}({students.id})")

class registration_course:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_students(self,id,name,email):
        if id not in self.students:
            self.students[id] = student(name,id,email)
            return True
        return False
    
    def add_course(self,course_code,title,max_students):
        if course_code not in self.courses:
            self.courses[course_code] = Course(course_code,title,max_students)
            return True
        return False
    
    def register_std_courses(self,id,course_code):
        if id in self.students and  course_code in self.courses:
            student = self.students[id]
            course = self.courses[course_code]
            if course.add_students(student) and student.register_course(course):
                return True
            return False
    
    def drop_students_from_course(self, id ,course_code):
        if  id in self.students and course_code in self.course:
            student = self.students[id]
            course= self.courses[course_code]
            if course.remove_student(student) and student.drop_course(course):
                return True
            return False
        
    def display_info(self):
        print("\n Available Courses:")
        for course_code, course in self.courses.items():
            print(f"\nCourse: {course.title} ({course_code})")
            print(f"Max Students:{course.max_students}")
            print("Enrolled Students:")
            for student in course.students_enrolled:
                print(f"-{student.name} {student.id} {student.email}")
    
if __name__ == "__main__":
    system = registration_course()

    system.add_students("23","sam","sam@gmail.com")
    system.add_students("12","alice","alice123@gmail.com")
    system.add_course("23","python",2)
    system.add_course("34","OS",44)

    system.register_std_courses("23","23")
    system.register_std_courses("12","23")
    system.register_std_courses("23","34")

    system.display_info()
    print("\n")
    system.students["23"].display_course()


