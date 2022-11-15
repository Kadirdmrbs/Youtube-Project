from dash import html, dcc, Input, Output
import pandas as pd
import plotly.express as px
from django_plotly_dash import DjangoDash
import os
from ...functions.feat_ext import fe_data
from ...functions.db_connect import return_df
import dash
from textwrap import dedent


app = DjangoDash('SimpleExample',add_bootstrap_links=True)
app.css.append_css({ "external_url" : "/static/assets/s1.css" })

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Colors
bgcolor = "#f3f3f1"  # mapbox light map land color
bar_bgcolor = "#b0bec5"  # material blue-gray 200
bar_unselected_color = "#78909c"  # material blue-gray 400
bar_color = "#546e7a"  # material blue-gray 600
bar_selected_color = "#37474f"  # material blue-gray 800
bar_unselected_opacity = 0.8


# Figure template
row_heights = [150, 500, 300]
template = {"layout": {"paper_bgcolor": bgcolor, "plot_bgcolor": bgcolor}}



def blank_fig(height):
    """
    Build blank figure with the requested height
    """
    return {
        "data": [],
        "layout": {
            "height": height,
            "template": template,
            "xaxis": {"visible": False},
            "yaxis": {"visible": False},
        },
    }


def build_modal_info_overlay(id, side, content):
    """
    Build div representing the info overlay for a plot panel
    """
    div = html.Div(
        [  # modal div
            html.Div(
                [  # content div
                    html.Div(
                        [
                            html.H4(
                                [
                                    "Info",
                                    html.Img(
                                        id=f"close-{id}-modal",
                                        src="/static/assets/times-circle-solid.svg",
                                        n_clicks=0,
                                        className="info-icon",
                                        style={"margin": 0},
                                    ),
                                ],
                                className="container_title",
                                style={"color": "white"},
                            ),
                            dcc.Markdown(content),
                        ]
                    )
                ],
                className=f"modal-content {side}",
            ),
            html.Div(className="modal"),
        ],
        id=f"{id}-modal",
        style={"display": "none"},
    )

    return div




"""
Dash Layout
"""
table = return_df()
df = fe_data(table)

table = df[['Id','Title','Date','Comments','Likes','Views','Duration','Categories','SubCategory']]
elements = ['Views','Likes','Comments','DurationinSeconds']

