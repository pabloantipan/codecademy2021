from random import choice
from datetime import datetime


GAME_AVALIABLE_CHOICES = ["rock", "paper", "scissor"]


def generate_response() -> str:
    return choice(GAME_AVALIABLE_CHOICES)
