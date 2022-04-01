class Processor:
    """
    Represents the processor in a computer
    Attributes
    ----------
    `interrupt_mode : int` (determines how the processor handles interrupt)

    `memory : Memory` (the memory unit)

    `modules : []` (list of IO modules)

    Methods
    -------
    `def execute() -> None` Executes an instruction
    """
    def __init__(self, interrupt_mode, modules, memory) -> None:
        self.interrupt_mode = interrupt_mode
        self.modules = modules
        self.memory = memory
        
        self._PSW = None
        self._PC = None
        pass

    def execute(self) -> None:
        """
        Simulates a three stage processor execution.
        1. fetch instruction from main memory
        2. execution of the fetched insruction
        3. check for interrupt
        """
        pass