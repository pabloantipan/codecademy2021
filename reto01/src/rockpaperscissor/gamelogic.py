from typing import Type


def build_typcal_game_structure(options: list) -> dict:
    """It takes a ordered list (criteria: element at right
    kills element at left. First kills last. I.e.:
    "rock", "paper", "scissor")
    It supports till three elemments for now.
    This function could help to build more
    complex games
    :args:
        list, with options to rule
    :raises:
        TypeError, if not list is provided
    :returns:
        dict, with rules
    """
    if not isinstance(options, list):
        raise TypeError("options must be and ordered list instance")
    result = {}
    for idx, item in enumerate(options):
        if idx == len(options) - 1:
            result[item] = {
                "kills": [options[idx - 1]],
                "dies": [options[0]],
            }
        else:
            result[item] = {
                "kills": [options[idx - 1]],
                "dies": [options[idx + 1]],
            }

    return result


def validate_rules_structure(rules: dict) -> bool:
    """It validates if rules dict has
    connvinient structure to work with
    For using with try/except
    :args:
        rules, dict to test
    :raises:
        TypeError,
    :returns:
        bool, True if all is right, else raises
    """
    if not isinstance(rules, dict):
        msg = f"rules must be dict instance. Got {type(rules)}"
        raise TypeError(msg)
    for item in rules:
        if not isinstance(rules[item], dict):
            msg = f"each item into rules must be dict instance. Got key {item}: {type(item)}"
            raise TypeError(msg)
        if not "kills" in rules[item] or not "dies" in rules[item]:
            msg = f"each item into rules must have keys 'kills' and 'dies'"
            raise TypeError(msg)
    return True


# HERE! I notice that in a simple game, I only need to kwnow
# about who kills who. I could eliminate 'dies' field, or
# let it empty

# HERE! I noticed that for n players, it is better to return
# lists of winner an loosers. Need Player class. Next stage?


def who_wins(rules: dict, choicea: str, choiceb: str) -> tuple:
    """Based on rules dict, it determines who wins, or tie
    :args:
        rules, dict with structure of rules. Kind this,
        {
            "rock": {
                "kills": ["scissor"],
                "dies": ["paper"],
            },
            "paper": {
                "kills": ["rock"],
                "dies": ["scissor"],
            },
            "scissor": {
                "kills": ["paper"],
                "dies": ["rock"],
            },
        }
        choicea, str with player a's choice,
        what must be a rules dict key, else raises
        choiceb, str with player b's choice,
        what must be a rules dict key, else raises
    :raises:
        TypeError, if rules dict has not correct
        structure
        ValueError, if choices are not into rules
    :returns:
        tuple, like this: (whowins:str, tie: bool)
            whowins in :
            [
                'player_a_wins',
                'player_b_wins',
                'tie'
            ]
    """
    # validating things
    validate_rules_structure(rules)

    if choicea not in rules:
        raise ValueError(f"choice a: {choicea} is not into rules")
    if choiceb not in rules:
        raise ValueError(f"choice b: {choiceb} is not into rules")
    # determining who wins or tie
    if choiceb == choicea:
        return ("tie", True)
    if choiceb in rules[choicea]["kills"]:
        return ("player_a_wins", False)
    if choicea in rules[choiceb]["kills"]:
        return ("player_b_wins", False)
