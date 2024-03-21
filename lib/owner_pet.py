class Owner:
    all = []

    def __init__(self, name):
        self.name = name
        self.all.append(self)

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise ValueError("Unknown pet.")
        pet.owner = self

    def pets(self):
        owner_pets = [pet for pet in Pet.all if pet.owner == self]
        return owner_pets

    def get_sorted_pets(self):
        owner_pets = self.pets()
        sorted_pets = sorted(owner_pets, key=lambda x: x.name)
        return sorted_pets

class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type.lower() not in self.PET_TYPES:
            raise ValueError(f"Invalid pet type. Allowed types are {', '.join(self.PET_TYPES)}")
        self.name = name
        self.pet_type = pet_type.lower()
        self.owner = owner
        self.all.append(self)
