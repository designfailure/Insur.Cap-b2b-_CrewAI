# Insur.Cap - Autonomous InsurTech Agentic Workflow System

This project implements an Autonomous InsurTech Agentic Workflow System using CrewAI for orchestration and Gradio for the user interface.

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your environment variables in the `.env` file
4. Run the application: `python main.py`

## System Architecture

The system consists of five main agents:
- MGA Analyst
- Underwriting
- Policy Management
- Risk Exposure
- ESG Compliance

These agents work together to analyze insurance-related queries, assess risks, recommend policies, and provide comprehensive insights.

## Usage

1. Launch the Gradio interface by running `main.py`
2. Enter your query in the text box
3. Optionally upload a file (.csv, .xls, .doc, .pdf)
4. Submit the query to start the analysis process
5. View the results in the output pane

## Extending the System

To add new capabilities:
1. Create new agent classes in the `agents/` directory
2. Implement new tools in the `tools/` directory
3. Update the `create_crew()` function in `main.py` to include new agents and tasks