import unittest
from copy import deepcopy
from TowerPuzzle import TowerPuzzle
from TowerPuzzle import get_field_from_array


class Test_TowerPuzzle(unittest.TestCase):
    def test_init(self):
        visibility = [[1, 2, 3], [1, 0, -5], [10, 12, 13], [11, 12, 13]]
        ss = TowerPuzzle(visibility)
        field = [[ss.Cell(3), ss.Cell(3), ss.Cell(3)], [ss.Cell(3), ss.Cell(3), ss.Cell(3)],
                 [ss.Cell(3), ss.Cell(3), ss.Cell(3)]]

        self.assertEqual(ss.visibility_left, visibility[0])
        self.assertEqual(ss.visibility_up, visibility[1])
        self.assertEqual(ss.visibility_right, visibility[2])
        self.assertEqual(ss.visibility_down, visibility[3])
        self.assertEqual(ss.field, field)

    def test_count_visibility(self):
        visibility = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        field = [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
        ss = TowerPuzzle(visibility)
        ss.field = get_field_from_array(field)

        self.assertEqual(ss.count_visibility_left(0), 3)
        self.assertEqual(ss.count_visibility_left(1), 2)
        self.assertEqual(ss.count_visibility_left(2), 1)

        self.assertEqual(ss.count_visibility_right(0), 1)
        self.assertEqual(ss.count_visibility_right(1), 2)
        self.assertEqual(ss.count_visibility_right(2), 2)

        self.assertEqual(ss.count_visibility_up(0), 3)
        self.assertEqual(ss.count_visibility_up(1), 2)
        self.assertEqual(ss.count_visibility_up(2), 1)

        self.assertEqual(ss.count_visibility_down(0), 1)
        self.assertEqual(ss.count_visibility_down(1), 2)
        self.assertEqual(ss.count_visibility_down(2), 2)

        field = [[3, 2, 5, 4, 1], [4, 5, 3, 1, 2], [5, 4, 1, 2, 3], [2, 1, 4, 3, 5], [1, 3, 2, 5, 4]]
        ss.size = 5
        ss.field = get_field_from_array(field)

        self.assertEqual(ss.count_visibility_left(0), 2)
        self.assertEqual(ss.count_visibility_left(1), 2)
        self.assertEqual(ss.count_visibility_left(2), 1)
        self.assertEqual(ss.count_visibility_left(3), 3)
        self.assertEqual(ss.count_visibility_left(4), 3)

        self.assertEqual(ss.count_visibility_right(0), 3)
        self.assertEqual(ss.count_visibility_right(1), 3)
        self.assertEqual(ss.count_visibility_right(2), 3)
        self.assertEqual(ss.count_visibility_right(3), 1)
        self.assertEqual(ss.count_visibility_right(4), 2)

        self.assertEqual(ss.count_visibility_up(0), 3)
        self.assertEqual(ss.count_visibility_up(1), 2)
        self.assertEqual(ss.count_visibility_up(2), 1)
        self.assertEqual(ss.count_visibility_up(3), 2)
        self.assertEqual(ss.count_visibility_up(4), 4)

        self.assertEqual(ss.count_visibility_down(0), 3)
        self.assertEqual(ss.count_visibility_down(1), 3)
        self.assertEqual(ss.count_visibility_down(2), 3)
        self.assertEqual(ss.count_visibility_down(3), 1)
        self.assertEqual(ss.count_visibility_down(4), 2)

    def test_count_unfilled(self):
        visibility = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        field = [[0, 0, 0], [1, 2, 3], [0, 2, 0]]
        ss = TowerPuzzle(visibility)
        ss.field = get_field_from_array(field)

        self.assertEqual(ss.count_unfilled_cells_horizontal(0), 3)
        self.assertEqual(ss.count_unfilled_cells_horizontal(1), 0)
        self.assertEqual(ss.count_unfilled_cells_horizontal(2), 2)

        self.assertEqual(ss.count_unfilled_cells_vertical(0), 2)
        self.assertEqual(ss.count_unfilled_cells_vertical(1), 1)
        self.assertEqual(ss.count_unfilled_cells_vertical(2), 2)

    def test_str(self):
        visibility = [[2, 2, 2, 3, 1], [2, 2, 3, 1, 3], [2, 2, 3, 1, 5], [1, 2, 3, 3, 2]]
        field = [[4, 3, 1, 5, 2], [1, 5, 2, 3, 4], [2, 1, 5, 4, 3], [3, 2, 4, 1, 5], [5, 4, 3, 2, 1]]
        field = get_field_from_array(field)
        ss = TowerPuzzle(visibility, field)
        str_result = "-----------------------------------------------------------\n"
        str_result += " |[----2----][----2----][----3----][----1----][----3----]|\n"
        str_result += "2|[- - - 4 -][- - 3 - -][1 - - - -][- - - - 5][- 2 - - -]|2\n"
        str_result += "2|[1 - - - -][- - - - 5][- 2 - - -][- - 3 - -][- - - 4 -]|2\n"
        str_result += "2|[- 2 - - -][1 - - - -][- - - - 5][- - - 4 -][- - 3 - -]|3\n"
        str_result += "3|[- - 3 - -][- 2 - - -][- - - 4 -][1 - - - -][- - - - 5]|1\n"
        str_result += "1|[- - - - 5][- - - 4 -][- - 3 - -][- 2 - - -][1 - - - -]|5\n"
        str_result += " |[----1----][----2----][----3----][----3----][----2----]|\n"
        str_result += "-----------------------------------------------------------\n"

        self.assertEqual(str(ss), str_result)

    def test_is_solved(self):
        visibility = [[2, 2, 2, 3, 1], [2, 2, 3, 1, 3], [2, 2, 3, 1, 5], [1, 2, 3, 3, 2]]
        field = [[4, 3, 1, 5, 2], [1, 5, 2, 3, 4], [2, 1, 5, 4, 3], [3, 2, 4, 1, 5], [5, 4, 3, 2, 1]]
        field = get_field_from_array(field)
        ss = TowerPuzzle(visibility, field)
        self.assertTrue(ss.is_solved())

        field = [[3, 1, 5, 2, 4], [5, 2, 3, 4, 1], [1, 5, 4, 3, 2], [2, 4, 1, 5, 3], [4, 3, 2, 1, 5]]
        ss.field = get_field_from_array(field)
        self.assertFalse(ss.is_solved())

        field = [[4, 0, 1, 5, 2], [1, 5, 2, 3, 4], [2, 1, 5, 4, 3], [3, 2, 4, 1, 5], [5, 4, 3, 2, 1]]
        ss.field = get_field_from_array(field)
        self.assertFalse(ss.is_solved())

        field = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        ss.field = get_field_from_array(field)
        self.assertFalse(ss.is_solved())

        visibility = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        field = [[3, 1, 5, 2, 4], [5, 2, 3, 4, 1], [1, 5, 4, 3, 2], [2, 4, 1, 5, 3], [4, 3, 2, 1, 5]]
        field = get_field_from_array(field)
        ss = TowerPuzzle(visibility, field)
        self.assertTrue(ss.is_solved())

        visibility = [[2, 2, 2, 3, 1], [2, 2, 3, 1, 3], [2, 2, 3, 1, 5], [1, 2, 3, 3, 2]]
        field = [[4, 0, 1, 5, 2], [1, 5, 2, 3, 4], [2, 1, 5, 4, 3], [3, 2, 4, 1, 5], [5, 4, 3, 2, 1]]
        field = get_field_from_array(field)
        ss = TowerPuzzle(visibility, field)
        self.assertFalse(ss.is_solved())

    def test_set(self):
        visibility = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        ss = TowerPuzzle(visibility)

        ss.set(0, 0, 2)
        self.assertEqual(ss.field[0][0], TowerPuzzle.Cell(3, 2))

        ss.set(0, 0, 2)
        self.assertEqual(ss.field[0][0], TowerPuzzle.Cell(3, 2))

        ss.set(0, 0, 3)
        self.assertEqual(ss.field[0][0], TowerPuzzle.Cell(3, 2))

        ss.set(0, 2, 3)
        self.assertEqual(ss.field[0][2], TowerPuzzle.Cell(3, 3))

        ss.set(2, 2, 1)
        self.assertEqual(ss.field[2][2], TowerPuzzle.Cell(3, 1))

    def test_remove(self):
        visibility = [[1, 0, 0], [1, 0, 2], [0, 1, 0], [0, 1, 2]]
        ss = TowerPuzzle(visibility)

        ss.remove(0, 0, 1)
        ss.remove(0, 0, 2)
        self.assertEqual(ss.field[0][0], TowerPuzzle.Cell(3, 3))

        ss.remove(0, 0, 1)
        self.assertEqual(ss.field[0][0], TowerPuzzle.Cell(3, 3))

        ss.remove(1, 2, 3)
        cell = TowerPuzzle.Cell(3)
        cell.remove(3)
        self.assertEqual(ss.field[1][2], cell)

        ss.remove(1, 2, 1)
        cell.remove(1)
        self.assertEqual(ss.field[1][2], cell)

    def test_remove_higher(self):
        visibility = [[1, 0, 0], [1, 0, 2], [0, 1, 0], [0, 1, 2]]
        ss = TowerPuzzle(visibility)

        ss.remove_higher(0, 0, 2)
        cell = TowerPuzzle.Cell(3)
        cell.remove(3)
        self.assertEqual(ss.field[0][0], cell)

        ss.remove_higher(0, 0, 1)
        cell.remove(2)
        self.assertEqual(ss.field[0][0], cell)

        ss.remove_higher(1, 1, 3)
        cell = TowerPuzzle.Cell(3)
        self.assertEqual(ss.field[1][1], cell)

        ss.remove_higher(2, 0, 1)
        cell = TowerPuzzle.Cell(3, 1)
        self.assertEqual(ss.field[2][0], cell)

    def test_solve_trivial_highest(self):
        visibility = [[1, 0, 0], [1, 0, 2], [0, 1, 0], [0, 1, 2]]
        ss = TowerPuzzle(visibility)
        ss.solve_trivial_highest()
        field = [[3, 0, 0], [0, 0, 3], [0, 3, 0]]
        field = get_field_from_array(field)
        self.assertEqual(ss.field, field)

        visibility = [[2, 1, 2, 2], [2, 2, 1, 2], [2, 2, 1, 2], [2, 1, 2, 2]]
        ss = TowerPuzzle(visibility)
        ss.solve_trivial_highest()
        field = [[0, 0, 4, 0], [4, 0, 0, 0], [0, 0, 0, 4], [0, 4, 0, 0]]
        field = get_field_from_array(field)
        self.assertEqual(ss.field, field)

        ss.solve_trivial_highest()
        self.assertEqual(ss.field, field)

    def test_solve_base_restrictions(self):
        visibility = [[1, 3, 2], [1, 3, 2], [2, 1, 2], [2, 1, 2]]
        ss = TowerPuzzle(visibility)
        field = [[0, 1, 0], [1, 0, 0], [0, 0, 0]]
        field = get_field_from_array(field)
        field[0][2].remove(3)
        field[1][1].remove(3)
        field[2][0].remove(3)
        field[2][2].remove(3)
        ss.solve_base_restrictions()

        self.assertEqual(ss.field, field)

    def test_solve_castle_restrictions(self):
        visibility = [[0, 0], [0, 0], [0, 0], [0, 0]]
        field = [[1, 0], [0, 0]]
        field = get_field_from_array(field)
        ss = TowerPuzzle(visibility, field)
        ss.solve_castle_restrictions(0, 0)
        field = [[1, 2], [2, 0]]
        field = get_field_from_array(field)

        self.assertEqual(ss.field, field)

        ss.solve_castle_restrictions(1, 0)
        field = [[1, 2], [2, 1]]
        field = get_field_from_array(field)
        self.assertEqual(ss.field, field)

        visibility = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        field = [[0, 0, 0], [0, 3, 0], [0, 0, 0]]
        field = get_field_from_array(field)
        ss = TowerPuzzle(visibility, field)
        ss.solve_castle_restrictions(1, 1)
        field[0][1].remove(3)
        field[1][0].remove(3)
        field[1][2].remove(3)
        field[2][1].remove(3)

        self.assertEqual(ss.field, field)

        field[2][0].set(1)
        ss.field = field
        ss.solve_castle_restrictions(2, 0)
        field[0][0].remove(1)
        field[1][0].set(2)
        field[2][1].set(2)
        field[2][2].remove(1)

        self.assertEqual(ss.field, field)

        visibility = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        field = [[0, 0, 0], [0, 3, 0], [0, 0, 0]]
        field = get_field_from_array(field)
        ss = TowerPuzzle(visibility, field)
        ss.solve_castle_restrictions(0, 0)

        self.assertEqual(ss.field, field)

        visibility = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        field = [[0, 0, 0], [0, 3, 0], [0, 0, 0]]
        field = get_field_from_array(field)
        ss = TowerPuzzle(visibility, field)
        field[0][1].remove(3)
        field[1][0].remove(3)
        field[1][2].remove(3)
        field[2][1].remove(3)
        field[2][0].set(3)
        ss.field = field
        field[0][0].remove(3)

        self.assertEqual(ss.field, field)

    def test_only_one_row(self):
        visibility = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        field = [[0, 0, 0], [0, 0, 1], [0, 0, 0]]
        field = get_field_from_array(field)
        field[1][1].remove(3)
        ss = TowerPuzzle(visibility, field)
        ss.solve_only_one_row(1)
        field[1][0].set(3)

        self.assertEqual(ss.field, field)

        ss.solve_only_one_row(1)
        field[1][1].set(2)

        self.assertEqual(ss.field, field)

        ss.solve_only_one_row(1)
        field[1][2].set(1)

        self.assertEqual(ss.field, field)

    def test_only_one_column(self):
        visibility = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        field = [[0, 0, 0], [0, 0, 0], [0, 0, 1]]
        field = get_field_from_array(field)
        field[1][2].remove(3)
        ss = TowerPuzzle(visibility, field)
        ss.solve_only_one_column(2)
        field[0][2].set(3)

        self.assertEqual(ss.field, field)

        ss.solve_only_one_column(2)
        field[1][2].set(2)

        self.assertEqual(ss.field, field)

        ss.solve_only_one_column(2)
        field[2][2].set(1)

        self.assertEqual(ss.field, field)

    def test_get_possible_rows(self):
        visibility = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        field = [[3, 0, 0, 4], [4, 0, 0, 3], [1, 4, 3, 2], [2, 3, 4, 1]]
        field = get_field_from_array(field)
        field[0][1].remove(4)
        field[0][1].remove(3)
        field[0][2].remove(4)
        field[0][2].remove(3)
        ss = TowerPuzzle(visibility, field)
        possible_rows = [[3, 1, 1, 4], [3, 2, 1, 4], [3, 1, 2, 4], [3, 2, 2, 4]]
        possible_rows = get_field_from_array(possible_rows)
        self.assertEqual(ss.get_possible_rows(0), possible_rows)

    def test_get_possible_columns(self):
        visibility = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        field = [[3, 0, 0, 4], [4, 0, 0, 3], [1, 4, 3, 2], [2, 3, 4, 1]]
        field = get_field_from_array(field)
        field[0][1].remove(4)
        field[0][1].remove(3)
        field[1][1].remove(4)
        field[1][1].remove(3)
        ss = TowerPuzzle(visibility, field)
        possible_columns = [[1, 1, 4, 3], [2, 1, 4, 3], [1, 2, 4, 3], [2, 2, 4, 3]]
        possible_columns = get_field_from_array(possible_columns)
        result = ss.get_possible_columns(1)
        self.assertEqual(ss.get_possible_columns(1), possible_columns)

    def test_get_right_vector_from_possible(self):
        possible_matrix = [[1, 1, 4, 3], [2, 1, 4, 3], [1, 2, 4, 3], [2, 2, 4, 3]]
        possible_matrix = get_field_from_array(possible_matrix)
        right_matrix = [[2, 1, 4, 3], [1, 2, 4, 3]]
        right_matrix = get_field_from_array(right_matrix)

        self.assertEqual(TowerPuzzle.get_right_vector_from_possible(0, 0, possible_matrix), right_matrix)

        possible_matrix = [[1, 1, 4, 3], [2, 1, 4, 3], [1, 2, 4, 3], [2, 2, 4, 3], [3, 4, 2, 1], [1, 2, 3, 4],
                           [4, 3, 1, 2]]
        possible_matrix = get_field_from_array(possible_matrix)
        right_matrix = [[2, 1, 4, 3], [1, 2, 4, 3], [3, 4, 2, 1], [1, 2, 3, 4], [4, 3, 1, 2]]
        right_matrix = get_field_from_array(right_matrix)

        self.assertEqual(TowerPuzzle.get_right_vector_from_possible(0, 0, possible_matrix), right_matrix)

        possible_matrix = [[1, 1, 4, 3], [2, 1, 4, 3], [1, 2, 4, 3], [2, 2, 4, 3]]
        possible_matrix = get_field_from_array(possible_matrix)
        right_matrix = [[1, 2, 4, 3]]
        right_matrix = get_field_from_array(right_matrix)

        self.assertEqual(TowerPuzzle.get_right_vector_from_possible(3, 2, possible_matrix), right_matrix)

        possible_matrix = [[1, 1, 4, 3], [2, 1, 4, 3], [1, 2, 4, 3], [2, 2, 4, 3], [3, 4, 2, 1], [1, 2, 3, 4],
                           [4, 3, 1, 2]]
        possible_matrix = get_field_from_array(possible_matrix)
        right_matrix = [[1, 2, 4, 3]]
        right_matrix = get_field_from_array(right_matrix)

        self.assertEqual(TowerPuzzle.get_right_vector_from_possible(3, 2, possible_matrix), right_matrix)

        possible_matrix = [[1, 1, 4, 3], [2, 1, 4, 3], [1, 2, 4, 3], [2, 2, 4, 3], [3, 4, 2, 1], [1, 2, 3, 4],
                           [4, 3, 1, 2]]
        possible_matrix = get_field_from_array(possible_matrix)
        right_matrix = []
        right_matrix = get_field_from_array(right_matrix)

        self.assertEqual(TowerPuzzle.get_right_vector_from_possible(2, 1, possible_matrix), right_matrix)

    def test_get_cell_vector_from_matrix(self):
        matrix = [[2, 1, 4, 3], [1, 2, 4, 3]]
        matrix = get_field_from_array(matrix)
        vector = [[0, 0, 4, 3]]
        vector = get_field_from_array(vector)
        vector[0][0].remove(3)
        vector[0][0].remove(4)
        vector[0][1].remove(3)
        vector[0][1].remove(4)
        self.assertEqual(TowerPuzzle.get_cell_vector_from_matrix(matrix), vector[0])

        matrix = [[2, 1, 6, 9, 7, 8, 4, 3, 5], [2, 8, 6, 9, 7, 1, 4, 3, 5], [2, 8, 6, 9, 7, 3, 4, 1, 5]]
        matrix = get_field_from_array(matrix)
        vector = [[2, 0, 6, 9, 7, 0, 4, 0, 5]]
        vector = get_field_from_array(vector)
        vector[0][1].remove(2)
        vector[0][1].remove(3)
        vector[0][1].remove(4)
        vector[0][1].remove(5)
        vector[0][1].remove(6)
        vector[0][1].remove(7)
        vector[0][1].remove(9)
        vector[0][5].remove(2)
        vector[0][5].remove(4)
        vector[0][5].remove(5)
        vector[0][5].remove(6)
        vector[0][5].remove(7)
        vector[0][5].remove(9)
        vector[0][7].remove(2)
        vector[0][7].remove(4)
        vector[0][7].remove(5)
        vector[0][7].remove(6)
        vector[0][7].remove(7)
        vector[0][7].remove(8)
        vector[0][7].remove(9)

        self.assertEqual(TowerPuzzle.get_cell_vector_from_matrix(matrix), vector[0])

    def test_solve_visibility_restriction_row(self):
        visibility = [[2, 2, 1, 4], [3, 2, 1, 2], [2, 3, 3, 1], [2, 3, 2, 1]]
        field = [[2, 1, 4, 3], [3, 4, 0, 0], [4, 3, 0, 0], [1, 2, 3, 4]]
        field = get_field_from_array(field)
        field[1][2].remove(4)
        field[1][2].remove(3)
        field[1][3].remove(4)
        field[1][3].remove(3)
        field[2][2].remove(4)
        field[2][2].remove(3)
        field[2][3].remove(4)
        field[2][3].remove(3)
        ss = TowerPuzzle(visibility, deepcopy(field))
        field[1][2].set(2)
        field[1][3].set(1)

        ss.solve_visibility_restriction_row(1)
        self.assertEqual(ss.field, field)

        field[2][2].set(1)
        field[2][3].set(2)

        ss.solve_visibility_restriction_row(2)
        self.assertEqual(ss.field, field)


class Test_Cell(unittest.TestCase):

    def test_init(self):
        cell = TowerPuzzle.Cell(9)
        self.assertEqual(cell.array, [1, 2, 3, 4, 5, 6, 7, 8, 9])

        cell = TowerPuzzle.Cell(1)
        self.assertEqual(cell.array, [1])

        cell = TowerPuzzle.Cell(20)
        self.assertEqual(cell.array, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

        cell = TowerPuzzle.Cell(0)
        self.assertEqual(cell.array, [])

        cell = TowerPuzzle.Cell(0, 4)
        self.assertEqual(cell.array, [])

        cell = TowerPuzzle.Cell(4, 4)
        self.assertEqual(cell.array, [0, 0, 0, 4])

    def test_remove(self):
        cell = TowerPuzzle.Cell(9)

        cell.remove(1)
        self.assertEqual(cell.array, [0, 2, 3, 4, 5, 6, 7, 8, 9])

        cell.remove(1)
        self.assertEqual(cell.array, [0, 2, 3, 4, 5, 6, 7, 8, 9])

        cell.remove(7)
        self.assertEqual(cell.array, [0, 2, 3, 4, 5, 6, 0, 8, 9])

    def test_set(self):
        cell = TowerPuzzle.Cell(9)

        cell.set(4)
        self.assertEqual(cell.array, [0, 0, 0, 4, 0, 0, 0, 0, 0, ])

        cell.set(6)
        self.assertEqual(cell.array, [0, 0, 0, 0, 0, 6, 0, 0, 0, ])

        cell.set(6)
        self.assertEqual(cell.array, [0, 0, 0, 0, 0, 6, 0, 0, 0, ])

    def test_get_not_zeros(self):
        cell = TowerPuzzle.Cell(9)

        self.assertEqual(cell.get_not_zeros(), [1, 2, 3, 4, 5, 6, 7, 8, 9])

        cell.array = [1, 0, 3, 4, 0, 0, 0, 8, 0]
        self.assertEqual(cell.get_not_zeros(), [1, 3, 4, 8])

        cell.array = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(cell.get_not_zeros(), [])

    def test_str(self):
        cell = TowerPuzzle.Cell(9)

        self.assertEqual(str(cell), "[1 2 3 4 5 6 7 8 9]")

        cell.remove(6)
        self.assertEqual(str(cell), "[1 2 3 4 5 - 7 8 9]")

        cell.remove(5)
        self.assertEqual(str(cell), "[1 2 3 4 - - 7 8 9]")

        cell.set(6)
        self.assertEqual(str(cell), "[- - - - - 6 - - -]")

    def test_int(self):
        cell = TowerPuzzle.Cell(9)

        self.assertEqual(int(cell), 0)

        cell.remove(8)
        self.assertEqual(int(cell), 0)

        cell.set(3)
        self.assertEqual(int(cell), 3)

        cell.set(9)
        self.assertEqual(int(cell), 9)

    def test_bool(self):
        cell = TowerPuzzle.Cell(3)
        self.assertFalse(cell)

        cell = TowerPuzzle.Cell(0)
        self.assertFalse(cell)

        cell = TowerPuzzle.Cell(1, 1)
        self.assertTrue(cell)

        cell = TowerPuzzle.Cell(4)
        cell.set(4)
        self.assertTrue(cell)

        cell = TowerPuzzle.Cell(3)
        cell.remove(1)
        cell.remove(2)
        self.assertTrue(cell)


class Test_get_field_from_array(unittest.TestCase):
    def test_function(self):
        array = [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
        field = [[TowerPuzzle.Cell(3, 1), TowerPuzzle.Cell(3, 2), TowerPuzzle.Cell(3, 3)],
                 [TowerPuzzle.Cell(3, 2), TowerPuzzle.Cell(3, 3), TowerPuzzle.Cell(3, 1)],
                 [TowerPuzzle.Cell(3, 3), TowerPuzzle.Cell(3, 1), TowerPuzzle.Cell(3, 2)]]

        self.assertEqual(get_field_from_array(array), field)

        array = [[1, 0, 3], [0, 0, 0], [0, 0, 0]]
        field = [[TowerPuzzle.Cell(3, 1), TowerPuzzle.Cell(3), TowerPuzzle.Cell(3, 3)],
                 [TowerPuzzle.Cell(3), TowerPuzzle.Cell(3), TowerPuzzle.Cell(3)],
                 [TowerPuzzle.Cell(3), TowerPuzzle.Cell(3), TowerPuzzle.Cell(3)]]

        self.assertEqual(get_field_from_array(array), field)
