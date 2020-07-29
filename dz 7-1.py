x = [[1, 3, 5], [2, 2, 2], [7, 4, 1]]
y = [[9, 7, 2], [4, 1, 1], [8, 6, 0]]


class Matrix:
    def __init__(self, list):
        self.list = list

    def __str__(self):
        return "\n".join(map(str, self.list))

    def __add__(self, other):
        result = []
        for i in range(len(self.list)):
            result.append([])
            for j in range(len(self.list[0])):
                result[i].append(self.list[i][j] + other.list[i][j])
        return "\n".join(map(str, result))


x = Matrix(x)
y = Matrix(y)
print("Первая матрица \n", x)
print("Вторая матрица \n", y)
print("Сумма матриц \n", x + y)
