import random

class BlockingEvent:
    """
    Simulates an interrupt, interrupt servicing takes any 
    time between 1.5 and 2.5 seconds to complete

    Alternatively, if interrupt is enabled, the interrupt signal
    will come after 1 - 3 instructions
    """
    def __init__(self, priority) -> None:
        self.instruction_elapsed = random.randint(1,3)
        self.blocking_time = random.uniform(2.5, 3.5)
        pass