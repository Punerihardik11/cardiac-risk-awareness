"""
Feature Preprocessing Module
Handles loading scalers and preprocessing patient features for model prediction.
"""

import logging
from pathlib import Path
from typing import Union, Tuple
import numpy as np
import pandas as pd
import joblib

# Configure logging
logger = logging.getLogger(__name__)

# Define continuous features that are scaled
CONTINUOUS_FEATURES = ['age', 'sysBP', 'totChol', 'BMI', 'heartRate']
EXPECTED_SCALER_FEATURES = len(CONTINUOUS_FEATURES)


def load_scaler(scaler_path: Union[str, Path]):
    """
    Load a trained scaler from disk.
    
    Args:
        scaler_path: Path to the saved scaler pickle file
        
    Returns:
        Loaded scaler object
        
    Raises:
        FileNotFoundError: If scaler file doesn't exist
        ValueError: If scaler is invalid or corrupted
    """
    scaler_path = Path(scaler_path)
    
    if not scaler_path.exists():
        raise FileNotFoundError(f"Scaler file not found: {scaler_path}")
    
    try:
        logger.info(f"Loading scaler from {scaler_path}")
        scaler = joblib.load(scaler_path)
        logger.debug(f"Scaler loaded successfully: {type(scaler).__name__}")
        return scaler
    except Exception as e:
        logger.error(f"Failed to load scaler: {str(e)}")
        raise ValueError(f"Invalid or corrupted scaler file: {str(e)}")


def validate_scaler(scaler) -> bool:
    """
    Validate that a scaler object is properly configured.
    
    Args:
        scaler: Scaler object to validate
        
    Returns:
        True if valid, raises ValueError otherwise
    """
    if scaler is None:
        raise ValueError("Scaler is None")
    
    if not hasattr(scaler, 'transform'):
        raise ValueError(f"Scaler missing 'transform' method: {type(scaler).__name__}")
    
    if not hasattr(scaler, 'n_features_in_'):
        raise ValueError("Scaler missing 'n_features_in_' attribute - not fitted")
    
    if scaler.n_features_in_ != EXPECTED_SCALER_FEATURES:
        raise ValueError(
            f"Scaler expects {scaler.n_features_in_} features, "
            f"but {EXPECTED_SCALER_FEATURES} were expected"
        )
    
    logger.debug(f"Scaler validation passed: {scaler.n_features_in_} features")
    return True


def preprocess_features(
    features: Union[list, tuple, np.ndarray, pd.Series],
    scaler,
    continuous_only: bool = False
) -> np.ndarray:
    """
    Prepare patient features for model prediction.
    
    Converts features to numeric array and applies scaling.
    
    Args:
        features: Input features (can be list, array, or Series)
        scaler: Fitted scaler object for normalization
        continuous_only: If True, only use continuous features (for demo)
        
    Returns:
        Scaled features as numpy array
        
    Raises:
        ValueError: If features are invalid or incompatible with scaler
        TypeError: If scaler is invalid
    """
    if features is None or len(features) == 0:
        raise ValueError("Features cannot be empty")
    
    # Validate scaler
    validate_scaler(scaler)
    
    try:
        # Convert to pandas Series for consistent handling
        if isinstance(features, pd.DataFrame):
            features = features.iloc[0] if features.shape[0] > 0 else features.iloc[:1]
        
        features_series = pd.Series(features) if not isinstance(features, pd.Series) else features
        
        # Convert to numeric, coercing errors to NaN
        features_numeric = pd.to_numeric(features_series, errors='coerce')
        
        # Fill missing values with 0
        features_numeric = features_numeric.fillna(0)
        
        # Convert to numpy array
        features_array = features_numeric.values.astype(float)
        
        logger.debug(f"Features converted: shape={features_array.shape}, dtype={features_array.dtype}")
        
        # Validate feature count
        if continuous_only:
            # For demo purposes - only use continuous features
            if len(features_array) >= EXPECTED_SCALER_FEATURES:
                features_array = features_array[:EXPECTED_SCALER_FEATURES]
            else:
                raise ValueError(
                    f"Expected at least {EXPECTED_SCALER_FEATURES} features, "
                    f"got {len(features_array)}"
                )
        
        # Reshape if single sample (required by scaler)
        if features_array.ndim == 1:
            features_array = features_array.reshape(1, -1)
            logger.debug(f"Reshaped features to: {features_array.shape}")
        
        # Validate after reshaping
        if features_array.shape[1] != EXPECTED_SCALER_FEATURES:
            raise ValueError(
                f"Feature count mismatch: expected {EXPECTED_SCALER_FEATURES}, "
                f"got {features_array.shape[1]}"
            )
        
        # Scale features
        logger.info("Scaling features...")
        features_scaled = scaler.transform(features_array)
        logger.debug(f"Features scaled successfully: shape={features_scaled.shape}")
        
        # Return as 1D array for single sample
        if features_scaled.shape[0] == 1:
            return features_scaled.ravel()
        
        return features_scaled
        
    except Exception as e:
        logger.error(f"Preprocessing failed: {str(e)}")
        raise


def preprocess_batch(
    features_batch: Union[np.ndarray, pd.DataFrame],
    scaler
) -> np.ndarray:
    """
    Preprocess a batch of features.
    
    Args:
        features_batch: Multiple samples (2D array or DataFrame)
        scaler: Fitted scaler object
        
    Returns:
        Scaled features as numpy array
        
    Raises:
        ValueError: If input is invalid
    """
    if isinstance(features_batch, pd.DataFrame):
        logger.debug(f"Converting DataFrame with shape {features_batch.shape}")
        # Convert all columns to numeric
        features_numeric = features_batch.apply(pd.to_numeric, errors='coerce').fillna(0)
        features_array = features_numeric.values.astype(float)
    else:
        features_array = np.asarray(features_batch, dtype=float)
    
    if features_array.ndim != 2:
        raise ValueError(f"Expected 2D array, got shape {features_array.shape}")
    
    validate_scaler(scaler)
    
    if features_array.shape[1] != EXPECTED_SCALER_FEATURES:
        raise ValueError(
            f"Feature count mismatch: expected {EXPECTED_SCALER_FEATURES}, "
            f"got {features_array.shape[1]}"
        )
    
    logger.info(f"Preprocessing batch: {features_array.shape}")
    features_scaled = scaler.transform(features_array)
    
    return features_scaled
