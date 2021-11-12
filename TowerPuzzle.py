import sys


class TowerPuzzle:

    def __init__(self, visibility_):
        # visibility - числа по краям поля
        self.__visibility_left = visibility_[0]
        self.__visibility_up = visibility_[1]
        self.__visibility_right = visibility_[2]
        self.__visibility_down = visibility_[3]
        self.__field = [[0] * len(visibility_[0])] * len(visibility_[0])

    def get_visibility_left(self):
        return self.__visibility_left

    def get_visibility_right(self):
        return self.__visibility_right

    def get_visibility_up(self):
        return self.__visibility_up

    def get_visibility_down(self):
        return self.__visibility_down

    def get_field(self):
        return self.__field

    def __count_visibility_horizontal(self, index):
        result = 0
        max_height = 0
        for i in range(len(self.__field[0])):
            if max_height < self.__field[index][i]:
                max_height = self.__field[index][i]
                result += 1
        return result

    def __count_visibility_vertical(self, index):
        result = 0
        max_height = 0
        for i in range(len(self.__field[0])):
            if max_height < self.__field[i][index]:
                max_height = self.__field[i][index]
                result += 1
        return result


if __name__ == '__main__':
    visibility = [[1, 2, 3], [1, 0, -5], [10, 12, 13], [11, 12, 13]]
    ss = TowerPuzzle(visibility)
