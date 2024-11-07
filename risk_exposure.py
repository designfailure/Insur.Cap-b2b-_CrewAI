import logging
from crewai import Agent
from typing import Dict, Any, List

class RiskExposure(Agent):
    def __init__(self):
        super().__init__(
            role="Risk Exposure",
            goal="Measure and calculate the underwritten coverage and policy premium portfolio exposed",
            backstory="You are an expert in nurturing the risk exposure of the underwriter portfolio."
        )
        self.logger = logging.getLogger(__name__)

    def calculate_portfolio_exposure(self, portfolio_data: List[Dict[str, Any]]) -> Dict[str, float]:
        self.logger.info("Calculating portfolio exposure")
        try:
            total_exposure = sum(policy["coverage_amount"] for policy in portfolio_data)
            max_single_exposure = max(policy["coverage_amount"] for policy in portfolio_data)
            avg_exposure = total_exposure / len(portfolio_data) if portfolio_data else 0

            exposure_data = {
                "total_exposure": total_exposure,
                "max_single_exposure": max_single_exposure,
                "average_exposure": avg_exposure
            }
            self.logger.info("Portfolio exposure calculated successfully")
            return exposure_data
        except Exception as e:
            self.logger.error(f"Error during portfolio exposure calculation: {str(e)}")
            raise

    def analyze_risk_factors(self, policy_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        self.logger.info("Analyzing risk factors")
        try:
            risk_factors = [
                self._assess_geographic_risk(policy_data),
                self._assess_industry_risk(policy_data),
                self._assess_claims_history(policy_data),
                self._assess_coverage_limits(policy_data)
            ]
            self.logger.info("Risk factors analyzed successfully")
            return risk_factors
        except Exception as e:
            self.logger.error(f"Error during risk factor analysis: {str(e)}")
            raise

    def generate_risk_report(self, exposure_data: Dict[str, float], risk_factors: List[Dict[str, Any]]) -> str:
        self.logger.info("Generating risk report")
        try:
            report = f"""
            Risk Exposure Report

            Portfolio Exposure:
            - Total Exposure: ${exposure_data['total_exposure']:,.2f}
            - Maximum Single Exposure: ${exposure_data['max_single_exposure']:,.2f}
            - Average Exposure: ${exposure_data['average_exposure']:,.2f}

            Risk Factors:
            """
            for factor in risk_factors:
                report += f"- {factor['name']}: {factor['level']} (Score: {factor['score']})\n"
                report += f"  {factor['description']}\n\n"

            overall_risk_score = sum(factor['score'] for factor in risk_factors) / len(risk_factors)
            report += f"\nOverall Risk Score: {overall_risk_score:.2f} out of 5.00"

            self.logger.info("Risk report generated successfully")
            return report
        except Exception as e:
            self.logger.error(f"Error during risk report generation: {str(e)}")
            raise

    def _assess_geographic_risk(self, policy_data: Dict[str, Any]) -> Dict[str, Any]:
        # Implement geographic risk assessment logic
        location = policy_data.get("location", "").lower()
        if "flood zone" in location:
            return {"name": "Geographic Risk", "level": "High", "score": 4.5, "description": "Property located in a flood zone"}
        elif "coastal area" in location:
            return {"name": "Geographic Risk", "level": "Medium", "score": 3.0, "description": "Property in a coastal area with potential hurricane exposure"}
        else:
            return {"name": "Geographic Risk", "level": "Low", "score": 1.5, "description": "Property in a low-risk geographic area"}

    def _assess_industry_risk(self, policy_data: Dict[str, Any]) -> Dict[str, Any]:
        # Implement industry risk assessment logic
        industry = policy_data.get("industry", "").lower()
        if industry in ["construction", "manufacturing"]:
            return {"name": "Industry Risk", "level": "High", "score": 4.0, "description": "High-risk industry with potential for workplace accidents"}
        elif industry in ["retail", "hospitality"]:
            return {"name": "Industry Risk", "level": "Medium", "score": 3.0, "description": "Medium-risk industry with moderate liability exposure"}
        else:
            return {"name": "Industry Risk", "level": "Low", "score": 2.0, "description": "Low-risk industry with minimal liability concerns"}

    def _assess_claims_history(self, policy_data: Dict[str, Any]) -> Dict[str, Any]:
        # Implement claims history assessment logic
        claims_count = policy_data.get("previous_claims", 0)
        if claims_count > 3:
            return {"name": "Claims History", "level": "High", "score": 4.5, "description": "Multiple claims in recent history"}
        elif claims_count > 0:
            return {"name": "Claims History", "level": "Medium", "score": 3.0, "description": "Some claims in recent history"}
        else:
            return {"name": "Claims History", "level": "Low", "score": 1.0, "description": "No recent claims history"}

    def _assess_coverage_limits(self, policy_data: Dict[str, Any]) -> Dict[str, Any]:
        # Implement coverage limits assessment logic
        coverage_amount = policy_data.get("coverage_amount", 0)
        if coverage_amount > 1000000:
            return {"name": "Coverage Limits", "level": "High", "score": 4.0, "description": "High coverage limits increase potential exposure"}
        elif coverage_amount > 500000:
            return {"name": "Coverage Limits", "level": "Medium", "score": 3.0, "description": "Moderate coverage limits with balanced exposure"}
        else:
            return {"name": "Coverage Limits", "level": "Low", "score": 2.0, "description": "Low coverage limits minimize potential exposure"}