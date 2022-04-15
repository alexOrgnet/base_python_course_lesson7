
'''1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.'''


class Matrix:

    def __init__(self, mylist):
        self.mylist = mylist

    def __str__(self):
        for row in self.mylist:
            for i in row:
                print(f"{i:4}", end="")
            print("", end="\n")
        return ""

    def __add__(self, other):
        for i in range(len(self.mylist)):
            for i2 in range(len(other.mylist[i])):
                self.mylist[i][i2] = self.mylist[i][i2] + other.mylist[i][i2]
        return Matrix.__str__(self)


matrix = Matrix([[5, 18, 11], [6, 17, 23], [41, 50, 9], [6, 7, 93]])
new_matrix = Matrix([[-5, 2, -13], [-21, 10, -12], [10, 8, -6], [1, 12, -71]])
#print(matrix)
#print(new_matrix)
print(matrix.__add__(new_matrix))
