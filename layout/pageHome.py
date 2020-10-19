#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 21:43:14 2020

@author: kangningli
"""


import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc

import pandas as pd

from app import app

layout = html.Div([
            #row 1
            html.Div([
                html.Div([
                    html.Div([
                        html.I(className='fa fa-book')
                    ],style={'width':'25%','float':'left','padding-right':'15px','padding-left':'15px','font-size':'180px','line-height':'200px'}),
                    
                    html.Div([
                        html.H1('Squirrel Finance Planner',className='homeHeaderMain'),
                        html.P('Ongoing Updates · Data Visualization · Open Source',className='homeHeaderSub'),
                        
                        html.Div([
                            dcc.Link("Dashboard", href='/squirrel/dashboard' ,id='go_dash_btn', className="homeButton"), 
                            html.A("Github",href='https://github.com/kangning0125/KL_Tool', target='_blank',className="homeButton")
                                 
                        ],className='homeButtonContainer'),
                        
                    ],style={'width':'70%','float':'left','padding-right':'15px','padding-left':'15px','height':'100%'})
                    
                ],style={'display':'block','box-sizing':'border-box','position':'relative','z-index':2,'max-width':'100%','width':'1000px',
                         'padding-left':'15px','padding-right':'15px','margin-left':'auto','margin-right':'auot','color':'#fff'})
                         
            ],className="rowHome",style={"margin-bottom": "0px",'min-height':'300px','max-height':'500px'}),
            
            #row 2
            html.Div([
                html.H3('Note: choose another date to review previous records:',style={'color':'black', 'font-size':'14px','padding-left':'40px'}),
                dcc.Dropdown(
                    id='date-selector',
                    options=[],
                    value='1/31/2019',
                    style={'width':'150px','margin-left':'20px','color':'black'}
                ),
                #html.Div(id='date-display-value',style={'color':'black'}),
            ],className="rowHome",style={"display":'inline-flex','background':'#f5f5f5', 'width':'100%','max-height':'50px','padding-top':'10px','padding-bottom':'10px'}),
            
            #row 3
            html.Div([
                html.Div([
                    html.P(['The Squirrel Finance Planner demonstrates the integration of Dash package, CSS styling, open source programming, and data visualization.'],
                           style={'color':'#333', 'font-weight':'300', 'line-height': "1.6rem",'font-size':'24px','padding-left':'40px','padding-right':'20px'}),
                    html.Div([
                        html.Div([
                            html.I('  All codes shared on Github',className='fa fa-github', style={'color':'inherit','font-weight':500,'line-height':'1.1rem','font-size':'23px','margin-top':'10px','margin-bottom':'10px'}),
                            html.H4('The codes for this app are shared on Github for your reference.', style={'color':'inherit','line-height':'1.1rem','font-size':'14px'})
                        ],className='homeIconContainer'),
                        
                        html.Div([
                            html.I('  Unlimited Scalability',className='fa fa-arrows-alt', style={'color':'inherit','font-weight':500,'line-height':'1.1rem','font-size':'23px','margin-top':'10px','margin-bottom':'10px'}),
                            html.H4('Dash provides combination of web page design and Python programming. Users can achieve and visualize unlimited ideas.', style={'color':'inherit','line-height':'1.1rem','font-size':'14px'})
                        ],className='homeIconContainer'),
                        
                        html.Div([
                            html.I('  100% open source language',className='fa fa-file-code-o', style={'color':'inherit','font-weight':500,'line-height':'1.1rem','font-size':'23px','margin-top':'10px','margin-bottom':'10px'}),
                            html.H4('All packages used in the development are 100% free.', style={'color':'inherit','line-height':'1.1rem','font-size':'14px'})
                        ],className='homeIconContainer'),
                        
                        html.Div([
                            html.I('  Styled in Python and CSS',className='fa fa-css3', style={'color':'inherit','font-weight':500,'line-height':'1.1rem','font-size':'23px','margin-top':'10px','margin-bottom':'10px'}),
                            html.H4('Web styles can be specified in CSS or directly in Python, depneding on user\'s preference.', style={'color':'inherit','line-height':'1.1rem','font-size':'14px'})
                        ],className='homeIconContainer'),
                        
                        html.Div([
                            html.I('  Responsive Design',className='fa fa-desktop', style={'color':'inherit','font-weight':500,'line-height':'1.1rem','font-size':'23px','margin-top':'10px','margin-bottom':'10px'}),
                            html.H4('The layout of elements are designed responsively for different devices and screen sizes.', style={'color':'inherit','line-height':'1.1rem','font-size':'14px'})
                        ],className='homeIconContainer'),
                        
                        html.Div([
                            html.I('  Link to Cloud Database',className='fa fa-cloud-upload', style={'color':'inherit','font-weight':500,'line-height':'1.1rem','font-size':'23px','margin-top':'10px','margin-bottom':'10px'}),
                            html.H4('Heroku provides addons to connect with salesforce.com, which provides cloud solution for datawarehouse.', style={'color':'inherit','line-height':'1.1rem','font-size':'14px'})
                        ],className='homeIconContainer'),
                        
                        
                        
                    ],style={'margin-top':'20px','display':'block'})
                ],style={'margin-right':'0px','margin-left':'0px','width':'100%','display':'block','box-sizing':'border-box'})
            ],className="rowHome",style={"margin-bottom": "0px",'background':'#ffffff','min-height':'400px'}),

    ])

@app.callback(
    Output('date-selector', 'options'),
    [Input('url', 'pathname')])
def display_value(path):
    if path == '/squirrel/home':
        data = pd.read_csv('Records.csv')
        dates = data['Date'].tolist()
        date_list1 = set()
        date_list = [x for x in dates if not (x in date_list1 or date_list1.add(x))]
        
        return [{'label': i, 'value': i} for i in date_list[12:]]
    else:
        raise PreventUpdate

@app.callback(
    Output('date_selected','children'),
    [Input('date-selector', 'value')])
def display_value1(value):
    return value




