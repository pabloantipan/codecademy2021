from datetime import datetime
from .gamelogic import build_typcal_game_structure, who_wins

GAME_AVALIABLE_CHOICES = ["rock", "paper", "scissor"]
GAME_LOGIC_DICT = build_typcal_game_structure(GAME_AVALIABLE_CHOICES)


class Game:
    def __init__(self):
        self._rules: dict = GAME_LOGIC_DICT
        self._matchid: int = None
        self._createdon: datetime = datetime.now()
        # 1: untouched, 2: player a won, 3: player b won, 4: tie
        self._winner: int = 0
        # 1: rock, 2: paper, 3: scissor
        self._choicea: str = None
        # 1: rock, 2: paper, 3: scissor
        self._choiceb: str = None

    def lets_play(self, choicea: str, choiceb: str) -> str:
        game_result, tie_bool = who_wins(self._rules, choicea, choiceb)

        if tie_bool:
            self._winner = 4

        if game_result == "player_a_wins":
            self._winner = 2

        if game_result == "player_b_wins":
            self._winner = 3

    @property
    def player_a(self) -> any:
        return self._choicea

    @player_a.setter
    def player_a(self, choice: any) -> bool:
        self._choicea = choice
        return True

    @property
    def player_b(self) -> any:
        return self._choiceb

    @player_b.setter
    def player_b(self, choice: any) -> bool:
        self._choiceb = choice
        return True

    @property
    def rules(self) -> dict:
        return self._rules

    @rules.setter
    def rules(self, r: dict) -> bool:
        self._rules = r
        return True

    @property
    def created_on(self) -> datetime:
        return self._createdon


# Play till one wins!
class Match:
    def __init__(self, gamesforwinning: int):
        self._sessionid = None
        self._createdon = datetime.now()
        self._games_for_winning = gamesforwinning
        self._scores: tuple
        self._winner = None
        self._games = []  # [ Game(), ... ]

    def add_game(self, game: Game) -> bool:
        self._games.append(game)
        return True

    def _who_wins(self) -> bool:
        # True if someone wins, else False
        for game in self._games:
            if game._winner == 2:  # wins player a

                pass
            if game._winner == 3:  # wins player b
                pass
            if game._winner == 4:  # tie
                pass

        pass

    @property
    def lenght(self) -> int:
        return len(self._games)

    @property
    def games(self) -> list:
        return self._games

    @property
    def created_on(self) -> datetime:
        return self._createdon


class Session:
    def __init__(self):
        self._sessionid = None
        self._createdon = datetime.now()

    @property
    def created_on(self) -> datetime:
        return self._createdon
