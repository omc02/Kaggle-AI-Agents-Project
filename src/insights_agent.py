"""
AI Insights Agent Module.

This module provides an AI Agent that generates executive and product manager
insights from the Bank Customer Churn Prediction Dataset.
"""

import pandas as pd
from typing import Dict, List, Any, Optional
from datetime import datetime
from dataclasses import dataclass

from .data_loader import DataLoader
from .analytics import ChurnAnalytics, ChurnMetrics, SegmentInsight


@dataclass
class ExecutiveInsight:
    """Container for executive-level insights."""

    title: str
    summary: str
    key_metric: str
    business_impact: str
    priority: str  # HIGH, MEDIUM, LOW


@dataclass
class ProductInsight:
    """Container for product manager insights."""

    title: str
    finding: str
    affected_segment: str
    recommendation: str
    expected_impact: str
    implementation_effort: str  # HIGH, MEDIUM, LOW


class InsightsAgent:
    """
    AI Agent that generates insights for executives and product managers.

    This agent analyzes the Bank Customer Churn dataset and provides
    actionable insights tailored for different stakeholder audiences.
    """

    def __init__(self, data_path: Optional[str] = None):
        """
        Initialize the InsightsAgent.

        Args:
            data_path: Optional path to the dataset CSV file.
                       If None, will attempt to download from Kaggle.
        """
        self.data_loader = DataLoader(data_path)
        self._data: Optional[pd.DataFrame] = None
        self._analytics: Optional[ChurnAnalytics] = None
        self._metrics: Optional[ChurnMetrics] = None

    def initialize(self) -> None:
        """Load data and initialize analytics."""
        self._data = self.data_loader.load_data()
        self._analytics = ChurnAnalytics(self._data)
        self._metrics = self._analytics.get_churn_metrics()

    def _ensure_initialized(self) -> None:
        """Ensure the agent is initialized before generating insights."""
        if self._data is None:
            self.initialize()

    def generate_executive_summary(self) -> Dict[str, Any]:
        """
        Generate an executive summary of customer churn.

        Returns:
            Dictionary containing the executive summary with key metrics
            and high-level insights.
        """
        self._ensure_initialized()

        metrics = self._metrics
        high_risk = self._analytics.get_high_risk_segments()
        correlations = self._analytics.get_correlation_analysis()

        # Calculate financial impact estimate
        avg_customer_value = self._data["EstimatedSalary"].mean() * 0.05
        churn_financial_impact = metrics.churned_customers * avg_customer_value

        return {
            "report_date": datetime.now().isoformat(),
            "overview": {
                "total_customers": metrics.total_customers,
                "churn_rate": f"{metrics.overall_churn_rate}%",
                "churned_customers": metrics.churned_customers,
                "retained_customers": metrics.retained_customers,
            },
            "financial_impact": {
                "estimated_revenue_at_risk": f"${churn_financial_impact:,.2f}",
                "avg_customer_value": f"${avg_customer_value:,.2f}",
            },
            "key_risk_indicators": [
                {
                    "segment": s.segment_value,
                    "dimension": s.segment_name,
                    "churn_rate": f"{s.churn_rate}%",
                    "affected_customers": s.customer_count,
                }
                for s in high_risk[:5]
            ],
            "top_churn_correlations": [
                {"factor": k, "correlation": v}
                for k, v in list(correlations.items())[:3]
            ],
        }

    def generate_executive_insights(self) -> List[ExecutiveInsight]:
        """
        Generate executive-level insights about customer churn.

        Returns:
            List of ExecutiveInsight objects with strategic recommendations.
        """
        self._ensure_initialized()

        insights = []
        metrics = self._metrics
        high_risk = self._analytics.get_high_risk_segments()
        geography = self._analytics.analyze_segment("Geography")
        activity = self._analytics.get_activity_analysis()

        # Overall churn insight
        churn_status = "concerning" if metrics.overall_churn_rate > 15 else "moderate"
        insights.append(
            ExecutiveInsight(
                title="Overall Customer Retention Status",
                summary=f"Current churn rate of {metrics.overall_churn_rate}% "
                f"represents {metrics.churned_customers:,} lost customers.",
                key_metric=f"{metrics.overall_churn_rate}% churn rate",
                business_impact=f"Estimated revenue impact of "
                f"${metrics.churned_customers * 5000:,.0f} "
                f"based on average customer lifetime value.",
                priority="HIGH" if metrics.overall_churn_rate > 15 else "MEDIUM",
            )
        )

        # Geographic risk insight
        if geography:
            highest_geo = max(geography, key=lambda x: x.churn_rate)
            insights.append(
                ExecutiveInsight(
                    title=f"Geographic Risk Alert: {highest_geo.segment_value}",
                    summary=f"{highest_geo.segment_value} region shows the highest "
                    f"churn rate at {highest_geo.churn_rate}%, affecting "
                    f"{highest_geo.customer_count:,} customers.",
                    key_metric=f"{highest_geo.churn_rate}% regional churn",
                    business_impact="Regional strategy review recommended. "
                    "Consider market-specific retention programs.",
                    priority=highest_geo.risk_level,
                )
            )

        # Activity-based insight
        if activity:
            inactive = next((a for a in activity if a.segment_value == "Inactive"), None)
            if inactive:
                insights.append(
                    ExecutiveInsight(
                        title="Inactive Customer Risk",
                        summary=f"Inactive customers have a {inactive.churn_rate}% "
                        f"churn rate, representing {inactive.customer_count:,} "
                        "customers at elevated risk.",
                        key_metric=f"{inactive.customer_count:,} at-risk customers",
                        business_impact="Customer engagement programs could "
                        "significantly reduce churn in this segment.",
                        priority=inactive.risk_level,
                    )
                )

        # High-risk segment summary
        if high_risk:
            total_high_risk = sum(s.customer_count for s in high_risk[:5])
            insights.append(
                ExecutiveInsight(
                    title="High-Risk Segment Summary",
                    summary=f"{len(high_risk)} customer segments identified as "
                    f"high-risk, affecting approximately {total_high_risk:,} "
                    "customers across multiple dimensions.",
                    key_metric=f"{len(high_risk)} high-risk segments",
                    business_impact="Targeted intervention programs for these "
                    "segments could improve overall retention by 5-10%.",
                    priority="HIGH",
                )
            )

        # Age-based insight
        age_analysis = self._analytics.get_age_group_analysis()
        if age_analysis:
            highest_age_risk = age_analysis[0]
            insights.append(
                ExecutiveInsight(
                    title=f"Age Group Risk: {highest_age_risk.segment_value}",
                    summary=f"Customers aged {highest_age_risk.segment_value} show "
                    f"the highest churn rate at {highest_age_risk.churn_rate}%.",
                    key_metric=f"{highest_age_risk.churn_rate}% age group churn",
                    business_impact="Product and service offerings may need "
                    "adjustment for this demographic segment.",
                    priority=highest_age_risk.risk_level,
                )
            )

        return insights

    def generate_product_insights(self) -> List[ProductInsight]:
        """
        Generate product manager-focused insights with actionable recommendations.

        Returns:
            List of ProductInsight objects with specific recommendations.
        """
        self._ensure_initialized()

        insights = []
        comparison = self._analytics.get_churned_vs_retained_comparison()
        products = self._analytics.get_product_usage_analysis()
        activity = self._analytics.get_activity_analysis()
        balance = self._analytics.get_balance_tier_analysis()
        tenure = self._analytics.get_tenure_analysis()

        # Product usage insight
        if products:
            high_churn_products = [p for p in products if p.churn_rate > 20]
            if high_churn_products:
                worst = high_churn_products[0]
                insights.append(
                    ProductInsight(
                        title="Product Portfolio Optimization",
                        finding=f"Customers with {worst.segment_value} products "
                        f"have a {worst.churn_rate}% churn rate.",
                        affected_segment=f"{worst.customer_count:,} customers "
                        f"({worst.percentage_of_total}% of total)",
                        recommendation="Review product bundling strategy. "
                        "Consider creating product combinations that increase "
                        "engagement and reduce churn.",
                        expected_impact="5-8% reduction in churn for affected segment",
                        implementation_effort="MEDIUM",
                    )
                )

        # Activity engagement insight
        if activity:
            inactive = next((a for a in activity if a.segment_value == "Inactive"), None)
            if inactive and inactive.churn_rate > 20:
                insights.append(
                    ProductInsight(
                        title="Customer Engagement Enhancement",
                        finding=f"Inactive members churn at {inactive.churn_rate}%, "
                        f"significantly higher than active members.",
                        affected_segment=f"{inactive.customer_count:,} inactive "
                        f"customers ({inactive.percentage_of_total}% of base)",
                        recommendation="Implement a re-engagement program: "
                        "personalized notifications, special offers, "
                        "and feature highlights to drive activity.",
                        expected_impact="10-15% conversion from inactive to active, "
                        "reducing churn by 3-5% in this segment",
                        implementation_effort="LOW",
                    )
                )

        # Balance tier insight
        if balance:
            zero_balance = next(
                (b for b in balance if "Zero" in b.segment_value), None
            )
            if zero_balance and zero_balance.churn_rate > 20:
                insights.append(
                    ProductInsight(
                        title="Zero Balance Customer Retention",
                        finding=f"Customers with zero balance have a "
                        f"{zero_balance.churn_rate}% churn rate.",
                        affected_segment=f"{zero_balance.customer_count:,} customers "
                        f"({zero_balance.percentage_of_total}% of base)",
                        recommendation="Introduce incentive programs for maintaining "
                        "minimum balance: bonus interest rates, fee waivers, "
                        "or loyalty points.",
                        expected_impact="15-20% reduction in zero-balance "
                        "customer churn",
                        implementation_effort="MEDIUM",
                    )
                )

        # New customer retention insight
        if tenure:
            new_customers = next(
                (t for t in tenure if "0-2" in t.segment_value), None
            )
            if new_customers and new_customers.churn_rate > 18:
                insights.append(
                    ProductInsight(
                        title="New Customer Onboarding Improvement",
                        finding=f"Customers with 0-2 years tenure have a "
                        f"{new_customers.churn_rate}% churn rate.",
                        affected_segment=f"{new_customers.customer_count:,} "
                        f"new customers",
                        recommendation="Enhance onboarding experience: "
                        "welcome program, guided product tours, "
                        "early engagement touchpoints, and first-year benefits.",
                        expected_impact="20-25% improvement in first-year retention",
                        implementation_effort="MEDIUM",
                    )
                )

        # Age-specific product insight
        age = self._analytics.get_age_group_analysis()
        if age:
            senior = next((a for a in age if "65" in a.segment_value), None)
            if senior and senior.churn_rate > 25:
                insights.append(
                    ProductInsight(
                        title="Senior Customer Experience",
                        finding=f"Senior customers (65+) have a "
                        f"{senior.churn_rate}% churn rate.",
                        affected_segment=f"{senior.customer_count:,} senior customers",
                        recommendation="Develop senior-friendly features: "
                        "simplified UI, dedicated support line, "
                        "in-branch services, and retirement planning tools.",
                        expected_impact="10-15% churn reduction for seniors",
                        implementation_effort="HIGH",
                    )
                )

        # Credit score insight
        if "CreditScore" in comparison:
            credit_diff = comparison["CreditScore"]["difference"]
            if credit_diff < -20:
                insights.append(
                    ProductInsight(
                        title="Credit Score Risk Indicator",
                        finding="Churned customers have lower average credit "
                        f"scores by {abs(credit_diff):.0f} points.",
                        affected_segment="Customers with below-average credit scores",
                        recommendation="Implement credit improvement programs: "
                        "financial education, credit monitoring tools, "
                        "and personalized financial advice.",
                        expected_impact="Improved customer financial health and "
                        "5-7% churn reduction",
                        implementation_effort="HIGH",
                    )
                )

        # Gender-based insight
        gender = self._analytics.analyze_segment("Gender")
        if gender:
            higher_churn_gender = max(gender, key=lambda x: x.churn_rate)
            if higher_churn_gender.churn_rate > 20:
                insights.append(
                    ProductInsight(
                        title=f"Gender-Specific Retention Strategy",
                        finding=f"{higher_churn_gender.segment_value} customers "
                        f"have a {higher_churn_gender.churn_rate}% churn rate.",
                        affected_segment=f"{higher_churn_gender.customer_count:,} "
                        f"{higher_churn_gender.segment_value.lower()} customers",
                        recommendation="Conduct customer research to understand "
                        "gender-specific needs and preferences. "
                        "Develop targeted marketing and product features.",
                        expected_impact="3-5% churn reduction through personalization",
                        implementation_effort="MEDIUM",
                    )
                )

        return insights

    def generate_full_report(self) -> Dict[str, Any]:
        """
        Generate a comprehensive report with all insights.

        Returns:
            Dictionary containing executive summary, executive insights,
            and product insights.
        """
        self._ensure_initialized()

        executive_summary = self.generate_executive_summary()
        executive_insights = self.generate_executive_insights()
        product_insights = self.generate_product_insights()

        return {
            "report_metadata": {
                "generated_at": datetime.now().isoformat(),
                "dataset_info": self.data_loader.get_feature_info(),
            },
            "executive_summary": executive_summary,
            "executive_insights": [
                {
                    "title": i.title,
                    "summary": i.summary,
                    "key_metric": i.key_metric,
                    "business_impact": i.business_impact,
                    "priority": i.priority,
                }
                for i in executive_insights
            ],
            "product_insights": [
                {
                    "title": i.title,
                    "finding": i.finding,
                    "affected_segment": i.affected_segment,
                    "recommendation": i.recommendation,
                    "expected_impact": i.expected_impact,
                    "implementation_effort": i.implementation_effort,
                }
                for i in product_insights
            ],
            "detailed_analytics": {
                "geography_analysis": [
                    {
                        "segment": s.segment_value,
                        "churn_rate": s.churn_rate,
                        "customer_count": s.customer_count,
                        "risk_level": s.risk_level,
                    }
                    for s in self._analytics.analyze_segment("Geography")
                ],
                "age_analysis": [
                    {
                        "segment": s.segment_value,
                        "churn_rate": s.churn_rate,
                        "customer_count": s.customer_count,
                        "risk_level": s.risk_level,
                    }
                    for s in self._analytics.get_age_group_analysis()
                ],
                "product_analysis": [
                    {
                        "segment": s.segment_value,
                        "churn_rate": s.churn_rate,
                        "customer_count": s.customer_count,
                        "risk_level": s.risk_level,
                    }
                    for s in self._analytics.get_product_usage_analysis()
                ],
                "churned_vs_retained": self._analytics.get_churned_vs_retained_comparison(),
                "correlations": self._analytics.get_correlation_analysis(),
            },
        }

    def print_executive_summary(self) -> None:
        """Print a formatted executive summary to console."""
        summary = self.generate_executive_summary()

        print("\n" + "=" * 60)
        print("EXECUTIVE SUMMARY - CUSTOMER CHURN ANALYSIS")
        print("=" * 60)
        print(f"\nReport Date: {summary['report_date'][:10]}")

        print("\n📊 OVERVIEW")
        print("-" * 40)
        overview = summary["overview"]
        print(f"Total Customers: {overview['total_customers']:,}")
        print(f"Churn Rate: {overview['churn_rate']}")
        print(f"Churned Customers: {overview['churned_customers']:,}")
        print(f"Retained Customers: {overview['retained_customers']:,}")

        print("\n💰 FINANCIAL IMPACT")
        print("-" * 40)
        financial = summary["financial_impact"]
        print(f"Estimated Revenue at Risk: {financial['estimated_revenue_at_risk']}")
        print(f"Average Customer Value: {financial['avg_customer_value']}")

        print("\n⚠️ KEY RISK INDICATORS")
        print("-" * 40)
        for risk in summary["key_risk_indicators"]:
            print(f"  • {risk['dimension']}: {risk['segment']} - "
                  f"{risk['churn_rate']} ({risk['affected_customers']:,} customers)")

        print("\n📈 TOP CHURN FACTORS")
        print("-" * 40)
        for factor in summary["top_churn_correlations"]:
            print(f"  • {factor['factor']}: {factor['correlation']:.4f}")

        print("\n" + "=" * 60)

    def print_insights(self) -> None:
        """Print formatted insights for executives and product managers."""
        exec_insights = self.generate_executive_insights()
        prod_insights = self.generate_product_insights()

        print("\n" + "=" * 60)
        print("EXECUTIVE INSIGHTS")
        print("=" * 60)

        for i, insight in enumerate(exec_insights, 1):
            priority_emoji = "🔴" if insight.priority == "HIGH" else (
                "🟡" if insight.priority == "MEDIUM" else "🟢"
            )
            print(f"\n{i}. {priority_emoji} {insight.title}")
            print("-" * 50)
            print(f"Summary: {insight.summary}")
            print(f"Key Metric: {insight.key_metric}")
            print(f"Business Impact: {insight.business_impact}")
            print(f"Priority: {insight.priority}")

        print("\n" + "=" * 60)
        print("PRODUCT MANAGER INSIGHTS")
        print("=" * 60)

        for i, insight in enumerate(prod_insights, 1):
            effort_emoji = "⬆️" if insight.implementation_effort == "HIGH" else (
                "➡️" if insight.implementation_effort == "MEDIUM" else "⬇️"
            )
            print(f"\n{i}. {effort_emoji} {insight.title}")
            print("-" * 50)
            print(f"Finding: {insight.finding}")
            print(f"Affected Segment: {insight.affected_segment}")
            print(f"Recommendation: {insight.recommendation}")
            print(f"Expected Impact: {insight.expected_impact}")
            print(f"Implementation Effort: {insight.implementation_effort}")

        print("\n" + "=" * 60)
