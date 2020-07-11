class Animal:
    def __init__(self, **args):
        self.type = args['type']
        self.species = args['species']
        domesticAnimals = ['rat', 'donkey', 'horse', 'chicken', 'lamb',
                           'goat', 'cow', 'duck', 'parrot', 'fish', 'dog', 'cat']
        if args['species'] not in domesticAnimals and args["type"] == "domestic":
            raise Exception(f"{args['species']} is not a domestic animal")
        else:
            print(f"{args['species']} is a domestic animal")


class Pet:
    def __init__(self, **args):
        pets = ['dog', 'parrot', 'fish', 'cat']
        if args['animal'].type != "domestic":
            raise Exception(f"{args['name']} is not domestic")
        if args['animal'].species not in pets:
            raise Exception(f"{args['name']} is not a Pet")


class FarmAnimal:
    def __init__(self, animal):
        FarmAnimals = ['horse', 'donky', 'cow',
                       'lamb', 'goat', 'chicken', 'duck']
        if animal.species not in FarmAnimals:
            raise Exception(f"{animal.species} is not a farm animal")
        else:
            raise Exception(f"{animal.species} is a farm animal")


# domesticTiger = Animal(species="tiger", type="domestic")
rabbit = Animal(species="rabbit", type="wild")
rexy = Pet(animal=rabbit, name="Rexy")
# domesticRabbit = Animal(species="cow", type="domestic")
# rexy = Pet(animal=domesticRabbit, name="Rexy")
# domesticDog = Animal(species="dog", type="domestic")
# bojo = Pet(animal=domesticDog, name="bojo")
# wildCat = Animal(species="cat", type="wild")
# farmCat = FarmAnimal(wildCat)
# domesticCow = Animal(species="cow", type="domestic")
# farmCow = FarmAnimal(domesticCow)
# wildCow = Animal(species="cow", type="wild")
# farmCow = FarmAnimal(wildCow)
