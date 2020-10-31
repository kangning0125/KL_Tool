#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 21:43:14 2020

@author: kangningli
"""

import dash
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


layout = html.Div(id='page_dashCN',
         children=[
            html.Div([
                html.Div(['Dashboard'],className='rowHeader',style={'font-size':'24px'}),
                html.Div([ # Summary Numbers Containers Row
                    html.Div([ #Net worth Container
                        html.I(className='fa fa-usd',style=dash_icon_style),
                        html.Div([
                            html.H4(['财富净值']),
                            html.P(['200,000'],id='net_worth_numCN',className='statusInfo')                            
                        ],style={'display':'block','padding':'20px'}),
                    ],className='summaryContainer',style={'background':'#348fe2'}), # End of Net worth Container
                    
                    html.Div([
                        html.I(className='fa fa-bank',style=dash_icon_style),
                        html.Div([
                            html.H4(['总资产']),
                            html.P(['700,000'],id='asset_numCN',className='statusInfo')                            
                        ],style={'display':'block','padding':'20px'}),
                    ],className='summaryContainer',style={'margin-left':'0px','background':'#49b6d6'}),
                    
                    html.Div([
                        html.I(className='fa fa-sign-out',style=dash_icon_style),    
                        html.Div([
                            html.H4(['个人债务']),
                            html.P(['200,000'],id='liability_numCN',className='statusInfo')                            
                        ],style={'display':'block','padding':'20px'}),
                    ],className='summaryContainer',style={'margin-left':'0px','background':'#f59c1a'}),
                    
                    html.Div([
                        html.I(className='fa fa-calendar',style=dash_icon_style),
                        html.Div([
                            html.H4(['日历']),
                            html.P(['01/31/2015'],id='calendar_strCN',className='statusInfo')                            
                        ],style={'display':'block','padding':'20px'}),
                    ],className='summaryContainer',style={'margin-left':'0px','background':'#ff5b57'}),
                    
                ],className='summaryRow')
            
            ],className='rowDash',style={'overflow-x':'auto'}),
            
            html.Div([
                html.Div([ # Wide charts column
                    html.Div([
                        html.Div([
                            '个人净值归因分析',
                            html.Div([
                                html.I(className='fa fa-times-circle chartHeaderButton',id='close_btn_w1cn',style={'color':'red'}),
                                html.I(className='fa fa-minus-circle chartHeaderButton',id='hide_btn_w1cn',style={'color':'orange'}),
                                html.I(className='fa fa-repeat chartHeaderButton',style={'color':'#60f704'})   
                            ],style={'float':'right','width':'100px'})
                            
                        ],className='chartHeader'),
                        html.Div([
                            dcc.Graph(id='waterfallCN',
                                figure={          
                                },style={'margin-top':'0px','overflow-y':'hidden','height':'270px','width':'600px','maxHeight':'300px','background':'white'}
                            )
                            
                        ],className='chartBody',style={'padding-top':'15px'},id='chartpanel_wide_1cn'),
                    ],className='chartContainer',id='chart_wide_1cn'),
                    html.Div([
                        html.Div([
                            '资产成长趋势',
                            html.Div([
                                html.I(className='fa fa-times-circle chartHeaderButton',id='close_btn_w2cn',style={'color':'red'}),
                                html.I(className='fa fa-minus-circle chartHeaderButton',id='hide_btn_w2cn',style={'color':'orange'}),
                                html.I(className='fa fa-repeat chartHeaderButton',style={'color':'#60f704'})   
                            ],style={'float':'right','width':'100px'})
                        ],className='chartHeader',style={}),
                        html.Div([
                            dcc.Graph(id='12_mo_lineCN',
                                figure={          
                                },style={'margin-top':'0px','overflow-y':'hidden','height':'270px','width':'600px','maxHeight':'300px','background':'white'}
                            )    
                        ],className='chartBody',style={'padding-top':'15px'},id='chartpanel_wide_2cn'),
                    ],className='chartContainer',id='chart_wide_2cn'),
                ],className='column12',style={'min-height':'100px'}), #end of wide chart column
                
                html.Div([ # Narrow charts column
                    html.Div([
                        html.Div([
                            '三级资产分布',
                            html.Div([
                                html.I(className='fa fa-times-circle chartHeaderButton',id='close_btn_n1cn',style={'color':'red'}),
                                html.I(className='fa fa-minus-circle chartHeaderButton',id='hide_btn_n1cn',style={'color':'orange'}),
                                html.I(className='fa fa-repeat chartHeaderButton',style={'color':'#60f704'})   
                            ],style={'float':'right','width':'100px'})
                            
                        ],className='chartHeader',style={}),
                        html.Div([
                            dcc.Graph(id='asset_tier_barCN',
                                figure={          
                                },
                                config={'displayModeBar': False},
                                style={'margin-bottom':'0px','overflow-y':'hidden','height':'270px','width':'300px','maxHeight':'300px','background':'white'}
                            )                             
                        ],className='chartBody',style={},id='chartpanel_narrow_1cn'),
                    ],className='chartContainer',id='chart_narrow_1cn'),
                    
                    html.Div([
                        html.Div([
                            '资产构成分析',
                            html.Div([
                                html.I(className='fa fa-times-circle chartHeaderButton',id='close_btn_n2cn',style={'color':'red'}),
                                html.I(className='fa fa-minus-circle chartHeaderButton',id='hide_btn_n2cn',style={'color':'orange'}),
                                html.I(className='fa fa-repeat chartHeaderButton',style={'color':'#60f704'})   
                            ],style={'float':'right','width':'100px'})
                        ],className='chartHeader',style={}),
                        html.Div([
                            dcc.Graph(id='asset_pieCN',
                                figure={          
                                },
                                config={'displayModeBar': False},
                                style={'margin-top':'0px','overflow-y':'hidden','height':'270px','width':'300px','maxHeight':'300px','background':'white'}
                            )    
                        ],className='chartBody',style={},id='chartpanel_narrow_2cn'),
                    ],className='chartContainer',id='chart_narrow_2cn'),
                ],className='column6',style={'min-height':'100px','margin-left':'20px'}), #end of narrow chart column
                
                ],className='rowDash',style={'display':'inline-flex','overflow-y':'auto','height':'80%','width':'100%','padding-bottom':'100px'}),


],style={'display':'block','height':'98%','width':'100%','overflow':'hidden'})

@app.callback(
    [Output('net_worth_numCN','children'),
     Output('asset_numCN','children'),
     Output('liability_numCN','children'),
     Output('calendar_strCN','children')],    
    [Input('url','pathname')],
    [State('date_selectedCN','children')])
def update_summary_info(url,month_end):
    if url == '/squirrel_cn/dashboard':
        data = pd.read_csv('Records.csv')    
        net_worth, assets, liability = calculations.finance_metric_calc(data,month_end)
        net_worth_str = f"{net_worth:,.0f}"
        asset_str = f"{assets:,.0f}"
        liability_str = f"{liability:,.0f}"
        return [net_worth_str,asset_str,liability_str,month_end]
    else:
        raise PreventUpdate
        
@app.callback(
    [Output('waterfallCN','figure'),
     Output('12_mo_lineCN','figure'),
     Output('asset_tier_barCN','figure'),
     Output('asset_pieCN','figure')],
    [Input('url','pathname')],
    [State('date_selectedCN','children')])
def update_dash_plots(url,month_end):
    if url == '/squirrel_cn/dashboard':
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
        
######### Define Panel Control Buttons ###########
@app.callback(
    Output('chart_wide_1cn','style'),
    [Input('close_btn_w1cn','n_clicks')]    
)
def panel_display_change(click):
    trigger = dash.callback_context.triggered[0]
    close_style = {'display':'none'}
    if 'w1cn' in trigger['prop_id']:
        return close_style

    else:
        raise PreventUpdate()
    
@app.callback(
    Output('chart_wide_2cn','style'),
    [Input('close_btn_w2cn','n_clicks')]    
)
def panel_display_change(click):
    trigger = dash.callback_context.triggered[0]
    close_style = {'display':'none'}
    if 'w2cn' in trigger['prop_id']:
        return close_style

    else:
        raise PreventUpdate()
    
@app.callback(
    Output('chart_narrow_1cn','style'),
    [Input('close_btn_n1cn','n_clicks')]    
)
def panel_display_change(click):
    trigger = dash.callback_context.triggered[0]
    close_style = {'display':'none'}
    if 'n1cn' in trigger['prop_id']:
        return close_style

    else:
        raise PreventUpdate()
        
@app.callback(
    Output('chart_narrow_2cn','style'),
    [Input('close_btn_n2cn','n_clicks')]    
)
def panel_display_change(click):
    trigger = dash.callback_context.triggered[0]
    close_style = {'display':'none'}
    if 'n2cn' in trigger['prop_id']:
        return close_style

    else:
        raise PreventUpdate()

@app.callback(
    Output('chartpanel_wide_1cn','style'),
    [Input('hide_btn_w1cn','n_clicks')],
    [State('chartpanel_wide_1cn','style')]    
)
def panel_display_change(click,style):
    trigger = dash.callback_context.triggered[0]
    hide_style = {'display':'none'}
    show_style = {'padding-top':'15px'}
    if 'w1cn' in trigger['prop_id']:
        if style == {'display':'none'}:
            return show_style
        else:
            return hide_style

    else:
        raise PreventUpdate()  
        
@app.callback(
    Output('chartpanel_wide_2cn','style'),
    [Input('hide_btn_w2cn','n_clicks')],
    [State('chartpanel_wide_2cn','style')]    
)
def panel_display_change(click,style):
    trigger = dash.callback_context.triggered[0]
    hide_style = {'display':'none'}
    show_style = {'padding-top':'15px'}
    if 'w2cn' in trigger['prop_id']:
        if style == {'display':'none'}:
            return show_style
        else:
            return hide_style

    else:
        raise PreventUpdate()
        
@app.callback(
    Output('chartpanel_narrow_1cn','style'),
    [Input('hide_btn_n1cn','n_clicks')],
    [State('chartpanel_narrow_1cn','style')]    
)
def panel_display_change(click,style):
    trigger = dash.callback_context.triggered[0]
    hide_style = {'display':'none'}
    show_style = {}
    if 'n1cn' in trigger['prop_id']:
        if style == {'display':'none'}:
            return show_style
        else:
            return hide_style

    else:
        raise PreventUpdate()

@app.callback(
    Output('chartpanel_narrow_2cn','style'),
    [Input('hide_btn_n2cn','n_clicks')],
    [State('chartpanel_narrow_2cn','style')]    
)
def panel_display_change(click,style):
    trigger = dash.callback_context.triggered[0]
    hide_style = {'display':'none'}
    show_style = {}
    if 'n2cn' in trigger['prop_id']:
        if style == {'display':'none'}:
            return show_style
        else:
            return hide_style

    else:
        raise PreventUpdate()
    
