from math import sqrt


def calculate_area_bh(base: int or float, height: int or float) -> int or float:
    """It ...
    :args:
    :raises:
    :returns:
    """
    if not isinstance(base, [int, float]) or not isinstance(height, [int, float]):
        raise TypeError("args must be int or float instances")

    return base * height / 2


def triangle_type(
    sidea: int or float, sideb: int or float, sidec: int or float
) -> tuple:
    """It ...
    :args:
    :raises:
    :returns:
    """
    # (istriangle: bool, type:str)
    sides = [sidea, sideb, sidec]
    # get if it is a triangle
    if not validate_triangle(sides):
        # raise ValueError("Please be sure that sides are a triangle")
        return (False, None)

    if sides[0] == sides[1] and sides[0] == sides[2]:
        return (True, "equilatero")

    if sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]:
        return (True, "isoceles")

    return (True, "escaleno")


def calculate_area_semiperimeter(
    sidea: int or float, sideb: int or float, sidec: int or float
) -> int or float:
    """It ...
    :args:
    :raises:
    :returns:
    """
    if (
        not isinstance(sidea, (int, float))
        or not isinstance(sideb, (int, float))
        or not isinstance(sidec, (int, float))
    ):
        raise TypeError("args must be int or float instances")
    sides = [sidea, sideb, sidec]
    sides.sort(reverse=True)

    sp = sum(sides) / 2
    return sqrt(sp * (sp - sidea) * (sp - sideb) * (sp - sidec))


def validate_triangle(sides: list) -> bool:
    """It ...
    :args:
    :raises:
    :returns:
    """
    if not isinstance(sides, list) or len(sides) != 3:
        raise TypeError(f"Argument must be a list instance. Got {sides}: {type(sides)}")
    for side in sides:
        if not isinstance(side, (int, float)):
            raise TypeError(
                f"Side must be int or float instance. Got {side}: {type(side)}"
            )
    sides.sort(reverse=True)
    # get if it is a triangle
    if not sides[0] < sides[1] + sides[2]:
        return False
    if not sides[1] < sides[0] + sides[2]:
        return False
    if not sides[2] < sides[1] + sides[0]:
        return False
    return True
