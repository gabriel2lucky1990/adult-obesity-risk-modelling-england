# Predicting Adult Obesity Prevalence Across English Local Authorities Using Behavioural and Socioeconomic Machine Learning Indicators

**MSc Data Science Final Project Report**  
**University of Hertfordshire — 7PAM2002**  
**Student:** Gabriel Lucky Lotanna  
**Supervisor:** Dhairya Kataria  
**Submission Date:** 22 April 2026

---

## Project Overview

This project investigates the determinants of adult obesity prevalence across 147 English Local Authorities using data from NHS Fingertips (2020–2023). Four supervised machine learning models are compared — Lasso Regression, Ridge Regression, Random Forest, and Gradient Boosting — to identify which behavioural and socioeconomic factors most strongly predict area-level obesity prevalence.

**Random Forest was selected as the final model** through a principled hierarchical selection framework incorporating cross-validation performance, residual diagnostic validity (Shapiro-Wilk normality test), and generalisation stability.

**Key finding:** SHAP analysis revealed that behavioural factors (physical inactivity, diet, smoking) contribute 58% of total predictive influence and socioeconomic factors (IMD, child poverty) contribute 42% — confirming that effective obesity reduction requires integrated interventions addressing both simultaneously.

---

## Research Questions

- **RQ1:** Which behavioural and socioeconomic indicators are most strongly associated with adult obesity prevalence across English Local Authorities?
- **RQ2:** Which supervised machine learning model provides optimal predictive performance for area-level obesity modelling?
- **RQ3:** Do model explainability techniques reveal meaningful differences in the relative contributions of behavioural versus socioeconomic determinants?

---

## Dataset

**Source:** NHS Fingertips — Public Health Profiles  
**URL:** https://fingertips.phe.org.uk/  
**Coverage:** 147 English Local Authorities, 2020–2023  
**Observations:** 583 (Local Authority × year combinations)

| Variable | Type | Description |
|---|---|---|
| obesity_prevalence (%) | Target | Adults with BMI ≥ 30 |
| physical_inactivity (%) | Behavioural | Adults with < 30 min MVPA/week |
| smoking_prevalence (%) | Behavioural | Current smokers aged 18+ |
| diet_5_a_day_pct (%) | Behavioural | Adults meeting fruit/veg recommendations |
| imd_score | Socioeconomic | Index of Multiple Deprivation |
| children_low_income_pct (%) | Socioeconomic | Children under 16 in low-income families |

---

## Results Summary

| Model | Test R² | CV R² | MAE | Diagnostics |
|---|---|---|---|---|
| Lasso Regression | 0.4065 | 0.2789 | 4.15 pp | PASS |
| Ridge Regression | 0.4186 | 0.2777 | 4.10 pp | PASS |
| **Random Forest ★** | **0.6012** | **0.4388** | **3.22 pp** | **PASS** |
| Gradient Boosting | 0.6303 | 0.5080 | 2.99 pp | FAIL |

★ Selected final model. Gradient Boosting was rejected despite higher CV R² due to significant overfitting (training-to-test residual ratio 10.7×) and failed Shapiro-Wilk normality test (p = 0.0431).

**SHAP Feature Contributions (Random Forest):**
- IMD score: 1.2815 (primary predictor)
- Physical inactivity: 1.2767 (near-equal primary)
- Diet quality: 0.9015
- Child poverty: 0.6180
- Smoking prevalence: 0.4181

---

## Repository Structure

```
adult-obesity-risk-modelling-england/
├── notebooks/
│   └── Predicting_Obesity_From_Health_Behaviors_in_England.ipynb
├── data/
│   └── obesity_enhanced_5features.csv
├── results/
│   ├── Model_Comparison_Results.csv
│   └── visualizations/
│       ├── EDA_histogram_distributions.png
│       ├── EDA_pairwise_relationships.png
│       ├── EDA_correlation_matrix.png
│       ├── Model1_Lasso_Diagnostics.png
│       ├── Model2_Ridge_Diagnostics.png
│       ├── Model3_RandomForest_Diagnostics.png
│       ├── Model4_GradientBoosting_Diagnostics.png
│       ├── Model_Comparison_R2_RMSE.png
│       ├── Model_Comparison_CV_Gap.png
│       ├── QQ_Comparison_RF_vs_GB.png
│       ├── Feature_Importance_RF.png
│       ├── SHAP_Beeswarm.png
│       ├── SHAP_Bar_Importance.png
│       ├── SHAP_Dependence_IMD.png
│       ├── SHAP_Dependence_Inactivity.png
│       ├── Residual_Diagnostics_RF.png
│       └── Geographic_Predictions.png
├── requirements.txt
├── .gitignore
└── README.md
```

---

## How to Run

### Option 1 — Google Colab (Recommended)

1. Open `notebooks/Predicting_Obesity_From_Health_Behaviors_in_England.ipynb` in Google Colab
2. Upload `data/obesity_enhanced_5features.csv` to your Google Drive
3. Update the file path in the data loading cell to match your Drive location
4. Run all cells sequentially (Runtime → Run all)

The notebook is self-contained and produces all figures, model diagnostics, SHAP analysis, and the model comparison table.

### Option 2 — Local (Jupyter)

```bash
# Clone the repository
git clone https://github.com/gabriel2lucky1990/adult-obesity-risk-modelling-england.git
cd adult-obesity-risk-modelling-england

# Install dependencies
pip install -r requirements.txt

# Launch notebook
jupyter notebook notebooks/Predicting_Obesity_From_Health_Behaviors_in_England.ipynb
```

### Requirements

```
pandas>=1.5.0
numpy>=1.23.0
matplotlib>=3.6.0
seaborn>=0.12.0
scikit-learn>=1.2.0
shap>=0.41.0
scipy>=1.9.0
```

---

## Reproducibility

All results are fully reproducible using the fixed random seed throughout:

```python
random_state = 50   # train-test split and all models
test_size    = 0.2  # 80/20 split (466 train / 117 test)
cv_folds     = 5    # KFold cross-validation
```

---

## Methodology

### Model Selection Framework
A three-criterion hierarchical framework was applied:
1. **Primary** — Cross-validation R² (generalisation to unseen data)
2. **Secondary** — MAE (typical prediction accuracy in percentage points)
3. **Tertiary** — Residual diagnostics (Shapiro-Wilk normality test + training-to-test residual ratio)

### SHAP Explainability
TreeExplainer (Lundberg et al., 2020) was applied to the final Random Forest model. Mean absolute SHAP values quantify each feature's marginal contribution, correctly handling the near-perfect multicollinearity between IMD score and child poverty (r = 0.958).

### Data Preparation
- StandardScaler fitted on training data only (prevents data leakage)
- GridSearchCV with 5-fold cross-validation for hyperparameter tuning
- Stratified train-test split (random_state = 50)

---

## Ethical Considerations

This analysis uses fully aggregated, anonymised, publicly available data from NHS Fingertips. No individual-level data is used. All results are expressed at Local Authority level only and must not be applied to individual risk assessment (ecological fallacy). No ethical approval was required.

---

## Citation

```
Lotanna, G. L. (2026). Predicting Adult Obesity Prevalence Across English
Local Authorities Using Behavioural and Socioeconomic Machine Learning Indicators.
MSc Data Science Final Project Report, University of Hertfordshire.
```

---

## Acknowledgements

**Data:** NHS Fingertips, Office for Health Improvement & Disparities  
**Supervisor:** Dhairya Kataria, University of Hertfordshire  
**Programme:** MSc Data Science, School of Physics, Engineering and Computer Science, University of Hertfordshire (2025–2026)
