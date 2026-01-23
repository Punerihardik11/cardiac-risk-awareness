# Task Breakdown – Cardiac Risk Awareness System

---

## Milestone 1: Data Readiness
- [ ] Collect and load Kaggle, Framingham, and UCI datasets
- [ ] Align datasets to internal feature schema
- [ ] Handle missing values and invalid entries
- [ ] Perform basic data sanity checks

---

## Milestone 2: Feature Engineering
- [ ] Encode categorical features
- [ ] Normalize numerical features
- [ ] Create lifestyle proxy scores
- [ ] Group features into medical risk categories
- [ ] Ensure training–inference feature parity

---

## Milestone 3: Model Training & Evaluation
- [ ] Train baseline logistic regression model
- [ ] Evaluate using recall, ROC-AUC, and calibration
- [ ] Experiment with advanced models if needed
- [ ] Select final model based on interpretability and safety

---

## Milestone 4: Explainability
- [ ] Extract feature importance
- [ ] Aggregate category-level risk contribution
- [ ] Create human-readable explanation templates
- [ ] Validate explanations against known medical logic

---

## Milestone 5: Inference Pipeline
- [ ] Validate user inputs and ranges
- [ ] Handle partial and missing inputs gracefully
- [ ] Apply preprocessing pipeline at inference time
- [ ] Generate risk category and explanations
- [ ] Add preventive lifestyle guidance

---

## Milestone 6: Doctor Recommendation Module
- [ ] Define risk-to-doctor mapping rules
- [ ] Validate city input for recommendations
- [ ] Fetch city-based doctor listings (public data)
- [ ] Rank doctors using ratings and reviews
- [ ] Apply fairness-aware weighted randomization
- [ ] Ensure no single provider is always ranked first
- [ ] Add user-facing disclaimer for recommendations
