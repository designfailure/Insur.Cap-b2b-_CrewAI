from crewai import Crew, Task
from agents.mga_analyst import MGAAnalyst
from agents.underwriting import Underwriting
from agents.policy_management import PolicyManagement
from agents.risk_exposure import RiskExposure
from agents.esg_compliance import ESGCompliance
from ui.gradio_interface import create_interface
from logger import main_logger

def create_crew():
    mga_analyst = MGAAnalyst()
    underwriting = Underwriting()
    policy_management = PolicyManagement()
    risk_exposure = RiskExposure()
    esg_compliance = ESGCompliance()

    crew = Crew(
        agents=[mga_analyst, underwriting, policy_management, risk_exposure, esg_compliance],
        tasks=[
            Task(
                description="Analyze the input and categorize the agentic delegation",
                agent=mga_analyst
            ),
            Task(
                description="Evaluate risks and recommend policies",
                agent=underwriting
            ),
            Task(
                description="Draft policy management details",
                agent=policy_management
            ),
            Task(
                description="Outline risk exposure",
                agent=risk_exposure
            ),
            Task(
                description="Assess ESG compliance and carbon risk",
                agent=esg_compliance
            ),
            Task(
                description="Compile final summary",
                agent=mga_analyst
            )
        ]
    )

    return crew

def main():
    main_logger.info("Starting the InsurTech Agentic Workflow System")
    try:
        crew = create_crew()
        interface = create_interface(crew)
        main_logger.info("Launching Gradio interface")
        interface.launch()
    except Exception as e:
        main_logger.error(f"An error occurred while running the system: {str(e)}")
        raise

if __name__ == "__main__":
    main()