app.layout = html.Div(
    children=[
        html.Div(
            [
                html.H1(
                    children=[
                        "S Sport Youtube Channel Dashboard",
                        
                    ],
                    style={"text-align": "left"},
                ),
            ]
        ),
        html.Div(
            children=[
                build_modal_info_overlay(
                    "subscriberInfo",
                    "top",
                    dedent(
                        """
            Total Subscriber S Sport has as 04/11/2022
            """
                    ),
                ),
                build_modal_info_overlay(
                    "videosInfo",
                    "top",
                    dedent(
                        """
            Total Videos S Sport uploaded as 04/11/2022
        """
                    ),
                ),
                build_modal_info_overlay(
                    "viewsInfo",
                    "top",
                    dedent(
                        """
            Total views S Sport has as 04/11/2022
        """
                    ),
                ),
                build_modal_info_overlay(
                    "scatterInfo",
                    "top",
                    dedent(
                        """
            The _**Videos by Categories**_ panel displays a scatter plot of the all videos
            in the dataset.

            It can be customized by selecting a year range, x axis value and
            y axis value respectively.

            Left-click on categories on the right to exclude or include them.
        """
                    ),
                ),
                build_modal_info_overlay(
                    "count",
                    "middle",
                    dedent(
                        """
            The _**Count**_ panel displays a histogram of the total video amount by
            subcategories.

            It can be customized by selecting a year range

            Left-click on categories on the right to exclude or include them.
        """
                    ),
                ),
                build_modal_info_overlay(
                    "yearassess",
                    "middle",
                    dedent(
                        """
            The _**Annual Summary**_ panel displays a bar plot of the channel details
            by year.

            It can be customized by selecting a y axis value.

            It can either show mean or sum of the selected value.

        """
                    ),
                ),
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                html.H4(
                                    [
                                        "Subscribers",
                                        html.Img(
                                            id="show-subscriberInfo-modal",
                                            src="/static/assets/question-circle-solid.svg",
                                            n_clicks=0,
                                            className="info-icon",
                                        ),
                                    ],
                                    className="container_title",
                                ),
                                html.Div([
                                dcc.Markdown('# 1.130.000 #')],style={'textAlign': 'center'}),


                                    ]
                                ),
                            ],
                            className="four columns pretty_container",
                            id="subscriberInfo-div",
                        ),
                        html.Div(
                            children=[
                                html.H4(
                                    [
                                        "Videos",
                                        html.Img(
                                            id="show-videosInfo-modal",
                                            src="/static/assets/question-circle-solid.svg",
                                            n_clicks=0,
                                            className="info-icon",
                                        ),
                                    ],
                                    className="container_title",
                                ),
                                html.Div([
                                dcc.Markdown('# 9.702 #')],style={'textAlign': 'center'}),


                            ],
                            className="four columns pretty_container",
                            id="videosInfo-div",
                        ),
                        html.Div(
                            children=[
                                html.H4(
                                    [
                                        "Views",
                                        html.Img(
                                            id="show-viewsInfo-modal",
                                            src="/static/assets/question-circle-solid.svg",
                                            n_clicks=0,
                                            className="info-icon",
                                        ),
                                    ],
                                    className="container_title",
                                ),
                                html.Div([
                                dcc.Markdown('# 227.818.009 #')],style={'textAlign': 'center'}),


                            ],
                            className="four columns pretty_container",
                            id="viewsInfo-div",
                        ),
                        html.Div(
                            children=[
                                html.H4(
                                    [
                                        "Videos by Categories",
                                        html.Img(
                                            id="show-scatterInfo-modal",
                                            src="/static/assets/question-circle-solid.svg",
                                            className="info-icon",
                                        ),
                                    ],
                                    className="container_title",
                                ),
                                html.H6(['Select Year, Xaxis and Yaxis respectively']),
                                html.Div([
                                dcc.RangeSlider(
                                    id='range-slider',
                                    min=2018, max=2023, step=1,
                                    marks={2018:'2018', 2019:'2019', 2020:'2020', 2021:'2021', 2022:'2022', 2023: '2023'},
                                    value=[2018, 2023],
                                    ),
                                dcc.Dropdown(
                                    elements,
                                    'DurationinSeconds',
                                    id='xaxis-column',
                                ),
                                dcc.Dropdown(
                                    elements,
                                    'Views',
                                    id='yaxis-column',
                                ),
                                    ],
                                    style={"display": "grid", "grid-template-columns": "50% 25% 25%"},
                                ),
                                dcc.Graph(
                                    id="scatterInfo-graph",
                                    figure=blank_fig(row_heights[1]),
                                    config={"displayModeBar": False},
                                )
                            ],
                            className="twelve columns pretty_container",
                            style={
                                "width": "98%",
                                "margin-right": "0",
                            },
                            id="scatterInfo-div",
                    ),
                    html.Div(
                    children=[
                        html.Div(
                            children=[
                                html.H4(
                                    [
                                        "Count",
                                        html.Img(
                                            id="show-count-modal",
                                            src="/static/assets/question-circle-solid.svg",
                                            className="info-icon",
                                        ),
                                    ],
                                    className="container_title",
                                ),
                                dcc.RangeSlider(
                                    id='histo-year',
                                    min=2018, max=2023, step=1,
                                    marks={2018:'2018', 2019:'2019', 2020:'2020', 2021:'2021', 2022:'2022', 2023: '2023'},
                                    value=[2018, 2023],
                                    ),
                                dcc.Graph(
                                    id="count-histogram",
                                    figure=blank_fig(row_heights[2]),

                                    config={"displayModeBar": False},
                                ),

                            ],
                            className="six columns pretty_container",
                            id="count-div",
                        ),
                        html.Div(
                            children=[
                                html.H4(
                                    [
                                        "Annual Summary",
                                        html.Img(
                                            id="show-yearassess-modal",
                                            src="/static/assets/question-circle-solid.svg",
                                            className="info-icon",
                                        ),
                                    ],
                                    className="container_title",
                                ),
                                html.Div([
                                dcc.RadioItems(
                                    ['Average', 'Total'],
                                    'Average',
                                    id='radiotype',
                                    labelStyle={'display': 'inline-block', 'marginTop': '5px'}
                                ),
                                dcc.Dropdown(
                                    elements,
                                    'Views',
                                    id='year-dropdown',
                                ),

                                    ],
                                    style={"display": "grid", "grid-template-columns": "30% 70%"},
                                ),

                                dcc.Graph(
                                    id="yearassess-histogram",
                                    config={"displayModeBar": False},
                                    figure=blank_fig(row_heights[2]),
                                ),

                            ],
                            className="six columns pretty_container",
                            id="yearassess-div",
                        ),
                    ]
                ),
            ]
        ),

        html.Div(
            [
                html.H4("Acknowledgements", style={"margin-top": "0"}),
                dcc.Markdown(
                    """\
 - Dashboard written in Python using the [Dash](https://dash.plot.ly/) web framework.
 - Data acquired by Youtube Data API.
 - Later data stored on a AWS PostgresSQL database.
 - After pulling data from AWS PostgresSQL database it goes into data cleaning pipelines
 and ready for building the dashboard.
"""
                ),
            ],
            style={
                "width": "98%",
                "margin-right": "0",
                "padding": "10px",
            },
            className="twelve columns pretty_container",
        ),
    ]
)




