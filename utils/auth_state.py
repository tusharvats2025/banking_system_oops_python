from enum import Enum

class AuthState(Enum):
    """Authentication flow states"""

    LOGGED_OUT ="logged_out"
    AWAITING_PASSWORD = "awaiting_password"
    AWAITING_PIN = "awaiting_pin"
    LOGGED_IN = "logged_in"
    