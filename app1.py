"""
app1.py : drawing some nice graphs
"""


import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np

app = dash.Dash()

x1 = np.arange(0, np.ceil(2 * np.pi), 0.1)
y1 = np.sin(x1)
y2 = np.cos(x1)

app.layout = html.Div(children=[
    
    html.H1('Dash app'),
    
    dcc.Graph(id='nice graph',
              figure={
                  'data': [
                      {'x': x1, 'y': y1, 'type': 'line', 'name': 'sin'},
                      {'x': x1, 'y': y2, 'type': 'bar', 'name': 'cos'}
                  ],
                  
                  'layout': {'title': 'Basic geometry example'}
              })])

if __name__ == "__main__":
    app.run_server(debug=True)

