"""Tests for the InsightsAgent module."""

import pytest
import pandas as pd
import numpy as np
from unittest.mock import Mock, patch
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.insights_agent import InsightsAgent, ExecutiveInsight, ProductInsight
from src.analytics import ChurnAnalytics, ChurnMetrics, SegmentInsight
from src.data_loader import DataLoader


@pytest.fixture
def sample_data():
    """Create sample data for testing."""
    np.random.seed(42)
    n_samples = 1000

    return pd.DataFrame({
        "CreditScore": np.random.randint(300, 850, n_samples),
        "Geography": np.random.choice(["France", "Germany", "Spain"], n_samples),
        "Gender": np.random.choice(["Male", "Female"], n_samples),
        "Age": np.random.randint(18, 92, n_samples),
        "Tenure": np.random.randint(0, 10, n_samples),
        "Balance": np.random.uniform(0, 250000, n_samples),
        "NumOfProducts": np.random.choice([1, 2, 3, 4], n_samples, p=[0.5, 0.4, 0.08, 0.02]),
        "HasCrCard": np.random.choice([0, 1], n_samples),
        "IsActiveMember": np.random.choice([0, 1], n_samples),
        "EstimatedSalary": np.random.uniform(10000, 200000, n_samples),
        "Exited": np.random.choice([0, 1], n_samples, p=[0.8, 0.2]),
    })


@pytest.fixture
def analytics(sample_data):
    """Create ChurnAnalytics instance with sample data."""
    return ChurnAnalytics(sample_data)


class TestChurnMetrics:
    """Tests for ChurnMetrics calculation."""

    def test_churn_metrics_calculation(self, analytics):
        """Test that churn metrics are calculated correctly."""
        metrics = analytics.get_churn_metrics()

        assert isinstance(metrics, ChurnMetrics)
        assert metrics.total_customers == 1000
        assert metrics.churned_customers + metrics.retained_customers == 1000
        assert 0 <= metrics.overall_churn_rate <= 100

    def test_churn_rate_percentage(self, analytics, sample_data):
        """Test churn rate is correctly calculated as percentage."""
        metrics = analytics.get_churn_metrics()
        expected_rate = (sample_data["Exited"].sum() / len(sample_data)) * 100

        assert round(metrics.overall_churn_rate, 2) == round(expected_rate, 2)


class TestSegmentAnalysis:
    """Tests for segment analysis functions."""

    def test_analyze_geography_segment(self, analytics):
        """Test geography segment analysis."""
        insights = analytics.analyze_segment("Geography")

        assert len(insights) > 0
        assert all(isinstance(i, SegmentInsight) for i in insights)
        assert all(i.segment_name == "Geography" for i in insights)

    def test_analyze_gender_segment(self, analytics):
        """Test gender segment analysis."""
        insights = analytics.analyze_segment("Gender")

        assert len(insights) == 2  # Male and Female
        assert all(i.segment_name == "Gender" for i in insights)

    def test_age_group_analysis(self, analytics):
        """Test age group analysis."""
        insights = analytics.get_age_group_analysis()

        assert len(insights) > 0
        assert all(i.segment_name == "AgeGroup" for i in insights)
        # Should be sorted by churn rate descending
        churn_rates = [i.churn_rate for i in insights]
        assert churn_rates == sorted(churn_rates, reverse=True)

    def test_balance_tier_analysis(self, analytics):
        """Test balance tier analysis."""
        insights = analytics.get_balance_tier_analysis()

        assert len(insights) > 0
        assert all(i.segment_name == "BalanceTier" for i in insights)

    def test_product_usage_analysis(self, analytics):
        """Test product usage analysis."""
        insights = analytics.get_product_usage_analysis()

        assert len(insights) > 0
        assert all(i.segment_name == "NumOfProducts" for i in insights)

    def test_activity_analysis(self, analytics):
        """Test activity status analysis."""
        insights = analytics.get_activity_analysis()

        assert len(insights) == 2
        statuses = [i.segment_value for i in insights]
        assert "Active" in statuses
        assert "Inactive" in statuses


class TestRiskLevel:
    """Tests for risk level determination."""

    def test_high_risk_threshold(self, analytics):
        """Test high risk level assignment."""
        risk = analytics.get_risk_level(30.0)
        assert risk == "HIGH"

    def test_medium_risk_threshold(self, analytics):
        """Test medium risk level assignment."""
        risk = analytics.get_risk_level(20.0)
        assert risk == "MEDIUM"

    def test_low_risk_threshold(self, analytics):
        """Test low risk level assignment."""
        risk = analytics.get_risk_level(10.0)
        assert risk == "LOW"


class TestCorrelationAnalysis:
    """Tests for correlation analysis."""

    def test_correlation_analysis_returns_dict(self, analytics):
        """Test correlation analysis returns dictionary."""
        correlations = analytics.get_correlation_analysis()

        assert isinstance(correlations, dict)
        assert len(correlations) > 0

    def test_correlation_values_range(self, analytics):
        """Test correlation values are in valid range."""
        correlations = analytics.get_correlation_analysis()

        for col, value in correlations.items():
            assert -1 <= value <= 1


