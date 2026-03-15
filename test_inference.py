import joblib
import numpy as np
from src.inference import load_model, predict_risk

# Load the model
try:
    model = load_model('data/processed/logistic_regression_model.pkl')
    print("✓ Model loaded successfully!")
except Exception as e:
    print(f"✗ Error loading model: {e}")
    exit(1)

# Load the scaler
try:
    scaler = joblib.load('data/processed/scaler.pkl')
    print("✓ Scaler loaded successfully!")
except Exception as e:
    print(f"✗ Error loading scaler: {e}")
    exit(1)

# Load actual test data
import pandas as pd
X_test = pd.read_csv('data/processed/X_scaled.csv')

# Select first row and convert to numeric, replacing any strings with NaN then 0
test_data = X_test.iloc[0].copy()
test_data = pd.to_numeric(test_data, errors='coerce').fillna(0)
test_features_scaled = test_data.values

print(f"✓ Using test features with {test_features_scaled.shape[0]} features")
print(f"  Features dtype: {test_features_scaled.dtype}")

# Test prediction
try:
    probability, risk = predict_risk(model, test_features_scaled)
    print(f"\n✓ Prediction successful!")
    print(f"  - Probability: {probability:.4f}")
    print(f"  - Risk Category: {risk}")
except Exception as e:
    print(f"✗ Error during prediction: {e}")
    exit(1)

print("\n✓ All tests passed! inference.py is working correctly.")
