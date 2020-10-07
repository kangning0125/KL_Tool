#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 21:43:14 2020

@author: kangningli
"""


import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()])


def get_header(app):
    header = html.Div([
                html.Div([
                    html.Img(src=app.get_asset_url("squirrel_icon.png"),className="reportLogo"),
                ],className="reportRow"),
                html.Div([
                    html.Div([
                        html.H5("Squirrel Family Finance Monthly Report - May 2015",className='reportH5')],
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
                            style={"color": "#ffffff"},className="row"),
                        ],className="product")
                    ],className="row"),                    
                ],className='reportSubpage')
           ],style={})

                                    
                                    
                                    
layout_2 = html.Div(id='page_report', className='reportPage',
         children=[
            html.Div([Header(app)]),
            html.Div([
                html.Div(['Developers'],className='rowHeader'),
                html.Div(['this is a container of developers'],className='columnCard',style={'height':'200px'})
                
                ],className='row'),
            html.Div([
                html.Div(['Release Notes'],className='rowHeader'),
                html.Div(['this is a container of release notes'],className='columnCard',style={'height':'100px'})
                
                ],className='row')

            ],style={})




layout_3 = html.Div(id='page_report', className='reportPage',
         children=[
            html.Div([Header(app)]),
            html.Div([
                html.Div(['Developers'],className='rowHeader'),
                html.Div(['this is a container of developers'],className='columnCard',style={'height':'200px'})
                
                ],className='row'),
            html.Div([
                html.Div(['Release Notes'],className='rowHeader'),
                html.Div(['this is a container of release notes'],className='columnCard',style={'height':'100px'})
                
                ],className='row')

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
                                    html.Div(
                                        [
                                            html.P(
                                                "10/25/16    The rise of indexing and the fall of costs"
                                            ),
                                            html.P(
                                                "08/31/16    It's the index mutual fund's 40th anniversary: Let the low-cost, passive party begin"
                                            ),
                                        ],
                                        style={"color": "#7a7a7a"},
                                    ),
                                ],
                                className="row",
                            ),
                            html.Div(
                                [
                                    html.H6("Reviews", className="subtitle padded"),
                                    html.Br([]),
                                    html.Div(
                                        [
                                            html.Li("Launched in 1976."),
                                            html.Li(
                                                "On average, has historically produced returns that have far outpaced the rate of inflation.*"
                                            ),
                                            html.Li(
                                                "Quantitative Equity Group, the fund's advisor, is among the world's largest equity index managers."
                                            ),
                                        ],
                                        id="reviews-bullet-pts",
                                    ),
                                    html.Div(
                                        [
                                            html.P(
                                                "Did you know? The fund launched in 1976 as First Index Investment Trust—the nation's first index fund available to individual investors."
                                            ),
                                            html.Br([]),
                                            html.P(
                                                "* The performance of an index is not an exact representation of any particular investment, as you cannot invest directly in an index."
                                            ),
                                            html.Br([]),
                                            html.P(
                                                "Past performance is no guarantee of future returns. See performance data current to the most recent month-end."
                                            ),
                                        ],
                                        style={"color": "#7a7a7a"},
                                    ),
                                ],
                                className="row",
                            ),
                        ],
                        className="row ",
                    )
                    
                ],className='reportSubpage')

           ],style={})


