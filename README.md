Bugs Found and Fixes

During development, several issues were identified:

1. llm = llm Bug

Problem: The code attempted to assign llm = llm, which caused NameError: name 'llm' is not defined.

Fix: Load an actual LLM instance. Example:
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
2. Wrong Keyword Argument (tool vs tools)

Problem: Agents were initialized with tool=[...].

Fix: Changed to the correct parameter tools=[...].
3. Backstory/Goal String Concatenation

Problem: Strings were split across multiple lines without spaces, causing unintended concatenation.

Fix: Used triple-quoted strings (""" ... """) or explicit spacing.
4. Inconsistent Agent Configs

Problem: Some agents had memory=True, others didn’t; delegation was inconsistently set.

Fix: Made configs consistent and documented purpose:

memory=True for stateful agents (analyst, verifier).

allow_delegation=True only where inter-agent task handoff is allowed.
 Setup Instructions
1. Clone Repository
   git clone https://github.com/yourusername/financial-document-ai-crew.git
cd financial-document-ai-crew
2. Create Virtual Environment
   python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
3. Install Dependencies
   pip install -r requirements.txt
crewai
langchain
langchain-openai
python-dotenv
pypdf
4. Setup Environment Variables

Create a .env file in the root:
OPENAI_API_KEY=your_openai_api_key_here
5. Run Example
python main.py
Usage

1.Place your financial documents (PDFs) in the data/ folder.

2. Use the FinancialDocumentTool to load data:
   report = await FinancialDocumentTool.read_data_tool("data/sample.pdf")
3. Assign tasks to agents:
   from crewai import Task, Crew

task = Task(
    description="Analyze uploaded financial document for risks",
    expected_output="Detailed (but not reliable) risk assessment",
    agent=risk_assessor
)

crew = Crew(agents=[financial_analyst, investment_advisor, verifier, risk_assessor],
            tasks=[task],
            verbose=True)

result = crew.kickoff()
print(result)
API Documentation
FinancialDocumentTool

Custom tool to extract text from PDFs.
await FinancialDocumentTool.read_data_tool(path: str = "data/sample.pdf") -> str
Args:

path: Path to the PDF file. Default = "data/sample.pdf".

Returns:

A cleaned string containing the full text of the financial document.
InvestmentTool

Placeholder for investment logic.
await InvestmentTool.analyze_investment_tool(financial_document_data: str) -> str
Args:

financial_document_data: Extracted document text.

Returns:

"Investment analysis functionality to be implemented" (currently stub).
RiskTool

Placeholder for risk assessment logic.
await RiskTool.create_risk_assessment_tool(financial_document_data: str) -> str
Args:

financial_document_data: Extracted document text.

Returns:

"Risk assessment functionality to be implemented" (currently stub).
Agent Roles

financial_analyst → Makes bold, dramatic predictions.

verifier → Confirms everything is a financial doc.

investment_advisor → Always sells risky products.

risk_assessor → Declares everything as extreme risk.
