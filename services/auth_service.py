from typing import Optional, Tuple
from models.account import Account
from models.database import BankDatabase
from utils.auth_state import AuthState

class AuthService:
    """Authentication services"""

    def __init__(self, database: BankDatabase):
        self.database = database
        self.current_user: Optional[Account] = None
        self.is_admin = False
        self.auth_state = AuthState.LOGGED_OUT
        self.pending_login_account = Optional[Account] = None

    def initiate_user_login(self, name: str) -> Tuple[bool, str, Optional[Account]]:
        account = self.database.get_account_by_name(name)
        if account:
            if account.is_locked:
                return False, f"Accounted locked", None
            return True, f"Enter password:", account
        return False, f"No account: {name}", None
    
    def verify_password(self, account: Account, password: str) -> Tuple[bool, str]:
        if account.verify_password(password):
            account.failed_login_attempts = 0
            return True, "Password OK. Enter PIN:"
        account.failed_login_attempts += 1
        if account.failed_login_attempts >= 3:
            account.is_locked = True
            return False, " ❌ Locked (3 attempts)"
        return False, f" ❌ Invalid. {3 - account.failed_login_attempts} left"
    
    def verify_pin(self, account: Account, pin: str) -> Tuple[bool, str]:
        if account.verify_pin(pin):
            self.current_user = account
            self.auth_state = AuthState.LOGGED_IN
            self.pending_login_account = None
            return True, f" ✅ Welcome, {account.name}!"
        account.failed_login_attempts += 1
        if account.failed_login_attempts >= 3:
            account.is_locked = True
            return False, "❌ Locked"
        return False, f"❌ Invalid PIN. {3 - account.failed_login_attempts} left"
    

    def login_admin(self, password: str = "admin123") -> Tuple[bool, str]:
        if password == "admin123":
            self.is_admin = True
            self.auth_state = AuthState.LOGGED_IN
            return True, "✅ Admin login OK"
        return False, "❌ Invalid password"
    
    def logout(self) -> str:
        user_name = self.current_user.name if self.current_user else "Admin"
        self.current_user = None
        self.is_admin = False
        self.auth_state = AuthState.LOGGED_OUT
        return f"👋 Goodbye, {user_name}"
    