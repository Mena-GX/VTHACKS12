
# teacher
class Teacher:
    # basic information for teacher to login 
    t_username = None
    t_password = None
    # student list to add
    # section to add
    def __init__(self, tu, tp):
        self.t_username = tu
        self.t_password = tp
    # function to reward student to add
    # function to make new assignment to add
    


#Bob = input("Enter username:")
#print("Username is: " + username)

#Bob = Teacher(input("Enter username:"), "gtb")
#print(Bob.t_username)


Teachers = []
Teachers.append(Teacher("Vlad", "rjgjgj"))
Teachers.append(Teacher("Walt", "rg16?"))
Teachers.append(Teacher("Charles", "tptptp"))

# login but need more code
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
        
Vlad = Teacher (Teachers[0].t_username, Teachers[0].t_password)
Walt = Teacher (Teachers[1].t_username, Teachers[1].t_password)
Charles = Teacher (Teachers[2].t_username, Teachers[2].t_password)
