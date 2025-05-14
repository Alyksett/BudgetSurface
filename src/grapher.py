from decimal import Decimal
import pandas as pd
import plotly.graph_objects as go

import plotly.express as px
import numpy as np

def graph(data: list[Decimal]):
    fig = px.line(x=list(range(len(data))), y=[float(d) for d in data])
    fig.show()
    
def graph_two(data1: list[Decimal], data2: list[Decimal]):
    steps = len(data1)
 
    a =np.array([float(x) for x in data1], dtype=np.float64)
    b =np.array([float(x) for x in data2], dtype=np.float64)
    
    surface_z = np.array([
        (1 - t) * a + t * b
        for t in np.linspace(0, 1, steps + 1)
    ])
    fig = go.Figure(data=[go.Surface(z=surface_z)])
    fig.show()
    
    
    
    
