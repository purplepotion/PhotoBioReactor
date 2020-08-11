import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd

from web_app.app import app

from web_app.apps.helpers.graph_helpers import (nutrients_graph,
                                                light_energy_graph,
                                                temp_graph,
                                                pH_graph,
                                                afdw_graph,
                                                do_graph,
                                                dates)

COLORS = ["#fad3cf", "#7971ea", "#a7d129",
          "#b643cd", "#f95959", "#f5f5c6", "#f6f4f4"]

dropdownOptions = [{'label': date, "value": date} for date in dates]


layout = html.Div([
    html.Div([
        html.Div([
            html.H1(
                children='DASHBOARD',
                id="dashboard_title",
                className="col-12"
            ),
        ], className="row"),

        html.Div([
            html.Div([
                html.H4(
                    "DATE",
                    className="imgTitle"
                ),
                html.P(
                    "Visualizations of the data collected from the selected date will be displayed.",
                    className="imgDesc"
                ),
                dcc.Dropdown(
                    options=dropdownOptions,
                    # value=dates[0],
                    id="dateDropdown",
                    placeholder="Select a Date",
                    style={
                        'width': '300px',
                        'color': '#000000',
                        'margin-top': '10px',
                    }),
            ],
                className="col-4 divGraphs divInputs"
            ),
            html.Div([
                dcc.Graph(
                    id="nutrients_graph",
                    style={
                        'width': '100%',
                        'height': '100%',
                        'border-radius': '5px',
                    },
                    figure=nutrients_graph()
                )
            ],
                className="col-6 divGraphs divDisplay",
                style={
                    # 'align-self': 'end'
                    # 'margin-left': '70px'
            }
            ),
        ], className="row justify-content-center"),

        html.Div([
            html.Div([
                dcc.Graph(
                    id="light_energy_graph",
                    style={
                        'width': '100%',
                        'height': '100%',
                        'border-radius': '5px',
                    },
                    figure=light_energy_graph()
                )
            ],
                className="col-5 divGraphs divDisplay"
            ),
            html.Div([
                dcc.Graph(
                    id="temp_graph",
                    style={
                        'width': '100%',
                        'height': '100%',
                        'border-radius': '5px',
                    },
                    figure=temp_graph()
                )
            ],
                className="col-5 divGraphs divDisplay"
            ),
        ], className="row justify-content-center"),

        html.Div([
            html.Div([
                dcc.Graph(
                    id="afdw_graph",
                    style={
                        'width': '100%',
                        'height': '100%',
                        'border-radius': '5px',
                    },
                    figure=afdw_graph()
                )
            ],
                className="col-5 divGraphs divDisplay"
            ),
            html.Div([
                dcc.Graph(
                    id="do_graph",
                    style={
                        'width': '100%',
                        'height': '100%',
                        'border-radius': '5px',
                    },
                    figure=do_graph()
                )
            ],
                className="col-5 divGraphs divDisplay"
            ),
        ], className="row justify-content-center"),

        html.Div([
            html.Div([
                html.Button([
                    dcc.Link('BUILDING', href='/apps/building')
                ],
                    id='btnPageChange',
                ),
            ],className='col-2')
        ], className='row justify-content-end')
    ], className="container-fluid justify-content-center")
])


@ app.callback(
    [Output('nutrients_graph', 'figure'), ],
    [Input('dateDropdown', 'value')],
)
def update_nutrients_graph(value):
    if not value:
        value = dates[0]
    return nutrients_graph(value),


@ app.callback(
    [Output('light_energy_graph', 'figure'), ],
    [Input('dateDropdown', 'value')],
)
def update_light_energy_graph(value):
    if not value:
        value = dates[0]
    return light_energy_graph(value),


@ app.callback(
    [Output('temp_graph', 'figure'), ],
    [Input('dateDropdown', 'value')],
)
def update_temp_graph(value):
    if not value:
        value = dates[0]
    return temp_graph(value),


@ app.callback(
    [Output('afdw_graph', 'figure'), ],
    [Input('dateDropdown', 'value')],
)
def update_afdw_graph(value):
    if not value:
        value = dates[0]
    return afdw_graph(value),


@ app.callback(
    [Output('do_graph', 'figure'), ],
    [Input('dateDropdown', 'value')],
)
def update_do_graph(value):
    if not value:
        value = dates[0]
    return do_graph(value),
