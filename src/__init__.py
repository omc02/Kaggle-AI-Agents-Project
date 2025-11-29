"""
Bank Customer Churn Prediction - AI Insights Agent

This module provides an AI Agent that generates executive and product manager
insights from the Bank Customer Churn Prediction Dataset.
"""

from .insights_agent import InsightsAgent
from .data_loader import DataLoader
from .analytics import ChurnAnalytics

__version__ = "1.0.0"
__all__ = ["InsightsAgent", "DataLoader", "ChurnAnalytics"]
