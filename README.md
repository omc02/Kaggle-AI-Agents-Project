# 🤖 Multi-Agent Intelligent Insights Engine: Bank Customer Churn Analytics
## Subtitle: Executive Intelligence Platform with Gemini-Powered Q&A and Web Search Integration

**Submission Track:** Enterprise Agents

---

## 📦 Data Source

- **Dataset**: [Bank Customer Churn Prediction Dataset](https://www.kaggle.com/datasets/saurabhbadole/bank-customer-churn-prediction-dataset)
- **Source**: Kaggle

---

## 📋 Project Overview

This project demonstrates an advanced **multi-agent agentic AI system** that transforms raw bank customer churn data into actionable executive insights. Built for the **Enterprise Agents track**, it showcases a production-ready architecture where specialized AI agents work autonomously to deliver intelligent analysis, combining internal data exploration with external market intelligence through web search capabilities.

**Problem Statement:**
Data analysis and insights generation is too manual and time-intensive for executives who need actionable intelligence quickly. Business stakeholders struggle to identify churn patterns, risk segments, and retention strategies from raw datasets. This project solves this by building an AI-powered agent system that automates comprehensive analysis while enabling real-time market context through intelligent web search, allowing executives to get data-driven insights with industry benchmarks.

**Solution:**
A sophisticated multi-agent system powered by Google's Gemini LLM that autonomously:
- Analyzes multi-dimensional customer churn data (geographic, demographic, financial, behavioral)
- Executes parallel and sequential agent workflows for specialized analysis
- Integrates web search to enrich insights with industry trends and benchmarks
- Provides natural language Q&A interface tailored for executive decision-making
- Maintains context and conversation history for multi-turn dialogue

---

## 🎯 Key Features & Technologies Implemented

### 1. **Multi-Agent System Architecture**
- **Analytics Agent**: Autonomous engine performing multi-dimensional churn analysis
- **Web Search Agent**: Secondary agent enriching insights with external market intelligence (optional activation)
- **Gemini LLM Agent**: Orchestrator synthesizing insights and generating executive-level natural language responses
- **Sequential & Parallel Execution**: Agents coordinate to maximize analysis depth and breadth

### 2. **Tools & Integration**
- **Custom Analytics Tools**: Python-based functions for geographic, demographic, financial, and risk analysis
- **Google Search Integration**: Web search grounding with Gemini for industry benchmarks and trends
- **Function Tools**: Custom data transformation and insight generation functions
- **API Integration**: Google Generative AI (Gemini 2.5 Flash) for LLM capabilities

### 3. **Sessions & Memory Management**
- **InMemorySessionService**: Maintains conversation state and chat history across interactions
- **Context Engineering**: Intelligent data preparation for optimal LLM processing
- **State Persistence**: Preserves agent insights and analysis results for consistent multi-turn dialogue
- **Chat History Tracking**: Records all user questions and agent responses for audit and refinement

### 4. **Advanced Agent Capabilities**
- **Autonomous Decision-Making**: Agents decide when to use web search based on query relevance
- **Real-time Data Analysis**: On-demand generation of executive summaries and risk assessments
- **Market Intelligence**: Web search capability filtered for churn-related industry insights
- **Conversational Q&A**: Natural language interface supporting complex business questions
- **Data-Driven Recommendations**: Actionable insights with specific numbers and percentages

### 5. **Executive-Level Interface**
- **Visual Chatbot**: Jupyter widgets-based UI with real-time chat and quick-access buttons
- **Web Search Toggle**: Users can enable/disable external research per query
- **Formatted Responses**: Color-coded messages and professional formatting for executive consumption
- **Interactive Exploration**: Quick buttons for common analyses (churn rate, risk segments, recommendations)

---

## 📊 Core Analysis Dimensions

### Executive Summary
- Total customers, churn rate, demographic averages, account metrics
- Active member rates and credit card holder distributions

### Geographic Analysis
- Churn rates by country/region
- Financial metrics comparison across geographies
- High-risk geographic segments

### Demographic Insights
- Churn patterns by age group (<30, 30-40, 40-50, 50-60, 60+)
- Gender-based churn analysis with credit score correlations
- Age-gender interaction effects

### Product & Engagement Analysis
- Churn correlation with number of products held
- Customer tenure patterns by product count
- Active vs. inactive member engagement levels

### Risk Segmentation
- High-risk customer profile identification
- Multi-dimensional segmentation (geography × gender × activity status)
- Ranking of segments by churn severity

### Financial Profiling
- Comparison of churned vs. retained customer profiles
- Balance, credit score, and salary analysis
- Zero-balance identification for inactive segments

### Customer Lifetime Value Impact
- Total balance lost to churn
- Estimated annual revenue loss calculation
- Average tenure of churned customers

---

## 🔧 Technical Implementation

### Architecture Components
```
┌─────────────────────────────────────────────────────────────┐
│              Executive Query Interface                      │
│        (Jupyter Widgets Chatbot with Web Search Toggle)     │
└──────────────────┬──────────────────────────────────────────┘
                   │
┌──────────────────▼──────────────────────────────────────────┐
│         Gemini LLM Orchestrator Agent                       │
│  (Synthesizes insights & generates natural language)        │
└──────────────────┬──────────────────────────────────────────┘
                   │
        ┌──────────┴──────────┐
        │                     │
┌───────▼────────────┐  ┌─────▼──────────────────┐
│ Analytics Agent    │  │ Web Search Agent       │
│ (Data Analysis)    │  │ (Market Intelligence)  │
└────────────────────┘  └────────────────────────┘
        │                     │
┌───────▼────────────┐  ┌─────▼──────────────────┐
│ Insights Database  │  │ External Search Index  │
│ (Processed Data)   │  │ (Industry Trends)      │
└────────────────────┘  └────────────────────────┘
```

### Data Flow
1. **Data Ingestion**: Bank Customer Churn dataset (10,000 records)
2. **Analysis Execution**: AnalyticsAgent performs autonomous multi-dimensional analysis
3. **Context Preparation**: Formatted insights prepared for LLM processing
4. **Query Processing**: User questions routed through Gemini orchestrator
5. **Optional Web Search**: Queries analyzed for churn-relevance; searches executed if relevant
6. **Response Generation**: Natural language responses with data citations
7. **History Management**: All interactions stored in chat history for continuity

### Technologies Used
- **LLM**: Google Gemini 2.5 Flash (`models/gemini-2.5-flash`)
- **Frameworks**: Google ADK (Agents Development Kit)
- **Data Processing**: Pandas, NumPy
- **UI**: IPyWidgets (Jupyter Notebook Interface)
- **API**: Google Generative AI, Google Search (via Gemini Grounding)
- **Language**: Python 3.x

---

## 🚀 Usage Examples

### Quick Start: Interactive Chatbot
```python
# Create and launch the visual chatbot
visual_chatbot = create_visual_chatbot(agent)
```

### Sample Questions
- **"What's our overall churn rate?"** → Executive summary with key metrics
- **"Which geography has the highest churn?"** → Geographic analysis with comparisons
- **"Who are our high-risk customer segments?"** → Top 5 risk profiles with details
- **"What's the financial impact of churn?"** → Revenue loss calculations
- **"What recommendations would reduce churn?"** → Data-driven action items

### Advanced Queries with Web Search
Enable the web search toggle for questions like:
- *"Compare our churn rate to industry benchmarks"*
- *"What strategies are banks using to reduce churn?"*
- *"Look up retention best practices for our high-risk demographics"*

---

## 📈 Key Insights from Analysis

The system analyzes the Bank Customer Churn dataset to reveal:
- **Churn Patterns**: Geographic variations (Spain, France, Germany show different patterns)
- **Risk Profiles**: Female customers, inactive members, and 40-60 age group show elevated churn
- **Product Paradox**: Customers with more products unexpectedly show higher churn (potential friction point)
- **Financial Impact**: Significant revenue loss concentrated in specific demographic segments
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
