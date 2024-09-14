# student names
class StudentAccount:
    username = None
    password = None
    def __init__(self, u, p):
        self.username = u
        self.password = p
        
    
class Student(StudentAccount):
    full_name = None
    def __init__():
        super().__init__(u, p)
    level = 1