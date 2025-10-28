from typing import Tuple
from models.account import Account

class BankingService:
    """Banking operations"""

    @staticmethod
    def check_balance(account: Account) -> str:
        return f"💰 Balance: ${account.balance:.2f}"
    
    @staticmethod
    def deposit(account: Account, amount: float) -> Tuple[bool, str]:
        if account.deposit(amount):
            return True, f"✅ Deposited ${amount:.2f}. Balance: ${account.balance:.2f}"
        return False, "❌ Invalid amount"
    
    @staticmethod
    def withdraw(account: Account, amount: float) -> Tuple[bool, str]:
        if account.transfer(amount):
            return True, f"✅ Withdrawn ${amount:.2f}. Balance: ${account.balance:.2f}"
        return False, "❌ Insufficient funds"
    
    @staticmethod
    def transfer(from_acc: Account, to_acc: Account, amount:float) -> Tuple[bool, str]:
        if from_acc.transfer(to_acc, amount):
            return True, f"✅ Transferred ${amount:.2f} to {to_acc.name}"
        return False, "❌ Transfer failed"
    
    @staticmethod
    def get_transaction_history(account: Account, limit: int = 10) -> str:
        if not account.transactions:
            return "No transactions"
        history = "📊 Recent Transactions:\n\n"
        for i, trans in enumerate(account.transactions[-limit:], 1):
            history += f"{i}. {trans['type']}: ${trans['amount']:.2f} on {trans['timestamp']}\n"
        return history
    

    