import pandas as pd

from app.calculator_memento import CalculatorMemento, CalculatorCaretaker


def test_memento_stores_state_copy():
    state = pd.DataFrame([{"operation": "add", "result": 5}])
    memento = CalculatorMemento(state)

    saved_state = memento.get_state()

    assert saved_state.equals(state)


def test_memento_returns_copy():
    state = pd.DataFrame([{"operation": "add", "result": 5}])
    memento = CalculatorMemento(state)

    saved_state = memento.get_state()
    saved_state.loc[0, "result"] = 10

    assert memento.get_state().loc[0, "result"] == 5


def test_save_state_adds_to_undo_stack():
    caretaker = CalculatorCaretaker()
    state = pd.DataFrame([{"operation": "add", "result": 5}])

    caretaker.save_state(CalculatorMemento(state))

    assert len(caretaker.undo_stack) == 1


def test_save_state_clears_redo_stack():
    caretaker = CalculatorCaretaker()
    state = pd.DataFrame([{"operation": "add", "result": 5}])

    caretaker.redo_stack.append(CalculatorMemento(state))
    caretaker.save_state(CalculatorMemento(state))

    assert len(caretaker.redo_stack) == 0


def test_undo_returns_previous_state():
    caretaker = CalculatorCaretaker()
    old_state = pd.DataFrame([{"operation": "add", "result": 5}])
    current_state = pd.DataFrame([{"operation": "multiply", "result": 10}])

    caretaker.save_state(CalculatorMemento(old_state))
    restored_state = caretaker.undo(current_state)

    assert restored_state.equals(old_state)


def test_undo_without_state_returns_current_state():
    caretaker = CalculatorCaretaker()
    current_state = pd.DataFrame([{"operation": "add", "result": 5}])

    restored_state = caretaker.undo(current_state)

    assert restored_state.equals(current_state)


def test_redo_returns_redo_state():
    caretaker = CalculatorCaretaker()
    old_state = pd.DataFrame([{"operation": "add", "result": 5}])
    current_state = pd.DataFrame([{"operation": "multiply", "result": 10}])

    caretaker.save_state(CalculatorMemento(old_state))
    caretaker.undo(current_state)
    redo_state = caretaker.redo(old_state)

    assert redo_state.equals(current_state)


def test_redo_without_state_returns_current_state():
    caretaker = CalculatorCaretaker()
    current_state = pd.DataFrame([{"operation": "add", "result": 5}])

    redo_state = caretaker.redo(current_state)

    assert redo_state.equals(current_state)