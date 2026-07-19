 # Predictive Material Quality Pipeline

## Overview
This project is a full-stack data science pipeline designed to analyze core material properties (like carbon percentage, tensile strength, and yield stress) to predict whether a manufacturing batch will pass or fail quality inspection.

## Architecture 
*   **Database:** A relational MySQL database storing supplier information, material batch features, and historical quality test results.
*   **Data Bridge:** Python's `mysql-connector` used to securely query and extract relational data into Pandas DataFrames.
*   **Machine Learning:** A Scikit-Learn `RandomForestClassifier` trained to detect physical failure patterns, achieving an ~89% prediction accuracy.

## Tech Stack
*   Python 3
*   MySQL
*   Pandas
*   Scikit-Learn
