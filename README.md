# Distributor Performance Dashboard

## Overview

This project simulates a real-world scenario of distributor performance tracking during a sales incentive campaign.

The goal is to analyze how distributors perform against targets, identify bottlenecks, and evaluate reward distribution.

The dataset is fully synthetic but designed to simulate realistic business behavior.

---

## Business Problem

Companies running incentive programs need to understand:

* Which distributors are meeting targets
* Where performance gaps exist
* How rewards are being distributed
* Which categories are underperforming

This dashboard provides a clear and actionable view of these metrics.

---

## Project Structure

```text
distributor-performance-dashboard/
├── dashboard/
│   └── Analysis_Dashboard.pbix
├── data/
│   └── dataset.csv
├── scripts/
│   └── generate_data.py
├── images/
│   └── preview.png
└── README.md
```

---

## Dataset Description

The dataset simulates:

* 50-100 distributors (randomized)
* Monthly records for the entire year of 2025
* 7 product categories
* Performance vs targets
* Reward eligibility logic

### Main Fields

* `Distributor` -> Distributor name (synthetic)
* `Grupo` -> Distributor group (1-5)
* `Categoria` -> Product category
* `Meta` -> Target value
* `Realizado` -> Achieved value
* `Premiacao` -> Reward earned
* `Cobertura` -> Target achievement flag
* `Data` -> Monthly date in `YYYY-MM`

---

## Data Generation

Data is generated using Python with controlled randomness to simulate:

* High and low performers
* Near-target scenarios
* Realistic distribution patterns

To generate the dataset:

```bash
python scripts/generate_data.py
```

To reproduce the same dataset:

```bash
python scripts/generate_data.py --seed 42
```

Optional parameters:

* `--min-distributors` and `--max-distributors` to control the distributor range
* `--year` to change the reference year
* `--output` to save the CSV to another location

The script now uses only the Python standard library, so no external packages are required to generate the CSV.

---

## Dashboard

The Power BI dashboard provides:

* Total performance overview
* Reward distribution analysis
* Conversion rates
* Ranking of distributors
* Category-level performance
* Drop-off analysis

---

## Key Insights Example

* Majority of distributors fail to reach volume targets
* Significant portion is close to achieving goals
* Reward distribution is concentrated among top performers

---

## Tools & Technologies

* Python (data generation)
* Power BI (data visualization)

---

## Notes

* All data is fictional
* No real company or sensitive information is used
* Project focused on portfolio demonstration

---

## Author

Augusto Rocha  
Data Analyst | Data Engineering  
Focused on building scalable data solutions and business-driven analytics
