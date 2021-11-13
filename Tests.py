import unittest
import TowerPuzzle


class Test_TowerPuzzle(unittest.TestCase):
    def test_init(self):
        visibility = [[1, 2, 3], [1, 0, -5], [10, 12, 13], [11, 12, 13]]
        field = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        ss = TowerPuzzle.TowerPuzzle(visibility)

        self.assertEqual(ss.visibility_left, visibility[0])
        self.assertEqual(ss.visibility_up, visibility[1])
        self.assertEqual(ss.visibility_right, visibility[2])
        self.assertEqual(ss.visibility_down, visibility[3])
        self.assertEqual(ss.field, field)

    def test_count_visibility(self):
        visibility = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        field = [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
        ss = TowerPuzzle.TowerPuzzle(visibility)
        ss.field = field

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
        ss.field = field

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
        ss = TowerPuzzle.TowerPuzzle(visibility)
        ss.field = field

        self.assertEqual(ss.count_unfilled_cells_horizontal(0), 3)
        self.assertEqual(ss.count_unfilled_cells_horizontal(1), 0)
        self.assertEqual(ss.count_unfilled_cells_horizontal(2), 2)

        self.assertEqual(ss.count_unfilled_cells_vertical(0), 2)
        self.assertEqual(ss.count_unfilled_cells_vertical(1), 1)
        self.assertEqual(ss.count_unfilled_cells_vertical(2), 2)


class Test_Cell(unittest.TestCase):

    def test_init(self):
        cell = TowerPuzzle.TowerPuzzle.Cell(9)
        self.assertEqual(cell.array, [1, 2, 3, 4, 5, 6, 7, 8, 9])

        cell = TowerPuzzle.TowerPuzzle.Cell(1)
        self.assertEqual(cell.array, [1])

        cell = TowerPuzzle.TowerPuzzle.Cell(20)
        self.assertEqual(cell.array, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

        cell = TowerPuzzle.TowerPuzzle.Cell(0)
        self.assertEqual(cell.array, [])

        cell = TowerPuzzle.TowerPuzzle.Cell(0, 4)
        self.assertEqual(cell.array, [])

        cell = TowerPuzzle.TowerPuzzle.Cell(4, 4)
        self.assertEqual(cell.array, [0, 0, 0, 4])

    def test_remove(self):
        cell = TowerPuzzle.TowerPuzzle.Cell(9)

        cell.remove(1)
        self.assertEqual(cell.array, [0, 2, 3, 4, 5, 6, 7, 8, 9])

        cell.remove(1)
        self.assertEqual(cell.array, [0, 2, 3, 4, 5, 6, 7, 8, 9])

        cell.remove(7)
        self.assertEqual(cell.array, [0, 2, 3, 4, 5, 6, 0, 8, 9])

    def test_set(self):
        cell = TowerPuzzle.TowerPuzzle.Cell(9)

        cell.set(4)
        self.assertEqual(cell.array, [0, 0, 0, 4, 0, 0, 0, 0, 0, ])

        cell.set(6)
        self.assertEqual(cell.array, [0, 0, 0, 0, 0, 6, 0, 0, 0, ])

        cell.set(6)
        self.assertEqual(cell.array, [0, 0, 0, 0, 0, 6, 0, 0, 0, ])

    def test_get_not_zeros(self):
        cell = TowerPuzzle.TowerPuzzle.Cell(9)

        self.assertEqual(cell.get_not_zeros(), [1, 2, 3, 4, 5, 6, 7, 8, 9])

        cell.array = [1, 0, 3, 4, 0, 0, 0, 8, 0]
        self.assertEqual(cell.get_not_zeros(), [1, 3, 4, 8])

        cell.array = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(cell.get_not_zeros(), [])

    def test_str(self):
        cell = TowerPuzzle.TowerPuzzle.Cell(9)

        self.assertEqual(str(cell), "[1 2 3 4 5 6 7 8 9]")

        cell.remove(6)
        self.assertEqual(str(cell), "[1 2 3 4 5 - 7 8 9]")

        cell.remove(5)
        self.assertEqual(str(cell), "[1 2 3 4 - - 7 8 9]")

        cell.set(6)
        self.assertEqual(str(cell), "[- - - - - 6 - - -]")

    def test_int(self):
        cell = TowerPuzzle.TowerPuzzle.Cell(9)

        self.assertEqual(int(cell), 0)

        cell.remove(8)
        self.assertEqual(int(cell), 0)

        cell.set(3)
        self.assertEqual(int(cell), 3)

        cell.set(9)
        self.assertEqual(int(cell), 9)
