class ApplicationException(Exception):
    """
    Base applications exceptions
    """

    def message(self):
        ...
