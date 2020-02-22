"""
app2.py : input/output app
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1("Fahrenheit to Celcius"),
    dcc.Input(id='input', value=23, type='number'),
    html.Div(id='output')
])

@app.callback(
    Output(component_id='output', component_property='children'),
    [Input(component_id='input', component_property='value')])
def update_value(input_data):
    return 'Temperature in Celcius : {}'.format(round(5/9  * (input_data - 32),2))


if __name__ == "__main__":
    app.run_server(debug=True)


