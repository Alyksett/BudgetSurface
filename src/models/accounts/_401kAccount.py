# I'm not doing FourOhOneK because that looks stupid
from dataclasses import dataclass
from decimal import Decimal
import math
from models.misc import MonthlyIncome

from values import ANNUAL_INTEREST_RATE, NUM_COMPOUNDS, NUM_YEARS, _401k_LIMIT
from decimal import Decimal


    
    
class _401k:
    @dataclass(kw_only=True)
    class EmployerMatch:
        does_match: bool
        match_rate: Decimal
        max_contribution: Decimal
        current_contribution: Decimal
        
    def __init__(self, *, name: str, starting_balance: Decimal, employer: EmployerMatch | None, contribution_rate = Decimal(0)):
        self.name = name
        self.principle = starting_balance
        self.balance = starting_balance
        self.num_months = 0
        self.employer = employer
        self.balance_history: list[Decimal] = []
        self.contribution_rate = contribution_rate
        self.remaining_balance = _401k_LIMIT - starting_balance
        
    def compound(self):
        monthly_rate = ANNUAL_INTEREST_RATE / Decimal('12')
        self.balance *= (1 + monthly_rate)
    
    def apply(self, paycheck: MonthlyIncome) -> MonthlyIncome:
        if(self.num_months == 12):
            self.num_months = 0
            self.remaining_balance = _401k_LIMIT
            
        if(self.balance >= self.remaining_balance):
            self.balance_history.append(self.balance)
            return paycheck
        
        contribution = paycheck.gross * self.contribution_rate
        
        if(self.employer and
            self.employer.does_match and
            self.employer.current_contribution < self.employer.max_contribution):
            
            employer_contribution = contribution * self.employer.match_rate
            if(self.balance + employer_contribution > self.remaining_balance):
                employer_contribution = self.remaining_balance - self.balance
            self.employer.current_contribution += employer_contribution
            contribution += employer_contribution
        

        # put as much into the 401k as possible
        if(self.balance + contribution > self.remaining_balance):
            contribution = self.remaining_balance - self.balance
        
        self.principle += contribution
        self.balance += contribution
        self.remaining_balance -= contribution
        
        paycheck.net -= contribution
        
        self.compound()
        self.balance_history.append(self.balance)
        return paycheck
    
    def __str__(self):
        employer_contribution = self.employer.current_contribution if self.employer else 0
        return f'Account: {self.name}\n\tBalance: {self.balance}\n\tPrinciple: {self.principle}\n\tEmployer Contributions: {employer_contribution}'
