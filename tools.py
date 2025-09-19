## Importing libraries and files
import os
import re
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader

from crewai_tools.tools.serper_dev_tool import SerperDevTool

load_dotenv()

# -------------------------------
# Creating search tool
# -------------------------------
search_tool = SerperDevTool()

# -------------------------------
# Custom PDF Reader Tool
# -------------------------------
class FinancialDocumentTool:
    @staticmethod
    def read_data_tool(path: str = "data/sample.pdf") -> str:
        """Read and clean financial document data from a PDF file.

        Args:
            path (str): Path of the pdf file. Defaults to 'data/sample.pdf'.

        Returns:
            str: Cleaned full financial document content.
        """
        loader = PyPDFLoader(path)
        docs = loader.load()

        full_report = ""
        for data in docs:
            content = data.page_content
            # Normalize whitespace
            content = re.sub(r"\n\s*\n", "\n", content)
            content = re.sub(r"\s{2,}", " ", content)
            full_report += content.strip() + "\n"

        return full_report

# -------------------------------
# Investment Analysis Tool
# -------------------------------
class InvestmentTool:
    @staticmethod
    def analyze_investment_tool(financial_document_data: str) -> str:
        """Stub for investment analysis.

        Args:
            financial_document_data (str): Extracted financial document text.

        Returns:
            str: Investment insights (currently placeholder).
        """
        cleaned_data = re.sub(r"\s{2,}", " ", financial_document_data).strip()
        # TODO: Implement proper financial analysis logic here
        return "Investment analysis functionality to be implemented"

# -------------------------------
# Risk Assessment Tool
# -------------------------------
class RiskTool:
    @staticmethod
    def create_risk_assessment_tool(financial_document_data: str) -> str:
        """Stub for risk assessment.

        Args:
            financial_document_data (str): Extracted financial document text.

        Returns:
            str: Risk assessment insights (currently placeholder).
        """
        # TODO: Implement proper risk assessment logic here
        return "Risk assessment functionality to be implemented"
