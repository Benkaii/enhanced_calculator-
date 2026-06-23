from app.operations import (
    AddOperation,
    SubtractOperation,
    MultiplyOperation,
    DivideOperation,
    PowerOperation,
    RootOperation,
)
from app.exceptions import OperationError


class Calculation:
    """Represents a calculation using an operation strategy."""

    def __init__(self, operation_name, a, b, operation):
        self.operation_name = operation_name
        self.a = a
        self.b = b
        self.operation = operation

    def perform(self):
        return self.operation.execute(self.a, self.b)


class CalculationFactory:
    """Factory for creating calculation objects."""

    operations = {
        "add": AddOperation,
        "subtract": SubtractOperation,
        "multiply": MultiplyOperation,
        "divide": DivideOperation,
        "power": PowerOperation,
        "root": RootOperation,
    }

    @classmethod
    def create(cls, operation_name, a, b):
        if operation_name not in cls.operations:
            raise OperationError("Invalid operation")

        operation = cls.operations[operation_name]()
        return Calculation(operation_name, a, b, operation)