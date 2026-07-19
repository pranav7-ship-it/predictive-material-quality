# Predictive Material Quality Pipeline

## Project Overview
This project is an end-to-end data science pipeline built to automate manufacturing quality inspection. By moving away from manual data entry to a structured relational database, this system uses machine learning to predict material failure before it happens, visualized through an interactive BI dashboard.

## System Architecture
*   **Data Storage:** A relational **MySQL** database managing supplier reliability and batch test results.
*   **Data Bridge:** **Python** scripts using `mysql-connector` to extract, clean, and analyze relational data.
*   **Intelligence:** A **RandomForestClassifier** trained on material physical properties (Carbon %, Tensile Strength, Yield Stress) to achieve ~89% prediction accuracy.
*   **Insights:** An interactive **Power BI** dashboard providing real-time quality monitoring and supplier performance analytics.

## Dashboard Preview
 <img width="1292" height="722" alt="Screenshot 2026-07-19 191956" src="https://github.com/user-attachments/assets/49f69857-967a-4cd7-b658-e866f6ebd683" />


## Tech Stack
*   **Language:** Python 3
*   **Database:** MySQL
*   **Libraries:** Pandas, Scikit-Learn, MySQL-Connector
*   **Visualization:** Power BI

## How It Works
1.  **Data Extraction:** Python queries the `MaterialQualityDB` to pull batch properties and inspection outcomes.
2.  **Predictive Modeling:** The trained model processes batch data to output a pass/fail probability.
3.  **Visualization:** The results are loaded into Power BI for stakeholder analysis, allowing for supplier-level filtering and stress-test distribution analysis.
