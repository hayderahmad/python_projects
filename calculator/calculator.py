import requests
import validations


class calculator:

    def __init__(self, number):
        self.memory = []
        self.number = validations.is_int(number)
        self.first = validations.is_int(number)

    def mult(self, number):
        number = validations.is_int(number)
        self.number *= number
        self.memory.append(('*', number))
        return self

    def div(self, number):
        number = validations.is_int(number)
        self.number /= number
        self.memory.append(('/', number))
        return self

    def sub(self, number):
        number = validations.is_int(number)
        self.number -= number
        self.memory.append(('-', number))
        return self

    def add(self, number):
        number = validations.is_int(number)
        self.number += number
        self.memory.append(('+', number))
        return self

    def back(self, number):
        number = validations.is_int(number)
        number = round(validations.less_than_one(number))
        if number > len(self.memory):
            raise Exception(
                f"you are asking to go back more than available operations please select a number less than {len(self.memory)} operations")
        else:
            for number in range(len(self.memory)):
                x = self.memory.pop()
                if x[0] == '*':
                    self.number /= x[1]
                if x[0] == '/':
                    self.number *= x[1]
                if x[0] == '+':
                    self.number -= x[1]
                if x[0] == '-':
                    self.number += x[1]
                return self

    def print_and_facts(self):
        equation = f"{self.first}"
        for x in self.memory:
            equation += f" {x[0]} {x[1]}"
        equation += f" = {self.number}"
        print(equation)

        fact = requests.get(f"http://numbersapi.com/{self.number}/trivia").text
        print(f"some facts about the number {self.number}: \n {fact}")


x = calculator(5).mult(5).sub(6).mult(3).add(1).back(1).print_and_facts()
