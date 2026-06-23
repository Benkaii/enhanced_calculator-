import pytest

from app.calculation import Calculation, CalculationFactory
from app.exceptions import OperationError
from app.operations import AddOperation


def test_calculation_perform():
    calculation = Calculation("add", 2, 3, AddOperation())

    assert calculation.perform() == 5


@pytest.mark.parametrize(
    "operation_name, a, b, expected",
    [
        ("add", 2, 3, 5),
        ("subtract", 10, 4, 6),
        ("multiply", 3, 4, 12),
        ("divide", 10, 2, 5),
        ("power", 2, 3, 8),
        ("root", 9, 2, 3),
    ],
)
def test_calculation_factory(operation_name, a, b, expected):
    calculation = CalculationFactory.create(operation_name, a, b)

    assert calculation.perform() == expected


def test_calculation_factory_invalid_operation():
    with pytest.raises(OperationError, match="Invalid operation"):
        CalculationFactory.create("bad", 1, 2)
