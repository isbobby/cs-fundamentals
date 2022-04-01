import random

class InterruptServiceRoutine:
    """
    Simulates an interrupt, interrupt servicing takes any 
    time between 1.0 and 1.5 seconds to complete
    """
    def __init__(self, priority) -> None:
        self.priority = priority
        self.service_time = random.uniform(1.0, 1.5)
        pass