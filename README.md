# Predicting Adult Obesity from Health Behaviours in England

**MSc Data Science Dissertation**  
**University of Hertfordshire**  
**Student:** Gabriel Lucky Lotanna  
**Submission Date:** April 22, 2026

---

## Project Status

**Current Stage:** Exploratory Data Analysis and Initial Machine Learning Models Complete  
**Last Updated:** February 18, 2026  
**Progress:** 60% Complete

**Completed:**
- Data extraction and merging from NHS Fingertips
- Comprehensive exploratory data analysis with 8+ visualizations
- Correlation analysis (Research Question 1 answered)
- Lasso Regression model implemented
- Ridge Regression model implemented

**In Progress:**
- Random Forest model
- Gradient Boosting model

**Pending:**
- SHAP analysis for model explainability
- Final report writing

---

## Project Overview

This dissertation investigates the relationship between behavioural health indicators and adult obesity prevalence across 147 English Local Authorities using data from NHS Fingertips (2020-2023).

The analysis employs multiple machine learning approaches to identify which health behaviors most strongly predict obesity and to understand the temporal patterns that emerged during the COVID-19 pandemic and subsequent cost-of-living crisis.

---

## Research Questions

1. Which health behaviors are most strongly associated with adult obesity prevalence across English Local Authorities?
2. Which machine learning models perform best in predicting obesity prevalence from behavioral indicators?
3. How can model predictions be explained and what patterns emerge from the analysis?

---

## Dataset

**Source:** NHS Fingertips - Obesity, Physical Activity & Nutrition Profile  
**URL:** https://fingertips.phe.org.uk/profile/obesity-physical-activity-nutrition

**Important Note:** This project uses NHS Fingertips aggregated Local Authority data, NOT the Health Survey for England (HSE) individual-level survey data. These are different datasets from different sources.

**Dataset Specifications:**
- 583 observations (147 Local Authorities × 4 years)
- Years covered: 2020, 2021, 2022, 2023
- Geographic level: Upper Tier Local Authorities (England)
- Data quality: Zero missing values (100% complete)

**Variables:**
- Target variable: Obesity prevalence (percentage of adults with BMI ≥30)
- Predictors:
  - Physical inactivity (percentage of adults with <30 minutes MVPA per week)
  - Smoking prevalence (percentage of current smokers aged 18+)
  - Diet (5-a-day) (percentage meeting fruit/vegetable recommendations)

---

## Repository Structure
```
adult-obesity-risk-modelling-england/
├── docs/
│   └── project_report.pdf
├── notebooks/
│   └── Predicting_Obesity_Analysis.ipynb
├── results/
│   ├── visualizations/
│   │   ├── distributions_histograms.png
│   │   ├── temporal_trends.png
│   │   ├── correlation_heatmap.png
│   │   └── model_comparison.png
│   └── model_outputs/
├── scripts/
│   └── data_processing.py
├── .gitignore
└── README.md
```

---

## Methods

### Exploratory Data Analysis
- Distribution analysis (histograms, box plots, violin plots)
- Outlier detection and assessment
- Temporal trend analysis (2020-2023)
- Correlation analysis using Pearson correlation coefficients
- Pairwise relationship visualization

### Machine Learning Models

**Implemented:**
- Lasso Regression (L1 regularization)
- Ridge Regression (L2 regularization)

**Pending Implementation:**
- Random Forest Regressor
- Gradient Boosting Regressor

### Model Evaluation
- R² score (coefficient of determination)
- RMSE (Root Mean Squared Error)
- MAE (Mean Absolute Error)
- 5-fold cross-validation
- SHAP analysis for explainability (pending)

---

## Key Findings (Preliminary)

### 1. COVID-19 Obesity Paradox Discovered

Temporal analysis revealed an unexpected pattern:
- Obesity prevalence INCREASED by 1.23% (2020: 25.83% → 2023: 27.07%)
- Physical inactivity DECREASED by 1.05% (improved activity levels)
- Diet quality DECLINED by 3.65% (worst deterioration)

**Interpretation:** Obesity worsened despite improved physical activity because diet quality declined substantially, likely due to cost-of-living crisis affecting food affordability.

