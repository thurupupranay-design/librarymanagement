class InputHelper:

    @staticmethod
    def read_int(message):
        while True:
            try:
                return int(input(message))
            except ValueError:
                print("Please enter a valid integer.")

    @staticmethod
    def read_string(message):
        return input(message)