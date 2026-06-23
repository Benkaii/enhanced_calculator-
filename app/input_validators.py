from app.exceptions import ValidationError


class InputValidator:
    """Validates calculator user input."""

    valid_operations = [
        "add",
        "subtract",
        "multiply",
        "divide",
        "power",
        "root",
    ]

    valid_commands = [
        "help",
        "history",
        "exit",
        "clear",
        "undo",
        "redo",
        "save",
        "load",
    ]

    @classmethod
    def is_valid_operation(cls, operation):
        return operation in cls.valid_operations

    @classmethod
    def is_valid_command(cls, command):
        return command in cls.valid_commands

    @staticmethod
    def validate_number(value):
        try:
            return float(value)
        except ValueError as error:
            raise ValidationError("Input must be a number") from error