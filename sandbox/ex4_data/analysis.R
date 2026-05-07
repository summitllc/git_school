# Analysis Script
# This file should be tracked by git — it's source code.

load_data <- function(filepath) {
  read.csv(filepath)
}

summarize_data <- function(df) {
  summary(df)
}
