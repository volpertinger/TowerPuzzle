import sys
from copy import deepcopy


# чтобы составлять поля менее громоздко
def get_field_from_array(array):
    result = []
    for i in range(len(array)):
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
            result = False
            if self.array.count(number_) != 0:
                result = True
            self.array[number_ - 1] = 0
            return result

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

    @staticmethod
    def get_right_vector_from_possible(lhs_visibility, rhs_visibility, matrix):
        result = []
        for vector in matrix:
            max_height_lhs = 0
            max_height_rhs = 0
            current_lhs_visibility = 0
            current_rhs_visibility = 0
            unique_array = []
            for i in range(len(vector)):
                if unique_array.count(int(vector[i])) == 0:
                    unique_array.append(int(vector[i]))
                if int(vector[i]) > max_height_lhs:
                    current_lhs_visibility += 1
                    max_height_lhs = int(vector[i])
                if int(vector[len(vector) - 1 - i]) > max_height_rhs:
                    current_rhs_visibility += 1
                    max_height_rhs = int(vector[len(vector) - 1 - i])
            unique_array.sort()
            if ((lhs_visibility == current_lhs_visibility) or (rhs_visibility == 0)) and (
                    (rhs_visibility == current_rhs_visibility) or (rhs_visibility == 0)) and (
                    len(unique_array) == len(vector)):
                result.append(vector)
        return result

    @staticmethod
    def get_cell_vector_from_matrix(matrix):
        if len(matrix) == 0:
            return
        length = len(matrix[0])
        unique_vector = []
        for i in range(length):
            unique_column = []
            for j in range(len(matrix)):
                if unique_column.count(int(matrix[j][i])) == 0:
                    unique_column.append(int(matrix[j][i]))
            unique_vector.append(unique_column)
        result = []
        for vector in unique_vector:
            if len(vector) == 1:
                result.append(TowerPuzzle.Cell(length, vector[0]))
            else:
                result.append(TowerPuzzle.Cell(length))
                for i in range(length):
                    if vector.count(i + 1) == 0:
                        result[len(result) - 1].remove(i + 1)
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
        return self.field[row][column].remove(number)

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
            return False

        result = False
        number = int(self.field[row][column])
        for i in range(0, column):
            if self.remove(row, i, number):
                result = True
        for i in range(column + 1, self.size):
            if self.remove(row, i, number):
                result = True
        for i in range(0, row):
            if self.remove(i, column, number):
                result = True
        for i in range(row + 1, self.size):
            if self.remove(i, column, number):
                result = True
        return result

    def solve_only_one_row(self, row):
        count_list = {}
        result = False
        for i in range(self.size):
            count_list.update({i + 1: 0})
        for i in range(self.size):
            numbers = self.field[row][i].get_not_zeros()
            for number in numbers:
                count_list[number] += 1
        for i in range(self.size):
            if count_list[i + 1] == 1:
                number = i + 1
                for j in range(self.size):
                    if self.field[row][j].get_not_zeros().count(number) == 1:
                        self.field[row][j].set(number)
                        result = True
                        break
        return result

    def solve_only_one_column(self, column):
        count_list = {}
        result = False
        for i in range(self.size):
            count_list.update({i + 1: 0})
        for i in range(self.size):
            numbers = self.field[i][column].get_not_zeros()
            for number in numbers:
                count_list[number] += 1
        for i in range(self.size):
            if count_list[i + 1] == 1:
                number = i + 1
                for j in range(self.size):
                    if self.field[j][column].get_not_zeros().count(number) == 1:
                        self.field[j][column].set(number)
                        result = True
                        break
        return result

    def get_possible_rows(self, row):
        result = [[]]
        for i in range(self.size):
            if self.field[row][i]:
                for element in result:
                    element.append(deepcopy(self.field[row][i]))
            else:
                numbers = self.field[row][i].get_not_zeros()
                length = len(result)
                for j in range(len(numbers) - 1):
                    for k in range(length):
                        result.append(deepcopy(result[k]))
                begin = 0
                step = int(len(result) / len(numbers))
                end = step
                for number in numbers:
                    for j in range(begin, end):
                        result[j].append(TowerPuzzle.Cell(self.size, number))
                    begin += step
                    end += step
        return result

    def get_possible_columns(self, column):
        result = [[]]
        for i in range(self.size):
            if self.field[i][column]:
                for element in result:
                    element.append(self.field[i][column])
            else:
                numbers = self.field[i][column].get_not_zeros()
                length = len(result)
                for j in range(len(numbers) - 1):
                    for k in range(length):
                        result.append(deepcopy(result[k]))
                begin = 0
                step = int(len(result) / len(numbers))
                end = step
                for number in numbers:
                    for j in range(begin, end):
                        result[j].append(TowerPuzzle.Cell(self.size, number))
                    begin += step
                    end += step
        return result

    def solve_visibility_restriction_row(self, row):
        result = self.get_possible_rows(row)
        result = self.get_right_vector_from_possible(self.visibility_left[row], self.visibility_right[row], result)
        result = self.get_cell_vector_from_matrix(result)
        if self.field[row] == result:
            return False
        self.field[row] = deepcopy(result)
        return True

    def solve_visibility_restriction_column(self, column):
        result = self.get_possible_columns(column)
        result = self.get_right_vector_from_possible(self.visibility_up[column], self.visibility_down[column], result)
        result = self.get_cell_vector_from_matrix(result)
        for i in range(self.size):
            if self.field[i][column] != result[i]:
                for j in range(self.size):
                    self.field[j][column] = deepcopy(result[j])
                return True
        return False

    def solve_by_restrictions(self):
        self.solve_trivial_highest()
        self.solve_base_restrictions()

        while True:
            need_to_bruteforce = True

            for i in range(self.size):
                for j in range(self.size):
                    if self.solve_castle_restrictions(i, j):
                        need_to_bruteforce = False

            for i in range(self.size):
                if self.solve_only_one_row(i):
                    need_to_bruteforce = False
                if self.solve_only_one_column(i):
                    need_to_bruteforce = False

            for i in range(self.size):
                if self.solve_visibility_restriction_row(i):
                    need_to_bruteforce = False
                if self.solve_visibility_restriction_column(i):
                    need_to_bruteforce = False

            if need_to_bruteforce:
                break

        print(str(self))


if __name__ == '__main__':
    visibility = [[2, 1, 2, 3], [2, 3, 3, 1], [1, 2, 3, 2], [2, 2, 1, 4]]
    # visibility = [[2, 2, 1, 4], [3, 2, 1, 2], [2, 3, 3, 1], [2, 3, 2, 1]]
    ss = TowerPuzzle(visibility)
    ss.solve_by_restrictions()
