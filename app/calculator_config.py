import os
from dotenv import load_dotenv

from app.exceptions import ConfigurationError


class CalculatorConfig:
    """Loads and validates calculator configuration."""

    def __init__(self):
        load_dotenv()
        self.history_file = os.getenv("HISTORY_FILE", "history.csv")
        self.auto_save = os.getenv("AUTO_SAVE", "true").lower()

    def validate(self):
        if not self.history_file.endswith(".csv"):
            raise ConfigurationError("History file must be a CSV file")

        if self.auto_save not in ["true", "false"]:
            raise ConfigurationError("AUTO_SAVE must be true or false")

        return True

    def is_auto_save_enabled(self):
        return self.auto_save == "true"