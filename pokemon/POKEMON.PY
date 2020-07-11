import requests


class Pokemon:
    def __init__(self, *pokemons):
        self.report = {}
        self.raw_data = {}
        self.pokemons = pokemons
        for i in self.pokemons:
            self.request = requests.get(
                f'https://pokeapi.co/api/v2/pokemon/{i}').status_code
            if self.request == 404:
                raise Exception(
                    f"{i} is not a Pokemon please try a different Pokemon Name ")
        for i in self.pokemons:
            self.request = requests.get(
                f'https://pokeapi.co/api/v2/pokemon/{i}').json()
            self.raw_data[i] = self.request
        for i in self.pokemons:
            self.items = {}
            for h in self.raw_data[i]['stats']:
                self.items[h['stat']['name']] = h['base_stat']
                self.report[i] = self.items

    def get_pokemons(self):
        return self.request

    def get_raw_resp(self):
        return self.raw_data

    def get_abilities(self):
        self.abilities = {}
        for i in self.pokemons:
            x = []
            for h in self.raw_data[i]['abilities']:
                x.append(h['ability']['name'])
            self.abilities[i] = x
        return self.abilities

    def most_exp(self):
        self.exp_pairing = {}
        for i in self.pokemons:
            self.exp_pairing[i] = self.raw_data[i]['base_experience']

        return max(self.exp_pairing, key=self.exp_pairing.get)

    def get_stat_report(self):
        return self.report

    def get_hp(self):
        self.hp = {}
        for i in self.pokemons:
            self.hp[i] = self.report[i]['hp']
        return self.hp

    def get_attack(self):
        self.attack = {}
        for i in self.pokemons:
            self.attack[i] = self.report[i]['attack']
        return self.attack

    def get_defense(self):
        self.defense = {}
        for i in self.pokemons:
            self.defense[i] = self.report[i]['defense']
        return self.defense

    def get_special_attack(self):
        self.special_attack = {}
        for i in self.pokemons:
            self.special_attack[i] = self.report[i]['special_attack']
        return self.special_attack

    def get_special_defense(self):
        self.special_defense = {}
        for i in self.pokemons:
            self.special_defense[i] = self.report[i]['special_defense']
        return self.special_defense

    def get_speed(self):
        self.speed = {}
        for i in self.pokemons:
            self.speed[i] = self.report[i]['speed']
        return self.speed


my_pokemons = Pokemon("bulbasaur", "charmander")
print(my_pokemons.get_abilities())
