from typing import Optional, List, Dict
from models.account import Account

class BankDatabase:
    """Bank datbase for account management"""

    def __init__(self):
        self.accounts: Dict[str, Account] ={}
        self.account_counter = 1000

    def create_account(self, name: str, password: str, pin: str, balance: float = 0.0) -> Account:
        account_id = f"ACC{self.account_counter}"
        self.account_counter += 1
        account = Account(account_id, name, password, pin, balance)
        self.accounts[account_id] = account
        return account
    
    def get_acount_by_id(self, account_id: str) -> Optional[Account]:
        return self.accounts.get(account_id)
    
    def get_account_by_name(self, name: str) -> Optional[Account]:
        for account in self.accounts.values():
            if account.name.lower() == name.lower():
                return account
            return None
        
    def get_all_accounts(self) -> List[Account]:
        return list(self.accounts.values())
    
    