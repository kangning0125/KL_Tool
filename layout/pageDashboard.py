#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 21:43:14 2020

@author: kangningli
"""


import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

import pandas as pd
import numpy as np

from src import calculations, page_plot

from app import app

dash_icon_style = {'color':'#00000026','position':'absolute','font-size':'42px','height':'56px','width':'56px',
                   'text-align':'center','line-height':'56px','right':'15px','top':'15px','margin-left':'15px'}


layout = html.Div(id='page_dash',
         children=[
            html.Div([
                html.Div(['Dashboard'],className='rowHeader',style={'font-size':'24px'}),
                html.Div([ # Summary Numbers Containers Row
                    html.Div([ #Net worth Container
                        html.I(className='fa fa-usd',style=dash_icon_style),
                        html.Div([
                            html.H4(['NET WORTH']),
                            html.P(['200,000'],id='net_worth_num',className='statusInfo')                            
                        ],style={'display':'block','padding':'20px'}),
                    ],className='summaryContainer',style={'background':'#348fe2'}), # End of Net worth Container
                    
                    html.Div([
                        html.I(className='fa fa-bank',style=dash_icon_style),
                        html.Div([
                            html.H4(['TOTAL ASSETS']),
                            html.P(['700,000'],id='asset_num',className='statusInfo')                            
                        ],style={'display':'block','padding':'20px'}),
                    ],className='summaryContainer',style={'margin-left':'0px','background':'#49b6d6'}),
                    
                    html.Div([
                        html.I(className='fa fa-sign-out',style=dash_icon_style),    
                        html.Div([
                            html.H4(['LIABILITIES']),
                            html.P(['200,000'],id='liability_num',className='statusInfo')                            
                        ],style={'display':'block','padding':'20px'}),
                    ],className='summaryContainer',style={'margin-left':'0px','background':'#f59c1a'}),
                    
                    html.Div([
                        html.I(className='fa fa-calendar',style=dash_icon_style),
                        html.Div([
                            html.H4(['CALENDAR']),
                            html.P(['01/31/2015'],id='calendar_str',className='statusInfo')                            
                        ],style={'display':'block','padding':'20px'}),
                    ],className='summaryContainer',style={'margin-left':'0px','background':'#ff5b57'}),
                    
                ],style={'height':'120px','width':'100%','margin-left':'0px','margin-right':'0px','display':'flex','flex-wrap':'wrap','overflow':'auto'})
            
            ],className='rowDash',style={'overflow-x':'auto'}),
            
            html.Div([
                html.Div([ # Wide charts column
                    html.Div([
                        html.Div(['Net Worth Attribution'],className='chartHeader',style={}),
                        html.Div([
                            dcc.Graph(id='waterfall',
                                figure={          
                                },style={'margin-top':'0px','overflow-y':'hidden','height':'270px','width':'600px','maxHeight':'300px','background':'white'}
                            )
                            
                        ],className='chartBody',style={}),
                    ],className='chartContainer'),
                    html.Div([
                        html.Div(['Asset Balance'],className='chartHeader',style={}),
                        html.Div([
                            dcc.Graph(id='12_mo_line',
                                figure={          
                                },style={'margin-top':'0px','overflow-y':'hidden','height':'270px','width':'600px','maxHeight':'300px','background':'white'}
                            )    
                        ],className='chartBody',style={}),
                    ],className='chartContainer'),
                ],className='column12',style={'height':'800px'}), #end of wide chart column
                
                html.Div([ # Narrow charts column
                    html.Div([
                        html.Div(['3-Tier Asset Allocation'],className='chartHeader',style={}),
                        html.Div([
                            dcc.Graph(id='asset_tier_bar',
                                figure={          
                                },
                                config={'displayModeBar': False},
                                style={'margin-bottom':'0px','overflow-y':'hidden','height':'270px','width':'300px','maxHeight':'300px','background':'white'}
                            )                             
                        ],className='chartBody',style={}),
                    ],className='chartContainer'),
                    
                    html.Div([
                        html.Div(['Assets Composition'],className='chartHeader',style={}),
                        html.Div([
                            dcc.Graph(id='asset_pie',
                                figure={          
                                },
                                config={'displayModeBar': False},
                                style={'margin-top':'0px','overflow-y':'hidden','height':'270px','width':'300px','maxHeight':'300px','background':'white'}
                            )    
                        ],className='chartBody',style={}),
                    ],className='chartContainer'),
                ],className='column6',style={'height':'800px','margin-left':'20px'}), #end of narrow chart column
                
                ],className='rowDash',style={'display':'inline-flex','overflow-y':'auto','max-height':'900px','width':'100%'}),


],style={'display':'block','height':'98%','width':'100%'})

@app.callback(
    [Output('net_worth_num','children'),
     Output('asset_num','children'),
     Output('liability_num','children'),
     Output('calendar_str','children')],    
    [Input('url','pathname')],
    [State('date_selected','children')])
def update_summary_info(url,month_end):
    if url == '/squirrel/dashboard':
        data = pd.read_csv('Records.csv')    
        net_worth, assets, liability = calculations.finance_metric_calc(data,month_end)
        net_worth_str = f"{net_worth:,.0f}"
        asset_str = f"{assets:,.0f}"
        liability_str = f"{liability:,.0f}"
        return [net_worth_str,asset_str,liability_str,month_end]
    else:
        raise PreventUpdate
        
@app.callback(
    [Output('waterfall','figure'),
     Output('12_mo_line','figure'),
     Output('asset_tier_bar','figure'),
     Output('asset_pie','figure')],
    [Input('url','pathname')],
    [State('date_selected','children')])
def update_dash_plots(url,month_end):
    if url == '/squirrel/dashboard':
        data = pd.read_csv('Records.csv') 
        interval='month'
        asset_name='Asset'
        fig_waterfall = page_plot.waterfall(data, month_end, interval)
        fig_line = page_plot.dash_line(data, month_end, asset_name)
        fig_bar = page_plot.dash_stackbar(data, month_end)
        fig_pie = page_plot.dash_pie(data, month_end, 'Total')
        return [fig_waterfall,fig_line,fig_bar,fig_pie]
    else:
        raise PreventUpdate        
