from decimal import Decimal
from typing import Any
from decimal import Decimal
from typing import Any
from values import NET_PAY

class MonthlyIncome:
    def __init__(self, gross: Decimal):
        self.gross = gross
        self.net = gross
        
        
class Account:
    def __init__(self, name: str, balance: Decimal):
        self.name = name
        self.balance = balance

    def __add__(self, paycheck: MonthlyIncome):
        self.balance += paycheck.gross
        return self
    
    def apply(self, *args: Any, **kwds: Any) -> Any:
        raise NotImplementedError("Subclasses must implement apply method")

    def compound(self, n):
        raise NotImplementedError("Subclasses must implement compound method")
    
    


class Portfolio:
    def __init__(self, name: str, accounts: list[Account]):
        self.name = name
        self.accounts: list[Account] = accounts
        self.paychecks: list[MonthlyIncome] = []
        self.gross = 0
    
    def step(self, repeat: int = 0):
        for i in range(repeat):
            paycheck = MonthlyIncome(NET_PAY)
            self.gross += paycheck.gross
            
            for account in self.accounts:
                account.apply(paycheck, Decimal(1))
            for account in self.accounts:
                account.compound(i)
    
    def __str__(self):
        return f'Portfolio: {self.name}\n\tAccounts: {self.accounts}\n\tPaychecks: {self.paychecks}\n\tGross: {self.gross}'

