class student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_name(self):
     return self.name
    
    def set_name(self,new_name):
       self.name = new_name
    
    def get_id(self):
        return self.id  
    
    def set_id(self,new_id):
       self.id= new_id
    
    def __str__(self):
       return f"the name of the student is {self.name} and the id is {self.id}"
    
    @staticmethod
    def school_info():
       return "ABC school"

s1 = student("samyam",29)
print(s1)
s1.set_name("samyam maharjan")
print(s1.get_name())
print(student.school_info())

    