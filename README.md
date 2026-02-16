# Modelling Adult Obesity Risks in England Using
Health Indicators: An Analysis of Health Survey
for England Data

**University of Hertfordshire**  
**Student:** Gabriel Lucky Lotanna 
**Submission Date:** April 22, 2026

---

## Project Overview

This Project investigates the relationship between behavioural health indicators and adult obesity prevalence across 147 English Local Authorities using data from NHS Fingertips (2020-2023).

## Research Questions

1. Which health behaviors are most strongly associated with adult obesity prevalence?
2. Which machine learning models perform best in predicting obesity from behavioral indicators?
3. How can model predictions be explained and what patterns emerge?

# MSc Data Science Project: Predicting Adult Obesity from Health Behaviours in England (2020-2023)
MSc Data Science project analysing adult obesity risk in England using Health Survey for England and ONS opinion data.

## Dataset

**Source:** NHS Fingertips - Obesity, Physical Activity & Nutrition Profile  
**URL:** https://fingertips.phe.org.uk/profile/obesity-physical-activity-nutrition

**Specifications:**
- 583 observations (147 Local Authorities × 4 years)
- Years covered: 2020-2023
- Zero missing values
- Variables: Obesity prevalence (target), Physical inactivity, Smoking prevalence, Diet (5-a-day)

## Repository Structure
```
obesity-dissertation/
├── data/
│   └── FINGERTIPS_MERGED_COMPLETE.csv
├── notebooks/
│   └── Predicting_Obesity_Analysis.ipynb
├── outputs/
│   ├── visualizations/
│   └── model_results/
├── docs/
│   └── project_report.pdf
└── README.md
```
## Methods

**Exploratory Data Analysis:**
- Distribution analysis (histograms, box plots, violin plots)
- Temporal trend analysis (2020-2023)
- Correlation analysis

**Machine Learning Models:**
- Lasso Regression
- Ridge Regression
- Random Forest Regressor
- Gradient Boosting Regressor

**Model Evaluation:**
- R² score
- RMSE (Root Mean Squared Error)
- 5-fold cross-validation
- SHAP analysis for explainability

- ## Key Findings (Preliminary)

1. **COVID-19 Obesity Paradox:** Obesity increased 1.23% (2020-2023) despite physical activity improvements, driven by 3.65% decline in diet quality
2. **Strongest Predictors:** Physical inactivity (r=0.495) and poor diet (r=-0.464)
3. **Model Performance:** Ridge Regression performs best (R²=0.355)

## License

This project is submitted as part of MSc Data Science coursework at University of Hertfordshire. All rights reserved.

### Update (Dataset Refinement)
The original HSE-based dataset was replaced with a consolidated dataset derived from the
Public Health Outcomes Framework (PHOF) via the Fingertips platform. This change was made
to improve indicator consistency, geographic alignment, and modelling suitability.