class TestChurnedVsRetainedComparison:
    """Tests for churned vs retained comparison."""

    def test_comparison_structure(self, analytics):
        """Test comparison returns expected structure."""
        comparison = analytics.get_churned_vs_retained_comparison()

        assert isinstance(comparison, dict)
        for col, values in comparison.items():
            assert "churned_avg" in values
            assert "retained_avg" in values
            assert "difference" in values
            assert "difference_pct" in values


class TestHighRiskSegments:
    """Tests for high risk segment identification."""

    def test_high_risk_segments_list(self, analytics):
        """Test high risk segments returns list."""
        high_risk = analytics.get_high_risk_segments()

        assert isinstance(high_risk, list)
        # All returned should be high risk
        assert all(s.risk_level == "HIGH" for s in high_risk)


class TestInsightsAgent:
    """Tests for the InsightsAgent."""

    @pytest.fixture
    def agent_with_data(self, sample_data, tmp_path):
        """Create an InsightsAgent with test data."""
        # Save sample data to temp file
        data_file = tmp_path / "test_data.csv"
        sample_data.to_csv(data_file, index=False)

        agent = InsightsAgent(data_path=str(data_file))
        agent.initialize()
        return agent

    def test_executive_summary_structure(self, agent_with_data):
        """Test executive summary has expected structure."""
        summary = agent_with_data.generate_executive_summary()

        assert "report_date" in summary
        assert "overview" in summary
        assert "financial_impact" in summary
        assert "key_risk_indicators" in summary
        assert "top_churn_correlations" in summary

    def test_executive_summary_overview(self, agent_with_data):
        """Test executive summary overview section."""
        summary = agent_with_data.generate_executive_summary()
        overview = summary["overview"]

        assert "total_customers" in overview
        assert "churn_rate" in overview
        assert "churned_customers" in overview
        assert "retained_customers" in overview

    def test_executive_insights_list(self, agent_with_data):
        """Test executive insights returns list of insights."""
        insights = agent_with_data.generate_executive_insights()

        assert isinstance(insights, list)
        assert len(insights) > 0
        assert all(isinstance(i, ExecutiveInsight) for i in insights)

    def test_executive_insight_structure(self, agent_with_data):
        """Test each executive insight has required fields."""
        insights = agent_with_data.generate_executive_insights()

        for insight in insights:
            assert insight.title
            assert insight.summary
            assert insight.key_metric
            assert insight.business_impact
            assert insight.priority in ["HIGH", "MEDIUM", "LOW"]

    def test_product_insights_list(self, agent_with_data):
        """Test product insights returns list."""
        insights = agent_with_data.generate_product_insights()

        assert isinstance(insights, list)
        # Product insights may be empty if no thresholds are met
        for insight in insights:
            assert isinstance(insight, ProductInsight)

    def test_product_insight_structure(self, agent_with_data):
        """Test product insight structure when available."""
        insights = agent_with_data.generate_product_insights()

        for insight in insights:
            assert insight.title
            assert insight.finding
            assert insight.affected_segment
            assert insight.recommendation
            assert insight.expected_impact
            assert insight.implementation_effort in ["HIGH", "MEDIUM", "LOW"]

    def test_full_report_structure(self, agent_with_data):
        """Test full report has all sections."""
        report = agent_with_data.generate_full_report()

        assert "report_metadata" in report
        assert "executive_summary" in report
        assert "executive_insights" in report
        assert "product_insights" in report
        assert "detailed_analytics" in report


class TestDataLoader:
    """Tests for the DataLoader."""

    def test_load_from_file(self, sample_data, tmp_path):
        """Test loading data from file."""
        data_file = tmp_path / "test_data.csv"

        # Add the required columns for preprocessing
        sample_data["RowNumber"] = range(len(sample_data))
        sample_data["CustomerId"] = range(1000, 1000 + len(sample_data))
        sample_data["Surname"] = "Test"

        sample_data.to_csv(data_file, index=False)

        loader = DataLoader(data_path=str(data_file))
        data = loader.load_data()

        assert isinstance(data, pd.DataFrame)
        # RowNumber, CustomerId, Surname should be dropped
        assert "RowNumber" not in data.columns
        assert "CustomerId" not in data.columns
        assert "Surname" not in data.columns

    def test_file_not_found(self):
        """Test error when file not found."""
        loader = DataLoader(data_path="/nonexistent/path.csv")

        with pytest.raises(FileNotFoundError):
            loader.load_data()

    def test_get_feature_info(self, sample_data, tmp_path):
        """Test feature info extraction."""
        data_file = tmp_path / "test_data.csv"
        sample_data.to_csv(data_file, index=False)

        loader = DataLoader(data_path=str(data_file))
        info = loader.get_feature_info()

        assert "total_records" in info
        assert "total_features" in info
        assert "target_column" in info
        assert "churn_rate" in info


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
