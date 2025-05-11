from dataclasses import dataclass
from typing import Any, Callable
import numpy as np
from values import _401k_LIMIT, NET_PAY
from utils import compound
class Paycheck:
    def __init__(self, gross: float):
        self.gross = gross
        self.net = gross
    
class Account:
    def __init__(self, name: str, balance: float):
        self.name = name
        self.balance = balance

    def __add__(self, paycheck: Paycheck):
        self.balance += paycheck.gross
        return self
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        raise NotImplementedError("Subclasses must implement __call__ method")

    def compound(self):
        raise NotImplementedError("Subclasses must implement compound method")
    
# I'm not doing FourOhOneK because that looks stupid
class _401k(Account):
    def __init__(self, name: str, balance: float, contribution_rate: float):
        super().__init__(name, balance)
        self.contribution_rate = contribution_rate
        self.principle = balance

    def compound(self):
        new = compound(self.balance)
        self.balance = new
    
    def __call__(self, paycheck: Paycheck) -> float:
        if(self.balance > _401k_LIMIT):
            raise ValueError("401k limit exceeded")
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
        paycheck = Paycheck(NET_PAY)
        self.gross += paycheck.gross
        
        for account in self.accounts:
            account(paycheck)
        for account in self.accounts:
            account.compound()
        if(repeat > 0):
            self.step(repeat - 1)
    
    def __str__(self):
        return f'Portfolio: {self.name}\n\tAccounts: {self.accounts}\n\tPaychecks: {self.paychecks}\n\tGross: {self.gross}'



if __name__ == "__main__":
    _401k_account = _401k("401k", 0, 0.06)
    portfolio = Portfolio("Austin", [_401k_account])
    portfolio.step(10)
    print(portfolio.accounts[0])

'''

new Paycheck(100)
_401k_account = new _

401contribution = _401k("401k", 0, 0.05)
new 

Paycheck.reduce

Account+=Paycheck



'''
    

