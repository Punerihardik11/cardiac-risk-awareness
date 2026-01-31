# System & Machine Learning Plan
## Cardiac Risk Awareness System

---

## 1. System Architecture Overview

The system is designed as a modular, explainable pipeline with an additional
post-risk recommendation layer for healthcare consultation guidance.

High-level flow:
User Input → Validation → Feature Engineering → ML Risk Estimation →
Risk Stratification → Doctor Recommendation → Explainability → User Output

Each module operates independently to preserve maintainability.

---

## 2. Data Flow Pipeline

### Training-Time
- Load and align datasets
- Preprocess and encode features
- Train and evaluate models

### Inference-Time
- Validate user input
- Apply preprocessing
- Generate risk estimate
- Assign risk category
- Trigger doctor recommendation logic
- Generate explanation and guidance

---

## 3. Feature Engineering Strategy

- Mandatory: age, sex
- Optional: clinical and lifestyle indicators
- Lifestyle inputs act as risk modifiers
- Features grouped for interpretability

Doctor recommendation logic does not affect feature engineering.

---

## 4. Missing Data Handling

- Missing required inputs block inference
- Missing optional inputs use risk-neutral defaults
- Missing city disables doctor recommendation gracefully

---

## 5. Model Selection Strategy

- Baseline: Logistic Regression
- Optional: Tree-based models if explainability preserved

Model output remains a probability score only.

---

## 6. Training & Evaluation Plan

- Recall prioritized for high-risk class
- ROC-AUC and calibration tracked
- No leakage between preprocessing and modeling

---

## 7. Risk Stratification Logic

Probability output mapped into:
- Low Risk
- Medium Risk
- High Risk

Thresholds tuned conservatively.

---

## 8. Doctor Recommendation Module

This module operates **after risk stratification**.

### 8.1 Risk-to-Doctor Mapping (Rule-Based)
- Low → GP / Ayurvedic / Homeopathic
- Medium → GP / Cardiologist / Ayurvedic
- High → Cardiologist only

### 8.2 City-Based Doctor Lookup
- Uses user-provided city
- Fetches publicly available doctor listings
- No private or sensitive data access

### 8.3 Ranking Strategy
- Sort by ratings, reviews, and relevance
- No paid promotion or prioritization
- Transparent ranking criteria

---

## 9. Explainability Strategy

Explanations include:
- Risk-driving factors
- Risk category meaning
- Reason for suggested doctor types

Doctor suggestions are clearly labeled as informational.

---

## 10. Inference Workflow

1. Validate input
2. Preprocess features
3. Predict risk probability
4. Assign risk category
5. Map risk to doctor types
6. Fetch and rank city-based doctors
7. Generate explanation and guidance
8. Return structured output

---

## 11. Edge Case Handling

- Unknown city → disable doctor suggestions
- No doctors found → informative message
- Contradictory inputs handled safely

---

## 12. Non-Functional Requirements

- Modular recommendation logic
- Deterministic rules
- Auditable ranking behavior
- Easy future extension (API/UI)

---

## 13. Design Rationale

Medical risk estimation and doctor recommendation are deliberately separated.
This ensures safety, clarity, and ethical compliance while maintaining
user usefulness.

### 8.4 Fairness-Aware Distribution Strategy

To prevent concentration of users toward a single provider, the system applies
a fairness-aware ranking strategy.

Approach:
- Doctors with similar ratings are grouped
- Final ordering is determined using weighted randomization
- Higher-rated doctors retain higher selection probability
- No single doctor is always shown first

This strategy balances recommendation quality with equitable distribution and
reduces unintentional overcrowding at clinics.
