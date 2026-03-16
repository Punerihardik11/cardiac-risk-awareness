"""
Test and demo script for preprocessing module
Shows how to use the preprocessing functions for production
"""

import logging
from src.preprocessing import load_scaler, preprocess_features, preprocess_batch
import pandas as pd

# Configure logging for demo
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def main():
    """Demonstrate preprocessing module usage"""
    
    print("=" * 70)
    print("PREPROCESSING MODULE DEMO")
    print("=" * 70)
    
    # Load scaler
    print("\n1. Loading scaler...")
    scaler = load_scaler('data/processed/scaler.pkl')
    print(f"   Scaler type: {type(scaler).__name__}")
    print(f"   Expected features: 5 (age, sysBP, totChol, BMI, heartRate)")
    
    # Load sample data
    print("\n2. Loading sample data...")
    X_data = pd.read_csv('data/processed/X_scaled.csv')
    continuous_features = ['age', 'sysBP', 'totChol', 'BMI', 'heartRate']
    
    # Single sample preprocessing
    print("\n3. Preprocessing single patient...")
    patient_single = X_data[continuous_features].iloc[0].values
    print(f"   Input shape: {patient_single.shape}")
    print(f"   Input values: {patient_single}")
    
    scaled_single = preprocess_features(patient_single, scaler)
    print(f"   Output shape: {scaled_single.shape}")
    print(f"   Scaled values: {scaled_single}")
    
    # Batch preprocessing
    print("\n4. Preprocessing multiple patients (batch)...")
    patients_batch = X_data[continuous_features].iloc[:10].values
    print(f"   Input shape: {patients_batch.shape}")
    
    scaled_batch = preprocess_batch(patients_batch, scaler)
    print(f"   Output shape: {scaled_batch.shape}")
    print(f"   First scaled patient: {scaled_batch[0]}")
    
    # Preprocessing with all features
    print("\n5. Preprocessing with all 44 features (continuous_only=True)...")
    patient_full = X_data.iloc[0].values
    print(f"   Input shape: {patient_full.shape}")
    
    scaled_full = preprocess_features(patient_full, scaler, continuous_only=True)
    print(f"   Output shape: {scaled_full.shape}")
    print(f"   Only 5 continuous features extracted and scaled")
    
    # Error handling demonstration
    print("\n6. Error handling...")
    try:
        bad_data = [1, 2, 3]  # Wrong number of features
        preprocess_features(bad_data, scaler)
    except ValueError as e:
        print(f"   CAUGHT ERROR: {str(e)[:60]}...")
    
    try:
        scaler_bad = load_scaler('nonexistent.pkl')
    except FileNotFoundError as e:
        print(f"   CAUGHT ERROR: File not found")
    
    print("\n" + "=" * 70)
    print("PREPROCESSING MODULE READY FOR PRODUCTION")
    print("=" * 70)


if __name__ == "__main__":
    main()
