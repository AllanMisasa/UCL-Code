# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.DataFrame({
    "Temperature": [22.8, 23.0, 23.2, 23.8, 24.5, 23.5],
    "Humidity": [45.0, 46.2, 46.8, 48.1, 50.4, 49.5],
    "hPa": [1020.12, 1021.01 , 1022.00 , 1022.32 , 1023.45, 1022.98],
    "Minutes": [0, 10, 20, 30, 40, 50]
})

fig = px.line(df, x="Minutes", y="Temperature", title='Temperature the last 60 minutes')

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)