from datetime import date

class Plant:
    def __init__(self, species: str, schedule: int, id=0):
        self.id = id
        self.species = species
        self.schedule = schedule
        self.last_watered = None

    def set_id(self, id_num):
        self.id = id_num

    def set_last_watered(self, day: date):
        self.last_watered = day
