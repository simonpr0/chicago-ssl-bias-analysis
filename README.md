# Bias in the Chicago Strategic Subject List

A case study of the Chicago Police Department's Strategic Subject List (SSL). The SSL was an algorithm that gave about 400,000 people a 0–500 "risk score" for involvement in a shooting. CPD stopped using it in 2019.

## Contents

| File | What it is |
|---|---|
| `bias_analysis.ipynb` | The main analysis: a surrogate model of the score, fictional profiles and what-if changes, representation vs. the 2020 Census, factor prevalence by group, a breakdown of the score gap, and geography |
| `analysis.ipynb` | A first look at the data: missing values, score distribution, scores by demographic group, correlations between predictors |
| `load_data.py` | `load_ssl()` loads and cleans the raw CSV (snake_case columns, boolean flags, ordered age bands, readable race/sex labels) |

## Key findings

- **Age drives most of the score.** A fictional 19-year-old with no counted arrests scores about 338, higher than 86% of the list.
- **Being a victim raises the score more than committing violence.** One assault victimization adds about 34 points; one violent-offense arrest adds about 16.
- **The biggest disparity is who is on the list.** Black residents are about 29% of Chicago but 52–58% of the list.
- **Race is not an input, but the disparity comes in through the inputs.** Black people on the list are about 15x as likely as White people to be recorded as shooting victims and about 8x as likely to carry a gang flag.

## Getting the data

The dataset (about 95 MB) isn't included in this repo. Download **"Strategic Subject List - Historical"** as CSV from the [Chicago Data Portal](https://data.cityofchicago.org/browse?q=Strategic%20Subject%20List). Then:
1. Save it in this folder.
2. If the filename differs, update `RAW_CSV` in `load_data.py`.

## Running it

Requires Python 3 with pandas, numpy, matplotlib, seaborn, scikit-learn and Jupyter.

```bash
jupyter notebook bias_analysis.ipynb
```
