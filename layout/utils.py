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

from app import app
from layout import app1, app2


create_body = html.Div(id='page-content',
    children=[
    # header row
    html.Div([
        html.Div([
            html.Div([
                html.Img(src=app.get_asset_url('squirrel_icon.png'),style={'width':100,'height':60}) #https://pnglibs.com/images/bt/squirrel-clipart-transparent-background-6.png
            ],style={'text-align':'center','width':'11%'}),
            html.Div(['Squirrel: the family finance planner'],className='appHeader'),
        ],style={'display':'inline-flex','vertical-align':'bottom','height':'100%','margin-left':0,'width':'100%'}),
    ],className='rowHeader'),
    # end of header row
    # display
    html.Div(id='page_display',
        children=[
        html.Div(id='menu',className='Menu',
                children=[
                html.Div(['Menu'],style={'text-align':'center','font-size':'larger','font-weight':'bold','margin-top':'20px'}),    
                html.Div([
                    dcc.Link('Home',id='menu_home',href='/squirrel/home',className='menu_item'),
                    dcc.Link('Dashboard',id='menu_item1',href='/squirrel/dashboard',className='menu_item'),
                    dcc.Link('Log it',id='menu_item2',href='/squirrel/logging',className='menu_item'),
                    dcc.Link('Report',id='menu_item3',href='/squirrel/FinancialReport',className='menu_item'),
                    dcc.Link('About Us',id='menu_item4',href='/squirrel/aboutus',className='menu_item'),                     
                ],style={'margin-left':'5px'}),    
                 ],style={'height':'700px'}),
         html.Div(id='dashboard_display',style={'display':'inline-flex','width':'90%','vertical-align':'text-top','margin-top':0,'height':'690px'}),   
            
        ]),                       
                           
    ], className='wrapper',style={'margin':0})

@app.callback(
            Output('dashboard_display','children'),
            [Input('url','pathname')]        
)
def display_page(path):
    if path == '/squirrel/home':
        return html.Div(['Home Page'])
    elif path == '/squirrel/dashboard':
        return app1.layout
    elif path == '/squirrel/logging':
        return app2.layout
    elif path == '/squirrel/FinancialReport':
        return html.Div('This is your personal financial report')
    elif path == "/squirrel/aboutus":
        return html.Div('This is about us page')
    else:
        return html.Div(['Home Page'])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    