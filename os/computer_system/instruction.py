import random

class Instruction:
    """
    Simulates an instruction - an event can be a normal instruction or an interrupt

    An instruction takes any where between 0.5 and 1.5 seconds to execute
    """
    def __init__(self) -> None:
        self.time = random.uniform(0.5, 1.5)