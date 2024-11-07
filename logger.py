import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(name, log_file, level=logging.INFO):
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s: %(message)s')

    handler = RotatingFileHandler(log_file, maxBytes=10*1024*1024, backupCount=5)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

# Set up loggers for each component
mga_analyst_logger = setup_logger('mga_analyst', 'logs/mga_analyst.log')
underwriting_logger = setup_logger('underwriting', 'logs/underwriting.log')
policy_management_logger = setup_logger('policy_management', 'logs/policy_management.log')
risk_exposure_logger = setup_logger('risk_exposure', 'logs/risk_exposure.log')
esg_compliance_logger = setup_logger('esg_compliance', 'logs/esg_compliance.log')
main_logger = setup_logger('main', 'logs/main.log')

# Ensure the logs directory exists
os.makedirs('logs', exist_ok=True)