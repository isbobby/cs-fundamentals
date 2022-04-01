from enum import Enum
import time

from computer_system.instruction import Instruction
from computer_system.interrupt import Interrupt
from computer_system.blocking_event import BlockingEvent

class INTERRUPT_MODE(Enum):
    no_interrupt_handling = 0
    disable_interrupt = 1
    priority_interrupt = 2

class Event(Enum):
    instruction = 0 # normal fetch and execute
    interrupt = 1   # interrupt signal
    blocking = 2    # fetch and execute but blocks at the end
    
class Processor:
    """
    Represents the processor in a computer
    Attributes
    ----------
    `interrupt_mode : int` (determines how the processor handles interrupt)

    Methods
    -------
    `def execute() -> None` Executes an instruction
    """
    def __init__(self, interrupt_mode : INTERRUPT_MODE) -> None:
        self.interrupt_mode = interrupt_mode

    def execute(self, event_list : list) -> None:
        """
        Simulates a three stage processor execution.
        1. fetch instruction from main memory
        2. execution of the fetched insruction
        3. check for interrupt
        """
        for index, event in enumerate(event_list):
            if event == Event.instruction:
                instruction = Instruction()
                print(f"Execute Instruction - {instruction.time}")
                time.sleep(instruction.time)
                
            elif event == Event.blocking:
                instruction = Instruction()
                print(f"Execute Blocking Instruction - {instruction.time}")
                time.sleep(instruction.time)
                blocking = BlockingEvent(priority=1)
                if self.interrupt_mode == INTERRUPT_MODE.disable_interrupt:
                    # handle interrupt - simulate by inserting an interrupt event after 
                    # x number of instructions
                    n_instruction = blocking.instruction_elapsed
                    event_list.insert(index + n_instruction, Event.interrupt)
                
                elif self.interrupt_mode == INTERRUPT_MODE.no_interrupt_handling:
                    # do not handle interrupts, wait for blocking event
                    print(f"Wait for blocking event - {blocking.blocking_time}")
                    time.sleep(blocking.blocking_time)

                elif self.interrupt_mode == INTERRUPT_MODE.priority_interrupt:
                    # priority handling
                    print("WARNING - Priority interrupt is not implemented, revert to disable interrupts")
                    n_instruction = blocking.instruction_elapsed
                    event_list.insert(index + n_instruction, Event.interrupt)
            
            elif event == Event.interrupt:
                interrupt = Interrupt(priority=1)
                print(f"Service Interrupt - {interrupt.service_time}")
                self.service_interrupt(interrupt=interrupt)
    
    def service_interrupt(self, interrupt : Interrupt) -> None:
        time.sleep(interrupt.service_time)