### 2. Strongest Predictors Identified (RQ1 Answered)

Correlation analysis revealed:
- Physical inactivity: r = +0.495 (STRONGEST positive predictor)
- Diet (5-a-day): r = -0.464 (strong PROTECTIVE factor)
- Smoking prevalence: r = +0.390 (weakest direct association)

**Conclusion:** Physical activity and diet are primary behavioral levers for obesity intervention.

### 3. Model Performance (RQ2 Partial Answer)

Initial results:
- Ridge Regression: R² = 0.355, RMSE = 5.01%
- Lasso Regression: R² = 0.349, RMSE = 5.03%

Both models show acceptable performance for health behavior data. Linear relationships dominate, suggesting ensemble methods may not substantially improve predictions (to be confirmed).

---

## How to Access and Run

### Google Colab Notebook (Recommended)
**Colab Link:** [Insert Colab share link here]

The notebook includes:
- Automatic data loading from Google Drive
- All visualizations with interpretations
- Step-by-step analysis workflow
- Detailed explanations of findings

### Running Locally
```bash
# Clone repository
git clone https://github.com/gabriel2lucky1990/adult-obesity-risk-modelling-england.git

# Navigate to project
cd adult-obesity-risk-modelling-england

# Open notebook
jupyter notebook notebooks/Predicting_Obesity_Analysis.ipynb
```

**Requirements:**
```
pandas >= 1.5.0
numpy >= 1.23.0
matplotlib >= 3.6.0
seaborn >= 0.12.0
scikit-learn >= 1.2.0
shap >= 0.41.0
gdown >= 4.6.0
```

---

## Development Timeline

**Completed Phases:**
- Week 1-2 (January 2026): Dataset identification, extraction, and merging
- Week 3-4 (February 2026): Exploratory data analysis and visualization
- Week 5 (February 2026): Correlation analysis and initial ML models

**Current Phase:**
- Week 6 (February 2026): Ensemble model implementation

**Upcoming Phases:**
- Week 7 (March 2026): SHAP analysis and model explainability
- Week 8-10 (March-April 2026): Report writing and final refinements
- April 22, 2026: Final submission

---

## Ethical Considerations

This analysis uses fully aggregated, anonymized, publicly available data from NHS Fingertips. No individual-level data is used. All analysis is conducted at population level (Local Authority aggregates).

There are no privacy or consent concerns under GDPR as the data:
- Is publicly accessible
- Contains no personal identifiers
- Represents aggregated population statistics
- Is intended for public health research and policy

---

## Academic Integrity Statement

This project is submitted as part of MSc Data Science coursework at University of Hertfordshire. All code, analysis, and interpretation are my own work. Data sources are properly cited and all methods are transparently documented.

**GitHub Repository:** https://github.com/gabriel2lucky1990/adult-obesity-risk-modelling-england

---

## License

This project is submitted as part of MSc Data Science coursework at University of Hertfordshire. All rights reserved.

The code and analysis methods may be referenced for educational purposes with proper citation.

---

## Contact

For questions about this project, please contact via University of Hertfordshire email.

---

## Acknowledgments

**Data Source:** NHS Fingertips (Office for Health Improvement & Disparities)  
**Dataset:** Public Health Outcomes Framework - Obesity, Physical Activity & Nutrition Profile  
**University:** University of Hertfordshire, School of Physics, Engineering and Computer Science  
**Programme:** MSc Data Science

---

## Version History

**v0.6 (February 18, 2026)**
- Added EDA interpretations to notebook
- Implemented Lasso and Ridge Regression models
- Documented COVID-19 obesity paradox finding
- Updated README with current progress

**v0.5 (February 15, 2026)**
- Completed comprehensive EDA with 8 visualizations
- Performed correlation analysis
- Answered Research Question 1

**v0.3 (February 10, 2026)**
- Merged 4 NHS Fingertips indicator datasets
- Verified data quality (zero missing values)
- Created initial project structure

**v0.1 (January 2026)**
- Initial repository setup
- Dataset identification and extraction planning

---

**Note:** This README is actively maintained and updated as the project progresses. Last major update: February 18, 2026.
