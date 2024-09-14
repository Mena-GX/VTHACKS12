# studymon objects
import requests
import json
class Studymon():
    level = 0
    name = ""
    api_info = ""
    has_evo_chain = False
    evolution_level = 0
    next_stage = None
    sprite = None
    def __init__(self, n, l):
        #attribute
        self.name = n
        self.level = l
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
        #determines whether a studymon is a part of an evolutionary chain
        if(len(evo_chain.get("evolution_details")) > 0):
            self.has_evo_chain = True
        #gets the level the mon needs to be to evolve as well as the name of its evolution
        if(self.has_evo_chain):
            self.evolution_level = evo_chain.get("evolves_to").get("evolution_details")[0].get("min_level")
            self.next_stage = evo_chain.get("evolves_to").get("species").get("name")
        #sprite stuff
        self.sprite = general_info.get("sprites").get("front_default")
    
    def getSprite(self) -> str:
        return self.sprite
    
    #Turns this studymon into a new studymon
    def evolve(self):
        if(not self.has_evo_chain):
            return
        else:
            self = Studymon(self.next_stage)

    #runs the exp calculator to earn exp
    
    def gainLevel(self): 
        self.level += 1
        if(self.level >= self.evolution_level):
            self.evolve()



print("hello")
#class SubClass(SuperClass):
    #def __init__(self, name, age):
        # Call the constructor of the superclass
        #super().__init__(name)