import sys


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

        def set(self, number_):
            if (number_ > len(self.array)) or (number_ < 1):
                raise RuntimeError("Number " + str(number_) + " doesn't exist in cell")
            result = [0] * len(self.array)
            result[number_ - 1] = number_
            self.array = result

        def remove(self, number_):
            if (number_ > len(self.array)) or (number_ < 1):
                raise RuntimeError("Number " + str(number_) + " doesn't exist in cell")
            self.array[number_ - 1] = 0

        def get_not_zeros(self):
            result = []
            for i in range(len(self.array)):
                if self.array[i] != 0:
                    result.append(self.array[i])
            return result

    def __init__(self, visibility_, field_=None):
        # visibility - числа по краям поля
        self.visibility_left = visibility_[0]
        self.visibility_up = visibility_[1]
        self.visibility_right = visibility_[2]
        self.visibility_down = visibility_[3]

        if field_ is None:
            self.field = [[0] * len(visibility_[0])] * len(visibility_[0])
        else:
            self.field = field_
        self.size = len(visibility_[0])

    def count_visibility_left(self, index_):
        result = 0
        max_height = 0
        for i in range(self.size):
            if max_height < self.field[index_][i]:
                max_height = self.field[index_][i]
                result += 1
        return result

    def count_visibility_right(self, index_):
        result = 0
        max_height = 0
        for i in range(self.size):
            if max_height < self.field[index_][self.size - i - 1]:
                max_height = self.field[index_][self.size - i - 1]
                result += 1
        return result

    def count_visibility_up(self, index_):
        result = 0
        max_height = 0
        for i in range(self.size):
            if max_height < self.field[i][index_]:
                max_height = self.field[i][index_]
                result += 1
        return result

    def count_visibility_down(self, index_):
        result = 0
        max_height = 0
        for i in range(self.size):
            if max_height < self.field[self.size - i - 1][index_]:
                max_height = self.field[self.size - i - 1][index_]
                result += 1
        return result

    def count_unfilled_cells_horizontal(self, index_):
        result = 0
        for i in range(self.size):
            if self.field[index_][i] == 0:
                result += 1
        return result

    def count_unfilled_cells_vertical(self, index_):
        result = 0
        for i in range(self.size):
            if self.field[i][index_] == 0:
                result += 1
        return result

    def is_solved(self):
        visibility_left_current = []
        visibility_up_current = []
        visibility_right_current = []
        visibility_down_current = []

        for i in range(self.size):
            visibility_left_current.append(self.count_visibility_left(i))
            visibility_right_current.append(self.count_visibility_right(i))
            visibility_up_current.append(self.count_visibility_up(i))
            visibility_down_current.append(self.count_visibility_down(i))
        return (visibility_left_current == self.visibility_left) and (
                visibility_right_current == self.visibility_right) and (
                       visibility_up_current == self.visibility_up) and (
                       visibility_down_current == self.visibility_down)


if __name__ == '__main__':
    visibility = [[1, 2, 3], [1, 0, -5], [10, 12, 13], [11, 12, 13]]
    ss = TowerPuzzle(visibility)
