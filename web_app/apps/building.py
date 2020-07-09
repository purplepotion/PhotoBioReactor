import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# colors = {
#     'background': '#111111',
#     'text': '#7FDBFF'
# }

# df = pd.DataFrame({"x": [1, 2, 3], "SF": [4, 1, 2], "Montreal": [2, 4, 5]})

# fig = px.bar(df, x="x", y=["SF", "Montreal"], barmode="group")
#
# fig.update_layout(plot_bgcolor=colors['background'],
#                   paper_bgcolor=colors['background'], font_color=colors['text'])

layout = html.Div([
    html.Div([
        html.Div([
            html.H1(
                children='BUILDING',
                id="dashboard_title",
                className="col"
            ),
        ], className="row"),
        html.Div([
            html.Div(
                children='DIV 1',
                id="notDivUserInput",
                className="col-md divDisplay"
            ),
            html.Div(
                children='DIV 2',
                id="divBuildingColor",
                className="col-md divDisplay"
            ),
        ], className="row"),
        html.Div([
            html.Div(
                children='DIV 3',
                id="divGraph1",
                className="col-md divDisplay"
            ),
            html.Div(
                children='DIV 4',
                id="divGraph2",
                className="col-md divDisplay"
            ),
        ], className="row"),
        html.Div([
            html.Button([
                dcc.Link('DASHBOARD', href='/apps/dashboard')
            ],
                id='btnPageChange',
            ),
        ], className='row')
    ], className="container")
])
