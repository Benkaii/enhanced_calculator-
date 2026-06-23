class CalculatorError(Exception):
    """Base exception for calculator errors."""


class ValidationError(CalculatorError):
    """Raised when user input is invalid."""


class OperationError(CalculatorError):
    """Raised when an operation cannot be completed."""


class ConfigurationError(CalculatorError):
    """Raised when configuration is invalid."""