import sys


class TowerPuzzle:

    def __init__(self, visibility_):
        # visibility - числа по краям поля
        self.visibility_left = visibility_[0]
        self.visibility_up = visibility_[1]
        self.visibility_right = visibility_[2]
        self.visibility_down = visibility_[3]
        self.field = [[0] * len(visibility_[0])] * len(visibility_[0])


if __name__ == '__main__':
    visibility = [[1, 2, 3], [1, 0, -5], [10, 12, 13], [11, 12, 13]]
    ss = TowerPuzzle(visibility)
