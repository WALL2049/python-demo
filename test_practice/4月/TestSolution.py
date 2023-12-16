import unittest
from word_search import Solution


class TestSolution(unittest.TestCase):
    def test_WordSearch(self):
        board = [['c', 'f', 'b', 'm'], ['r', 'o', 'o', 'd'], ['a', 't', 'w', 'k'], ['h', 'c', 'e', 'f']]
        words = ['food', 'foot', 'rat', 'wet']
        a = Solution()
        result = a.findWords(board, words)
        self.assertEqual(result, ["food", "rat"])
