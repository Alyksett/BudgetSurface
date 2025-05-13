# I'm not doing FourOhOneK because that looks stupid
from decimal import Decimal
from models.base import Account, MonthlyIncome
from values import _401k_LIMIT
from values import ANNUAL_INTEREST_RATE, NUM_COMPOUNDS, NUM_YEARS
from decimal import Decimal

class _401k(Account):
    def __init__(self, name: str, balance: Decimal):
        super().__init__(name, balance)
        self.principle = balance

    def compound(self, n):
        new = compound(self.balance, n)
        self.balance = new
    
    def apply(self, paycheck: MonthlyIncome, contribution_rate: Decimal) -> Decimal:
        if(self.balance > _401k_LIMIT):
            return self.balance
        
        # PRE-TAX
        contribution = paycheck.gross * contribution_rate
        
        self.balance += contribution
        self.principle += contribution
        
        paycheck.net = paycheck.gross - contribution
        
        return self.balance
    
    def __str__(self):
        return f'Account: {self.name}\n\tBalance: {self.balance}\n\tPrinciple: {self.principle}'

def compound(principle: Decimal, cur_year) -> Decimal:
    return principle * (((1 + ((ANNUAL_INTEREST_RATE / 100) / NUM_COMPOUNDS)) ** (NUM_COMPOUNDS * cur_year)))