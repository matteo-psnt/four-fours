# Four Fours Challenge Solver

This Python project provides an automated solution to the classic "Four Fours" challenge. The challenge involves using exactly four instances of the number 4 and any operations to formulate expressions that equal each of the numbers from 0 to a certain target, typically 100. This solver extends the challenge to allow for customizable number ranges and additional flexibility in the rules.

## Usage

To use the Four Fours Challenge Solver, run the script from the command line, optionally specifying the target number range and whether to display numbers without a solution.

```bash
python four_fours_solver.py [--min MIN] [--max MAX] [--show-all]

Arguments
--min MIN: Specify the minimum target number (default is 1).
--max MAX: Specify the maximum target number (default is 100).
--show-all: Include this flag to display all numbers within the range, indicating which ones do not have a solution.
```

Example
To find expressions for numbers 1 through 100:

`python four_fours_solver.py 4 4 4 4 --min 1 --max 100 --show-all`