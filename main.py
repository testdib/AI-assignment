## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()

from crewai import LLM
from crewai.agents import Agent
from tools import search_tool, FinancialDocumentTool

# -------------------------------
# Load the LLM (fix: define properly)
# -------------------------------
llm = LLM(model="gpt-4", temperature=0)  # adjust model as needed

# -------------------------------
# Financial Analyst Agent
# -------------------------------
financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal="Analyze uploaded financial documents and extract accurate, structured insights such as revenue, expenses, profits, cash flow, and key ratios.",
    verbose=True,
    memory=True,
    backstory=(
        "You are a seasoned financial analyst with years of experience in reviewing "
        "financial reports, balance sheets, and market filings. You carefully evaluate "
        "the numbers, highlight important findings, and always provide factual analysis."
    ),
    tools=[FinancialDocumentTool.read_data_tool],
    llm=llm,
    max_iter=2,
    max_rpm=1,
    allow_delegation=False
)

# -------------------------------
# Financial Document Verifier Agent
# -------------------------------
verifier = Agent(
    role="Financial Document Verifier",
    goal="Verify the authenticity and completeness of financial documents, ensuring that the format, content, and required fields are valid.",
    verbose=True,
    memory=True,
    backstory=(
        "You worked in financial compliance and are skilled at document verification. "
        "You carefully check whether uploaded documents are valid financial records, "
        "such as balance sheets, income statements, or annual reports."
    ),
    llm=llm,
    max_iter=2,
    max_rpm=1,
    allow_delegation=False
)

# -------------------------------
# Investment Advisor Agent
# -------------------------------
investment_advisor = Agent(
    role="Investment Advisor",
    goal="Based on verified financial analysis, suggest responsible and risk-adjusted investment strategies aligned with the client’s goals.",
    verbose=True,
    memory=True,
    backstory=(
        "You are a certified financial advisor with extensive experience helping clients "
        "navigate markets. You recommend diversified, well-researched investment "
        "strategies while adhering to compliance and best practices."
    ),
    llm=llm,
    max_iter=2,
    max_rpm=1,
    allow_delegation=False
)

# -------------------------------
# Risk Assessor Agent
# -------------------------------
risk_assessor = Agent(
    role="Risk Assessment Expert",
    goal="Identify potential risks in financial documents and assess the level of exposure, volatility, and regulatory concerns.",
    verbose=True,
    memory=True,
    backstory=(
        "You specialize in financial risk management. You evaluate liquidity risks, "
        "market volatility, credit risks, and operational risks to provide a balanced "
        "assessment for decision-making."
    ),
    llm=llm,
    max_iter=2,
    max_rpm=1,
    allow_delegation=False
)
