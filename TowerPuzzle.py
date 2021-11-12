import sys


class TowerPuzzle:

    def __init__(self, visibility_):
        # visibility - числа по краям поля
        self.visibility_left = visibility_[0]
        self.visibility_up = visibility_[1]
        self.visibility_right = visibility_[2]
        self.visibility_down = visibility_[3]
        self.field = [[0] * len(visibility_[0])] * len(visibility_[0])

    def count_visibility_horizontal(self, index):
        result = 0
        max_height = 0
        for i in range(len(self.field[0])):
            if max_height < self.field[index][i]:
                max_height = self.field[index][i]
                result += 1
        return result

    def count_visibility_vertical(self, index):
        result = 0
        max_height = 0
        for i in range(len(self.field[0])):
            if max_height < self.field[i][index]:
                max_height = self.field[i][index]
                result += 1
        return result


if __name__ == '__main__':
    visibility = [[1, 2, 3], [1, 0, -5], [10, 12, 13], [11, 12, 13]]
    ss = TowerPuzzle(visibility)
