import unittest
import TowerPuzzle


class Test_class(unittest.TestCase):
    def test_init(self):
        visibility = [[1, 2, 3], [1, 0, -5], [10, 12, 13], [11, 12, 13]]
        field = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        ss = TowerPuzzle.TowerPuzzle(visibility)

        self.assertEqual(ss.visibility_left, visibility[0])
        self.assertEqual(ss.visibility_up, visibility[1])
        self.assertEqual(ss.visibility_right, visibility[2])
        self.assertEqual(ss.visibility_down, visibility[3])
        self.assertEqual(ss.field, field)

    def test_count(self):
        visibility = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        field = [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
        ss = TowerPuzzle.TowerPuzzle(visibility)
        ss.field = field

        self.assertEqual(ss.count_visibility_horizontal(0), 3)
        self.assertEqual(ss.count_visibility_horizontal(1), 2)
        self.assertEqual(ss.count_visibility_horizontal(2), 1)

        self.assertEqual(ss.count_visibility_vertical(0), 3)
        self.assertEqual(ss.count_visibility_vertical(1), 2)
        self.assertEqual(ss.count_visibility_vertical(2), 1)

        field = [[3, 2, 5, 4, 1], [4, 5, 3, 1, 2], [5, 4, 1, 2, 3], [2, 1, 4, 3, 5], [1, 3, 2, 5, 4]]
        ss.field = field

        self.assertEqual(ss.count_visibility_horizontal(0), 2)
        self.assertEqual(ss.count_visibility_horizontal(1), 2)
        self.assertEqual(ss.count_visibility_horizontal(2), 1)
        self.assertEqual(ss.count_visibility_horizontal(3), 3)
        self.assertEqual(ss.count_visibility_horizontal(4), 3)

        self.assertEqual(ss.count_visibility_vertical(0), 3)
        self.assertEqual(ss.count_visibility_vertical(1), 2)
        self.assertEqual(ss.count_visibility_vertical(2), 1)
        self.assertEqual(ss.count_visibility_vertical(3), 2)
        self.assertEqual(ss.count_visibility_vertical(4), 4)
