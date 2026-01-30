# Copilot instructions for 45_days_task ✅

Purpose
-------
Short, actionable guidance to help an AI coding agent make productive changes in this repository quickly.

Quick project snapshot
----------------------
- Small learning repository organized by day: `Day1/`, `Day2/`, … `Day7/` (each folder contains small, runnable Python scripts).
- Data is stored under `Datasets/` (CSV files such as `small.csv`, `car_data_final.csv`).
- Common libraries used: `pandas`, `numpy`, `matplotlib`, `scikit-learn` (see `Day5/linear_reg.py` and `Day5_plots/plots.py`).
- CI: `.github/workflows/python-package.yml` runs on Python 3.9–3.11, installs `flake8` and `pytest` and will try `requirements.txt` if present.

What to expect in the code
---------------------------
- Files are short example scripts (top-level code, minimal packaging). Typical patterns:
  - Data load: `pd.read_csv('C:\Users\...\Datasets\small.csv')` or relative `pd.read_csv('Datasets/small.csv')` (`Day3/read_csv.py`).
  - Data mutation: adding columns (`df['PriceIndia'] = PriceIndia`), creating NaNs and inserting columns.
  - ML examples use `sklearn.datasets` (e.g., `load_diabetes`) and `LinearRegression` (`Day5/linear_reg.py`).
  - Plotting code calls `plt.show()` (interactive scripts in `Day5_plots/`).
- Functions often print results instead of returning values (e.g., `Day2/functions.py` prints inside the function). Be conservative when changing behavior.

Agent guidelines (do these first)
----------------------------------
1. Run and reproduce: execute example scripts locally with `python <path>` to see current behavior before editing.
   - Example: `python Day3/read_csv.py` or `python Day5/linear_reg.py`.
2. Prefer non-breaking small changes: avoid changing top-level printing behavior unless you add tests that assert the new behavior.
3. Replace absolute user-specific paths with project-relative, cross-platform code. Example safe pattern to use:

```py
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'Datasets' / 'small.csv'
df = pd.read_csv(DATA)
```

4. If you add third-party deps, update/add `requirements.txt` and document why.
5. Run linters and tests before pushing: `flake8 .` and `pytest` (CI expects those; GH Action runs flake8 and pytest). There are currently no tests—add minimal tests for any refactor that changes behavior.

Files to check first (high ROI)
-------------------------------
- `Day3/read_csv.py` — absolute paths + data transformation examples.
- `Day5/linear_reg.py` — ML example showing `sklearn` usage and plotting.
- `Day5_plots/plots.py` — plotting conventions (use of `plt.show()`).
- `.github/workflows/python-package.yml` — CI expectations for Python versions and tools.

Examples of safe edits
----------------------
- Convert absolute CSV path to project-relative as shown above.
- Add docstrings for top-level functions and small unit tests under a new `tests/` folder.
- Add `requirements.txt` listing `pandas`, `numpy`, `matplotlib`, `scikit-learn` if you introduce new dependencies.

What *not* to do without tests or maintainers' sign-off
-------------------------------------------------------
- Change function semantics (printing → returning) across many files without adding tests.
- Remove or massively refactor plotting/visual code without verifying visual output.

PR checklist for agents
------------------------
- [ ] Run the modified script(s) locally and confirm behavior matches expectations.
- [ ] Add or update `requirements.txt` if you introduced libs.
- [ ] Add tests for behavioral changes under `tests/` and ensure `pytest` passes.
- [ ] Run `flake8 .` and fix reported issues (CI enforces `flake8`).

If anything is unclear
-----------------------
Please tell me which file or behavior you want more detail on (for example: "How should `Day3/read_csv.py` handle paths?"). I'll iterate quickly. ⚡
