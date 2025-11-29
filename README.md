# Bank Customer Churn Insights Agent

An AI Agent that generates actionable insights for executives and product managers using the Bank Customer Churn Prediction Dataset.

## Overview

This project provides an intelligent analytics agent that analyzes customer churn patterns and generates tailored insights for different stakeholders:

- **Executive Insights**: High-level strategic summaries focusing on business impact, risk indicators, and key metrics
- **Product Manager Insights**: Actionable recommendations with specific implementation guidance and expected outcomes

## Features

- 📊 **Comprehensive Churn Analysis**: Overall metrics, segment analysis, and trend identification
- 🎯 **Risk Assessment**: Automatic identification of high-risk customer segments
- 💼 **Executive Summaries**: Financial impact estimates and strategic recommendations
- 🛠️ **Product Recommendations**: Specific, actionable insights with implementation effort estimates
- 📈 **Correlation Analysis**: Identify key factors contributing to customer churn
- 🔄 **Flexible Data Sources**: Use local CSV files or download directly from Kaggle

## Installation

```bash
# Clone the repository
git clone https://github.com/omc02/kaggle.git
cd kaggle

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Command Line Interface

```bash
# Run with default Kaggle dataset download
python main.py

# Use a local data file
python main.py --data-path data/churn_data.csv

# Save full report to JSON
python main.py --output report.json

# Output as JSON to console
python main.py --format json

# Print only executive summary
python main.py --summary-only
```

### Python API

```python
from src.insights_agent import InsightsAgent

# Initialize the agent
agent = InsightsAgent(data_path="path/to/data.csv")
agent.initialize()

# Generate executive summary
summary = agent.generate_executive_summary()
print(summary)

# Generate executive insights
exec_insights = agent.generate_executive_insights()
for insight in exec_insights:
    print(f"{insight.title}: {insight.summary}")

# Generate product manager insights
prod_insights = agent.generate_product_insights()
for insight in prod_insights:
    print(f"{insight.title}: {insight.recommendation}")

# Generate full report
full_report = agent.generate_full_report()

# Print formatted output
agent.print_executive_summary()
agent.print_insights()
```

## Dataset

This agent uses the [Bank Customer Churn Prediction](https://www.kaggle.com/datasets/shantanudhakadd/bank-customer-churn-prediction) dataset from Kaggle.

### Dataset Features

| Feature | Description |
|---------|-------------|
| CreditScore | Customer's credit score |
| Geography | Customer's country (France, Germany, Spain) |
| Gender | Customer's gender |
| Age | Customer's age |
| Tenure | Years as a customer |
| Balance | Account balance |
| NumOfProducts | Number of bank products used |
| HasCrCard | Has credit card (0/1) |
| IsActiveMember | Active member status (0/1) |
| EstimatedSalary | Estimated annual salary |
| Exited | Churned status (0/1) - Target variable |

## Project Structure

```
kaggle/
├── main.py                 # CLI entry point
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── src/
│   ├── __init__.py
│   ├── data_loader.py     # Data loading and preprocessing
│   ├── analytics.py       # Churn analytics functions
│   └── insights_agent.py  # Main insights generation agent
├── tests/
│   ├── __init__.py
│   └── test_insights_agent.py  # Unit tests
└── data/                  # Data directory (optional)
```

## Sample Output

### Executive Summary

```
============================================================
EXECUTIVE SUMMARY - CUSTOMER CHURN ANALYSIS
============================================================

📊 OVERVIEW
----------------------------------------
Total Customers: 10,000
Churn Rate: 20.37%
Churned Customers: 2,037
Retained Customers: 7,963

💰 FINANCIAL IMPACT
----------------------------------------
Estimated Revenue at Risk: $5,092,500.00
Average Customer Value: $2,500.00

⚠️ KEY RISK INDICATORS
----------------------------------------
  • NumOfProducts: 4 - 100.0% (60 customers)
  • NumOfProducts: 3 - 82.71% (220 customers)
  • AgeGroup: 56-65 - 44.78% (1,499 customers)
```

### Product Manager Insights

```
1. ➡️ Product Portfolio Optimization
--------------------------------------------------
Finding: Customers with 4 products have a 100.0% churn rate.
Affected Segment: 60 customers (0.6% of total)
Recommendation: Review product bundling strategy...
Expected Impact: 5-8% reduction in churn for affected segment
Implementation Effort: MEDIUM
```

## Running Tests

```bash
# Run all tests
python -m pytest tests/ -v

# Run with coverage
python -m pytest tests/ -v --cov=src
```

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
