class CalculatorMemento:
    """Stores a snapshot of calculator history."""

    def __init__(self, state):
        self.state = state.copy()

    def get_state(self):
        return self.state.copy()


class CalculatorCaretaker:
    """Manages undo and redo history."""

    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def save_state(self, memento):
        self.undo_stack.append(memento)
        self.redo_stack.clear()

    def undo(self, current_state):
        if not self.undo_stack:
            return current_state

        self.redo_stack.append(CalculatorMemento(current_state))
        return self.undo_stack.pop().get_state()

    def redo(self, current_state):
        if not self.redo_stack:
            return current_state

        self.undo_stack.append(CalculatorMemento(current_state))
        return self.redo_stack.pop().get_state()