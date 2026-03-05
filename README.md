# Quick-Calc (Software Testing Assignment)

Quick-Calc is a small calculator project created for the Advanced Software Engineering practical assignment (Lecture 3 — Software Engineering & Testing).
It supports addition, subtraction, multiplication, division (with safe handling of division by zero), and Clear (C) to reset the calculator state.

## Tech Stack
- Python (run with `py`)
- Pytest for testing

## Project Structure
- `quick_calc/core.py` — pure calculation logic
- `quick_calc/engine.py` — input layer (button press simulation) + state
- `tests/` — unit and integration tests

## Setup
1. Install Python (Windows: ensure `py` command works)
2. Install dependencies:

```bash
py -m pip install -r requirements.txt
