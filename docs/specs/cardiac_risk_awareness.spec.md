# Cardiac Risk Awareness System
## Formal Specification (SpecKit)

---

## 1. Purpose

The Cardiac Risk Awareness System is designed to estimate an individual’s
cardiac risk level and provide awareness-oriented guidance, including
risk-based healthcare consultation suggestions. The system is strictly
non-diagnostic and intended for educational and preventive awareness only.

---

## 2. Problem Definition

Cardiovascular diseases are often underdiagnosed due to lack of awareness,
irregular checkups, and limited access to early medical guidance.

This system:
- Estimates cardiac risk using structured data
- Categorizes users into Low / Medium / High risk
- Suggests appropriate types of healthcare professionals based on risk level
- Provides city-based doctor suggestions using public information

The system explicitly avoids medical diagnosis or treatment decisions.

---

## 3. Scope

### In Scope
- Cardiac risk estimation
- Risk stratification
- Explainable risk factors
- Risk-based doctor type recommendation
- City-based doctor lookup and ranking
- Informational healthcare guidance

### Out of Scope
- Medical diagnosis or prognosis
- Emergency decision-making
- Treatment or medication advice
- Endorsement of specific doctors

---

## 4. Target Users

- Adults aged 18+
- Non-medical users
- Users with partial or self-reported health data
- Educational and awareness-focused users

---

## 5. System Inputs

### 5.1 Required Inputs
- Age
- Sex

### 5.2 Optional Health Inputs
- Blood pressure
- Cholesterol
- Blood sugar
- BMI
- Heart rate

### 5.3 Optional Lifestyle Inputs
- Physical activity level
- Diet quality
- Stress level
- Sleep duration

### 5.4 Optional Location Input
- City (required for doctor recommendation feature)

---

## 6. Data Sources

- Kaggle heart disease datasets
- Framingham Heart Study dataset
- UCI Heart Disease dataset
- Publicly available doctor listings and review sources

---

## 7. Feature Categorization

Risk factors are grouped into:
- Demographic Risk Factors
- Medical Indicators
- Physical Measurements
- Lifestyle Indicators
- Behavioral Trends

This categorization supports both modeling and explainability.

---

## 8. System Outputs

### 8.1 Primary Outputs
- Risk Category: Low / Medium / High
- Risk explanation by category

### 8.2 Secondary Outputs
- Internal probability score (not exposed)
- Preventive lifestyle guidance
- Suggested healthcare professional types
- City-based doctor list (ranked by public ratings/reviews)

---

## 9. Doctor Recommendation Logic (Non-Diagnostic)

Doctor recommendations are informational and rule-based:

- Low Risk:
  - General Physician
  - Ayurvedic Doctor
  - Homeopathic Doctor

- Medium Risk:
  - General Physician
  - Cardiologist
  - Ayurvedic Doctor

- High Risk:
  - Cardiologist only

Recommendations are based on risk category and user city and do not constitute
medical endorsement.

---

## 10. Modeling Constraints

- Explainability prioritized over accuracy
- Conservative handling of uncertainty
- No black-box-only models
- Stable and calibrated probability outputs

---

## 11. Ethical & Safety Constraints

- No diagnostic or prescriptive language
- Clear disclaimers on medical authority
- No endorsement of specific doctors
- Transparent data limitations

---

## 12. Success Criteria

The system is successful if:
- Risk stratification is consistent and interpretable
- Doctor suggestions align with risk severity
- Outputs are understandable to non-medical users
- The system remains modular and auditable

---

## 13. Assumptions

- User data may be incomplete or approximate
- Doctor listings and ratings are publicly sourced
- System is used for awareness, not clinical decisions

---

## Doctor Recommendation Fairness & Distribution

To avoid excessive crowding at a single healthcare provider, the system applies
fairness-aware doctor recommendation logic.

Doctor suggestions are not strictly ordered by rating alone. Instead, doctors
with comparable ratings may be rotated or probabilistically reordered to ensure
more equitable distribution of users across available providers.

This mechanism aims to:
- Reduce patient congestion at individual clinics
- Improve user experience by minimizing wait times
- Promote fair exposure of qualified healthcare professionals

The fairness logic is informational, non-commercial, and does not prioritize
paid promotions or endorsements.

