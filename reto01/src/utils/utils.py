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


def yesorno_task(task: str) -> bool:
    # (task: bool, exit: bool)
    task = f"{task}: Si / No . (Escribe 'Salir' para terminar): "
    while True:
        res = input(task)
        if res.lower() == "si":
            return (True, False)
        if res.lower() == "no":
            return (False, False)
        if res.lower() == "salir":
            return (None, True)
        else:
            print("Por favor, responde 'Si' o 'No'")
            continue
