from decimal import Decimal
from typing import Any
from decimal import Decimal
from typing import Any
from models.accounts import _401k
from models.misc import MonthlyIncome
from values import NET_PAY

type Account = _401k


class Portfolio:
    def __init__(self, name: str, _401kAccount: _401k):
        self._401k = _401kAccount
        self.name = name
        self.paychecks: list[MonthlyIncome] = []
        self.gross = 0
    
    def step(self, repeat: int = 0, paycheck: MonthlyIncome = MonthlyIncome(NET_PAY)) -> None:
        for _ in range(repeat):
            self.gross += paycheck.gross
            paycheck = self._401k.apply(paycheck=paycheck)
    
    
    def __str__(self):
        return f'Portfolio: {self.name}\n\tPaychecks: {self.paychecks}\n\tGross: {self.gross}'

