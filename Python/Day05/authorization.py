# authorization.py
import re
import json
import logging

# Set up logging (console output only)
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',level=logging.INFO)

class LaunchAuthorizationSystem:
    """Handles nuclear launch authorization validation."""
    
    AUTH_PATTERN = r"^AUTH-[A-Z]{3}\d{3}-\d{4}-SECURE$"# Regex for security code validation

    @staticmethod
    def validate_code(code):
        """Validates the launch authorization code."""
        if re.match(LaunchAuthorizationSystem.AUTH_PATTERN,code) :
            logging.info("Authorization code validated sucessfully..")
            return True
        else :
            logging.warning("Invalid authorization code...!!!")

