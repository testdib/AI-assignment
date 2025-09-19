## Importing libraries and files
from crewai import Task

from agents import financial_analyst, verifier, investment_advisor, risk_assessor
from tools import FinancialDocumentTool

# -------------------------------
# Task: Analyze Financial Document
# -------------------------------
analyze_financial_document = Task(
    description=(
        "Analyze the uploaded financial document in detail. "
        "Extract key insights such as revenue, expenses, profit, cash flow, liabilities, and ratios. "
        "Summarize the financial health of the company clearly and accurately."
    ),
    expected_output=(
        "A structured report with:\n"
        "- Income statement highlights\n"
        "- Balance sheet key items\n"
        "- Cash flow summary\n"
        "- Important ratios (profitability, liquidity, leverage)\n"
        "- Short conclusion about overall financial position"
    ),
    agent=financial_analyst,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False,
)

# -------------------------------
# Task: Investment Analysis
# -------------------------------
investment_analysis = Task(
    description=(
        "Based on the verified financial data, suggest potential investment opportunities. "
        "Identify strengths and weaknesses of the company. "
        "Provide recommendations such as buy, hold, or sell, with reasoning."
    ),
    expected_output=(
        "Investment recommendation that includes:\n"
        "- Summary of financial performance\n"
        "- Key opportunities and risks\n"
        "- Suggested strategy (buy/sell/hold)\n"
        "- Long-term and short-term outlook"
    ),
    agent=investment_advisor,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False,
)

# -------------------------------
# Task: Risk Assessment
# -------------------------------
risk_assessment = Task(
    description=(
        "Perform a financial risk assessment based on the company’s financial statements. "
        "Evaluate market, credit, operational, and liquidity risks. "
        "Highlight any red flags that may impact investors or stakeholders."
    ),
    expected_output=(
        "Risk assessment report with:\n"
        "- Identified risks (market, credit, liquidity, operational)\n"
        "- Severity of each risk (low/medium/high)\n"
        "- Possible mitigations\n"
        "- Overall risk rating"
    ),
    agent=risk_assessor,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False,
)

# -------------------------------
# Task: Verification
# -------------------------------
verification = Task(
    description=(
        "Verify whether the uploaded file is a valid financial document. "
        "Check for presence of balance sheets, income statements, or other standard financial sections. "
        "Confirm if the document meets the expected structure."
    ),
    expected_output=(
        "Verification status (Valid / Invalid financial document), "
        "with a short explanation of reasoning."
    ),
    agent=verifier,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False,
)

