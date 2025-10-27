import hashlib
from datetime import datetime
from typing import List, Dict, Any

class Account:
    """Bank account with security and transactions"""
    def __init__(self, account_id: str, name: str, password: str, pin: str, balance: float = 0.0):
        self.account_id = account_id
        self.name = name
        self.password_hash = self._hash(password)
        self.pin_hash = self._hash(pin)
        self.transactions: List[Dict[str, Any]] = []
        self.created_at = datetime.now()
        self.failed_login_attempts = 0
        self.is_locked = False

    @staticmethod
    def _hash(text: str) -> str:
        return hashlib.sha256(text.encode()).hexdigest()
    
    @staticmethod
    def verify_password(self, password: str) -> bool:
        return self.password_hash == self._hash(password)
    
    @staticmethod
    def verify_pin(self, pin: str) -> bool:
        return self.pin_hash == self._hash(pin)
    
    def add_transaction(self, trans_type: str, amount: float, desc : str = ""):
        self.transactions.append({
            "type":trans_type,
            "amount": amount,
            "description" : desc,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "balance_after": self.balance
        })

    def deposit(self, amount: float) -> bool:
        if amount <= 0:
            return False
        self.balance += amount
        self.add_transaction("DEPOSIT", amount, "Deposited")
        return True
    
    def withdraw(self, amount: float) -> bool:
        if amount <= 0 or amount > self.balance:
            return False
        
        self.balance -= amount
        self.add_transaction("WITHDRAWL", amount, "Withdraw")
        return True
    
    def transfer(self, to_account: 'Account', amount: float) -> bool:
        if amount <= 0 or amount > self.balance:
            return False
        self.balance -= amount
        to_account.balance += amount
        self.add_transaction("TRANSFER_OUT", amount, f"To {to_account.name}")
        to_account.add_transaction("TRANSFER_IN", amount, f"From {self.name}")
        return True
    
    def get_info(self) -> Dict[str, Any]:
        return {
            "account_id": self.account_id,
            "name": self.name,
            "balance": self.balance,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "total_transactions": len(self.transactions),
            "is_locked": self.is_locked
        }
    

    