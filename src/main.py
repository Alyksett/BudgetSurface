from decimal import Decimal

from models.accounts import _401k
from models.base import Portfolio

if __name__ == "__main__":
    NUM_YEARS = 3
    
    
    _401k_account = _401k("401k", Decimal(0))
    portfolio = Portfolio("Austin", [_401k_account])
    portfolio.step(12*NUM_YEARS)
    print(portfolio.accounts[0])