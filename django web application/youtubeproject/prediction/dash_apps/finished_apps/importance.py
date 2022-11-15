import dash
from dash import html, dcc, Input, Output, dash_table
import pandas as pd
import plotly.express as px
from django_plotly_dash import DjangoDash
import os

app = DjangoDash('Importance',add_bootstrap_links=True)
app.css.append_css({ "external_url" : "/static/assets/s1.css" })

os.chdir(os.path.dirname(os.path.abspath(__file__)))


df = pd.read_csv('Importance_04-11-22_RF_df.csv')


app.layout = html.Div(
    children=[
        html.Div(
                    children=[
                        html.Div(
                            children=[
                                html.H4(
                                    [
                                        "Feature Importance",
                                        
                                    ],
                                    className="container_title",
                                ),
                                html.Div([
                                dcc.Graph(
                                    id="scatterInfo-graph",
                                    figure=px.bar(df, x='value', y='Importance', height=420).update_xaxes(categoryorder='total descending').update_layout(paper_bgcolor="#f3f3f1",plot_bgcolor="#f3f3f1",yaxis=dict(showgrid=False),xaxis=dict(showgrid=False)),
                                    config={"displayModeBar": False},
                                )


                                    ]
                                ),
                            ],
                            className="twelve columns pretty_container",
                            id="subscriberInfo-div",
                        ),
                    ]
        )
    ]
)