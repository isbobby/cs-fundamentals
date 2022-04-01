"""
This file shows the differences in performance and behaviour when a computer adopts different
modes of handling interrupts.
"""
import time

from computer_system.processor import Processor, INTERRUPT_MODE, Event

class Driver:
    """
    Driver class to abstract memeber classes and run tests
    """
    def __init__(self, mode : INTERRUPT_MODE) -> None:
        """
        Driver initialise a computer object
        """
        print(" --- Startring driver ---")
        # Initialise processor
        self._processor = Processor(interrupt_mode=mode)
    
    def test(self) -> None:
        """"
        Test and output different interrupt servicing methods
        """
        event_list = [
            Event.instruction, # 0 - 0.5s
            Event.instruction, # 0 - 0.5s
            Event.instruction, # 0 - 0.5s
            Event.blocking,    # 2.5 - 3.5s
            Event.instruction, # 0 - 0.5s
            Event.blocking,    # 2.5 - 3.5s
            Event.instruction, # 0 - 0.5s
            Event.instruction, # 0 - 0.5s
            Event.instruction, # 0 - 0.5s
        ]

        time_start = time.time()

        self._processor.execute(event_list)

        time_elapsed = time.time() - time_start
        
        print(f"Test done, time taken - {time_elapsed}\n")

driver = Driver(INTERRUPT_MODE.no_interrupt_handling)
driver.test()

driver = Driver(INTERRUPT_MODE.disable_interrupt)
driver.test()