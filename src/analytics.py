"""
Churn Analytics Module.

This module provides analytical functions for understanding customer churn
patterns and generating insights from the Bank Customer Churn dataset.
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Any, Optional
from dataclasses import dataclass


@dataclass
class ChurnMetrics:
    """Container for churn-related metrics."""

    overall_churn_rate: float
    churned_customers: int
    retained_customers: int
    total_customers: int


@dataclass
class SegmentInsight:
    """Container for segment-specific insights."""

    segment_name: str
    segment_value: str
    churn_rate: float
    customer_count: int
    percentage_of_total: float
    risk_level: str


class ChurnAnalytics:
    """Provides analytical functions for customer churn analysis."""

    HIGH_RISK_THRESHOLD = 25.0  # Churn rate above this is high risk
    MEDIUM_RISK_THRESHOLD = 15.0  # Churn rate above this is medium risk

    def __init__(self, data: pd.DataFrame, target_column: str = "Exited"):
        """
        Initialize the ChurnAnalytics with data.

        Args:
            data: DataFrame containing customer data.
            target_column: Name of the target column indicating churn.
        """
        self.data = data
        self.target_column = target_column

    def get_churn_metrics(self) -> ChurnMetrics:
        """Calculate overall churn metrics."""
        total = len(self.data)
        churned = self.data[self.target_column].sum()
        retained = total - churned

        return ChurnMetrics(
            overall_churn_rate=round((churned / total) * 100, 2),
            churned_customers=int(churned),
            retained_customers=int(retained),
            total_customers=total,
        )

    def get_risk_level(self, churn_rate: float) -> str:
        """Determine risk level based on churn rate."""
        if churn_rate >= self.HIGH_RISK_THRESHOLD:
            return "HIGH"
        elif churn_rate >= self.MEDIUM_RISK_THRESHOLD:
            return "MEDIUM"
        return "LOW"

    def analyze_segment(
        self, column: str, value: Optional[Any] = None
    ) -> List[SegmentInsight]:
        """
        Analyze churn for a specific segment or all values in a column.

        Args:
            column: Column name to segment by.
            value: Specific value to analyze. If None, analyze all values.

        Returns:
            List of SegmentInsight objects.
        """
        insights = []
        total_customers = len(self.data)

        if value is not None:
            segment_data = self.data[self.data[column] == value]
            if len(segment_data) > 0:
                churn_rate = segment_data[self.target_column].mean() * 100
                insights.append(
                    SegmentInsight(
                        segment_name=column,
                        segment_value=str(value),
                        churn_rate=round(churn_rate, 2),
                        customer_count=len(segment_data),
                        percentage_of_total=round(
                            len(segment_data) / total_customers * 100, 2
                        ),
                        risk_level=self.get_risk_level(churn_rate),
                    )
                )
        else:
            for val in self.data[column].unique():
                segment_data = self.data[self.data[column] == val]
                if len(segment_data) > 0:
                    churn_rate = segment_data[self.target_column].mean() * 100
                    insights.append(
                        SegmentInsight(
                            segment_name=column,
                            segment_value=str(val),
                            churn_rate=round(churn_rate, 2),
                            customer_count=len(segment_data),
                            percentage_of_total=round(
                                len(segment_data) / total_customers * 100, 2
                            ),
                            risk_level=self.get_risk_level(churn_rate),
                        )
                    )

        return sorted(insights, key=lambda x: x.churn_rate, reverse=True)

    def get_age_group_analysis(self) -> List[SegmentInsight]:
        """Analyze churn by age groups."""
        bins = [0, 25, 35, 45, 55, 65, 100]
        labels = ["18-25", "26-35", "36-45", "46-55", "56-65", "65+"]

        data_copy = self.data.copy()
        data_copy["AgeGroup"] = pd.cut(data_copy["Age"], bins=bins, labels=labels)

        insights = []
        total_customers = len(data_copy)

        for age_group in labels:
            segment_data = data_copy[data_copy["AgeGroup"] == age_group]
            if len(segment_data) > 0:
                churn_rate = segment_data[self.target_column].mean() * 100
                insights.append(
                    SegmentInsight(
                        segment_name="AgeGroup",
                        segment_value=age_group,
                        churn_rate=round(churn_rate, 2),
                        customer_count=len(segment_data),
                        percentage_of_total=round(
                            len(segment_data) / total_customers * 100, 2
                        ),
                        risk_level=self.get_risk_level(churn_rate),
                    )
                )

        return sorted(insights, key=lambda x: x.churn_rate, reverse=True)

    def get_balance_tier_analysis(self) -> List[SegmentInsight]:
        """Analyze churn by account balance tiers."""
        # Create balance tiers
        data_copy = self.data.copy()

        # Define balance tiers
        conditions = [
            data_copy["Balance"] == 0,
            data_copy["Balance"] < 50000,
            data_copy["Balance"] < 100000,
            data_copy["Balance"] < 150000,
            data_copy["Balance"] >= 150000,
        ]
        labels = ["Zero Balance", "Low (<50K)", "Medium (50K-100K)",
                  "High (100K-150K)", "Premium (>150K)"]

        data_copy["BalanceTier"] = np.select(conditions, labels, default="Unknown")

        insights = []
        total_customers = len(data_copy)

        for tier in labels:
            segment_data = data_copy[data_copy["BalanceTier"] == tier]
            if len(segment_data) > 0:
                churn_rate = segment_data[self.target_column].mean() * 100
                insights.append(
                    SegmentInsight(
                        segment_name="BalanceTier",
                        segment_value=tier,
                        churn_rate=round(churn_rate, 2),
                        customer_count=len(segment_data),
                        percentage_of_total=round(
                            len(segment_data) / total_customers * 100, 2
                        ),
                        risk_level=self.get_risk_level(churn_rate),
                    )
                )

        return sorted(insights, key=lambda x: x.churn_rate, reverse=True)

    def get_tenure_analysis(self) -> List[SegmentInsight]:
        """Analyze churn by customer tenure."""
        bins = [0, 2, 4, 6, 8, 10]
        labels = ["0-2 years", "2-4 years", "4-6 years", "6-8 years", "8-10 years"]

        data_copy = self.data.copy()
        data_copy["TenureGroup"] = pd.cut(data_copy["Tenure"], bins=bins, labels=labels)

        insights = []
        total_customers = len(data_copy)

        for tenure_group in labels:
            segment_data = data_copy[data_copy["TenureGroup"] == tenure_group]
            if len(segment_data) > 0:
                churn_rate = segment_data[self.target_column].mean() * 100
                insights.append(
                    SegmentInsight(
                        segment_name="TenureGroup",
                        segment_value=tenure_group,
                        churn_rate=round(churn_rate, 2),
                        customer_count=len(segment_data),
                        percentage_of_total=round(
                            len(segment_data) / total_customers * 100, 2
                        ),
                        risk_level=self.get_risk_level(churn_rate),
                    )
                )

        return sorted(insights, key=lambda x: x.churn_rate, reverse=True)

    def get_product_usage_analysis(self) -> List[SegmentInsight]:
        """Analyze churn by number of products used."""
        return self.analyze_segment("NumOfProducts")

    def get_activity_analysis(self) -> List[SegmentInsight]:
        """Analyze churn by customer activity status."""
        data_copy = self.data.copy()
        data_copy["ActivityStatus"] = data_copy["IsActiveMember"].map(
            {1: "Active", 0: "Inactive"}
        )
        insights = []
        total_customers = len(data_copy)

        for status in ["Active", "Inactive"]:
            segment_data = data_copy[data_copy["ActivityStatus"] == status]
            if len(segment_data) > 0:
                churn_rate = segment_data[self.target_column].mean() * 100
                insights.append(
                    SegmentInsight(
                        segment_name="ActivityStatus",
                        segment_value=status,
                        churn_rate=round(churn_rate, 2),
                        customer_count=len(segment_data),
                        percentage_of_total=round(
                            len(segment_data) / total_customers * 100, 2
                        ),
                        risk_level=self.get_risk_level(churn_rate),
                    )
                )

        return sorted(insights, key=lambda x: x.churn_rate, reverse=True)

    def get_correlation_analysis(self) -> Dict[str, float]:
        """Calculate correlation between numeric features and churn."""
        numeric_cols = self.data.select_dtypes(include=[np.number]).columns.tolist()
        if self.target_column in numeric_cols:
            numeric_cols.remove(self.target_column)

        correlations = {}
        for col in numeric_cols:
            corr = self.data[col].corr(self.data[self.target_column])
            correlations[col] = round(corr, 4)

        # Sort by absolute correlation value
        return dict(
            sorted(correlations.items(), key=lambda x: abs(x[1]), reverse=True)
        )

    def get_high_risk_segments(self) -> List[SegmentInsight]:
        """Identify all high-risk customer segments."""
        all_insights = []

        # Analyze all key dimensions
        all_insights.extend(self.analyze_segment("Geography"))
        all_insights.extend(self.analyze_segment("Gender"))
        all_insights.extend(self.get_age_group_analysis())
        all_insights.extend(self.get_product_usage_analysis())
        all_insights.extend(self.get_activity_analysis())
        all_insights.extend(self.get_balance_tier_analysis())

        # Filter to only high-risk segments
        high_risk = [s for s in all_insights if s.risk_level == "HIGH"]

        return sorted(high_risk, key=lambda x: x.churn_rate, reverse=True)

    def get_summary_statistics(self) -> Dict[str, Any]:
        """Get summary statistics for numeric features."""
        numeric_data = self.data.select_dtypes(include=[np.number])

        summary = {}
        for col in numeric_data.columns:
            if col != self.target_column:
                summary[col] = {
                    "mean": round(self.data[col].mean(), 2),
                    "median": round(self.data[col].median(), 2),
                    "std": round(self.data[col].std(), 2),
                    "min": round(self.data[col].min(), 2),
                    "max": round(self.data[col].max(), 2),
                }

        return summary

    def get_churned_vs_retained_comparison(self) -> Dict[str, Dict[str, float]]:
        """Compare average values between churned and retained customers."""
        churned = self.data[self.data[self.target_column] == 1]
        retained = self.data[self.data[self.target_column] == 0]

        numeric_cols = self.data.select_dtypes(include=[np.number]).columns.tolist()
        if self.target_column in numeric_cols:
            numeric_cols.remove(self.target_column)

        comparison = {}
        for col in numeric_cols:
            comparison[col] = {
                "churned_avg": round(churned[col].mean(), 2),
                "retained_avg": round(retained[col].mean(), 2),
                "difference": round(churned[col].mean() - retained[col].mean(), 2),
                "difference_pct": round(
                    (
                        (churned[col].mean() - retained[col].mean())
                        / retained[col].mean()
                    )
                    * 100
                    if retained[col].mean() != 0
                    else 0,
                    2,
                ),
            }

        return comparison
