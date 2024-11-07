import unittest
from crewai import Crew, Task
from agents.mga_analyst import MGAAnalyst
from agents.underwriting import Underwriting
from agents.policy_management import PolicyManagement
from agents.risk_exposure import RiskExposure
from agents.esg_compliance import ESGCompliance

class TestInsurTechSystem(unittest.TestCase):
    def setUp(self):
        self.mga_analyst = MGAAnalyst()
        self.underwriting = Underwriting()
        self.policy_management = PolicyManagement()
        self.risk_exposure = RiskExposure()
        self.esg_compliance = ESGCompliance()

        self.crew = Crew(
            agents=[self.mga_analyst, self.underwriting, self.policy_management, self.risk_exposure, self.esg_compliance],
            tasks=[
                Task(
                    description="Analyze the input and categorize the agentic delegation",
                    agent=self.mga_analyst
                ),
                Task(
                    description="Evaluate risks and recommend policies",
                    agent=self.underwriting
                ),
                Task(
                    description="Draft policy management details",
                    agent=self.policy_management
                ),
                Task(
                    description="Outline risk exposure",
                    agent=self.risk_exposure
                ),
                Task(