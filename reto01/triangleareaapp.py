from multiprocessing import Process, Event
from statistics import mean
from math import sqrt
import enquiries


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


def get_dim(task: str) -> tuple:
    # (result:float, exit: bool)
    dimm = None
    task = f"{task}. (Escribe 'Salir' para terminar): "
    while True:
        dimm = input(task)
        if dimm.lower() == "salir":
            return (None, True)
        if not dimm.isnumeric():
            print("Por favor ingresa un numero")
            continue
        dimm = float(dimm)
        break
    return (dimm, False)


class TriangleAreaApp(Process):
    def __init__(self):
        self.shutdown_evt = Event()
        super(TriangleAreaApp, self).__init__()

    def run(self):
        while not self.shutdown_evt.is_set():
            exit_flag = False
            base_options = [
                "Calcular area triangulo segun b x h / 2",
                "Calular area segun semiperimetro",
                "Determinar tipo de triangulo",
                "Salir",
            ]

            user_task = enquiries.choose(
                "Por favor indica la operacion que deseas realizar:",
                base_options,
            )
            if user_task == "Salir":
                self.shutdown()
                print("Adios ... ")
                return
            elif user_task == "Calcular area triangulo segun b x h / 2":
                _, exit_flag = self.calculate_area_bh()

            elif user_task == "Calular area segun semiperimetro":
                _, exit_flag = self.calculate_area_sp()

            elif user_task == "Determinar tipo de triangulo":
                _, exit_flag = self.get_triangle_type()

            if exit_flag:
                self.shutdown()
                print("Adios ... ")
                break

    def calculate_area_bh(self) -> tuple:
        # (result:float, exit: bool)
        task = "Ingresa el valor de la base del triangulo"
        base, exit = get_dim(task)
        if exit:
            return (None, True)

        task = "Ingresa el valor de la altura del triangulo"
        height, exit = get_dim(task)
        if exit:
            return (None, True)
        area = base * height / 2
        print(f"El area de tu triangulo es: {area}\n")
        return (area, False)

    def calculate_area_sp(self) -> tuple:
        # (result:float, exit: bool)
        sides = []
        for sidd in ["a", "b", "c"]:
            task = f"Ingresa el valor del lado {sidd}"
            dimm, exit = get_dim(task)
            if exit:
                return (None, True)
            sides.append(dimm)

        sidea, sideb, sidec = sides
        if not validate_triangle(sides):
            print(
                f"Las dimensiones que ingresaste: {sidea}, {sideb}, {sidec}; no son un triangulo\n"
            )
            return (None, False)

        area = calculate_area_semiperimeter(sidea, sideb, sidec)
        print(f"El area de tu triangulo es: {area}\n")
        return (area, False)

    def get_triangle_type(self) -> str:
        # (result:float, exit: bool)
        sides = []
        for sidd in ["a", "b", "c"]:
            task = f"Ingresa el valor del lado {sidd}"
            dimm, exit = get_dim(task)
            if exit:
                return (None, True)
            sides.append(dimm)

        print(sides)

        sidea, sideb, sidec = sides
        is_tr, tr_type = triangle_type(sidea, sideb, sidec)
        if is_tr:
            print(f"Tu triangulo es de tipo: {tr_type}\n")
        else:
            print(
                f"Las dimensiones que ingresaste: {sidea}, {sideb}, {sidec}; no es un triangulo\n"
            )

        return (tr_type, False)

    def shutdown(self) -> bool:
        self.shutdown_evt.set()
        return True
