
# teacher
class Teacher:
    # basic information for teacher to login 
    t_username = None
    t_password = None
    def __init__(self, tu, tp):
        self.t_username = tu
        self.t_password = tp
    section = []

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

#Bob = input("Enter username:")
#print("Username is: " + username)

#Bob = Teacher(input("Enter username:"), "gtb")
#print(Bob.t_username)


Teachers = []
Teachers.append(Teacher("Vlad", "rjgjgj"))
Teachers.append(Teacher("Walt", "rg16?"))
Teachers.append(Teacher("Charles", "tptptp"))


i = 0
j = 0
while i != 1:
    userInput = input("What is your username?\n")
    userName = input("What is your password?\n")
    for j in range(3):
        if (userInput == Teachers[j].t_username) and (userName == Teachers[j].t_password):
            print("confirm")
            i += 1
        j += 1
    j = j - 2
    if i == 0:
        print("wrong username or password, please try again")