# studymon objects
class Studymon():
    level = 0
    name = "mon"
    modelID = 1
    def __init__(self, l, n, m):
        self.level = l
        self.name = n
        self.modelID = m
    def sayhi():
        print("hello")
    
# fire type studymon class
class Firemon(Studymon):
    type = "Fire"
    experience = 0
    def __init__(self, l, n, m, e):
        super().__init__(l, n, m)
        self.experience = e
    def ShowFire():
        print("")

# water type studymon class
class Watermon(Studymon):
    type = "Water"
    experience = 0
    def __init__(self, l, n, m, e):
        super().__init__(l, n, m)
        self.experience = e
    def LiftWater():
        print("")

# Earth type studymon class 
class Earthmon(Studymon):
    type = "Earth"
    experience = 0
    def __init__(self, l, n, m, e):
        super().__init__(l, n, m)
        self.experience = e
    def LiftEarth():
        print("")

# Air type studymon class
class Airmon(Studymon):
    type = "Air"
    experience = 0
    def __init__(self, l, n, m, e):
        super().__init__(l, n, m)
        self.experience = e
    def LiftSelf():
        print("")
    
    
    
#class SubClass(SuperClass):
    #def __init__(self, name, age):
        # Call the constructor of the superclass
        #super().__init__(name)