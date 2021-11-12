import sys


class TowerPuzzle:

    def __init__(self, visibility_):
        # visibility - числа по краям поля
        self.visibility_left = visibility_[0]
        self.visibility_up = visibility_[1]
        self.visibility_right = visibility_[2]
        self.visibility_down = visibility_[3]

        self.field = [[0] * len(visibility_[0])] * len(visibility_[0])
        self.size = len(visibility_[0])

    def count_visibility_left(self, index):
        result = 0
        max_height = 0
        for i in range(self.size):
            if max_height < self.field[index][i]:
                max_height = self.field[index][i]
                result += 1
        return result

    def count_visibility_right(self, index):
        result = 0
        max_height = 0
        for i in range(self.size):
            if max_height < self.field[index][self.size - i - 1]:
                max_height = self.field[index][self.size - i - 1]
                result += 1
        return result

    def count_visibility_up(self, index):
        result = 0
        max_height = 0
        for i in range(self.size):
            if max_height < self.field[i][index]:
                max_height = self.field[i][index]
                result += 1
        return result

    def count_visibility_down(self, index):
        result = 0
        max_height = 0
        for i in range(self.size):
            if max_height < self.field[self.size - i - 1][index]:
                max_height = self.field[self.size - i - 1][index]
                result += 1
        return result

    def count_unfilled_cells_horizontal(self, index):
        result = 0
        for i in range(self.size):
            if self.field[index][i] == 0:
                result += 1
        return result

    def count_unfilled_cells_vertical(self, index):
        result = 0
        for i in range(self.size):
            if self.field[i][index] == 0:
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
