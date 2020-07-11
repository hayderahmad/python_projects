class Matrix:
    def __init__(self, input):
        self.input = input
        if type(input) != list:
            raise Exception(f'the {input} is not a matrix')
        for i in input:
            if type(i) != list:
                raise Exception(f'the {input} is not a matrix')

    def hieght(self):
        return len(self.input)

    def width(self):
        return len(self.input[0])

    def transpose(self):
        self.final_matrix = []
        for i in range(len(self.input[0])):
            self.final_matrix.append([])

        for i in self.input:
            for l in i:
                x = i.index(l)
                self.final_matrix[x].append(l)

        return self.final_matrix

    def is_square(self):
        if len(self.input) == len(self.input[0]):
            return 'it is booleanly true'
        else:
            return 'it is booleanly false'

    def trace(self):
        x = 0
        if len(self.input) == len(self.input[0]):
            for i in self.input:
                x += i[self.input.index(i)]
            return x
        else:
            return 'we can not do tracelty because the submited matrix is irregularly irregular'


my_matrix = Matrix([
    [1, 2, 3],
    [5, 6, 7],
    [3, 5, 6]
])

my_matrix.transpose()

print(my_matrix.trace())
