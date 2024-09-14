# studymon objects
import requests
import json
class Studymon():
    def __init__(self, n, l):
        #attribute
        self.name = n
        self.level = l
        #getting stuff from pokeapi url
        base_url = "https://pokeapi.co/api/v2/"
        self.data = json.loads(requests.get(base_url + "pokemon/" + n))
        # general_info = json.loads(self.data)
        
        self.evo_chain = self.fetch_evolution_chain()

        #TODO get the level the mon needs to be to evolve as well as the name of its evolution

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
        species_data = json.loads(requests.get(species_url).json())
        evolution_url = species_data['evolution_chain']['url']
        return json.loads(requests.get(evolution_url).json())
    
    #Turns this studymon into a new studymon
    def evolve(self):
        if not self.can_evolve():
            print(f"{self.name} cannot evolve further.")
            return

        current_species = self.evolution_chain['chain']
        while current_species['species']['name'] != self.name:
            current_species = current_species['evolves_to'][0]
        
        evolved_species = current_species['evolves_to'][0]['species']['name']
        evolved_pokemon = Studymon(evolved_species)
        
        print(f"{self.name} evolved into {evolved_pokemon.name}!")
        self.__dict__.update(evolved_pokemon.__dict__)

    #runs the exp calculator to earn exp
    
    def gainLevel(self): 
        self.level += 1
        if(self.level >= self.evolution_level):
            self.evolve()
    
    def getSprite(self) -> str:
        return self.sprite

s = Studymon("bulbasaur", 1)
print(s.can_evolve)
print("\ntrue <-expected")