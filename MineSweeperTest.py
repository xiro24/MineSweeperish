import unittest

from MineSweeper import MineSweeper


class MineSweeperTest(unittest.TestCase):
    def setUp(self):
        self.minesweeper = MineSweeper(3, 3)

    def test_graph_is_set_correctly(self):
        self.assertEqual(len(self.minesweeper.graph), 3)


if __name__ == '__main__':
    unittest.main()
