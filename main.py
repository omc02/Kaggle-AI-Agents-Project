#!/usr/bin/env python3
"""
Main entry point for the Bank Customer Churn Insights Agent.

This script provides a command-line interface for generating insights
from the Bank Customer Churn Prediction dataset.
"""

import argparse
import json
import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from src.insights_agent import InsightsAgent


def main():
    """Main entry point for the insights agent."""
    parser = argparse.ArgumentParser(
        description="AI Agent for Bank Customer Churn Insights",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py                           # Print summary and insights
  python main.py --data-path data.csv      # Use custom data file
  python main.py --output report.json      # Save full report to JSON
  python main.py --format json             # Output as JSON to console
        """,
    )

    parser.add_argument(
        "--data-path",
        type=str,
        help="Path to the CSV data file. If not provided, "
        "will attempt to download from Kaggle.",
    )

    parser.add_argument(
        "--output",
        type=str,
        help="Path to save the full report as JSON file.",
    )

    parser.add_argument(
        "--format",
        choices=["text", "json"],
        default="text",
        help="Output format (default: text)",
    )

    parser.add_argument(
        "--summary-only",
        action="store_true",
        help="Print only the executive summary, not detailed insights.",
    )

    args = parser.parse_args()

    try:
        print("🚀 Initializing Bank Customer Churn Insights Agent...")
        agent = InsightsAgent(data_path=args.data_path)
        agent.initialize()
        print("✅ Data loaded successfully!\n")

        if args.output:
            # Generate and save full report
            print(f"📝 Generating full report...")
            report = agent.generate_full_report()

            output_path = Path(args.output)
            with open(output_path, "w") as f:
                json.dump(report, f, indent=2, default=str)

            print(f"✅ Report saved to {output_path}")

        if args.format == "json":
            # Output as JSON
            report = agent.generate_full_report()
            print(json.dumps(report, indent=2, default=str))
        else:
            # Output as formatted text
            agent.print_executive_summary()

            if not args.summary_only:
                agent.print_insights()

    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
        print("\nPlease provide a valid data file path or configure Kaggle credentials.")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
