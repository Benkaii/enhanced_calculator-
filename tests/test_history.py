from app.history import CalculationHistory


def test_history_starts_empty():
    history = CalculationHistory()

    assert history.get_history().empty


def test_add_record():
    history = CalculationHistory()

    history.add_record("add", 2, 3, 5)

    data = history.get_history()

    assert len(data) == 1
    assert data.iloc[0]["operation"] == "add"
    assert data.iloc[0]["result"] == 5


def test_clear_history():
    history = CalculationHistory()

    history.add_record("add", 2, 3, 5)
    history.clear()

    assert history.get_history().empty


def test_save_and_load_csv(tmp_path):
    file_path = tmp_path / "history.csv"

    history = CalculationHistory()
    history.add_record("multiply", 4, 5, 20)
    history.save_to_csv(file_path)

    new_history = CalculationHistory()
    new_history.load_from_csv(file_path)

    data = new_history.get_history()

    assert len(data) == 1
    assert data.iloc[0]["operation"] == "multiply"
    assert data.iloc[0]["result"] == 20