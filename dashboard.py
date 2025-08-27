from dash import Dash, html
import plotly.express as px
import pandas as pd

data = pd.read_csv('water_instake.csv')

app = Dash(__name__)
app.layout = html.Div(children=[
    html.H1(children='Отслеживание воды')
])

if __name__ == '__main__':
    app.run(debug=True)