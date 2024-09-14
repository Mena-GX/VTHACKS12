# studymon objects
import requests
import json
class Studymon():
    level = 0
    name = "mon"
    api_info = None
    experience = 0
    base_experience = 0
    modelID = None
    def __init__(self, l, n, e):
        #attribute
        self.level = l
        self.name = n
        #getting stuff from pokeapi url
        url = "https://pokeapi.co/api/v2/pokemon/" + n
        general_info = requests.get(url)
        api_info = json.loads(general_info.text)
        base_experience = api_info.get("base_experience")
        #more attributes
        self.experience = e
        modelID = api_info.get()
        
    def sayhi():
        print("hello")


print("hello")
#class SubClass(SuperClass):
    #def __init__(self, name, age):
        # Call the constructor of the superclass
        #super().__init__(name)