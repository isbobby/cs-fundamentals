class IOModule:
    """
    Represents an I/O module in a computer
    Attributes
    ----------
    priority : int (determines the interrupt request priority)

    Methods
    -------
    `def interrupt() -> int` Sends an interrupt signal to processor
    """
    def __init__(self) -> None:
        self.priority = None
        pass

    def interrupt() -> int:
        return 1