from app.exceptions import (
    CalculatorError,
    ValidationError,
    OperationError,
    ConfigurationError,
)


def test_validation_error_is_calculator_error():
    assert issubclass(ValidationError, CalculatorError)


def test_operation_error_is_calculator_error():
    assert issubclass(OperationError, CalculatorError)


def test_configuration_error_is_calculator_error():
    assert issubclass(ConfigurationError, CalculatorError)


def test_raise_validation_error():
    try:
        raise ValidationError("Invalid input")
    except ValidationError as error:
        assert str(error) == "Invalid input"