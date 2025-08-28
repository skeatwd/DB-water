from dash import Dash, html, dcc, Input, Output, callback, State
import plotly.express as px
import pandas as pd
from datetime import datetime




app = Dash(__name__)

app.layout = html.Div([
    html.Button('+', id='append-water', n_clicks=0),
    html.Div(id='output', children='Нажмите на плючик, чтобы добавить 250мл')
])

@callback(
    Output('output', 'children'),
    Input('append-water', 'n_clicks')
)
def append_water(n_clicks):
    ml = 0
    if n_clicks != 0:
        data = pd.read_csv('water_instake.csv')
        date = datetime.now()
        ml = 250
        new_entry = pd.DataFrame({'datetime': [date], 'amount_ml': [ml]})
        data = pd.concat([data, new_entry], ignore_index=True)
        data.to_csv('water_instake.csv', index=False)
        ml = data['amount_ml'].sum()
    

    return 'Было добавлено 250 мл воды. Выпито: {} мл'.format(ml)

if __name__ == '__main__':
    app.run(debug=True)

