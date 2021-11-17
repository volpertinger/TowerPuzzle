from copy import deepcopy


class TowerPuzzle:
    class __Cell:
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
        self.__visibility_left = visibility_[0]
        self.__visibility_up = visibility_[1]
        self.__visibility_right = visibility_[2]
        self.__visibility_down = visibility_[3]

        self.__size = len(visibility_[0])
        if field_ is None:
            # self.field = [[TowerPuzzle.Cell(len(visibility_[0]))] * len(visibility_[0])] * len(visibility_[0])
            self.__field = []
            for i in range(len(visibility_[0])):
                self.__field.append([])
                for j in range(len(visibility_[0])):
                    self.__field[i].append(TowerPuzzle.__Cell(len(visibility_[0])))
        else:
            self.__field = field_

    def __str__(self):
        border = '-' * (self.__size * (2 * self.__size + 1) + 4) + '\n'
        # Шапка
        result = border

        # visibility up
        result += ' |'
        for i in range(self.__size):
            result += '[' + str(self.__visibility_up[i]).center(2 * self.__size - 1, '-') + ']'
        result += '|\n'

        # field
        for i in range(self.__size):
            result += str(self.__visibility_left[i]) + '|'
            for j in range(self.__size):
                result += str(self.__field[i][j])
            result += '|' + str(self.__visibility_right[i]) + '\n'

        # visibility down
        result += ' |'
        for i in range(self.__size):
            result += '[' + str(self.__visibility_down[i]).center(2 * self.__size - 1, '-') + ']'
        result += '|\n'

        # подвал
        result += border

        return result

    # чтобы составлять поля менее громоздко
    @staticmethod
    def get_field_from_array(array):
        result = []
        for i in range(len(array)):
            result.append([])
            for j in range(len(array[0])):
                if array[i][j] == 0:
                    result[i].append(TowerPuzzle.__Cell(len(array[0])))
                else:
                    result[i].append(TowerPuzzle.__Cell(len(array[0]), array[i][j]))
        return result

    @staticmethod
    def __get_right_vector_from_possible(lhs_visibility, rhs_visibility, matrix):
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
            if ((lhs_visibility == current_lhs_visibility) or (lhs_visibility == 0)) and (
                    (rhs_visibility == current_rhs_visibility) or (rhs_visibility == 0)) and (
                    len(unique_array) == len(vector)):
                result.append(vector)
        return result

    @staticmethod
    def __get_cell_vector_from_matrix(matrix):
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
                result.append(TowerPuzzle.__Cell(length, vector[0]))
            else:
                result.append(TowerPuzzle.__Cell(length))
                for i in range(length):
                    if vector.count(i + 1) == 0:
                        result[len(result) - 1].remove(i + 1)
        return result

    def get_field_string(self):
        result = ''
        for i in range(self.__size):
            for j in range(self.__size):
                result += str(int(self.__field[i][j])) + ' '
            result = result[:-1]
            result += '\n'
        return result

    def __count_visibility_left(self, index_):
        result = 0
        max_height = 0
        for i in range(self.__size):
            if max_height < int(self.__field[index_][i]):
                max_height = int(self.__field[index_][i])
                result += 1
        return result

    def __count_visibility_right(self, index_):
        result = 0
        max_height = 0
        for i in range(self.__size):
            if max_height < int(self.__field[index_][self.__size - i - 1]):
                max_height = int(self.__field[index_][self.__size - i - 1])
                result += 1
        return result

    def __count_visibility_up(self, index_):
        result = 0
        max_height = 0
        for i in range(self.__size):
            if max_height < int(self.__field[i][index_]):
                max_height = int(self.__field[i][index_])
                result += 1
        return result

    def __count_visibility_down(self, index_):
        result = 0
        max_height = 0
        for i in range(self.__size):
            if max_height < int(self.__field[self.__size - i - 1][index_]):
                max_height = int(self.__field[self.__size - i - 1][index_])
                result += 1
        return result

    def __count_unfilled_cells_horizontal(self, index_):
        result = 0
        for i in range(self.__size):
            if int(self.__field[index_][i]) == 0:
                result += 1
        return result

    def __count_unfilled_cells_vertical(self, index_):
        result = 0
        for i in range(self.__size):
            if int(self.__field[i][index_]) == 0:
                result += 1
        return result

    def __count_brute_force_variants(self):
        # result = 1
        for i in range(self.__size):
            for j in range(self.__size):
                # result *= len(self.__field[i][j].get_not_zeros())
                if len(self.__field[i][j].get_not_zeros()) > 1:
                    return len(self.__field[i][j].get_not_zeros()) - 1
                    # return result

    def __is_unique_row(self, row):
        unique_stack = []
        for i in range(self.__size):
            if unique_stack.count(int(self.__field[row][i])) == 1:
                return False
            if (unique_stack.count(int(self.__field[row][i])) == 0) and (int(self.__field[row][i]) != 0):
                unique_stack.append(int(self.__field[row][i]))
        return True

    def __is_unique_column(self, column):
        unique_stack = []
        for i in range(self.__size):
            if unique_stack.count(int(self.__field[i][column])) == 1:
                return False
            if (unique_stack.count(int(self.__field[i][column])) == 0) and (int(self.__field[i][column]) != 0):
                unique_stack.append(int(self.__field[i][column]))
        return True

    def __is_solved(self):
        for i in range(self.__size):
            for j in range(self.__size):
                if int(self.__field[i][j]) == 0:
                    return False
            if (self.__visibility_left[i] != self.__count_visibility_left(i)) and (self.__visibility_left[i] != 0):
                return False

            if (self.__visibility_right[i] != self.__count_visibility_right(i)) and (
                    self.__visibility_right[i] != 0):
                return False

            if (self.__visibility_up[i] != self.__count_visibility_up(i)) and (self.__visibility_up[i] != 0):
                return False

            if (self.__visibility_down[i] != self.__count_visibility_down(i)) and (self.__visibility_down[i] != 0):
                return False

            if not self.__is_unique_row(i):
                return False
            if not self.__is_unique_column(i):
                return False

        return True

    def __is_correct(self):
        for i in range(self.__size):
            if not self.__is_unique_row(i):
                return False
            if not self.__is_unique_column(i):
                return False
            if self.__count_unfilled_cells_vertical(i) == 0:
                if (self.__count_visibility_up(i) != self.__visibility_up[i]) and (self.__visibility_up[i] != 0):
                    return False
                if (self.__count_visibility_down(i) != self.__visibility_down[i]) and (self.__visibility_down[i] != 0):
                    return False
            if self.__count_unfilled_cells_horizontal(i) == 0:
                if (self.__count_visibility_left(i) != self.__visibility_left[i]) and (self.__visibility_left[i] != 0):
                    return False
                if (self.__count_visibility_right(i) != self.__visibility_right[i]) and (
                        self.__visibility_right[i] != 0):
                    return False

        return True

    def __set(self, row, column, number):
        if self.__field[row][column]:
            return
        self.__field[row][column].set(number)

    def __remove(self, row, column, number):
        if int(self.__field[row][column]) != 0:
            return False
        return self.__field[row][column].remove(number)

    def __remove_higher(self, row, column, number):
        for i in range(number + 1, self.__size + 1):
            self.__remove(row, column, i)

    def __solve_trivial_highest(self):
        for i in range(self.__size):
            if self.__visibility_left[i] == 1:
                self.__set(i, 0, self.__size)
            if self.__visibility_right[i] == 1:
                self.__set(i, self.__size - 1, self.__size)
            if self.__visibility_up[i] == 1:
                self.__set(0, i, self.__size)
            if self.__visibility_down[i] == 1:
                self.__set(self.__size - 1, i, self.__size)

    def __solve_base_restrictions(self):
        for i in range(self.__size):
            for j in range(self.__size):
                restriction_left = self.__size - self.__visibility_left[i] + 1 + j
                restriction_right = self.__size - self.__visibility_right[i] - j + self.__size
                restriction_up = self.__size - self.__visibility_up[j] + 1 + i
                restriction_down = self.__size - self.__visibility_down[j] - i + self.__size
                restriction = min(restriction_left, restriction_right, restriction_up, restriction_down)
                self.__remove_higher(i, j, restriction)

    def __solve_castle_restrictions(self, row, column):
        if not self.__field[row][column]:
            return False

        result = False
        number = int(self.__field[row][column])
        for i in range(0, column):
            if self.__remove(row, i, number):
                result = True
        for i in range(column + 1, self.__size):
            if self.__remove(row, i, number):
                result = True
        for i in range(0, row):
            if self.__remove(i, column, number):
                result = True
        for i in range(row + 1, self.__size):
            if self.__remove(i, column, number):
                result = True
        return result

    def __solve_only_one_row(self, row):
        count_list = {}
        result = False
        for i in range(self.__size):
            count_list.update({i + 1: 0})
        for i in range(self.__size):
            numbers = self.__field[row][i].get_not_zeros()
            for number in numbers:
                count_list[number] += 1
        for i in range(self.__size):
            if count_list[i + 1] == 1:
                number = i + 1
                for j in range(self.__size):
                    if (self.__field[row][j].get_not_zeros().count(number) == 1) and (not self.__field[row][j]):
                        self.__field[row][j].set(number)
                        result = True
                        break
        return result

    def __solve_only_one_column(self, column):
        count_list = {}
        result = False
        for i in range(self.__size):
            count_list.update({i + 1: 0})
        for i in range(self.__size):
            numbers = self.__field[i][column].get_not_zeros()
            for number in numbers:
                count_list[number] += 1
        for i in range(self.__size):
            if count_list[i + 1] == 1:
                number = i + 1
                for j in range(self.__size):
                    if (self.__field[j][column].get_not_zeros().count(number) == 1) and (
                            not self.__field[j][column]):
                        self.__field[j][column].set(number)
                        result = True
                        break
        return result

    def __get_possible_rows(self, row):
        result = [[]]
        for i in range(self.__size):
            if self.__field[row][i]:
                for element in result:
                    element.append(deepcopy(self.__field[row][i]))
            else:
                numbers = self.__field[row][i].get_not_zeros()
                length = len(result)
                for j in range(len(numbers) - 1):
                    for k in range(length):
                        result.append(deepcopy(result[k]))
                begin = 0
                step = int(len(result) / len(numbers))
                end = step
                for number in numbers:
                    for j in range(begin, end):
                        result[j].append(TowerPuzzle.__Cell(self.__size, number))
                    begin += step
                    end += step
        return result

    def __get_possible_columns(self, column):
        result = [[]]
        for i in range(self.__size):
            if self.__field[i][column]:
                for element in result:
                    element.append(self.__field[i][column])
            else:
                numbers = self.__field[i][column].get_not_zeros()
                length = len(result)
                for j in range(len(numbers) - 1):
                    for k in range(length):
                        result.append(deepcopy(result[k]))
                begin = 0
                step = int(len(result) / len(numbers))
                end = step
                for number in numbers:
                    for j in range(begin, end):
                        result[j].append(TowerPuzzle.__Cell(self.__size, number))
                    begin += step
                    end += step
        return result

    def __solve_visibility_restriction_row(self, row):
        result = self.__get_possible_rows(row)
        result = self.__get_right_vector_from_possible(self.__visibility_left[row], self.__visibility_right[row],
                                                       result)
        result = self.__get_cell_vector_from_matrix(result)
        if (self.__field[row] == result) or (result == []) or (result is None):
            return False
        self.__field[row] = deepcopy(result)
        return True

    def __solve_visibility_restriction_column(self, column):
        result = self.__get_possible_columns(column)
        result = self.__get_right_vector_from_possible(self.__visibility_up[column], self.__visibility_down[column],
                                                       result)
        result = self.__get_cell_vector_from_matrix(result)
        if (not result) or (result is None):
            return False
        for i in range(self.__size):
            if self.__field[i][column] != result[i]:
                for j in range(self.__size):
                    self.__field[j][column] = deepcopy(result[j])
                return True
        return False

    def __solve_number_brute_force(self, variant=0):
        variant_counter = 0
        for i in range(self.__size):
            for j in range(self.__size):
                if not self.__field[i][j]:
                    for number in self.__field[i][j].get_not_zeros():
                        if variant_counter == variant:
                            self.__field[i][j].set(number)
                            return True
                        variant_counter += 1
        return False

    def __solve_trivial_cases(self):
        self.__solve_trivial_highest()
        self.__solve_base_restrictions()

    def __solve_by_restrictions(self):
        result = True
        while result:

            while result:
                result = False
                for i in range(self.__size):
                    for j in range(self.__size):
                        if self.__solve_castle_restrictions(i, j):
                            result = True

            result = True
            while result:
                result = False
                for i in range(self.__size):
                    if self.__solve_only_one_row(i):
                        result = True
                    if self.__solve_only_one_column(i):
                        result = True
                # каскад из условий, чтобы при успехе вернуться у первому циклу, которым решать наиболее эффективно
                if result:
                    break
            if result:
                continue

            result = True
            while result:
                result = False
                for i in range(self.__size):
                    if self.__solve_visibility_restriction_row(i):
                        result = True
                    if self.__solve_visibility_restriction_column(i):
                        result = True
                if result:
                    break
        return self.__is_solved()

    def solve(self):
        self.__solve_trivial_cases()
        brute_force_fields = []
        # variant - это позиция, с которой нужно начать перебор, если прошлая ведет в тупик
        brute_force_variants = [0]
        while True:
            if self.__solve_by_restrictions():
                break

            result_brute_force = False
            while not result_brute_force:
                if self.__count_brute_force_variants() is None:
                    if len(brute_force_fields) == 0:
                        return False
                    brute_force_variants.pop()
                    self.__field = deepcopy(brute_force_fields.pop())
                    continue

                if (self.__is_correct()) and (
                        self.__count_brute_force_variants() >= brute_force_variants[len(brute_force_variants) - 1]):
                    brute_force_fields.append(deepcopy(self.__field))
                    result_brute_force = self.__solve_number_brute_force(
                        brute_force_variants[len(brute_force_variants) - 1])
                    brute_force_variants[len(brute_force_variants) - 1] += 1
                    brute_force_variants.append(0)
                    if self.__is_solved():
                        return True
                    continue

                while (not self.__is_correct()) or (
                        self.__count_brute_force_variants() < brute_force_variants[len(brute_force_variants) - 1]):
                    if (len(brute_force_fields) == 0) or (len(brute_force_variants) == 0):
                        return False
                    self.__field = deepcopy(brute_force_fields.pop())
                    brute_force_variants.pop()
                continue

            if self.__is_solved():
                return True
        return False
