
from decimal import Decimal


class MonthlyIncome:
    def __init__(self, gross: Decimal):
        self.gross = gross
        self.net = gross
