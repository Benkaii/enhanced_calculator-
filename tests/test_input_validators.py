import pytest

from app.exceptions import ValidationError
from app.input_validators import InputValidator


@pytest.mark.parametrize(
    "operation",
    ["add", "subtract", "multiply", "divide", "power", "root"],
)
def test_valid_operations(operation):
    assert InputValidator.is_valid_operation(operation)


def test_invalid_operation():
    assert not InputValidator.is_valid_operation("bad")


@pytest.mark.parametrize(
    "command",
    ["help", "history", "exit", "clear", "undo", "redo", "save", "load"],
)
def test_valid_commands(command):
    assert InputValidator.is_valid_command(command)


def test_invalid_command():
    assert not InputValidator.is_valid_command("bad")


def test_validate_number():
    assert InputValidator.validate_number("5") == 5.0


def test_validate_decimal_number():
    assert InputValidator.validate_number("5.5") == 5.5


def test_validate_invalid_number():
    with pytest.raises(ValidationError, match="Input must be a number"):
        InputValidator.validate_number("hello")