import pandas as pd


class CalculationHistory:
    """Manages calculation history using pandas."""

    def __init__(self):
        self.history = pd.DataFrame(
            columns=["operation", "a", "b", "result"]
        )

    def add_record(self, operation, a, b, result):
        new_record = pd.DataFrame(
            [{
                "operation": operation,
                "a": a,
                "b": b,
                "result": result,
            }]
        )

        self.history = pd.concat(
            [self.history, new_record],
            ignore_index=True
        )

    def clear(self):
        self.history = self.history.iloc[0:0]

    def get_history(self):
        return self.history

    def save_to_csv(self, file_path):
        self.history.to_csv(file_path, index=False)

    def load_from_csv(self, file_path):
        self.history = pd.read_csv(file_path)