from multiprocessing import Process, Event


class rockPaperScissorApp(Process):
    def __init__(self) -> None:
        super(rockPaperScissorApp, self).__init__()
