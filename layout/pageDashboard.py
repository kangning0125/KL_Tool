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

layout = html.Div(id='page_dash',
         children=[
            html.Div([
                html.Div(['Dashboard'],className='rowHeader',style={'font-size':'24px'}),
                html.Div([
                    html.Div(['Net Worth'],className='summaryContainer',style={'background':'#348fe2'}),
                    html.Div(['Assets'],className='summaryContainer',style={'margin-left':'10px','background':'#49b6d6'}),
                    html.Div(['Liabilities'],className='summaryContainer',style={'margin-left':'10px','background':'#f59c1a'}),
                    
                    ],style={'height':'120px','width':'95%','margin-left':'0px','margin-right':'0px','display':'flex','flex-wrap':'wrap'})
            
            ],className='row',style={'overflow-x':'auto'}),
            
            html.Div([
                html.Div([ # Wide charts column
                    html.Div([
                        html.Div(['Wide Plot 1'],className='chartHeader',style={}),
                        html.Div([],className='chartBody',style={}),
                    ],className='chartContainer'),
                    html.Div([
                        html.Div(['Wide Plot 2'],className='chartHeader',style={}),
                        html.Div([],className='chartBody',style={}),
                    ],className='chartContainer'),
                ],className='column12',style={'height':'1500px'}), #end of wide chart column
                
                html.Div([ # Narrow charts column
                    html.Div([
                        html.Div(['Narrow Plot 1'],className='chartHeader',style={}),
                        html.Div([],className='chartBody',style={}),
                    ],className='chartContainer'),
                    html.Div([
                        html.Div(['Narrow Plot 2'],className='chartHeader',style={}),
                        html.Div([],className='chartBody',style={}),
                    ],className='chartContainer'),
                ],className='column6',style={'height':'1500px','margin-left':'20px'}), #end of narrow chart column
                
                ],className='row',style={'display':'inline-flex','overflow-y':'auto','max-height':'330px','width':'100%'}),


],style={'display':'block','height':'100%','width':'100%'})


