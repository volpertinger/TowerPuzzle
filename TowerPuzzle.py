import sys


# чтобы составлять поля менее громоздко
def get_field_from_array(array):
    result = []
    for i in range(len(array[0])):
        result.append([])
        for j in range(len(array[0])):
            if array[i][j] == 0:
                result[i].append(TowerPuzzle.Cell(len(array[0])))
            else:
                result[i].append(TowerPuzzle.Cell(len(array[0]), array[i][j]))
    return result


class TowerPuzzle:
    class Cell:
        def __init__(self, size_, number_=None):
            # если в процессе работы программы в этом массиве будет 0, то это так вычеркнут невозможный вариант
            self.array = []
            if number_ is None:
                for i in range(size_):
                    self.array.append(i + 1)
            else:
                for i in range(size_):
                    if i == number_ - 1:
                        self.array.append(number_)
                    else:
                        self.array.append(0)

        def __str__(self):
            result = '['
            for i in range(len(self.array)):
                if self.array[i] == 0:
                    result += '-'
                else:
                    result += str(self.array[i])
                if i != len(self.array) - 1:
                    result += ' '
            result += ']'
            return result

        def __int__(self):
            # если однозначно определили число в клетке
            if self.array.count(0) == len(self.array) - 1:
                for i in range(len(self.array)):
                    if self.array[i] != 0:
                        return self.array[i]
            # если явно число еще не определено в клетке, то считаем, что в ней ничего не стоит (высота здания == 0)
            else:
                return 0

        def __eq__(self, other):
            try:
                return self.array == other.array
            except BaseException:
                raise RuntimeError("Cell is not equal to other type")

        def __bool__(self):
            return self.array.count(0) == len(self.array) - 1

        def set(self, number_):
            if (number_ > len(self.array)) or (number_ < 1):
                raise RuntimeError("Number " + str(number_) + " doesn't exist in cell")
            result = [0] * len(self.array)
            result[number_ - 1] = number_
            self.array = result

        def remove(self, number_):
            if number_ < 1:
                raise RuntimeError("Number " + str(number_) + " < 1")
            self.array[number_ - 1] = 0

        def get_not_zeros(self):
            result = []
            for i in range(len(self.array)):
                if self.array[i] != 0:
                    result.append(self.array[i])
            return result

    def __init__(self, visibility_, field_=None):
        # visibility - числа по краям поля, если 0, то ограничений нет
        self.visibility_left = visibility_[0]
        self.visibility_up = visibility_[1]
        self.visibility_right = visibility_[2]
        self.visibility_down = visibility_[3]

        self.size = len(visibility_[0])
        if field_ is None:
            # self.field = [[TowerPuzzle.Cell(len(visibility_[0]))] * len(visibility_[0])] * len(visibility_[0])
            self.field = []
            for i in range(len(visibility_[0])):
                self.field.append([])
                for j in range(len(visibility_[0])):
                    self.field[i].append(TowerPuzzle.Cell(len(visibility_[0])))
        else:
            self.field = field_

    def __str__(self):
        border = '-' * (self.size * (2 * self.size + 1) + 4) + '\n'
        # Шапка
        result = border

        # visibility up
        result += ' |'
        for i in range(self.size):
            result += '[' + str(self.visibility_up[i]).center(2 * self.size - 1, '-') + ']'
        result += '|\n'

        # field
        for i in range(self.size):
            result += str(self.visibility_left[i]) + '|'
            for j in range(self.size):
                result += str(self.field[i][j])
            result += '|' + str(self.visibility_right[i]) + '\n'

        # visibility down
        result += ' |'
        for i in range(self.size):
            result += '[' + str(self.visibility_down[i]).center(2 * self.size - 1, '-') + ']'
        result += '|\n'

        # подвал
        result += border

        return result

    def count_visibility_left(self, index_):
        result = 0
        max_height = 0
        for i in range(self.size):
            if max_height < int(self.field[index_][i]):
                max_height = int(self.field[index_][i])
                result += 1
        return result

    def count_visibility_right(self, index_):
        result = 0
        max_height = 0
        for i in range(self.size):
            if max_height < int(self.field[index_][self.size - i - 1]):
                max_height = int(self.field[index_][self.size - i - 1])
                result += 1
        return result

    def count_visibility_up(self, index_):
        result = 0
        max_height = 0
        for i in range(self.size):
            if max_height < int(self.field[i][index_]):
                max_height = int(self.field[i][index_])
                result += 1
        return result

    def count_visibility_down(self, index_):
        result = 0
        max_height = 0
        for i in range(self.size):
            if max_height < int(self.field[self.size - i - 1][index_]):
                max_height = int(self.field[self.size - i - 1][index_])
                result += 1
        return result

    def count_unfilled_cells_horizontal(self, index_):
        result = 0
        for i in range(self.size):
            if int(self.field[index_][i]) == 0:
                result += 1
        return result

    def count_unfilled_cells_vertical(self, index_):
        result = 0
        for i in range(self.size):
            if int(self.field[i][index_]) == 0:
                result += 1
        return result

    def is_solved(self):
        for i in range(self.size):
            for j in range(self.size):
                if int(self.field[i][j]) == 0:
                    return False

            if (self.visibility_left[i] != self.count_visibility_left(i)) and (self.visibility_left[i] != 0):
                return False

            if (self.visibility_right[i] != self.count_visibility_right(i)) and (self.visibility_right[i] != 0):
                return False

            if (self.visibility_up[i] != self.count_visibility_up(i)) and (self.visibility_up[i] != 0):
                return False

            if (self.visibility_down[i] != self.count_visibility_down(i)) and (self.visibility_down[i] != 0):
                return False

        return True

    def set(self, row, column, number):
        if self.field[row][column]:
            return
        self.field[row][column].set(number)

    def remove(self, row, column, number):
        self.field[row][column].remove(number)

    def remove_higher(self, row, column, number):
        for i in range(number + 1, self.size + 1):
            self.remove(row, column, i)

    def solve_trivial_highest(self):
        for i in range(self.size):
            if self.visibility_left[i] == 1:
                self.set(i, 0, self.size)
            if self.visibility_right[i] == 1:
                self.set(i, self.size - 1, self.size)
            if self.visibility_up[i] == 1:
                self.set(0, i, self.size)
            if self.visibility_down[i] == 1:
                self.set(self.size - 1, i, self.size)

    def solve_base_restrictions(self):
        for i in range(self.size):
            for j in range(self.size):
                restriction_left = self.size - self.visibility_left[i] + 1 + j
                restriction_right = self.size - self.visibility_right[i] - j + self.size
                restriction_up = self.size - self.visibility_up[j] + 1 + i
                restriction_down = self.size - self.visibility_down[j] - i + self.size
                restriction = min(restriction_left, restriction_right, restriction_up, restriction_down)
                self.remove_higher(i, j, restriction)

    def solve_castle_restrictions(self, row, column):
        if not self.field[row][column]:
            return

        number = int(self.field[row][column])
        for i in range(0, column):
            self.remove(row, i, number)
        for i in range(column + 1, self.size):
            self.remove(row, i, number)
        for i in range(0, row):
            self.remove(i, column, number)
        for i in range(row + 1, self.size):
            self.remove(i, column, number)


if __name__ == '__main__':
    visibility = [[1, 2, 3], [1, 0, -5], [10, 12, 13], [11, 12, 13]]
    ss = TowerPuzzle(visibility)
