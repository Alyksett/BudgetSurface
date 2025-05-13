from dataclasses import dataclass
from decimal import Decimal
import sys
from typing import Any, Callable
import numpy as np
from values import _401k_LIMIT, NET_PAY
from utils import compound



class Paycheck:
    def __init__(self, gross: Decimal):
        self.gross = gross
        self.net = gross
    
class Account:
    def __init__(self, name: str, balance: Decimal):
        self.name = name
        self.balance = balance

    def __add__(self, paycheck: Paycheck):
        self.balance += paycheck.gross
        return self
    
    def apply(self, *args: Any, **kwds: Any) -> Any:
        raise NotImplementedError("Subclasses must implement apply method")

    def compound(self):
        raise NotImplementedError("Subclasses must implement compound method")
    
# I'm not doing FourOhOneK because that looks stupid
class _401k(Account):
    def __init__(self, name: str, balance: Decimal, contribution_rate: Decimal):
        super().__init__(name, balance)
        self.contribution_rate = contribution_rate
        self.principle = balance

    def compound(self):
        new = compound(self.balance)
        self.balance = new
    
    def apply(self, paycheck: Paycheck) -> Decimal:
        if(self.balance > _401k_LIMIT):
            return self.balance
        contribution =  paycheck.gross * self.contribution_rate
        
        self.balance += contribution
        self.principle += contribution
        
        paycheck.net = paycheck.gross - contribution
        
        return self.balance
    
    def __str__(self):
        return f'Account: {self.name}\n\tBalance: {self.balance}\n\tPrinciple: {self.principle}'
    
class Portfolio:
    def __init__(self, name: str, accounts: list[Account]):
        self.name = name
        self.accounts: list[Account] = accounts
        self.paychecks: list[Paycheck] = []
        self.gross = 0
    
    def step(self, repeat: int = 0):
        for _ in range(repeat):
            paycheck = Paycheck(NET_PAY)
            self.gross += paycheck.gross
            
            for account in self.accounts:
                account.apply(paycheck)
            for account in self.accounts:
                account.compound()
        
        
    
    def __str__(self):
        return f'Portfolio: {self.name}\n\tAccounts: {self.accounts}\n\tPaychecks: {self.paychecks}\n\tGross: {self.gross}'



if __name__ == "__main__":
    NUM_YEARS = 3
    
    
    cur = sys.getrecursionlimit()
    sys.setrecursionlimit(cur + (12*NUM_YEARS) + 10)
    _401k_account = _401k("401k", Decimal(0), Decimal(1))
    portfolio = Portfolio("Austin", [_401k_account])
    portfolio.step(12*NUM_YEARS)
    print(portfolio.accounts[0])

