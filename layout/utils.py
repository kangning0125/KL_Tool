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
                html.Img(src='https://n7.nextpng.com/sticker-png/599/270/sticker-png-computer-icons-directory-the-haute-gurney-kl-binder-angle-text-rectangle-logo.png',style={'width':100,'height':60})
            ],style={'text-align':'center','width':'11%'}),
            html.Div(['This is my app!']),
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
                    dcc.Link('Home',id='menu_home',href='/KLTool/home',className='menu_item'),
                    dcc.Link('Item1',id='menu_item1',href='/KLTool/page1',className='menu_item'),
                    dcc.Link('Item2',id='menu_item2',href='/KLTool/page2',className='menu_item'),
                    dcc.Link('Item3',id='menu_item3',href='/KLTool/page3',className='menu_item'),
                    dcc.Link('Item4',id='menu_item4',href='/KLTool/page4',className='menu_item'),                     
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
    if path == '/KLTool/home':
        return html.Div(['Home Page'])
    elif path == '/KLTool/page1':
        return app1.layout
    elif path == '/KLTool/page2':
        return app2.layout
    else:
        return html.Div(['I don\'t know what to put here yet!'])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    