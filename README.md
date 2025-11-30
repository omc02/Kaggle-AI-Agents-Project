# 🤖 AI-Powered Multi-Agent Banking Customer Churn Analytics Engine
## Use Case: Agentic Executive Intelligence Platform with Gemini-Powered Insights Q&A and Web Search

**Submission Track:** Enterprise Agents | **Dataset:** [Bank Customer Churn Prediction](https://www.kaggle.com/datasets/saurabhbadole/bank-customer-churn-prediction-dataset)

---

## 📋 Project Overview

This project demonstrates an advanced **multi-agent agentic AI system** that transforms raw bank customer churn data into actionable executive insights. Built for the **Enterprise Agents track**, it showcases a production-ready architecture where specialized AI agents autonomously deliver intelligent analysis, combining internal data exploration with external market intelligence.

**Problem Statement:** Data analysis is too manual and time-intensive for executives needing actionable intelligence quickly. Business stakeholders struggle to identify churn patterns and retention strategies from raw datasets.

**Solution:** A sophisticated multi-agent system powered by Google's Gemini LLM that autonomously analyzes multi-dimensional customer data, executes parallel workflows, integrates web search for industry context, and provides natural language Q&A interface tailored for executive decision-making.

---

## 🎯 Key Features & Technologies

### Multi-Agent System Architecture
- **Analytics Agent**: Multi-dimensional churn analysis (geographic, demographic, financial, behavioral)
- **Web Search Agent**: Enriches insights with external market intelligence
- **Gemini LLM Agent**: Orchestrates agents and synthesizes executive-level responses
- **Sequential & Parallel Execution**: Coordinated workflows for depth and breadth

### Core Technologies
- **LLM**: Google Gemini 2.5 Flash with Tool Calling & Grounding API
- **Framework**: Google ADK (Agents Development Kit)
- **Data Processing**: Pandas, NumPy on 10,000 customer records
- **UI**: IPyWidgets-based Jupyter Notebook interface
- **Memory**: InMemorySessionService for conversation state and chat history

### Advanced Capabilities
- Autonomous decision-making on when to use web search
- Real-time data analysis and executive summaries
- Market intelligence with industry benchmarks
- Conversational Q&A with multi-turn dialogue support
- Data-driven recommendations with specific metrics

---

## 📊 Core Analysis Dimensions

- **Executive Summary**: Total customers, churn rate, demographic averages, engagement metrics
- **Geographic Analysis**: Churn rates by region, financial comparisons, high-risk segments
- **Demographic Insights**: Age group and gender-based churn patterns with credit score correlations
- **Product & Engagement**: Churn correlation with products held, tenure patterns, activity levels
- **Risk Segmentation**: Multi-dimensional profiles ranked by churn severity
- **Financial Profiling**: Churned vs. retained customer comparisons, revenue loss calculations
- **Customer Lifetime Value**: Total balance lost, estimated annual revenue impact

---

## 🔧 Technical Architecture

### Data Flow
1. **Data Ingestion**: Bank Customer Churn dataset (10,000 records)
2. **Analysis Execution**: AnalyticsAgent performs autonomous multi-dimensional analysis
3. **Context Preparation**: Formatted insights prepared for LLM processing
4. **Query Processing**: User questions routed through Gemini orchestrator
5. **Optional Web Search**: Churn-relevant queries trigger external research
6. **Response Generation**: Natural language responses with data citations
7. **History Management**: Chat history maintained for multi-turn continuity

### Architecture Components
```
User Query (Natural Language)
        ↓
Gemini 2.5 Flash Orchestrator
        ↓
    ┌───┴───┐
    ↓       ↓
Analytics  Google Search
Agent      Agent
    ↓       ↓
 Pandas    Search
 Data      Results
    └───┬───┘
        ↓
 Response Synthesis
 (InMemorySession)
        ↓
 Executive Output
```

### Technologies Stack
- **Language**: Python 3.x
- **LLM**: `models/gemini-2.5-flash`
- **APIs**: Google Generative AI, Google Search
- **Data**: Pandas, NumPy
- **Interface**: IPyWidgets, Jupyter

---

## 🚀 Usage Examples

### Interactive Chatbot
```python
visual_chatbot = create_visual_chatbot(agent)
```

### Sample Executive Questions
- *"What's our overall churn rate?"* → Executive summary with key metrics
- *"Which geography has the highest churn?"* → Geographic breakdown with comparisons
- *"Who are our high-risk customer segments?"* → Top 5 risk profiles with details
- *"What's the financial impact of churn?"* → Revenue loss calculations
- *"What recommendations would reduce churn?"* → Data-driven action items

### Advanced Queries with Web Search
- *"Compare our churn rate to industry benchmarks"*
- *"What strategies are banks using to reduce churn?"*
- *"Look up retention best practices for our demographics"*

---

## 📈 Key Insights

The system reveals critical patterns:
- **Churn Patterns**: Geographic variations across Spain, France, Germany
- **Risk Profiles**: Female customers, inactive members, and 40-60 age group show elevated churn
- **Product Paradox**: Customers with more products unexpectedly show higher churn
- **Financial Impact**: Significant revenue loss concentrated in specific segments
- **Engagement Gap**: Active members with account activity show dramatically lower churn

---

## 🎓 Learning Outcomes & Agent Concepts Demonstrated

This project successfully demonstrates **4+ key concepts** from the Google AI Agents Intensive Course:

1. ✅ **Multi-Agent System**: Analytics, Web Search, and LLM orchestrator agents working in coordinated workflows
2. ✅ **LLM-Powered Agents**: Gemini-powered decision-making and natural language generation
3. ✅ **Tools Integration**: Custom analytics functions, Google Search grounding, and function-based tool execution
4. ✅ **Sessions & Memory**: InMemorySessionService for conversation state and chat history persistence
5. ✅ **Context Engineering**: Sophisticated data preparation and context formatting for optimal LLM performance

---

## 📂 Project Structure

```
capstone_notebook.ipynb          # Main Jupyter notebook with full implementation
├── Data Loading & Exploration   # Section 3: Bank Customer Churn dataset
├── AnalyticsAgent Class         # Section 4: Multi-dimensional analysis engine
├── Agent Initialization         # Section 5: Agent setup and basic Q&A
├── Interactive Demonstrations   # Section 6: Example queries
├── Visual Chatbot Interface     # Section 7-8: Jupyter widgets UI with web search
└── Advanced Examples            # Section 9: Complex query templates

README.md                         # This file
```

---

## 🔐 Authentication & Setup

The project uses Kaggle Secrets for secure API key management:
- Requires `GOOGLE_API_KEY` in Kaggle notebook secrets
- Automatically configures Google Generative AI on notebook startup
- Graceful fallback for unavailable APIs (simulated responses)

---

## 📝 Output Format

All responses are formatted for executive consumption with:
- Clear section headers (📊 📈 ⚠️ 💡 🎯 💰)
- Specific data citations and percentages
- Bullet-point summaries
- Actionable recommendations
- Professional formatting with strategic emphasis

---

## 🤝 Extensibility & Future Enhancements

The agent architecture is designed for extension:
- **Additional Data Sources**: Easy integration of new datasets
- **Custom Tools**: Add domain-specific analysis functions
- **Multi-Language Support**: Expand to multiple languages
- **Report Generation**: Automated PDF/PowerPoint executive reports
- **Scheduled Analysis**: Periodic churn analysis and alerts
- **Feedback Loop**: Agent refinement based on user satisfaction
- **A2A Protocol**: Agent-to-agent communication for distributed analysis

---

## 📄 Submission Details

- **Track**: Enterprise Agents (Business workflow automation & data analysis)
- **Dataset**: Bank Customer Churn Prediction (Kaggle)
- **LLM**: Google Gemini 2.5 Flash
- **Framework**: Google ADK (Agents Development Kit)
- **Interface**: Jupyter Notebook with Interactive Widgets
- **Status**: Complete & Production-Ready

---

## ✨ Highlights

🎯 **Autonomous Insight Generation**: Agents automatically analyze multi-dimensional data without manual intervention

🌐 **Web-Enriched Intelligence**: Optional market research integration provides industry context

💬 **Natural Language Interface**: Executive-friendly Q&A with multi-turn conversation support

📊 **Data-Driven Decisions**: All recommendations backed by specific metrics and analysis

🚀 **Enterprise-Ready Architecture**: Scalable, maintainable, production-ready system design

---

**Created by:** Omar Chehab  
**Date:** November 30, 2025  
**Version:** 1.0  
**Course:** Kaggle Google AI Agents Intensive - 5-Day Program
