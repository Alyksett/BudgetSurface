from values import ANNUAL_INTEREST_RATE, NUM_COMPOUNDS, NUM_YEARS

def compound(principle: float) -> float:
    return principle * (((1 + ((ANNUAL_INTEREST_RATE/100.0)/NUM_COMPOUNDS)) ** (NUM_COMPOUNDS*NUM_YEARS)))
    