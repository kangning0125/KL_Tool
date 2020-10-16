#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 23:05:23 2020

@author: kangningli
"""

import dash_html_components as html
import dash_core_components as dcc
import dash
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc

from app import app
from layout import app2, pageHome, pageDashboard, pageReport, pageAbout


create_body = html.Div(id='page-content',
    children=[
    # header row
    html.Div([
        html.Div([
            html.Div([
                html.Img(src=app.get_asset_url('squirrel_icon.png'),style={'width':100,'height':'100%','padding-left':'20px'}) #https://pnglibs.com/images/bt/squirrel-clipart-transparent-background-6.png
            ],style={'text-align':'center','width':'150px'}),
            html.Div(['Squirrel: the family finance planner'],className='appHeader'),
            dbc.ButtonGroup(
                [dbc.Button("中文", className="btn-primary"), dbc.Button("English",className="btn-primary")],className='btn-lang'),
        ],style={'display':'inline-flex','vertical-align':'bottom','height':'100%','margin-left':0,'width':'100%','min':''}),
    ],className='headerRow'),
    # end of header row
    # display
    html.Div(id='page_display',
        children=[
        html.Div(id='menu',className='Menu',
                children=[
                html.Div(['Navigation'],style={'font-size':'larger','font-weight':'bold','margin-top':'20px','margin-bottom':'10px','padding-left':'20px'}),    
                html.Div([
                    html.Div([
                        html.I(className='fa fa-home',style={'display':'inline','margin-right':'10px'}),
                        dcc.Link('Home',id='menu_home',href='/squirrel/home',style={'display':'inline','text-decoration':'none','color': '#b7b1b1'}),
                        ],className='menu_item'),
                    html.Div([
                        html.I(className='fa fa-bar-chart',style={'display':'inline','margin-right':'10px'}),
                        dcc.Link('Dashboard',id='menu_item1',href='/squirrel/dashboard',style={'display':'inline','text-decoration':'none','color': '#b7b1b1'}),
                        ],className='menu_item'),
                    
                    html.Div([
                        html.I(className='fa fa-file-text-o',style={'display':'inline','margin-right':'13px'}),
                        dcc.Link('Report',id='menu_item4',href='/squirrel/FinancialReport',style={'display':'inline','text-decoration':'none','color': '#b7b1b1'}),
                        ],className='menu_item'),
                    
                    html.Div([
                        html.I(className='fa fa-paint-brush',style={'display':'inline','margin-right':'10px'}),
                        dcc.Link('Record',id='menu_item2',href='/squirrel/logging',style={'display':'inline','text-decoration':'none','color': '#b7b1b1'}),
                        ],className='menu_item'),
                    
                    html.Div([
                        html.I(className='fa fa-address-card',style={'display':'inline','margin-right':'9px'}),
                        dcc.Link('About Us',id='menu_item3',href='/squirrel/aboutus',style={'display':'inline','text-decoration':'none','color': '#b7b1b1'}),
                        ],className='menu_item'),
                    
                    html.Div(['© 2020 Kangning Li'],style={'bottom':'15px','position':'absolute'})  
                ],style={'margin-left':'5px'}),    
                 ]),
         html.Div(id='dashboard_display',style={'display':'inline-block','width':'80%','vertical-align':'text-top','margin-top':0,'height':'95%','margin-left':'20px','overflow':'auto'}),   
         html.Div('1/31/2016',id='date_selected',style={'display':'none'})   
        ],style={'display':'inline'},)                       
                           
    ], className='wrapper',style={'margin':0})

@app.callback(
            Output('dashboard_display','children'),
            [Input('url','pathname')]        
)
def display_page(path):
    if path == '/squirrel/home':
        return pageHome.layout
    elif path == '/squirrel/dashboard':
        return pageDashboard.layout
    elif path == '/squirrel/logging':
        return app2.layout
    elif path == '/squirrel/FinancialReport':
        return [pageReport.layout_1, pageReport.layout_2, pageReport.layout_3, pageReport.layout_4]
    elif path == "/squirrel/aboutus":
        return pageAbout.layout
    else:
        return html.Div(['Home Page'])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    