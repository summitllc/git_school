# Data Folder — Exercise 4 (.gitignore)

This folder is used for a .gitignore exercise. `analysis.R` is present in the repo; during Exercise 4, create dummy local copies of the other files listed below so you can verify that only the correct file remains tracked by git.

Your job: create a .gitignore at the root of the repo that keeps only analysis.R tracked.
See EXERCISES.md for full instructions.

Files in this folder:
- analysis.R       <- should be tracked (source code)
- raw_data.csv     <- should NOT be tracked (large data file - ask facilitator for the file)
- results.csv      <- should NOT be tracked (generated output - ask facilitator for the file)
- secrets.env      <- should NEVER be tracked (contains credentials - ask facilitator for the file)
