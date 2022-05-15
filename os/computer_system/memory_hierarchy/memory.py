import random

class Memory:
    """
    Simulate a memory unit. It has three attributes - capacity, speed, and cost    
    """
    def __init__(self, capacity, speed, cost, hit_rate) -> None:
        self.capacity = capacity
        self.speed = speed
        self.cost = cost
        self.hit_rate = hit_rate # between 0-1
        pass

    def read(self) -> bool:
        roll = random.uniform(0,1)
        if roll < self.hit_rate:
            return True
        return False