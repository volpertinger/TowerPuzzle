import unittest
from copy import deepcopy
from TowerPuzzle import TowerPuzzle


class Test_TowerPuzzle(unittest.TestCase):
    def test_init(self):
        visibility = [[1, 2, 3], [1, 0, -5], [10, 12, 13], [11, 12, 13]]
        ss = TowerPuzzle(visibility)
        field = [[ss._TowerPuzzle__Cell(3), ss._TowerPuzzle__Cell(3), ss._TowerPuzzle__Cell(3)],
                 [ss._TowerPuzzle__Cell(3), ss._TowerPuzzle__Cell(3), ss._TowerPuzzle__Cell(3)],
                 [ss._TowerPuzzle__Cell(3), ss._TowerPuzzle__Cell(3), ss._TowerPuzzle__Cell(3)]]

        self.assertEqual(ss._TowerPuzzle__visibility_left, visibility[0])
        self.assertEqual(ss._TowerPuzzle__visibility_up, visibility[1])
        self.assertEqual(ss._TowerPuzzle__visibility_right, visibility[2])
        self.assertEqual(ss._TowerPuzzle__visibility_down, visibility[3])
        self.assertEqual(ss._TowerPuzzle__field, field)

    def test_get_field_from_array(self):
        array = [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
        field = [[TowerPuzzle._TowerPuzzle__Cell(3, 1), TowerPuzzle._TowerPuzzle__Cell(3, 2),
                  TowerPuzzle._TowerPuzzle__Cell(3, 3)],
                 [TowerPuzzle._TowerPuzzle__Cell(3, 2), TowerPuzzle._TowerPuzzle__Cell(3, 3),
                  TowerPuzzle._TowerPuzzle__Cell(3, 1)],
                 [TowerPuzzle._TowerPuzzle__Cell(3, 3), TowerPuzzle._TowerPuzzle__Cell(3, 1),
                  TowerPuzzle._TowerPuzzle__Cell(3, 2)]]

        self.assertEqual(TowerPuzzle.get_field_from_array(array), field)

        array = [[1, 0, 3], [0, 0, 0], [0, 0, 0]]
        field = [[TowerPuzzle._TowerPuzzle__Cell(3, 1), TowerPuzzle._TowerPuzzle__Cell(3),
                  TowerPuzzle._TowerPuzzle__Cell(3, 3)],
                 [TowerPuzzle._TowerPuzzle__Cell(3), TowerPuzzle._TowerPuzzle__Cell(3),
                  TowerPuzzle._TowerPuzzle__Cell(3)],
                 [TowerPuzzle._TowerPuzzle__Cell(3), TowerPuzzle._TowerPuzzle__Cell(3),
                  TowerPuzzle._TowerPuzzle__Cell(3)]]

        self.assertEqual(TowerPuzzle.get_field_from_array(array), field)

    def test_count_visibility(self):
        visibility = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        field = [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
        ss = TowerPuzzle(visibility)
        ss._TowerPuzzle__field = TowerPuzzle.get_field_from_array(field)

        self.assertEqual(ss._TowerPuzzle__count_visibility_left(0), 3)
        self.assertEqual(ss._TowerPuzzle__count_visibility_left(1), 2)
        self.assertEqual(ss._TowerPuzzle__count_visibility_left(2), 1)

        self.assertEqual(ss._TowerPuzzle__count_visibility_right(0), 1)
        self.assertEqual(ss._TowerPuzzle__count_visibility_right(1), 2)
        self.assertEqual(ss._TowerPuzzle__count_visibility_right(2), 2)

        self.assertEqual(ss._TowerPuzzle__count_visibility_up(0), 3)
        self.assertEqual(ss._TowerPuzzle__count_visibility_up(1), 2)
        self.assertEqual(ss._TowerPuzzle__count_visibility_up(2), 1)

        self.assertEqual(ss._TowerPuzzle__count_visibility_down(0), 1)
        self.assertEqual(ss._TowerPuzzle__count_visibility_down(1), 2)
        self.assertEqual(ss._TowerPuzzle__count_visibility_down(2), 2)

        field = [[3, 2, 5, 4, 1], [4, 5, 3, 1, 2], [5, 4, 1, 2, 3], [2, 1, 4, 3, 5], [1, 3, 2, 5, 4]]
        ss._TowerPuzzle__size = 5
        ss._TowerPuzzle__field = TowerPuzzle.get_field_from_array(field)

        self.assertEqual(ss._TowerPuzzle__count_visibility_left(0), 2)
        self.assertEqual(ss._TowerPuzzle__count_visibility_left(1), 2)
        self.assertEqual(ss._TowerPuzzle__count_visibility_left(2), 1)
        self.assertEqual(ss._TowerPuzzle__count_visibility_left(3), 3)
        self.assertEqual(ss._TowerPuzzle__count_visibility_left(4), 3)

        self.assertEqual(ss._TowerPuzzle__count_visibility_right(0), 3)
        self.assertEqual(ss._TowerPuzzle__count_visibility_right(1), 3)
        self.assertEqual(ss._TowerPuzzle__count_visibility_right(2), 3)
        self.assertEqual(ss._TowerPuzzle__count_visibility_right(3), 1)
        self.assertEqual(ss._TowerPuzzle__count_visibility_right(4), 2)

        self.assertEqual(ss._TowerPuzzle__count_visibility_up(0), 3)
        self.assertEqual(ss._TowerPuzzle__count_visibility_up(1), 2)
        self.assertEqual(ss._TowerPuzzle__count_visibility_up(2), 1)
        self.assertEqual(ss._TowerPuzzle__count_visibility_up(3), 2)
        self.assertEqual(ss._TowerPuzzle__count_visibility_up(4), 4)

        self.assertEqual(ss._TowerPuzzle__count_visibility_down(0), 3)
        self.assertEqual(ss._TowerPuzzle__count_visibility_down(1), 3)
        self.assertEqual(ss._TowerPuzzle__count_visibility_down(2), 3)
        self.assertEqual(ss._TowerPuzzle__count_visibility_down(3), 1)
        self.assertEqual(ss._TowerPuzzle__count_visibility_down(4), 2)

    def test_count_unfilled(self):
        visibility = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        field = [[0, 0, 0], [1, 2, 3], [0, 2, 0]]
        ss = TowerPuzzle(visibility)
        ss._TowerPuzzle__field = TowerPuzzle.get_field_from_array(field)

        self.assertEqual(ss._TowerPuzzle__count_unfilled_cells_horizontal(0), 3)
        self.assertEqual(ss._TowerPuzzle__count_unfilled_cells_horizontal(1), 0)
        self.assertEqual(ss._TowerPuzzle__count_unfilled_cells_horizontal(2), 2)

        self.assertEqual(ss._TowerPuzzle__count_unfilled_cells_vertical(0), 2)
        self.assertEqual(ss._TowerPuzzle__count_unfilled_cells_vertical(1), 1)
        self.assertEqual(ss._TowerPuzzle__count_unfilled_cells_vertical(2), 2)

    def test_str(self):
        visibility = [[2, 2, 2, 3, 1], [2, 2, 3, 1, 3], [2, 2, 3, 1, 5], [1, 2, 3, 3, 2]]
        field = [[4, 3, 1, 5, 2], [1, 5, 2, 3, 4], [2, 1, 5, 4, 3], [3, 2, 4, 1, 5], [5, 4, 3, 2, 1]]
        field = TowerPuzzle.get_field_from_array(field)
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
        field = TowerPuzzle.get_field_from_array(field)
        ss = TowerPuzzle(visibility, field)
        self.assertTrue(ss._TowerPuzzle__is_solved())

        field = [[3, 1, 5, 2, 4], [5, 2, 3, 4, 1], [1, 5, 4, 3, 2], [2, 4, 1, 5, 3], [4, 3, 2, 1, 5]]
        ss._TowerPuzzle__field = TowerPuzzle.get_field_from_array(field)
        self.assertFalse(ss._TowerPuzzle__is_solved())

        field = [[4, 0, 1, 5, 2], [1, 5, 2, 3, 4], [2, 1, 5, 4, 3], [3, 2, 4, 1, 5], [5, 4, 3, 2, 1]]
        ss._TowerPuzzle__field = TowerPuzzle.get_field_from_array(field)
        self.assertFalse(ss._TowerPuzzle__is_solved())

        field = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        ss._TowerPuzzle__field = TowerPuzzle.get_field_from_array(field)
        self.assertFalse(ss._TowerPuzzle__is_solved())

        visibility = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        field = [[3, 1, 5, 2, 4], [5, 2, 3, 4, 1], [1, 5, 4, 3, 2], [2, 4, 1, 5, 3], [4, 3, 2, 1, 5]]
        field = TowerPuzzle.get_field_from_array(field)
        ss = TowerPuzzle(visibility, field)
        self.assertTrue(ss._TowerPuzzle__is_solved())

        visibility = [[2, 2, 2, 3, 1], [2, 2, 3, 1, 3], [2, 2, 3, 1, 5], [1, 2, 3, 3, 2]]
        field = [[4, 0, 1, 5, 2], [1, 5, 2, 3, 4], [2, 1, 5, 4, 3], [3, 2, 4, 1, 5], [5, 4, 3, 2, 1]]
        field = TowerPuzzle.get_field_from_array(field)
        ss = TowerPuzzle(visibility, field)
        self.assertFalse(ss._TowerPuzzle__is_solved())

    def test_set(self):
        visibility = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        ss = TowerPuzzle(visibility)

        ss._TowerPuzzle__set(0, 0, 2)
        self.assertEqual(ss._TowerPuzzle__field[0][0], TowerPuzzle._TowerPuzzle__Cell(3, 2))

        ss._TowerPuzzle__set(0, 0, 2)
        self.assertEqual(ss._TowerPuzzle__field[0][0], TowerPuzzle._TowerPuzzle__Cell(3, 2))

        ss._TowerPuzzle__set(0, 0, 3)
        self.assertEqual(ss._TowerPuzzle__field[0][0], TowerPuzzle._TowerPuzzle__Cell(3, 2))

        ss._TowerPuzzle__set(0, 2, 3)
        self.assertEqual(ss._TowerPuzzle__field[0][2], TowerPuzzle._TowerPuzzle__Cell(3, 3))

        ss._TowerPuzzle__set(2, 2, 1)
        self.assertEqual(ss._TowerPuzzle__field[2][2], TowerPuzzle._TowerPuzzle__Cell(3, 1))

    def test_remove(self):
        visibility = [[1, 0, 0], [1, 0, 2], [0, 1, 0], [0, 1, 2]]
        ss = TowerPuzzle(visibility)

        ss._TowerPuzzle__remove(0, 0, 1)
        ss._TowerPuzzle__remove(0, 0, 2)
        self.assertEqual(ss._TowerPuzzle__field[0][0], TowerPuzzle._TowerPuzzle__Cell(3, 3))

        ss._TowerPuzzle__remove(0, 0, 1)
        self.assertEqual(ss._TowerPuzzle__field[0][0], TowerPuzzle._TowerPuzzle__Cell(3, 3))

        ss._TowerPuzzle__remove(1, 2, 3)
        cell = TowerPuzzle._TowerPuzzle__Cell(3)
        cell.remove(3)
        self.assertEqual(ss._TowerPuzzle__field[1][2], cell)

        ss._TowerPuzzle__remove(1, 2, 1)
        cell.remove(1)
        self.assertEqual(ss._TowerPuzzle__field[1][2], cell)

    def test_remove_higher(self):
        visibility = [[1, 0, 0], [1, 0, 2], [0, 1, 0], [0, 1, 2]]
        ss = TowerPuzzle(visibility)

        ss._TowerPuzzle__remove_higher(0, 0, 2)
        cell = TowerPuzzle._TowerPuzzle__Cell(3)
        cell.remove(3)
        self.assertEqual(ss._TowerPuzzle__field[0][0], cell)

        ss._TowerPuzzle__remove_higher(0, 0, 1)
        cell.remove(2)
        self.assertEqual(ss._TowerPuzzle__field[0][0], cell)

        ss._TowerPuzzle__remove_higher(1, 1, 3)
        cell = TowerPuzzle._TowerPuzzle__Cell(3)
        self.assertEqual(ss._TowerPuzzle__field[1][1], cell)

        ss._TowerPuzzle__remove_higher(2, 0, 1)
        cell = TowerPuzzle._TowerPuzzle__Cell(3, 1)
        self.assertEqual(ss._TowerPuzzle__field[2][0], cell)

    def test_solve_trivial_highest(self):
        visibility = [[1, 0, 0], [1, 0, 2], [0, 1, 0], [0, 1, 2]]
        ss = TowerPuzzle(visibility)
        ss._TowerPuzzle__solve_trivial_highest()
        field = [[3, 0, 0], [0, 0, 3], [0, 3, 0]]
        field = TowerPuzzle.get_field_from_array(field)
        self.assertEqual(ss._TowerPuzzle__field, field)

        visibility = [[2, 1, 2, 2], [2, 2, 1, 2], [2, 2, 1, 2], [2, 1, 2, 2]]
        ss = TowerPuzzle(visibility)
        ss._TowerPuzzle__solve_trivial_highest()
        field = [[0, 0, 4, 0], [4, 0, 0, 0], [0, 0, 0, 4], [0, 4, 0, 0]]
        field = TowerPuzzle.get_field_from_array(field)
        self.assertEqual(ss._TowerPuzzle__field, field)

        ss._TowerPuzzle__solve_trivial_highest()
        self.assertEqual(ss._TowerPuzzle__field, field)

    def test_solve_base_restrictions(self):
        visibility = [[1, 3, 2], [1, 3, 2], [2, 1, 2], [2, 1, 2]]
        ss = TowerPuzzle(visibility)
        field = [[0, 1, 0], [1, 0, 0], [0, 0, 0]]
        field = TowerPuzzle.get_field_from_array(field)
        field[0][2].remove(3)
        field[1][1].remove(3)
        field[2][0].remove(3)
        field[2][2].remove(3)
        ss._TowerPuzzle__solve_base_restrictions()

        self.assertEqual(ss._TowerPuzzle__field, field)

    def test_solve_castle_restrictions(self):
        visibility = [[0, 0], [0, 0], [0, 0], [0, 0]]
        field = [[1, 0], [0, 0]]
        field = TowerPuzzle.get_field_from_array(field)
        ss = TowerPuzzle(visibility, field)
        ss._TowerPuzzle__solve_castle_restrictions(0, 0)
        field = [[1, 2], [2, 0]]
        field = TowerPuzzle.get_field_from_array(field)

        self.assertEqual(ss._TowerPuzzle__field, field)

        ss._TowerPuzzle__solve_castle_restrictions(1, 0)
        field = [[1, 2], [2, 1]]
        field = TowerPuzzle.get_field_from_array(field)
        self.assertEqual(ss._TowerPuzzle__field, field)

        visibility = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        field = [[0, 0, 0], [0, 3, 0], [0, 0, 0]]
        field = TowerPuzzle.get_field_from_array(field)
        ss = TowerPuzzle(visibility, field)
        ss._TowerPuzzle__solve_castle_restrictions(1, 1)
        field[0][1].remove(3)
        field[1][0].remove(3)
        field[1][2].remove(3)
        field[2][1].remove(3)

        self.assertEqual(ss._TowerPuzzle__field, field)

        field[2][0].set(1)
        ss._TowerPuzzle__field = field
        ss._TowerPuzzle__solve_castle_restrictions(2, 0)
        field[0][0].remove(1)
        field[1][0].set(2)
        field[2][1].set(2)
        field[2][2].remove(1)

        self.assertEqual(ss._TowerPuzzle__field, field)

        visibility = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        field = [[0, 0, 0], [0, 3, 0], [0, 0, 0]]
        field = TowerPuzzle.get_field_from_array(field)
        ss = TowerPuzzle(visibility, field)
        ss._TowerPuzzle__solve_castle_restrictions(0, 0)

        self.assertEqual(ss._TowerPuzzle__field, field)

        visibility = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        field = [[0, 0, 0], [0, 3, 0], [0, 0, 0]]
        field = TowerPuzzle.get_field_from_array(field)
        ss = TowerPuzzle(visibility, field)
        field[0][1].remove(3)
        field[1][0].remove(3)
        field[1][2].remove(3)
        field[2][1].remove(3)
        field[2][0].set(3)
        ss._TowerPuzzle__field = field
        field[0][0].remove(3)

        self.assertEqual(ss._TowerPuzzle__field, field)

    def test_only_one_row(self):
        visibility = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        field = [[0, 0, 0], [0, 0, 1], [0, 0, 0]]
        field = TowerPuzzle.get_field_from_array(field)
        field[1][1].remove(3)
        ss = TowerPuzzle(visibility, field)
        ss._TowerPuzzle__solve_only_one_row(1)
        field[1][0].set(3)

        self.assertEqual(ss._TowerPuzzle__field, field)

        ss._TowerPuzzle__solve_only_one_row(1)
        field[1][1].set(2)

        self.assertEqual(ss._TowerPuzzle__field, field)

        ss._TowerPuzzle__solve_only_one_row(1)
        field[1][2].set(1)

        self.assertEqual(ss._TowerPuzzle__field, field)

    def test_only_one_column(self):
        visibility = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        field = [[0, 0, 0], [0, 0, 0], [0, 0, 1]]
        field = TowerPuzzle.get_field_from_array(field)
        field[1][2].remove(3)
        ss = TowerPuzzle(visibility, field)
        ss._TowerPuzzle__solve_only_one_column(2)
        field[0][2].set(3)

        self.assertEqual(ss._TowerPuzzle__field, field)

        ss._TowerPuzzle__solve_only_one_column(2)
        field[1][2].set(2)

        self.assertEqual(ss._TowerPuzzle__field, field)

        ss._TowerPuzzle__solve_only_one_column(2)
        field[2][2].set(1)

        self.assertEqual(ss._TowerPuzzle__field, field)

    def test_get_possible_rows(self):
        visibility = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        field = [[3, 0, 0, 4], [4, 0, 0, 3], [1, 4, 3, 2], [2, 3, 4, 1]]
        field = TowerPuzzle.get_field_from_array(field)
        field[0][1].remove(4)
        field[0][1].remove(3)
        field[0][2].remove(4)
        field[0][2].remove(3)
        ss = TowerPuzzle(visibility, field)
        possible_rows = [[3, 1, 1, 4], [3, 2, 1, 4], [3, 1, 2, 4], [3, 2, 2, 4]]
        possible_rows = TowerPuzzle.get_field_from_array(possible_rows)
        self.assertEqual(ss._TowerPuzzle__get_possible_rows(0), possible_rows)

    def test_get_possible_columns(self):
        visibility = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        field = [[3, 0, 0, 4], [4, 0, 0, 3], [1, 4, 3, 2], [2, 3, 4, 1]]
        field = TowerPuzzle.get_field_from_array(field)
        field[0][1].remove(4)
        field[0][1].remove(3)
        field[1][1].remove(4)
        field[1][1].remove(3)
        ss = TowerPuzzle(visibility, field)
        possible_columns = [[1, 1, 4, 3], [2, 1, 4, 3], [1, 2, 4, 3], [2, 2, 4, 3]]
        possible_columns = TowerPuzzle.get_field_from_array(possible_columns)
        self.assertEqual(ss._TowerPuzzle__get_possible_columns(1), possible_columns)

    def test_get_right_vector_from_possible(self):
        possible_matrix = [[1, 1, 4, 3], [2, 1, 4, 3], [1, 2, 4, 3], [2, 2, 4, 3]]
        possible_matrix = TowerPuzzle.get_field_from_array(possible_matrix)
        right_matrix = [[2, 1, 4, 3], [1, 2, 4, 3]]
        right_matrix = TowerPuzzle.get_field_from_array(right_matrix)

        self.assertEqual(TowerPuzzle._TowerPuzzle__get_right_vector_from_possible(0, 0, possible_matrix), right_matrix)

        possible_matrix = [[1, 1, 4, 3], [2, 1, 4, 3], [1, 2, 4, 3], [2, 2, 4, 3], [3, 4, 2, 1], [1, 2, 3, 4],
                           [4, 3, 1, 2]]
        possible_matrix = TowerPuzzle.get_field_from_array(possible_matrix)
        right_matrix = [[2, 1, 4, 3], [1, 2, 4, 3], [3, 4, 2, 1], [1, 2, 3, 4], [4, 3, 1, 2]]
        right_matrix = TowerPuzzle.get_field_from_array(right_matrix)

        self.assertEqual(TowerPuzzle._TowerPuzzle__get_right_vector_from_possible(0, 0, possible_matrix), right_matrix)

        possible_matrix = [[1, 1, 4, 3], [2, 1, 4, 3], [1, 2, 4, 3], [2, 2, 4, 3]]
        possible_matrix = TowerPuzzle.get_field_from_array(possible_matrix)
        right_matrix = [[1, 2, 4, 3]]
        right_matrix = TowerPuzzle.get_field_from_array(right_matrix)

        self.assertEqual(TowerPuzzle._TowerPuzzle__get_right_vector_from_possible(3, 2, possible_matrix), right_matrix)

        possible_matrix = [[1, 1, 4, 3], [2, 1, 4, 3], [1, 2, 4, 3], [2, 2, 4, 3], [3, 4, 2, 1], [1, 2, 3, 4],
                           [4, 3, 1, 2]]
        possible_matrix = TowerPuzzle.get_field_from_array(possible_matrix)
        right_matrix = [[1, 2, 4, 3]]
        right_matrix = TowerPuzzle.get_field_from_array(right_matrix)

        self.assertEqual(TowerPuzzle._TowerPuzzle__get_right_vector_from_possible(3, 2, possible_matrix), right_matrix)

        possible_matrix = [[1, 1, 4, 3], [2, 1, 4, 3], [1, 2, 4, 3], [2, 2, 4, 3], [3, 4, 2, 1], [1, 2, 3, 4],
                           [4, 3, 1, 2]]
        possible_matrix = TowerPuzzle.get_field_from_array(possible_matrix)
        right_matrix = []
        right_matrix = TowerPuzzle.get_field_from_array(right_matrix)

        self.assertEqual(TowerPuzzle._TowerPuzzle__get_right_vector_from_possible(2, 1, possible_matrix), right_matrix)

    def test_get_cell_vector_from_matrix(self):
        matrix = [[2, 1, 4, 3], [1, 2, 4, 3]]
        matrix = TowerPuzzle.get_field_from_array(matrix)
        vector = [[0, 0, 4, 3]]
        vector = TowerPuzzle.get_field_from_array(vector)
        vector[0][0].remove(3)
        vector[0][0].remove(4)
        vector[0][1].remove(3)
        vector[0][1].remove(4)
        self.assertEqual(TowerPuzzle._TowerPuzzle__get_cell_vector_from_matrix(matrix), vector[0])

        matrix = [[2, 1, 6, 9, 7, 8, 4, 3, 5], [2, 8, 6, 9, 7, 1, 4, 3, 5], [2, 8, 6, 9, 7, 3, 4, 1, 5]]
        matrix = TowerPuzzle.get_field_from_array(matrix)
        vector = [[2, 0, 6, 9, 7, 0, 4, 0, 5]]
        vector = TowerPuzzle.get_field_from_array(vector)
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

        self.assertEqual(TowerPuzzle._TowerPuzzle__get_cell_vector_from_matrix(matrix), vector[0])

    def test_solve_visibility_restriction_row(self):
        visibility = [[2, 2, 1, 4], [3, 2, 1, 2], [2, 3, 3, 1], [2, 3, 2, 1]]
        field = [[2, 1, 4, 3], [3, 4, 0, 0], [4, 3, 0, 0], [1, 2, 3, 4]]
        field = TowerPuzzle.get_field_from_array(field)
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

        ss._TowerPuzzle__solve_visibility_restriction_row(1)
        self.assertEqual(ss._TowerPuzzle__field, field)

        field[2][2].set(1)
        field[2][3].set(2)

        ss._TowerPuzzle__solve_visibility_restriction_row(2)
        self.assertEqual(ss._TowerPuzzle__field, field)

    def test_solve_visibility_restriction_column(self):
        visibility = [[2, 1, 2, 3], [2, 3, 3, 1], [1, 2, 3, 2], [2, 2, 1, 4]]
        field = [[3, 0, 0, 4], [4, 0, 0, 3], [1, 4, 3, 2], [2, 3, 4, 1]]
        field = TowerPuzzle.get_field_from_array(field)
        field[0][1].remove(4)
        field[0][1].remove(3)
        field[0][2].remove(4)
        field[0][2].remove(3)
        field[1][1].remove(4)
        field[1][1].remove(3)
        field[1][2].remove(4)
        field[1][2].remove(3)
        ss = TowerPuzzle(visibility, deepcopy(field))
        field[0][1].set(1)
        field[1][1].set(2)

        ss._TowerPuzzle__solve_visibility_restriction_column(1)
        self.assertEqual(ss._TowerPuzzle__field, field)

        field[0][2].set(2)
        field[1][2].set(1)

        ss._TowerPuzzle__solve_visibility_restriction_column(2)
        self.assertEqual(ss._TowerPuzzle__field, field)

    def test_solve_with_field(self):
        visibility = [[1, 4, 2, 2], [1, 2, 3, 2], [4, 1, 2, 2], [2, 1, 2, 3]]
        field = [[0, 0, 0, 0], [0, 2, 0, 0], [2, 1, 4, 3], [0, 0, 0, 0]]
        field = TowerPuzzle.get_field_from_array(field)
        ss = TowerPuzzle(visibility, deepcopy(field))
        field = [[4, 3, 2, 1], [1, 2, 3, 4], [2, 1, 4, 3], [3, 4, 1, 2]]
        field = TowerPuzzle.get_field_from_array(field)
        ss.solve()
        self.assertEqual(ss._TowerPuzzle__field, field)

    def test_solve_with_empty_visibility(self):
        visibility = [[1, 4, 0, 2], [1, 2, 3, 2], [4, 1, 0, 2], [2, 1, 2, 3]]
        field = [[0, 0, 0, 0], [0, 2, 0, 0], [2, 1, 4, 3], [0, 0, 0, 0]]
        field = TowerPuzzle.get_field_from_array(field)
        ss = TowerPuzzle(visibility, deepcopy(field))
        field = [[4, 3, 2, 1], [1, 2, 3, 4], [2, 1, 4, 3], [3, 4, 1, 2]]
        field = TowerPuzzle.get_field_from_array(field)
        ss.solve()
        self.assertEqual(ss._TowerPuzzle__field, field)

        visibility = [[1, 4, 0, 2], [1, 2, 3, 2], [4, 1, 0, 2], [2, 1, 2, 3]]
        field = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        field = TowerPuzzle.get_field_from_array(field)
        ss = TowerPuzzle(visibility, deepcopy(field))
        field = [[4, 3, 2, 1], [1, 2, 3, 4], [2, 1, 4, 3], [3, 4, 1, 2]]
        field = TowerPuzzle.get_field_from_array(field)
        ss.solve()
        self.assertEqual(ss._TowerPuzzle__field, field)

    def test_brute_force(self):
        visibility = [[0, 0], [0, 0], [0, 0], [0, 0]]
        ss = TowerPuzzle(visibility)
        ss.solve()
        field = [[1, 2], [2, 1]]
        field = TowerPuzzle.get_field_from_array(field)
        self.assertEqual(ss._TowerPuzzle__field, field)

        visibility = [[0, 0], [1, 0], [0, 0], [0, 0]]
        ss = TowerPuzzle(visibility)
        ss.solve()
        field = [[2, 1], [1, 2]]
        field = TowerPuzzle.get_field_from_array(field)
        self.assertEqual(ss._TowerPuzzle__field, field)

        visibility = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        ss = TowerPuzzle(visibility)
        ss.solve()
        field = [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
        field = TowerPuzzle.get_field_from_array(field)
        self.assertEqual(ss._TowerPuzzle__field, field)

        visibility = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        ss = TowerPuzzle(visibility)
        ss.solve()
        field = [[1, 2, 3, 4], [2, 1, 4, 3], [3, 4, 1, 2], [4, 3, 2, 1]]
        field = TowerPuzzle.get_field_from_array(field)
        self.assertEqual(ss._TowerPuzzle__field, field)

        visibility = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        field = [[0, 0, 0], [0, 2, 0], [0, 0, 0]]
        field = TowerPuzzle.get_field_from_array(field)
        ss = TowerPuzzle(visibility, deepcopy(field))
        ss.solve()
        field = [[1, 3, 2], [3, 2, 1], [2, 1, 3]]
        field = TowerPuzzle.get_field_from_array(field)
        self.assertEqual(ss._TowerPuzzle__field, field)

        visibility = [[0, 2, 0, 0], [0, 0, 0, 3], [0, 0, 0, 0], [0, 0, 2, 0]]
        field = [[0, 0, 0, 0], [0, 0, 0, 0], [2, 0, 0, 0], [0, 0, 0, 2]]
        field = TowerPuzzle.get_field_from_array(field)
        ss = TowerPuzzle(visibility, deepcopy(field))
        ss.solve()
        field = [[3, 2, 4, 1], [1, 4, 2, 3], [2, 3, 1, 4], [4, 1, 3, 2]]
        field = TowerPuzzle.get_field_from_array(field)
        self.assertEqual(ss._TowerPuzzle__field, field)

        visibility = [[0, 0, 0, 0], [3, 2, 1, 0], [0, 0, 0, 0], [0, 0, 3, 3]]
        ss = TowerPuzzle(visibility)
        field = [[1, 3, 4, 2], [2, 1, 3, 4], [4, 2, 1, 3], [3, 4, 2, 1]]
        field = TowerPuzzle.get_field_from_array(field)
        ss.solve()
        self.assertEqual(ss._TowerPuzzle__field, field)


class Test_Cell(unittest.TestCase):

    def test_init(self):
        cell = TowerPuzzle._TowerPuzzle__Cell(9)
        self.assertEqual(cell.array, [1, 2, 3, 4, 5, 6, 7, 8, 9])

        cell = TowerPuzzle._TowerPuzzle__Cell(1)
        self.assertEqual(cell.array, [1])

        cell = TowerPuzzle._TowerPuzzle__Cell(20)
        self.assertEqual(cell.array, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

        cell = TowerPuzzle._TowerPuzzle__Cell(0)
        self.assertEqual(cell.array, [])

        cell = TowerPuzzle._TowerPuzzle__Cell(0, 4)
        self.assertEqual(cell.array, [])

        cell = TowerPuzzle._TowerPuzzle__Cell(4, 4)
        self.assertEqual(cell.array, [0, 0, 0, 4])

    def test_remove(self):
        cell = TowerPuzzle._TowerPuzzle__Cell(9)

        cell.remove(1)
        self.assertEqual(cell.array, [0, 2, 3, 4, 5, 6, 7, 8, 9])

        cell.remove(1)
        self.assertEqual(cell.array, [0, 2, 3, 4, 5, 6, 7, 8, 9])

        cell.remove(7)
        self.assertEqual(cell.array, [0, 2, 3, 4, 5, 6, 0, 8, 9])

    def test_set(self):
        cell = TowerPuzzle._TowerPuzzle__Cell(9)

        cell.set(4)
        self.assertEqual(cell.array, [0, 0, 0, 4, 0, 0, 0, 0, 0, ])

        cell.set(6)
        self.assertEqual(cell.array, [0, 0, 0, 0, 0, 6, 0, 0, 0, ])

        cell.set(6)
        self.assertEqual(cell.array, [0, 0, 0, 0, 0, 6, 0, 0, 0, ])

    def test_get_not_zeros(self):
        cell = TowerPuzzle._TowerPuzzle__Cell(9)

        self.assertEqual(cell.get_not_zeros(), [1, 2, 3, 4, 5, 6, 7, 8, 9])

        cell.array = [1, 0, 3, 4, 0, 0, 0, 8, 0]
        self.assertEqual(cell.get_not_zeros(), [1, 3, 4, 8])

        cell.array = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(cell.get_not_zeros(), [])

    def test_str(self):
        cell = TowerPuzzle._TowerPuzzle__Cell(9)

        self.assertEqual(str(cell), "[1 2 3 4 5 6 7 8 9]")

        cell.remove(6)
        self.assertEqual(str(cell), "[1 2 3 4 5 - 7 8 9]")

        cell.remove(5)
        self.assertEqual(str(cell), "[1 2 3 4 - - 7 8 9]")

        cell.set(6)
        self.assertEqual(str(cell), "[- - - - - 6 - - -]")

    def test_int(self):
        cell = TowerPuzzle._TowerPuzzle__Cell(9)

        self.assertEqual(int(cell), 0)

        cell.remove(8)
        self.assertEqual(int(cell), 0)

        cell.set(3)
        self.assertEqual(int(cell), 3)

        cell.set(9)
        self.assertEqual(int(cell), 9)

    def test_bool(self):
        cell = TowerPuzzle._TowerPuzzle__Cell(3)
        self.assertFalse(cell)

        cell = TowerPuzzle._TowerPuzzle__Cell(0)
        self.assertFalse(cell)

        cell = TowerPuzzle._TowerPuzzle__Cell(1, 1)
        self.assertTrue(cell)

        cell = TowerPuzzle._TowerPuzzle__Cell(4)
        cell.set(4)
        self.assertTrue(cell)

        cell = TowerPuzzle._TowerPuzzle__Cell(3)
        cell.remove(1)
        cell.remove(2)
        self.assertTrue(cell)


class Test_text(unittest.TestCase):

    @staticmethod
    def get_result(i):
        directory = "Tests/"
        input_prefix = "input"
        output_prefix = "output"
        input_name = directory + input_prefix + str(int(i / 10)) + str(i % 10)
        output_name = directory + output_prefix + str(int(i / 10)) + str(i % 10)
        input_file = open(input_name)
        size = int(input_file.readline()[:-1])
        visibility = []
        input_file.readline()
        for i in range(4):
            split_array = input_file.readline()[:-1].split(' ')
            if len(split_array) == 0:
                i -= 1
                continue
            row = []
            if split_array == ['']:
                raise RuntimeError("Wrong input: empty string")
            for number in split_array:
                row.append(int(number))
            visibility.append(row)

        field = []
        input_file.readline()

        for i in range(size):
            split_array = input_file.readline()[:-1].split(' ')
            row = []
            if split_array == [''] and field != []:
                raise RuntimeError("Wrong input: empty string")
            if split_array == ['']:
                break
            for number in split_array:
                row.append(int(number))
            field.append(row)

        input_file.close()
        field = TowerPuzzle.get_field_from_array(field)

        if field:
            tower_puzzle = TowerPuzzle(visibility, field)
            tower_puzzle.solve()
            output = open(output_name)
            answer = ''
            for line in output.readlines():
                answer += line
            output.close()
            return tower_puzzle.get_field_string(), answer

        else:
            tower_puzzle = TowerPuzzle(visibility)
            tower_puzzle.solve()
            output = open(output_name)
            answer = ''
            for line in output.readlines():
                answer += line
            output.close()
            return tower_puzzle.get_field_string(), answer

    def test_1(self, i=1):
        result, answer = self.get_result(i)
        self.assertEqual(result, answer)

    def test_2(self, i=2):
        result, answer = self.get_result(i)
        self.assertEqual(result, answer)

    def test_3(self, i=3):
        result, answer = self.get_result(i)
        self.assertEqual(result, answer)

    def test_4(self, i=4):
        result, answer = self.get_result(i)
        self.assertEqual(result, answer)

    def test_5(self, i=5):
        result, answer = self.get_result(i)
        self.assertEqual(result, answer)

    def test_6(self, i=6):
        result, answer = self.get_result(i)
        self.assertEqual(result, answer)

    def test_7(self, i=7):
        result, answer = self.get_result(i)
        self.assertEqual(result, answer)

    def test_8(self, i=8):
        result, answer = self.get_result(i)
        self.assertEqual(result, answer)

    def test_9(self, i=9):
        result, answer = self.get_result(i)
        self.assertEqual(result, answer)

    def test_10(self, i=10):
        result, answer = self.get_result(i)
        self.assertEqual(result, answer)

    def test_11(self, i=11):
        result, answer = self.get_result(i)
        self.assertEqual(result, answer)

    def test_12(self, i=12):
        result, answer = self.get_result(i)
        self.assertEqual(result, answer)

    def test_13(self, i=13):
        result, answer = self.get_result(i)
        self.assertEqual(result, answer)


class Test_productivity(unittest.TestCase):

    @staticmethod
    def get_result(i):
        directory = "Tests/Productivity_tests/"
        input_prefix = "input"
        output_prefix = "output"
        input_name = directory + input_prefix + str(int(i / 10)) + str(i % 10)
        output_name = directory + output_prefix + str(int(i / 10)) + str(i % 10)
        input_file = open(input_name)
        size = int(input_file.readline()[:-1])
        visibility = []
        input_file.readline()
        for i in range(4):
            split_array = input_file.readline()[:-1].split(' ')
            if len(split_array) == 0:
                i -= 1
                continue
            row = []
            if split_array == ['']:
                raise RuntimeError("Wrong input: empty string")
            for number in split_array:
                row.append(int(number))
            visibility.append(row)

        field = []
        input_file.readline()

        for i in range(size):
            split_array = input_file.readline()[:-1].split(' ')
            row = []
            if split_array == [''] and field != []:
                raise RuntimeError("Wrong input: empty string")
            if split_array == ['']:
                break
            for number in split_array:
                row.append(int(number))
            field.append(row)

        input_file.close()
        field = TowerPuzzle.get_field_from_array(field)

        if field:
            tower_puzzle = TowerPuzzle(visibility, field)
            tower_puzzle.solve()
            output = open(output_name)
            answer = ''
            for line in output.readlines():
                answer += line
            output.close()
            return tower_puzzle.get_field_string(), answer

        else:
            tower_puzzle = TowerPuzzle(visibility)
            tower_puzzle.solve()
            output = open(output_name)
            answer = ''
            for line in output.readlines():
                answer += line
            output.close()
            return tower_puzzle.get_field_string(), answer

    @staticmethod
    def get_result_brute_force(i):
        directory = "Tests/Productivity_tests/"
        input_prefix = "input"
        output_prefix = "output"
        input_name = directory + input_prefix + str(int(i / 10)) + str(i % 10)
        output_name = directory + output_prefix + str(int(i / 10)) + str(i % 10)
        input_file = open(input_name)
        size = int(input_file.readline()[:-1])
        visibility = []
        input_file.readline()
        for i in range(4):
            split_array = input_file.readline()[:-1].split(' ')
            if len(split_array) == 0:
                i -= 1
                continue
            row = []
            if split_array == ['']:
                raise RuntimeError("Wrong input: empty string")
            for number in split_array:
                row.append(int(number))
            visibility.append(row)

        field = []
        input_file.readline()

        for i in range(size):
            split_array = input_file.readline()[:-1].split(' ')
            row = []
            if split_array == [''] and field != []:
                raise RuntimeError("Wrong input: empty string")
            if split_array == ['']:
                break
            for number in split_array:
                row.append(int(number))
            field.append(row)

        input_file.close()
        field = TowerPuzzle.get_field_from_array(field)

        if field:
            tower_puzzle = TowerPuzzle(visibility, field)
            tower_puzzle.solve_by_brute_force()
            output = open(output_name)
            answer = ''
            for line in output.readlines():
                answer += line
            output.close()
            return tower_puzzle.get_field_string(), answer

        else:
            tower_puzzle = TowerPuzzle(visibility)
            tower_puzzle.solve_by_brute_force()
            output = open(output_name)
            answer = ''
            for line in output.readlines():
                answer += line
            output.close()
            return tower_puzzle.get_field_string(), answer

    def test_1(self, i=1):
        result, answer = self.get_result(i)
        self.assertEqual(result, answer)

    def test_1_b(self, i=1):
        result, answer = self.get_result_brute_force(i)
        self.assertEqual(result, answer)

    def test_2(self, i=2):
        result, answer = self.get_result(i)
        self.assertEqual(result, answer)

    def test_2_b(self, i=2):
        result, answer = self.get_result_brute_force(i)
        self.assertEqual(result, answer)

    def test_3(self, i=3):
        result, answer = self.get_result(i)
        self.assertEqual(result, answer)

    def test_3_b(self, i=3):
        result, answer = self.get_result_brute_force(i)
        self.assertEqual(result, answer)

    def test_4(self, i=4):
        result, answer = self.get_result(i)
        self.assertEqual(result, answer)

    def test_4_b(self, i=4):
        result, answer = self.get_result_brute_force(i)
        self.assertEqual(result, answer)

    def test_5(self, i=5):
        result, answer = self.get_result(i)
        self.assertEqual(result, answer)

    def test_5_b(self, i=5):
        result, answer = self.get_result_brute_force(i)
        self.assertEqual(result, answer)

    def test_6(self, i=6):
        result, answer = self.get_result(i)
        self.assertEqual(result, answer)

    def test_6_b(self, i=6):
        result, answer = self.get_result_brute_force(i)
        self.assertEqual(result, answer)

    def test_7(self, i=7):
        result, answer = self.get_result(i)
        self.assertEqual(result, answer)

    def test_7_b(self, i=7):
        result, answer = self.get_result_brute_force(i)
        self.assertEqual(result, answer)

    def test_8(self, i=8):
        result, answer = self.get_result(i)
        self.assertEqual(result, answer)

    def test_8_b(self, i=8):
        result, answer = self.get_result_brute_force(i)
        self.assertEqual(result, answer)

    def test_9(self, i=9):
        result, answer = self.get_result(i)
        self.assertEqual(result, answer)

    def test_9_b(self, i=9):
        result, answer = self.get_result_brute_force(i)
        self.assertEqual(result, answer)



