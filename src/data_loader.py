"""
Data Loader Module for Bank Customer Churn Prediction Dataset.

This module handles loading and preprocessing the Bank Customer Churn
Prediction Dataset from Kaggle.
"""

import pandas as pd
import numpy as np
from pathlib import Path
from typing import Optional, Tuple


class DataLoader:
    """Handles loading and preprocessing of the Bank Customer Churn dataset."""

    # Dataset columns based on the Bank Customer Churn Prediction dataset
    EXPECTED_COLUMNS = [
        "RowNumber",
        "CustomerId",
        "Surname",
        "CreditScore",
        "Geography",
        "Gender",
        "Age",
        "Tenure",
        "Balance",
        "NumOfProducts",
        "HasCrCard",
        "IsActiveMember",
        "EstimatedSalary",
        "Exited",
    ]

    NUMERIC_COLUMNS = [
        "CreditScore",
        "Age",
        "Tenure",
        "Balance",
        "NumOfProducts",
        "EstimatedSalary",
    ]

    CATEGORICAL_COLUMNS = ["Geography", "Gender"]

    TARGET_COLUMN = "Exited"

    def __init__(self, data_path: Optional[str] = None):
        """
        Initialize the DataLoader.

        Args:
            data_path: Path to the CSV file. If None, will attempt to download
                       from Kaggle.
        """
        self.data_path = data_path
        self._data: Optional[pd.DataFrame] = None

    def load_data(self) -> pd.DataFrame:
        """
        Load the Bank Customer Churn dataset.

        Returns:
            DataFrame containing the loaded and preprocessed data.

        Raises:
            FileNotFoundError: If data file is not found and download fails.
            ValueError: If data format is invalid.
        """
        if self._data is not None:
            return self._data

        if self.data_path:
            self._data = self._load_from_file(self.data_path)
        else:
            self._data = self._download_from_kaggle()

        self._validate_data(self._data)
        self._data = self._preprocess_data(self._data)

        return self._data

    def _load_from_file(self, path: str) -> pd.DataFrame:
        """Load data from a local CSV file."""
        file_path = Path(path)
        if not file_path.exists():
            raise FileNotFoundError(f"Data file not found: {path}")

        return pd.read_csv(path)

    def _download_from_kaggle(self) -> pd.DataFrame:
        """Download the dataset from Kaggle using kagglehub."""
        try:
            import kagglehub

            path = kagglehub.dataset_download(
                "shantanudhakadd/bank-customer-churn-prediction"
            )
            csv_path = Path(path) / "Churn_Modelling.csv"
            if csv_path.exists():
                return pd.read_csv(csv_path)

            # Try to find any CSV file in the downloaded directory
            csv_files = list(Path(path).glob("*.csv"))
            if csv_files:
                return pd.read_csv(csv_files[0])

            raise FileNotFoundError(
                f"No CSV file found in downloaded dataset at {path}"
            )
        except ImportError:
            raise ImportError(
                "kagglehub is required to download data. "
                "Install with: pip install kagglehub"
            )
        except Exception as e:
            raise FileNotFoundError(
                f"Failed to download dataset from Kaggle: {e}. "
                "Please provide a local data path or ensure Kaggle credentials "
                "are configured."
            )

    def _validate_data(self, df: pd.DataFrame) -> None:
        """Validate the loaded data has expected structure."""
        # Check for target column
        if self.TARGET_COLUMN not in df.columns:
            raise ValueError(
                f"Missing target column '{self.TARGET_COLUMN}' in dataset. "
                f"Available columns: {list(df.columns)}"
            )

        # Check for essential columns
        essential_columns = self.NUMERIC_COLUMNS + self.CATEGORICAL_COLUMNS
        missing_columns = [col for col in essential_columns if col not in df.columns]
        if missing_columns:
            raise ValueError(
                f"Missing essential columns: {missing_columns}. "
                f"Available columns: {list(df.columns)}"
            )

    def _preprocess_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Preprocess the data for analysis."""
        # Create a copy to avoid modifying original
        df = df.copy()

        # Drop non-essential columns if they exist
        columns_to_drop = ["RowNumber", "CustomerId", "Surname"]
        existing_columns_to_drop = [col for col in columns_to_drop if col in df.columns]
        if existing_columns_to_drop:
            df = df.drop(columns=existing_columns_to_drop)

        # Handle missing values in numeric columns
        for col in self.NUMERIC_COLUMNS:
            if col in df.columns:
                df[col] = df[col].fillna(df[col].median())

        # Handle missing values in categorical columns
        for col in self.CATEGORICAL_COLUMNS:
            if col in df.columns:
                df[col] = df[col].fillna(df[col].mode().iloc[0])

        return df

    def get_train_test_split(
        self,
        test_size: float = 0.2,
        random_state: int = 42,
    ) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
        """
        Split data into training and testing sets.

        Args:
            test_size: Proportion of data to use for testing.
            random_state: Random seed for reproducibility.

        Returns:
            Tuple of (X_train, X_test, y_train, y_test).
        """
        from sklearn.model_selection import train_test_split

        df = self.load_data()

        X = df.drop(columns=[self.TARGET_COLUMN])
        y = df[self.TARGET_COLUMN]

        return train_test_split(X, y, test_size=test_size, random_state=random_state)

    def get_feature_info(self) -> dict:
        """Get information about the dataset features."""
        df = self.load_data()

        return {
            "total_records": len(df),
            "total_features": len(df.columns) - 1,  # Exclude target
            "numeric_features": [
                col for col in self.NUMERIC_COLUMNS if col in df.columns
            ],
            "categorical_features": [
                col for col in self.CATEGORICAL_COLUMNS if col in df.columns
            ],
            "target_column": self.TARGET_COLUMN,
            "churn_rate": df[self.TARGET_COLUMN].mean() * 100,
        }
