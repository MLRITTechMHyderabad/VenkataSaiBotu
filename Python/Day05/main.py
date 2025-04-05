import json
import logging
from authorization import LaunchAuthorizationSystem

# Set up logging (console output only)
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',level=logging.INFO)


class Warhead:
    """Represents a nuclear warhead with specific payload information."""
    
    def __init__(self, warhead_id, type, yield_kt):
        self.warhead_id = warhead_id
        self.type = type
        self.yield_kt = yield_kt  # Yield in kilotons

    def get_info(self):
        return f"Warehead {self.warhead_id} : Type {self.type}, Yield {self.yield_kt} kt !"
        
class Submarine:
    """Controls the nuclear missile launch sequence."""
    
    def __init__(self, name, warhead_data):
        self.name = name
        self.warheads = [Warhead(**w) for w in warhead_data]
        self.unauthorized_attempts = 0

    def authorize_launch(self, auth_code):
        """Attempts to authorize and launch a missile."""
        if LaunchAuthorizationSystem.validate_code(auth_code):
            logging.info(f"Launch authorized for {self.name} ")
            warhead = self.warheads[0]
            logging.info(f'Missile launced carrying {warhead.get_info()}')
        else :
            self.unauthorized_attempts += 1
            logging.error("Athorization failed")

        """Simulates launching a missile."""
    
        

# JSON Data (Simulating a warhead payload inventory)
warhead = [
    {"warhead_id": "W001", "type": "Thermonuclear", "yield_kt": 1000},
    {"warhead_id": "W002", "type": "Tactical", "yield_kt": 300}
]


# Load warhead data
warhead_json = json.dumps(warhead)
warhead_data = json.loads(warhead_json)

# Initialize submarine
submarine = Submarine("USS Trident", warhead_data)

# 🚀 Try launching with an incorrect code
submarine.authorize_launch("INVALID-123")

# 🚀 Try launching with a valid code
submarine.authorize_launch("AUTH-XYZ123-4567-SECURE")
