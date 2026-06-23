import os
import pytest

from app.calculator_config import CalculatorConfig
from app.exceptions import ConfigurationError


def test_default_config(monkeypatch):
    monkeypatch.delenv("HISTORY_FILE", raising=False)
    monkeypatch.delenv("AUTO_SAVE", raising=False)

    config = CalculatorConfig()

    assert config.history_file == "history.csv"
    assert config.auto_save == "true"


def test_custom_config(monkeypatch):
    monkeypatch.setenv("HISTORY_FILE", "custom.csv")
    monkeypatch.setenv("AUTO_SAVE", "false")

    config = CalculatorConfig()

    assert config.history_file == "custom.csv"
    assert config.auto_save == "false"


def test_validate_success(monkeypatch):
    monkeypatch.setenv("HISTORY_FILE", "history.csv")
    monkeypatch.setenv("AUTO_SAVE", "true")

    config = CalculatorConfig()

    assert config.validate()


def test_invalid_history_file(monkeypatch):
    monkeypatch.setenv("HISTORY_FILE", "history.txt")
    monkeypatch.setenv("AUTO_SAVE", "true")

    config = CalculatorConfig()

    with pytest.raises(ConfigurationError, match="History file must be a CSV file"):
        config.validate()


def test_invalid_auto_save(monkeypatch):
    monkeypatch.setenv("HISTORY_FILE", "history.csv")
    monkeypatch.setenv("AUTO_SAVE", "maybe")

    config = CalculatorConfig()

    with pytest.raises(ConfigurationError, match="AUTO_SAVE must be true or false"):
        config.validate()


def test_auto_save_enabled(monkeypatch):
    monkeypatch.setenv("AUTO_SAVE", "true")

    config = CalculatorConfig()

    assert config.is_auto_save_enabled()


def test_auto_save_disabled(monkeypatch):
    monkeypatch.setenv("AUTO_SAVE", "false")

    config = CalculatorConfig()

    assert not config.is_auto_save_enabled()