\# Testing Strategy (Quick-Calc)



\## What I tested

\- \*\*Unit tests (core logic):\*\* `add`, `subtract`, `multiply`, `divide`

\- \*\*Edge cases:\*\* division by zero, negative numbers, decimals, and large numbers

\- \*\*Integration tests (input layer + logic):\*\* simulated user actions with `CalculatorEngine.press()`:

&nbsp; - `5 + 3 =` returns `8`

&nbsp; - `Clear (C)` resets the display to `0`



\## What I did not test (and why)

\- UI design / visual layout: the project uses a minimal input layer and UI is not the focus.

\- Performance testing: calculations are simple and performance is not a requirement.

\- Security testing: the application has no networking and no sensitive data.



\## Lecture 3 Concepts



\### 1) Testing Pyramid

The test suite follows the testing pyramid idea:

\- \*\*More unit tests\*\* for fast and isolated verification of small functions (`core.py`).

\- \*\*Fewer integration tests\*\* to confirm components work together (`engine.py` + `core.py`).



\### 2) Black-box vs White-box Testing

\- \*\*Unit tests:\*\* closer to \*\*white-box\*\* testing because they directly test internal functions and expected outputs.

\- \*\*Integration tests:\*\* closer to \*\*black-box\*\* testing because they simulate user interaction through the input layer and check the visible output (`display`).



\### 3) Functional vs Non-Functional Testing

\- The suite focuses on \*\*functional testing\*\* (correct outputs, correct error handling for division by zero, correct reset behavior).

\- Non-functional testing (performance, usability, stress) is intentionally excluded because it is not required for this small assignment.



\### 4) Regression Testing

After future updates (new features/changes), running `py -m pytest -q` will confirm that old behavior still works and prevent regressions.



\## Test Results Summary



| Test Name                           | Type        | Status |

|------------------------------------|-------------|--------|

| test\_add\_basic                      | Unit        | Pass   |

| test\_subtract\_basic                 | Unit        | Pass   |

| test\_multiply\_basic                 | Unit        | Pass   |

| test\_divide\_basic                   | Unit        | Pass   |

| test\_divide\_by\_zero\_raises          | Unit        | Pass   |

| test\_negative\_numbers               | Unit        | Pass   |

| test\_decimal\_numbers                | Unit        | Pass   |

| test\_large\_numbers                  | Unit        | Pass   |

| test\_full\_user\_interaction\_addition | Integration | Pass   |

| test\_clear\_resets\_after\_calculation | Integration | Pass   |

