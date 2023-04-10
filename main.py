# Рабочая тетрадь 1
# Задание 1

# Треугольником Паскаля называется числовой треугольник, в котором по
# краям стоят единицы, а каждое число внутри равно сумме двух стоящих над ним
# сверху значений.
# Дано натуральное число . Получить первые строк треугольника Паскаля


class PaskalTriangle:
    def __init__(self, rows_num):
        self.rows_num = rows_num

    def get_triangle(self):
        row = [1]
        for i in range(self.rows_num):
            row = [sum(x) for x in zip([0] + row, row + [0])]
            yield row


triangle = PaskalTriangle(13)
for row in triangle.get_triangle():
    print(*row)


# Задание 2


