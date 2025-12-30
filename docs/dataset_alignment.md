# Dataset Alignment

This document maps external datasets to internal risk features.

---

## Primary Dataset Sources

- Kaggle Heart Disease Dataset
- Framingham Heart Study (processed versions)
- UCI Heart Disease Dataset

---

## Feature Alignment Table

| Dataset Feature | Internal Feature | Notes |
|-----------------|------------------|-------|
| age | age | direct |
| sex | sex | encoded |
| cp | chest_pain_type | categorical |
| trestbps | blood_pressure | systolic |
| chol | cholesterol | numeric |
| fbs | diabetes | proxy |
| restecg | ecg_result | optional |
| thalach | max_heart_rate | numeric |
| exang | exercise_angina | binary |
| oldpeak | st_depression | numeric |
| slope | st_slope | ordinal |
| ca | num_vessels | numeric |
| thal | thalassemia | categorical |

---

## Missing / User-Reported Features

These are **not** present in datasets but collected from users:
- diet_quality
- steps_per_day_avg
- stress_level
- sleep_hours_avg

Handled via:
- normalization
- proxy weighting
- optional inputs
