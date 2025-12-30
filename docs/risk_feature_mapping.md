# Risk Feature Mapping

This document defines how user-provided inputs are transformed into
machine-learning features for cardiac risk prediction.

This is NOT diagnosis. It is risk awareness.

---

## 1. Core Risk Categories

We group features into 5 categories:

1. Demographics
2. Medical History
3. Lifestyle Factors
4. Physical Indicators
5. Behavioral Trends (longitudinal)

---

## 2. Feature Mapping Table (Initial)

### Demographics
| Feature | Type | Example | Notes |
|------|------|--------|------|
| age | numeric | 45 | Strong risk driver |
| sex | categorical | male/female | Encoded |
| family_history | binary | yes/no | Genetic risk |

---

### Medical History
| Feature | Type | Example | Notes |
|------|------|--------|------|
| hypertension | binary | yes/no | Major risk |
| diabetes | binary | yes/no | High correlation |
| smoking | categorical | never/former/current | Dose-like |

---

### Lifestyle Factors
| Feature | Type | Example | Notes |
|------|------|--------|------|
| physical_activity_minutes | numeric | 30 | Daily avg |
| diet_quality | ordinal | low/medium/high | Subjective |
| alcohol_intake | ordinal | none/moderate/high | Moderation-aware |

---

### Physical Indicators
| Feature | Type | Example | Notes |
|------|------|--------|------|
| bmi | numeric | 27.4 | Derived |
| resting_heart_rate | numeric | 78 | If available |
| blood_pressure | numeric | 130/85 | Optional |

---

### Behavioral Trends (Future Phase)
| Feature | Type | Example | Notes |
|------|------|--------|------|
| steps_per_day_avg | numeric | 6000 | Trend-based |
| stress_level | ordinal | low/medium/high | Self-reported |
| sleep_hours_avg | numeric | 6.5 | Chronic impact |

---

## 3. Output Interpretation

Model outputs:
- Low Risk
- Medium Risk
- High Risk

Displayed with:
- Simple explanation
- Contributing factors
- Lifestyle guidance (non-medical)