for id in ["subscriberInfo", "videosInfo", "viewsInfo", "scatterInfo","count","yearassess"]:

    @app.callback(
        [Output(f"{id}-modal", "style"), Output(f"{id}-div", "style")],
        [Input(f"show-{id}-modal", "n_clicks"), Input(f"close-{id}-modal", "n_clicks")],
    )
    def toggle_modal(n_show, n_close):
        ctx = dash.callback_context
        if ctx.triggered and ctx.triggered[0]["prop_id"].startswith("show-"):
            return {"display": "block"}, {"zIndex": 1003}
        else:
            return {"display": "none"}, {"zIndex": 0}




@app.callback(
    Output('scatterInfo-graph', 'figure'),
    Input('xaxis-column', 'value'),
    Input('yaxis-column', 'value'),
    Input("range-slider", "value"))
def update_graph(xaxis_column_name, yaxis_column_name, slider_range):

    low, high = slider_range
    mask = (df['Year'].astype('int') >= low) & (df['Year'].astype('int') < high)

    fig = px.scatter(df[mask],x=xaxis_column_name,
            y=yaxis_column_name,
            hover_name='Title',
            color='Categories'
            )

    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    fig.update_layout(paper_bgcolor="#f3f3f1",plot_bgcolor="#f3f3f1",yaxis=dict(showgrid=False),xaxis=dict(showgrid=False))

    return fig


@app.callback(
    Output('yearassess-histogram','figure'),
    Input('radiotype','value'),
    Input('year-dropdown', 'value'))
def yeargraph(radiotype,yeardropdown):

    if radiotype == 'Average':
        fig = px.bar(df.groupby(['Year']).mean().reset_index(),
                    x='Year',
                    y=yeardropdown,
                    height=420)

    else:
        fig = px.bar(df.groupby(['Year']).sum().reset_index(),
                    x='Year',
                    y=yeardropdown,
                    height=420)

    fig.update_layout(paper_bgcolor="#f3f3f1",plot_bgcolor="#f3f3f1",yaxis=dict(showgrid=False),xaxis=dict(showgrid=False))

    return fig

@app.callback(
    Output('count-histogram','figure'),
    Input('histo-year','value'))
def histograph(year_lh):

    low, high = year_lh
    mask = (df['Year'].astype('int') >= low) & (df['Year'].astype('int') < high)

    fig = px.histogram(df[mask], y="SubCategory", color="Categories",height=420).update_xaxes(categoryorder='total descending')

    fig.update_layout(paper_bgcolor="#f3f3f1",plot_bgcolor="#f3f3f1",yaxis=dict(showgrid=False),xaxis=dict(showgrid=False))

    return fig



