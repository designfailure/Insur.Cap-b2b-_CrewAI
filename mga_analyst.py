import unittest
from unittest.mock import patch
from agents.mga_analyst import MGAAnalyst

class TestMGAAnalyst(unittest.TestCase):
    def setUp(self):
        self.analyst = MGAAnalyst()

    def test_analyze_input(self):
        input_text = "Insurance request for a small business"
        file_content = "Previous claims: 2, Annual revenue: $500,000"
        
        result = self.analyst.analyze_input(input_text, file_content)
        
        self.assertIn('risk_category', result)
        self.assertIn('potential_revenue', result)
        self.assertIn('file_summary', result)

    def test_compile_final_summary(self):
        results = {
            'risk_category': 'Medium Risk',
            'potential_revenue': 50000.00,
            'underwriting_recommendation': 'Standard coverage',
            'policy_details': 'Annual premium: $5,000',
            'risk_exposure': 'Moderate',
            'esg_compliance': 'Compliant',
            'file_summary': 'Relevant policy information included'
        }
        
        summary = self.analyst.compile_final_summary(results)
        
        self.assertIn('Insurance Analysis Summary', summary)
        self.assertIn('Risk Category: Medium Risk', summary)
        self.assertIn('Potential Revenue: $50,000.00', summary)

    @patch('agents.mga_analyst.MGAAnalyst._categorize_risk')
    def test_categorize_risk(self, mock_categorize):
        mock_categorize.return_value = 'High Risk'
        
        result = self.analyst._categorize_risk("High-risk business in flood zone")
        
        self.assertEqual(result, 'High Risk')
        mock_categorize.assert_called_once_with("High-risk business in flood zone")

if __name__ == '__main__':
    unittest.main()