from values import ANNUAL_INTEREST_RATE, NUM_COMPOUNDS, NUM_YEARS
import math
from decimal import Decimal

def compound(principle: Decimal) -> Decimal:
    return principle * (((1 + ((ANNUAL_INTEREST_RATE / 100) / NUM_COMPOUNDS)) ** (NUM_COMPOUNDS * NUM_YEARS)))