from sys import path as syspath
from os import path
import unittest

syspath.append(path.abspath("../../src"))

from rockpaperscissor import build_typcal_game_structure, who_wins


class TestingRockPaperScissor(unittest.TestCase):
    def setUp(self):
        pass

    def test010(self):
        # python gamelogic_test.py TestingRockPaperScissor.test010
        res = build_typcal_game_structure(["rock", "paper", "scissor"])
        print(res)

    def test020(self):
        # python gamelogic_test.py TestingRockPaperScissor.test020
        rules = build_typcal_game_structure(["rock", "paper", "scissor"])
        # player a wins
        self.assertEqual(who_wins(rules, "paper", "rock"), ("player_a_wins", False))
        self.assertEqual(who_wins(rules, "rock", "scissor"), ("player_a_wins", False))
        self.assertEqual(who_wins(rules, "scissor", "paper"), ("player_a_wins", False))
        # player b wins
        self.assertEqual(who_wins(rules, "scissor", "rock"), ("player_b_wins", False))
        self.assertEqual(who_wins(rules, "rock", "paper"), ("player_b_wins", False))
        self.assertEqual(who_wins(rules, "paper", "scissor"), ("player_b_wins", False))
        # tie
        self.assertEqual(who_wins(rules, "paper", "paper"), ("tie", True))
        self.assertEqual(who_wins(rules, "rock", "rock"), ("tie", True))
        self.assertEqual(who_wins(rules, "scissor", "scissor"), ("tie", True))


if __name__ == "__main__":
    unittest.main()
