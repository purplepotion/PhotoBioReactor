import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

from web_app.app import app

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
            html.Div([
                #####################################################
                # Make Changes in the below div in H3 and P
                ####################################################
                html.Div([
                    html.H3("WINTER LOOK", className="imgTitle"),
                    html.P("Description", className="imgDesc")
                ], className="divDescription"),
            ],
                className="col-md-12 col-xl-4 divDisplay"
            ),
            html.Div([
                html.Img(src=app.get_asset_url("./images/winter.PNG"),
                         className="buildingImg")
            ],
                className="col-md-12 col-xl-7 divDisplay divImages"
            ),
        ], className="row"),
        html.Div([
            html.Div([
                html.Img(src=app.get_asset_url("./images/algal diagram.PNG"),
                         className="buildingImg")
            ],
                className="col-md-12 col-xl-7 divDisplay divImages"
            ),
            html.Div([
                #####################################################
                # Make Changes in the below div in H3 and P
                ####################################################
                html.Div([
                    html.H3("ALGAL DIAGRAM", className="imgTitle"),
                    html.P("Description", className="imgDesc")
                ], className="divDescription"),
            ],
                className="col-md-12 col-xl-4 divDisplay divImages"
            ),
        ], className="row"),
        html.Div([
            html.Div([
                #####################################################
                # Make Changes in the below div in H3 and P
                ####################################################
                html.Div([
                    html.H3("ELEVATION", className="imgTitle"),
                    html.P("Description", className="imgDesc")
                ], className="divDescription"),
            ],
                className="col-md-12 col-xl-4 divDisplay divImages"
            ),
            html.Div([
                html.Img(src=app.get_asset_url("./images/elevation.PNG"),
                         className="buildingImg")
            ],
                className="col-md-12 col-xl-7 divDisplay divImages"
            ),
        ], className="row"),
        html.Div([
            html.Div([
                html.Img(src=app.get_asset_url("./images/roof plan.PNG"),
                         className="buildingImg")
            ],
                className="col-md-12 col-xl-7 divDisplay divImages"
            ),
            html.Div([
                #####################################################
                # Make Changes in the below div in H3 and P
                ####################################################
                html.Div([
                    html.H3("ROOF PLAN", className="imgTitle"),
                    html.P("Description", className="imgDesc")
                ], className="divDescription"),
            ],
                className="col-md-12 col-xl-4 divDisplay divImages"
            ),
        ], className="row"),
        html.Div([
            html.Div([
                #####################################################
                # Make Changes in the below div in H3 and P
                ####################################################
                html.Div([
                    html.H3("SPACE TYPES", className="imgTitle"),
                    html.P("Description", className="imgDesc")
                ], className="divDescription"),
            ],
                className="col-md-12 col-xl-4 divDisplay divImages"
            ),
            html.Div([
                html.Img(src=app.get_asset_url("./images/space types.PNG"),
                         className="buildingImg")
            ],
                className="col-md-12 col-xl-7 divDisplay divImages"
            ),
        ], className="row"),

        html.Div([
            html.Button([
                dcc.Link('DASHBOARD', href='/apps/dashboard')
            ],
                id='btnPageChange',
            ),
        ], className='row justify-content-center')
    ], className="container")
])
