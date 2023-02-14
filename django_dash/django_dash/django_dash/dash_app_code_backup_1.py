import os

import dash
import dash_core_components as dcc
import dash_html_components as html

from django_plotly_dash import DjangoDash

import plotly.graph_objs as go
import pandas as pd

external_stylesheets=['https://codepen.io/amyoshino/pen/jzXypZ.css']
app = DjangoDash('dash_integration_id')
# Create a DataFrame from the .csv file:
print(os.getcwd(), "pppppppppp")
df = pd.read_csv('templates/OldFaithful.csv')

# Create a Dash layout that contains a Graph component:
app.layout = html.Div([
    dcc.Graph(
        id='old_faithful',
        figure={
            'data': [
                go.Scatter(
                    x = df['X'],
                    y = df['Y'],
                    mode = 'markers'
                )
            ],
            'layout': go.Layout(
                title = 'Old Faithful Eruption Intervals v Durations',
                xaxis = {'title': 'Duration of eruption (minutes)'},
                yaxis = {'title': 'Interval to next eruption (minutes)'},
                hovermode='closest'
            )
        }
    )
])

# Add the server clause:
if __name__ == '__main__':
    app.run_server(8052, debug=True)
