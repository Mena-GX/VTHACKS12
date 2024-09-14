# studymon objects
import requests
import json
class Studymon():
    level = 0
    name = "mon"
    api_info = ""
    can_evolve = False
    evolution_level = 0
    sprite = None
    def __init__(self, n):
        #attribute
        self.name = n
        self.level = 1
        #getting stuff from pokeapi url
        base_url = "https://pokeapi.co/api/v2/"
        req_gen = requests.get(base_url + "pokemon/" + n)
        general_info = json.loads(req_gen.text)
        self.base_experience = general_info.get("base_experience")
        
        species_url = base_url + "pokemon-species/wooper"
        req_spec = requests.get(species_url)
        species_info = json.loads(req_spec)

        evolution_url = species_info.get("evolution_chain").get("url")
        req_evo = requests.get(evolution_url)
        evo_info = json.loads(req_evo)
        evo_chain = evo_info.get("chain")
        if(len(evo_chain.get("evolves_to")) > 0):
            self.can_evolve = True
        
        self.evolution_level = general_info.get("")
        self.sprite = general_info.get("sprites").get("front_default")
    
    def getSprite(self) -> str:
        return self.sprite
    
    #Turns this studymon into a new studymon
    def evolve(self):
        if(not self.can_evolve):
            return
        else:
            self = Studymon("evolution name")

    #runs the exp calculator to earn exp
    
    def gainLevel(self): 
        self.level += 1
        if(self.level >= self.evolution_level):
            self.evolve()

    def sayhi():
        print("hello")


print("hello")
#class SubClass(SuperClass):
    #def __init__(self, name, age):
        # Call the constructor of the superclass
        #super().__init__(name)