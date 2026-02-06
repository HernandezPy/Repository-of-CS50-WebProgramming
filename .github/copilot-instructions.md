# AI Coding Agent Instructions

## Project Overview
This is a **CS50 Web Programming course repository** containing 40+ independent learning projects across Python, Django, HTML/CSS, JavaScript, and SQL. Each directory is a self-contained exercise or assignment, not a monolithic application.

## Architecture & Organization

**Python Exercises** (individual functions/scripts):
- Each has a main entry point: `main()` function that orchestrates user input and helper functions
- Helper functions are pure (minimal state), named clearly: `value()`, `convert()`, `gauge()`, etc.
- Examples: `bank/bank.py` (greeting value calculator), `fuel/fuel.py` (fraction-to-percentage gauge)

**Django Projects**:
- Located in `Django/` with two main projects: `airline/` (flight booking) and `Project2/commerce/` (auction system)
- Standard Django structure: `manage.py`, apps (`flights/`, `users/`, `auctions/`), settings
- Database: SQLite (standard Django default); SQL examples in `Django/Project2/SQL/`

**Web Projects**:
- `HTML,CSS/`: Standalone HTML/CSS demonstrations with helper subdirectories (`googlesearch/`, `WebProgrammingPython/`, `Django/lecture3/`)
- `JavaScript/`: Django mail project (`project3mail/`) + standalone script examples (`Scripts/`)

## Testing Patterns (Critical for This Repo)

**Pytest Convention** (universal approach used):
- Test files named `test_*.py` parallel each exercise
- Import the module's core functions: `from fuel import convert, gauge`
- Test structure: separate test functions for each case, using `assert` statements

**Input/Output Testing** (unique pattern - use for interactive functions):
- Mock user input with `monkeypatch.setattr("builtins.input", lambda _: "value")`
- Capture print output with `capsys.readouterr()` to verify formatted display
- Example from `project/test_project.py`: Testing tabulate output and dict-based lookups

**Exception Testing**:
- Validate error handling with `pytest.raises(ExceptionType)`
- Functions raise exceptions rather than returning error values
- Example: `convert("1/0")` raises `ZeroDivisionError`, invalid formats raise `ValueError`

**Run tests**: `pytest filename.py` or `pytest` for full directory

## Code Style & Conventions

**Function Organization**:
- Always end with: `if __name__ == '__main__': main()` 
- Main logic in `main()`, helper functions separate
- Keep functions single-purpose (convert/validate/format pattern)

**Error Handling**:
- Raise exceptions (`ValueError`, `ZeroDivisionError`) for invalid conditions
- Don't catch-and-suppress; let caller decide handling
- Use `while True` + try/except for input validation loops (see `fuel/fuel.py` line 13-20)

**Data Structures**:
- Dictionaries map user options to values: `data = {"a": ("Description", 250)}`
- Lists and dicts preferred; avoid custom classes in simple exercises

**Libraries Used**:
- Common: `csv`, `re`, `sys`, `pathlib`, `sqlite3`
- Data display: `tabulate` (table formatting), `pyfiglet` (ASCII art)
- Testing: `pytest` exclusively (no unittest)

## Common Developer Tasks

**Running Exercises**:
```bash
python bank/bank.py
python fuel/fuel.py
```

**Testing a Program**:
```bash
pytest fuel/test_fuel.py -v
```

**Django Setup** (for `Django/project/` or `Django/Project2/`):
```bash
python manage.py runserver
python manage.py migrate
```

**File Patterns to Know**:
- `test_*.py`: Always paired with `*.py` counterpart; tests run with pytest
- Directories without tests (e.g., `adieu/`, `camel/`) are simpler scripts without formal test suites
- `README.md` files document project intent (see `project/README.md` for detailed project description)

## Key Files Exemplifying Patterns

- [fuel/fuel.py](fuel/fuel.py): Input validation loop, exception handling, calculation functions
- [fuel/test_fuel.py](fuel/test_fuel.py): Pytest exception testing, multiple assertion cases
- [project/test_project.py](project/test_project.py): Mock input, capsys output capture (unique pattern)
- [bank/bank.py](bank/bank.py): Simple pure function, case-insensitive string matching
- [Django/project/airline/airline/settings.py](Django/project/airline/airline/settings.py): Standard Django config

## Special Considerations

- **No Single Entry Point**: Each folder is independent; running tests requires `cd` into specific directories or use pytest discovery
- **Input Validation**: Many exercises accept string input; parse and validate before processing
- **Django Projects Use SQLite**: Check database state with shell commands when debugging
- **HTML/CSS Learning**: Separate from Python; static files only—no server code expected
- **Legacy Imports**: Some files use older patterns (e.g., `from project import ...`)—maintain compatibility when updating

## When Adding New Code

1. **Follow the folder's pattern**: If it has tests, write pytest-compatible functions
2. **Use clear function names** that describe transformation: `convert()`, `validate()`, `format()`, `calculate()`
3. **Raise exceptions** for invalid input, don't return status codes
4. **If adding Django views**: Follow MTV (Model-Template-View) pattern in existing apps
5. **Test with mock input** if the function accepts `input()` calls
