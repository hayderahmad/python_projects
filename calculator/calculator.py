class Calculator:
    def __init__(self, number):
        self.number = self.validate_int(number)
        self.initial = self.validate_int(number)
        self.saved = []

    def add(self, number):
        self.number += number
        self.saved.append(('+', number))
        return self

    def minus(self, number):
        self.number -= number
        self.saved.append(('-', number))
        return self

    def mult(self, number):
        self.number *= number
        self.saved.append(('*', number))
        return self

    def dvid(self, number):
        self.number /= number
        self.saved.append(('/', number))
        return self

    def get_results(self):
        return self.number

    def validate_int(self, k):
        if type(k) != int:
            raise Exception('you should use a number')
        return k

    def printing(self):
        equation = f"{self.initial}"
        for opTuple in self.saved:
            equation += f" {opTuple[0]} {opTuple[1]}"
        equation += f" = {self.number}"

        return equation

    def back(self, number):
        for _ in range(number):
            k = self.saved.pop()
            print(self.saved)
            if k[0] == '+':
                self.number -= k[1]
            if k[0] == '-':
                self.number += k[1]
            if k[0] == '/':
                self.number *= k[1]
            if k[0] == '*':
                self.number /= k[1]
        return self


calc1 = Calculator(1).add(4).minus(1).mult(5).back(2)
print(calc1.printing())
