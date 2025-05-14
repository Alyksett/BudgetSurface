from decimal import Decimal

from models.accounts import _401k
from models.misc import MonthlyIncome
from models.portfolio import Portfolio

from grapher import graph, graph_two

if __name__ == "__main__":
    NUM_MONTHS = 12 * 30
    employer = _401k.EmployerMatch(
        does_match=True,
        match_rate=Decimal(0.5),
        max_contribution=Decimal(0.05),
        current_contribution=Decimal(0))
    
    
    
    low_check = MonthlyIncome(Decimal(1000))
    low = Portfolio(
        "Low Contributions",
        _401k(name="401k",
              starting_balance=Decimal(0),
              employer=employer,
              contribution_rate=Decimal(0.5)
              )
            )
    
    low.step(NUM_MONTHS, low_check)
    
    high_check = MonthlyIncome(Decimal(1000))
    high = Portfolio(
        "High Contributions",
        _401k(
            name="401k",
            starting_balance=Decimal(4000),
            employer=employer,
            contribution_rate=Decimal(1)
            )
        )
    high.step(NUM_MONTHS, high_check)
    
    
    # print(portfolio._401k)
    # graph(portfolio._401k.balance_history)
    graph_two(low._401k.balance_history, high._401k.balance_history)