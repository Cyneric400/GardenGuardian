class Plant:
    def __init__(self, species: str, schedule: int, id=0):
        self.id = id
        self.species = species
        self.schedule = schedule
        
    def set_id(self, id_num):
        self.id = id_num