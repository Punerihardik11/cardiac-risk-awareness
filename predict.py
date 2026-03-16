"""
Cardiac Risk Prediction Module
Loads trained model, preprocesses patient data, and predicts cardiac risk.
"""

import sys
import logging
from pathlib import Path
from typing import Tuple, List, Union
import pandas as pd
import numpy as np
import joblib

from src.inference import load_model, predict_risk

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Model paths - relative to project root
MODEL_PATH = Path(__file__).parent / "data" / "processed" / "logistic_regression_model.pkl"

# Expected feature count
EXPECTED_FEATURES = 44

# Continuous features that were scaled during training
CONTINUOUS_FEATURES = ['age', 'sysBP', 'totChol', 'BMI', 'heartRate']


def validate_patient_data(patient: Union[List, np.ndarray, pd.Series]) -> bool:
    """
    Validate patient data before prediction.
    
    Args:
        patient: Patient features (list, numpy array, or pandas Series)
        
    Returns:
        True if valid, raises ValueError otherwise
    """
    if not isinstance(patient, (list, tuple, np.ndarray, pd.Series)):
        raise ValueError("Patient data must be a list, tuple, numpy array, or pandas Series")
    
    if len(patient) != EXPECTED_FEATURES:
        raise ValueError(f"Expected {EXPECTED_FEATURES} features, got {len(patient)}")
    
    return True


def preprocess_patient_data(patient: Union[List, pd.Series]) -> np.ndarray:
    """
    Preprocess patient data by converting to numeric and handling missing values.
    
    Args:
        patient: Patient features (may contain strings or non-numeric values)
        
    Returns:
        Numpy array of numeric features ready for prediction
    """
    # Convert to pandas Series for easier processing
    if not isinstance(patient, pd.Series):
        patient = pd.Series(patient)
    
    # Convert all values to numeric, coercing errors to NaN
    patient_numeric = pd.to_numeric(patient, errors='coerce')
    
    # Fill missing values with 0
    patient_numeric = patient_numeric.fillna(0)
    
    return patient_numeric.values


def predict_cardiac_risk(patient: Union[List, np.ndarray, pd.Series]) -> Tuple[float, str]:
    """
    Predict cardiac risk for a patient.
    
    Args:
        patient: List/array of 44 patient features (raw or preprocessed)
        
    Returns:
        Tuple of (probability, risk_category)
        
    Raises:
        ValueError: If patient data is invalid
        FileNotFoundError: If model file doesn't exist
    """
    # Validate input
    validate_patient_data(patient)
    
    # Check if model file exists
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")
    
    try:
        # Preprocess patient data
        logger.debug("Preprocessing patient data...")
        patient_processed = preprocess_patient_data(patient)
        
        # Load model
        logger.info("Loading model...")
        model = load_model(str(MODEL_PATH))
        logger.info("Model loaded successfully")
        
        logger.debug(f"Patient data shape: {patient_processed.shape}, dtype: {patient_processed.dtype}")
        
        # Predict
        probability, risk = predict_risk(model, patient_processed)
        logger.info(f"Prediction: Probability={probability:.3f}, Risk={risk}")
        
        return probability, risk
        
    except Exception as e:
        logger.error(f"Prediction failed: {str(e)}")
        raise


def main():
    """Main entry point - demonstrates prediction with example data."""
    try:
        # Check if command line arguments provided
        if len(sys.argv) > 1 and sys.argv[1] == "--help":
            print_usage()
            return 0
        
        # Load test data from the preprocessed dataset
        data_path = Path(__file__).parent / "data" / "processed" / "X_scaled.csv"
        
        if data_path.exists():
            logger.info("Loading patient data from preprocessed dataset...")
            X_test = pd.read_csv(data_path)
            patient = X_test.iloc[0].to_list()  # Use first row as example
            logger.info(f"Loaded {len(patient)} features from dataset")
        else:
            raise FileNotFoundError(f"Test data not found: {data_path}")
        
        logger.info(f"Processing patient with {len(patient)} features")
        
        # Predict
        probability, risk = predict_cardiac_risk(patient)
        
        # Display results
        print("\n" + "=" * 60)
        print("CARDIAC RISK PREDICTION RESULTS")
        print("=" * 60)
        print(f"Predicted Risk Probability:  {probability:.1%}")
        print(f"Risk Classification:         {risk}")
        print(f"Confidence Score:            {probability:.4f}")
        print("=" * 60 + "\n")
        
        return 0
        
    except (ValueError, FileNotFoundError) as e:
        logger.error(f"Validation error: {str(e)}")
        print(f"\nERROR: {str(e)}\n")
        return 1
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        print(f"\nUNEXPECTED ERROR: {str(e)}\n")
        return 2


def print_usage():
    """Print usage information."""
    print("""
Cardiac Risk Prediction Tool
=============================

Usage:
  python predict.py              # Run prediction with example data
  python predict.py --help       # Show this help message

Expected Input:
  - 44 patient features as preprocessed in the dataset
  - Features include demographics, medical history, and clinical measurements
  - Categorical values are automatically converted to numeric

Output:
  - Risk Probability (0-1): Model's confidence in risk prediction  
  - Risk Category: Low Risk, Medium Risk, or High Risk
  - Based on optimal threshold of 0.35

Requirements:
  - data/processed/logistic_regression_model.pkl
  - data/processed/X_scaled.csv (for test data)
    """)


if __name__ == "__main__":
    sys.exit(main())