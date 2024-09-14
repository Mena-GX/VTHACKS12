# studymon objects
import requests
import json
class Studymon():
    level = 0
    api_info = ""
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
        
        self.evo_chain = self.fetch_evolution_chain()

        #determines whether a studymon is a part of an evolutionary chain
        if(len(self.evo_chain.get("evolution_details")) > 0):
            self.can_evolve() = True
        #gets the level the mon needs to be to evolve as well as the name of its evolution
        if(self.can_evolve()):
            self.evolution_level = self.evo_chain.get("evolves_to").get("evolution_details")[0].get("min_level")
            self.next_stage = self.evo_chain.get("evolves_to").get("species").get("name")
        #sprite stuff
        self.sprite = general_info.get("sprites").get("front_default")
    
    
    #Determines whether a studymon can evolve
    def can_evolve(self) -> bool:
        current_species = self.evo_chain['chain']
        while current_species['species']['name'] != self.name:
            if 'evolves_to' in current_species and current_species['evolves_to']:
                current_species = current_species['evolves_to'][0]
            else:
                return False
        return bool(current_species['evolves_to'])
    
    def fetch_evolution_chain(self):
        species_url = self.data['species']['url']
        species_data = requests.get(species_url).json()
        evolution_url = species_data['evolution_chain']['url']
        return json.loads(requests.get(evolution_url).json())
    
    #Turns this studymon into a new studymon
    def evolve(self):
        if(not self.can_evolve()):
            return
        else:
            self = Studymon(self.next_stage)

    #runs the exp calculator to earn exp
    
    def gainLevel(self): 
        self.level += 1
        if(self.level >= self.evolution_level):
            self.evolve()
    
    def getSprite(self) -> str:
        return self.sprite
