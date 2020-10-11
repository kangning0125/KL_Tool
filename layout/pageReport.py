#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 21:43:14 2020

@author: kangningli
"""


import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
from dash.exceptions import PreventUpdate


import pandas as pd
import numpy as np

from src import report_plot, page_table
from app import app


df_graph = pd.read_csv("df_graph.csv")




def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()])


def get_header(app):
    header = html.Div([
                html.Div([
                    html.Img(src=app.get_asset_url("squirrel_icon.png"),className="reportLogo"),
                ],className="reportRow"),
                html.Div([
                    html.Div([
                        html.H5("Squirrel Family Finance Monthly Report",id='report_title',className='reportH5')],
                            className="seven columns main-title",
                        ),
                        html.Div([
                            dcc.Link(
                                "Full View",
                                href="/dash-financial-report/full-view",
                                className="full-view-link",)
                        ],className="five columns",),
                ],className="twelve columns",style={"padding-left": "0"}),
            ],className="reportRow")
    return header


def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                "Overview",
                href="/dash-financial-report/overview",
                className="reportTabFirst",
            ),
            dcc.Link(
                "Asset Details",
                href="/dash-financial-report/price-performance",
                className="reportTab",
            ),
            dcc.Link(
                "Investment Performance",
                href="/dash-financial-report/portfolio-management",
                className="reportTab",
            ),
            dcc.Link(
                "News & Reviews",
                href="/dash-financial-report/news-and-reviews",
                className="reportTab",
            ),
        ],
        className="reportMenuRow",
    )
    return menu


layout_1 = html.Div(id='page_report', className='reportPage', children=[
                html.Div([Header(app)]),
                #sub page
                html.Div([
                    # Row 3
                    html.Div([
                        html.Div([
                            html.H5("Account Summary",className='reportH5',style={'color':'#ffffff','font-size':'1.6rem'}),
                            html.Br([]),
                            html.P([
                                "\
                            As the industry’s first index fund for individual investors, \
                            the Calibre Index Fund is a low-cost way to gain diversified exposure \
                            to the U.S. equity market. The fund offers exposure to 500 of the \
                            largest U.S. companies, which span many different industries and \
                            account for about three-fourths of the U.S. stock market’s value. \
                            The key risk for the fund is the volatility that comes with its full \
                            exposure to the stock market. Because the Calibre Index Fund is broadly \
                            diversified within the large-capitalization market, it may be \
                            considered a core equity holding in a portfolio."],
                            style={"color": "#ffffff"},className="reportRow reportP"),
                        ],className="product")
                    ],className="reportRow"),
                                    
                    # Row 4
                    html.Div([
                        html.Div([
                            html.H6(["Personal Balance Sheet"], className="subtitle padded"),
                            html.Table(),
                        ],className="six columns",),
                        
                        html.Div([
                            html.H6("Net Worth Contribution",className="subtitle padded",),
                            dcc.Graph(
                                        id="graph_net_worth_waterfall",
                                        figure={},
                                        config={"displayModeBar": False}),
                                ],className="six columns"),
                        ],className="reportRow",style={"margin-bottom": "35px"}),
                    
                    # Row 5
                    html.Div([
                        html.Div([
                            html.H6("Net Worth 12 Month Trend",className="subtitle padded"),
                                    dcc.Graph(
                                        id="asset_12m_trend",
                                        figure={},
                                        config={"displayModeBar": False},),
                                ],className="six columns",),
                        
                            html.Div([
                                html.H6("Asset Liquidity",className="subtitle padded"),
                                html.Table(),
                            ],className="six columns",),
                        
                        ],className="reportRow"),
                ],className='reportSubpage')
           ],style={})

                                    
                                    
                                    
layout_2 = html.Div(id='page_report', className='reportPage',
         children=[
            html.Div([Header(app)]),
            html.Div([
                # Row 3
                    html.Div([
                        html.Div([
                            html.H6(["Asset Details"], className="subtitle padded"),
                            html.Table(),
                        ],className="six columns",),
                        html.Div([
                            html.H6("Historical Liquid Asset",className="subtitle padded",),
                            dash_table.DataTable(
                                    id='hist_liq_asset_table',
                                    columns=[{"name": i, "id": i} for i in ['Date','Amount']],
                            ),
                            
                        ],className="six columns"),
                    ],className="reportRow",style={"margin-bottom": "35px"}),
                        
                        # Row 3
                        html.Div([
                            html.Div([
                                html.H6(["Asset Allocation"], className="subtitle padded"),
                                html.Table(),
                            ],className="six columns",),
                            html.Div([
                                html.H6("Asset Top Movers",className="subtitle padded",),
                                dcc.Graph(
                                            id="top_mover_graph",
                                            figure={},
                                            config={"displayModeBar": False}),
                                    ],className="six columns"),
                            
                            ],className="reportRow",style={"margin-bottom": "35px"}),
                        
                        # Row 4
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.H6("Asset Growth", className="subtitle padded"),
                                        dcc.Graph(
                                            id="graph-4",
                                            figure={
                                                "data": [
                                                    go.Scatter(
                                                        x=df_graph["Date"],
                                                        y=df_graph["Calibre Index Fund"],
                                                        line={"color": "#97151c"},
                                                        mode="lines",
                                                        name="Calibre Index Fund",
                                                    ),
                                                    go.Scatter(
                                                        x=df_graph["Date"],
                                                        y=df_graph[
                                                            "MSCI EAFE Index Fund (ETF)"
                                                        ],
                                                        line={"color": "#b5b5b5"},
                                                        mode="lines",
                                                        name="MSCI EAFE Index Fund (ETF)",
                                                    ),
                                                ],
                                                "layout": go.Layout(
                                                    autosize=True,
                                                    width=700,
                                                    height=200,
                                                    font={"family": "Raleway", "size": 10},
                                                    margin={
                                                        "r": 30,
                                                        "t": 30,
                                                        "b": 30,
                                                        "l": 30,
                                                    },
                                                    showlegend=True,
                                                    titlefont={
                                                        "family": "Raleway",
                                                        "size": 10,
                                                    },
                                                    xaxis={
                                                        "autorange": True,
                                                        "range": [
                                                            "2007-12-31",
                                                            "2018-03-06",
                                                        ],
                                                        "rangeselector": {
                                                            "buttons": [
                                                                {
                                                                    "count": 1,
                                                                    "label": "1Y",
                                                                    "step": "year",
                                                                    "stepmode": "backward",
                                                                },
                                                                {
                                                                    "count": 3,
                                                                    "label": "3Y",
                                                                    "step": "year",
                                                                    "stepmode": "backward",
                                                                },
                                                                {
                                                                    "count": 5,
                                                                    "label": "5Y",
                                                                    "step": "year",
                                                                },
                                                                {
                                                                    "count": 10,
                                                                    "label": "10Y",
                                                                    "step": "year",
                                                                    "stepmode": "backward",
                                                                },
                                                                {
                                                                    "label": "All",
                                                                    "step": "all",
                                                                },
                                                            ]
                                                        },
                                                        "showline": True,
                                                        "type": "date",
                                                        "zeroline": False,
                                                    },
                                                    yaxis={
                                                        "autorange": True,
                                                        "range": [
                                                            18.6880162434,
                                                            278.431996757,
                                                        ],
                                                        "showline": True,
                                                        "type": "linear",
                                                        "zeroline": False,
                                                    },
                                                ),
                                            },
                                            config={"displayModeBar": False},
                                        ),
                                    ],
                                    className="twelve columns",
                                )
                            ],
                            className="reportRow",
                        ),
                
                ],className='reportSubpage'),
            
            ],style={})




layout_3 = html.Div(id='page_report', className='reportPage',
         children=[
            html.Div([Header(app)]),
            html.Div([
                # Row 3
                html.Div([
                    html.Div([
                        html.H5("Investment Portfolio Summary",className='reportH5',style={'color':'#ffffff','font-size':'1.6rem'}),
                        html.Br([]),
                        html.P([
                            "\
                        As the industry’s first index fund for individual investors, \
                        the Calibre Index Fund is a low-cost way to gain diversified exposure \
                        to the U.S. equity market. The fund offers exposure to 500 of the \
                        largest U.S. companies, which span many different industries and \
                        account for about three-fourths of the U.S. stock market’s value. \
                        The key risk for the fund is the volatility that comes with its full \
                        exposure to the stock market. Because the Calibre Index Fund is broadly \
                        diversified within the large-capitalization market, it may be \
                        considered a core equity holding in a portfolio."],
                        style={"color": "#ffffff"},className="reportRow reportP"),
                    ],className="product")
                ],className="reportRow"),
            
                # Row 4
                html.Div(
                    [
                        html.Div(
                            [
                                html.H6("Investment Performance", className="subtitle padded"),
                                dcc.Graph(
                                    id="investment_graph",
                                    figure={},
                                    config={"displayModeBar": False},
                                ),
                            ],className="twelve columns")
                    ],className="reportRow"),
                
                html.Div(
                    [
                        html.Div(
                            [
                                html.H6("Recent Investment Returns - updated as of 5/31/2016", className="subtitle padded"),
                                html.Table(),
                            ],className="twelve columns")
                    ],className="reportRow"),
                    
            ],className='reportSubpage'),

            ],style={})





layout_4 = html.Div(id='page_report', className='reportPage',
         children=[
            html.Div([Header(app)]),
            #sub page
                html.Div([
                    # Row 1
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6("News", className="subtitle padded"),
                                    html.Br([]),
                                    html.Div([
                                        html.P("10/25/16    The rise of indexing and the fall of costs",className='reportP'),
                                        html.P("08/31/16    It's the index mutual fund's 40th anniversary: Let the low-cost, passive party begin",className='reportP'),
                                    ],style={"color": "#7a7a7a"}),
                                ],className="reportRow",),
                            html.Div([
                                html.H6("Reviews", className="subtitle padded"),
                                html.Br([]),
                                html.Div([
                                    html.Li("Launched in 1976.",className='reportLi'),
                                    html.Li("On average, has historically produced returns that have far outpaced the rate of inflation.*"
                                    ,className='reportLi'),
                                    html.Li("Quantitative Equity Group, the fund's advisor, is among the world's largest equity index managers."
                                    ,className='reportLi'),
                                ],id="reviews-bullet-pts"),
                                html.Div([
                                    html.P("Did you know? The fund launched in 1976 as First Index Investment Trust—the nation's first index fund available to individual investors.",className='reportP'),
                                    html.Br([]),
                                    html.P("* The performance of an index is not an exact representation of any particular investment, as you cannot invest directly in an index.",className='reportP'),
                                    html.Br([]),
                                    html.P("Past performance is no guarantee of future returns. See performance data current to the most recent month-end.",className='reportP'),
                                ],style={"color": "#7a7a7a"}),
                            ],className="reportRow"),
                        ],className="reportRow",)
                    
                ],className='reportSubpage')

           ],style={})


@app.callback(
    [Output('graph_net_worth_waterfall','figure'), 
     Output('asset_12m_trend','figure'),
     Output('top_mover_graph','figure'),
     Output('investment_graph','figure')],   
    [Input('url','pathname')],
    [State('date_selected','children')])
def update_summary_info(url,month_end):
    if '/squirrel/FinancialReport' in url:
        data = pd.read_csv('Records.csv')   
        
        networth_waterfall_fig = report_plot.waterfall(data, month_end)
        asset_12m_fig = report_plot.report_12m_asset(data, month_end, "Asset")
        top_mover_fig = report_plot.top_mover_bar(data, month_end)
        investment_fig = report_plot.investment_line(data, month_end)
        
        return networth_waterfall_fig, asset_12m_fig, top_mover_fig, investment_fig
    
    else:
        raise PreventUpdate
        
@app.callback(
    Output('hist_liq_asset_table','data'),  
    [Input('url','pathname')],
    [State('date_selected','children')])
def update_table_data(url,month_end):
    if '/squirrel/FinancialReport' in url:
        data = pd.read_csv('Records.csv')   
        
        hist_liq_asset = page_table.get_hist_asset_data(data, month_end)
        hist_liq_asset_data = hist_liq_asset.to_dict('records')
        
        return hist_liq_asset_data
    
    else:
        raise PreventUpdate        
        
