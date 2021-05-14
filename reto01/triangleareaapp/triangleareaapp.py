from multiprocessing import Process, Event
import enquiries
from utils import get_dim, yesorno_task
from math import sqrt
from .api_triangle import (
    calculate_area_bh,
    triangle_type,
    calculate_area_semiperimeter,
    validate_triangle,
)


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
        # (result:float, triangle_type: str, exit: bool)
        task = "Ingresa el valor de la base del triangulo"
        base, exit = get_dim(task)
        if exit:
            return (None, None, True)

        task = "Ingresa el valor de la altura del triangulo"
        height, exit = get_dim(task)
        if exit:
            return (None, True)
        area = base * height / 2
        print(f"El area de tu triangulo es: {area}\n")

        self.determine_triangle_type(base, height)

        return (area, False)

    def determine_triangle_type(self, base: float, height: float) -> str:
        # (type: str, exit: bool)
        task = "La altura es mediana de la base?"
        res, exit = yesorno_task(task)
        eq_h = sqrt(3) / 2 * base
        if exit:
            return (None, True)
        if res and eq_h == height:
            print("Tu triangulo es equilatero\n")
            return ("equilatero", False)
        if res and not eq_h == height:
            print("Tu triangulo es isoceles\n")
            return ("isoceles", False)
        if not res:
            print("Tu triangulo es escaleno\n")
            return ("escaleno", False)

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
