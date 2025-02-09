from dash import Dash, html, dcc
import plotly.graph_objects as go

app = Dash(__name__)

app.layout = html.Div([
    dcc.Graph(
        id='3d-chart',
        figure=go.Figure(
            data=[go.Surface(z=[[1,2,3],[4,5,6],[7,8,9]])]
        )
    )
])

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050)
