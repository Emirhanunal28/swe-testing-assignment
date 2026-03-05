from __future__ import annotations
from dataclasses import dataclass
from . import core

_ALLOWED_OPS = {"+", "-", "*", "/"}

@dataclass
class CalculatorEngine:
    display: str = "0"
    _left: float | None = None
    _op: str | None = None
    _new_entry: bool = True

    def press(self, key: str) -> str:
        key = key.strip()

        if key.upper() == "C":
            self._clear()
            return self.display

        if key in _ALLOWED_OPS:
            self._set_operator(key)
            return self.display

        if key == "=":
            self._equals()
            return self.display

        if key.isdigit() or key == ".":
            self._input_char(key)
            return self.display

        raise ValueError(f"Unsupported key: {key}")

    def _clear(self) -> None:
        self.display = "0"
        self._left = None
        self._op = None
        self._new_entry = True

    def _input_char(self, ch: str) -> None:
        if self._new_entry:
            self.display = "0" if ch == "." else ""
            self._new_entry = False

        if ch == "." and "." in self.display:
            return

        if self.display == "0" and ch.isdigit():
            self.display = ch
        else:
            self.display += ch

    def _set_operator(self, op: str) -> None:
        if self._left is None:
            self._left = float(self.display)
        else:
            if not self._new_entry:
                self._equals()

        self._op = op
        self._new_entry = True

    def _equals(self) -> None:
        if self._op is None or self._left is None:
            return

        right = float(self.display)
        try:
            result = self._apply(self._left, self._op, right)
            self.display = self._format(result)
            self._left = result
        except ZeroDivisionError:
            self.display = "Error"
            self._left = None
            self._op = None
        finally:
            self._new_entry = True

    def _apply(self, a: float, op: str, b: float) -> float:
        if op == "+":
            return core.add(a, b)
        if op == "-":
            return core.subtract(a, b)
        if op == "*":
            return core.multiply(a, b)
        if op == "/":
            return core.divide(a, b)
        raise ValueError("Invalid operator")

    def _format(self, value: float) -> str:
        if value.is_integer():
            return str(int(value))
        return str(value)