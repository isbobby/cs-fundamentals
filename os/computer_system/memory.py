class Memory:
    """
    Represents the main memory in a computer
    Attributes
    ----------
    `priority : int` (determines the priority of interrupt signal)

    `size : int` (determines the size of the memory)

    Methods
    -------
    `def interrupt() -> None` Sends an interrupt signal to processor

    `def fetch(add) -> int` Returns an instruction/value based on the address
    """
    def __init__(self) -> None:
        pass

    def fetch(add) -> int:
        return 1