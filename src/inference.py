import joblib
import numpy as np
from src.risk_classifier import classify_risk


def load_model(model_path: str):
    """Load trained ML model"""
    return joblib.load(model_path)


def predict_risk(model, patient_features):
    """
    Predict cardiac risk from patient features.
    Returns probability and risk category.
    """

    # Ensure features are numpy array and numeric
    features = np.asarray(patient_features, dtype=float)
    
    # Reshape to 2D if necessary (required by sklearn predict_proba)
    if features.ndim == 1:
        features = features.reshape(1, -1)

    probability = model.predict_proba(features)[0][1]

    risk = classify_risk(probability)

    return probability, risk