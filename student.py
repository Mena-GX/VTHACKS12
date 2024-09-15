# student account
class StudentAccount:
    username = None
    password = None
    def __init__(self, u, p):
        self.username = u
        self.password = p
        
# student profile information    
class StudentProfile(StudentAccount):
    full_name = None
    #studymon list to add
    #studymon = []
    # section to add
    def __init__(self, u, p, f):
        super().__init__(u, p)
        self.full_name = f


Students = []
Students.append(StudentProfile("Jack", "rjgjgj", "Jack Smith"))
Students.append(StudentProfile("George", "rg16?", "George Bank"))
Students.append(StudentProfile("Christ", "tptptp", "Christ Titan"))

# login but more to fix
i = 0
j = 0
while i != 1:
    userInput = input("What is your username?\n")
    userName = input("What is your password?\n")
    for j in range(3):
        if (userInput == Students[j].username) and (userName == Students[j].password):
            print("confirm")
            i += 1
        j += 1
    j = j - 2
    if i == 0:
        print("wrong username or password, please try again")

Jack = StudentProfile(Students[0].username, Students[0].password, Students[0].full_name)
George = StudentProfile(Students[1].username, Students[1].password, Students[0].full_name)
Christ = StudentProfile(Students[2].username, Students[2].password, Students[2].full_name)
print(Christ.username)
print(Christ.password)
print(Christ.full_name)
     