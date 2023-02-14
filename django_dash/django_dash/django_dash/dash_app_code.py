import os

import dash
import dash_core_components as dcc
import dash_html_components as html

from django_plotly_dash import DjangoDash

import plotly.graph_objs as go
import pandas as pd
import plotly.graph_objects as go
import numpy as np

external_stylesheets=['https://codepen.io/amyoshino/pen/jzXypZ.css']
app = DjangoDash('dash_integration_id')
# Create a DataFrame from the .csv file:
print(os.getcwd(), "pppppppppp")
df = pd.read_csv('templates/OldFaithful.csv')
pts = np.loadtxt(np.DataSource().open('https://raw.githubusercontent.com/plotly/datasets/master/mesh_dataset.txt'))
x, y, z = pts.T
fig = go.Figure(data=[go.Mesh3d(x=x, y=y, z=z, color='lightpink', opacity=0.50)])

# Create a Dash layout that contains a Graph component:
app.layout = html.Div([
    dcc.Graph(
        id='old_faithful',
        figure=fig
    )
])

# Add the server clause:
if __name__ == '__main__':
    app.run_server(8052, debug=True)
