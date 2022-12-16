class InvalidFILEException(Exception):
    def __init__(self, message: str = "File is invalid. Please input the UTF8"):
        self.message = message
        super().__init__(self.message)