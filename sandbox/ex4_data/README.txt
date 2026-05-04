# Data Folder — Exercise 4 (.gitignore)

This folder contains a mix of files. Some should be tracked by git, others should not.

Your job: create a .gitignore at the root of the repo that keeps only analysis.R tracked.
See EXERCISES.md for full instructions.

Files in this folder:
- analysis.R       <- should be tracked (source code)
- raw_data.csv     <- should NOT be tracked (large data file)
- results.csv      <- should NOT be tracked (generated output)
- secrets.env      <- should NEVER be tracked (contains credentials)
