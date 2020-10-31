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
                    
                ],className='summaryRow')
            
            ],className='rowDash',style={'overflow-x':'auto'}),
            
            html.Div([
                html.Div([ # Wide charts column
                    html.Div([
                        html.Div([
                            'Net Worth Attribution',
                            html.Div([
                                html.I(className='fa fa-times-circle chartHeaderButton',id='close_btn_w1',style={'color':'red'}),
                                html.I(className='fa fa-minus-circle chartHeaderButton',id='hide_btn_w1',style={'color':'orange'}),
                                html.I(className='fa fa-repeat chartHeaderButton',style={'color':'#60f704'})   
                            ],style={'float':'right','width':'100px'})
                            
                        ],className='chartHeader'),
                        html.Div([
                            dcc.Graph(id='waterfall',
                                figure={          
                                },style={'margin-top':'0px','overflow-y':'hidden','height':'270px','width':'600px','maxHeight':'300px','background':'white'}
                            )
                            
                        ],className='chartBody',style={'padding-top':'15px'},id='chartpanel_wide_1'),
                    ],className='chartContainer',id='chart_wide_1'),
                    html.Div([
                        html.Div([
                            'Asset Balance',
                            html.Div([
                                html.I(className='fa fa-times-circle chartHeaderButton',id='close_btn_w2',style={'color':'red'}),
                                html.I(className='fa fa-minus-circle chartHeaderButton',id='hide_btn_w2',style={'color':'orange'}),
                                html.I(className='fa fa-repeat chartHeaderButton',style={'color':'#60f704'})   
                            ],style={'float':'right','width':'100px'})
                        ],className='chartHeader',style={}),
                        html.Div([
                            dcc.Graph(id='12_mo_line',
                                figure={          
                                },style={'margin-top':'0px','overflow-y':'hidden','height':'270px','width':'600px','maxHeight':'300px','background':'white'}
                            )    
                        ],className='chartBody',style={'padding-top':'15px'},id='chartpanel_wide_2'),
                    ],className='chartContainer',id='chart_wide_2'),
                ],className='column12',style={'min-height':'100px'}), #end of wide chart column
                
                html.Div([ # Narrow charts column
                    html.Div([
                        html.Div([
                            '3-Tier Asset Allocation',
                            html.Div([
                                html.I(className='fa fa-times-circle chartHeaderButton',id='close_btn_n1',style={'color':'red'}),
                                html.I(className='fa fa-minus-circle chartHeaderButton',id='hide_btn_n1',style={'color':'orange'}),
                                html.I(className='fa fa-repeat chartHeaderButton',style={'color':'#60f704'})   
                            ],style={'float':'right','width':'100px'})
                            
                        ],className='chartHeader',style={}),
                        html.Div([
                            dcc.Graph(id='asset_tier_bar',
                                figure={          
                                },
                                config={'displayModeBar': False},
                                style={'margin-bottom':'0px','overflow-y':'hidden','height':'270px','width':'300px','maxHeight':'300px','background':'white'}
                            )                             
                        ],className='chartBody',style={},id='chartpanel_narrow_1'),
                    ],className='chartContainer',id='chart_narrow_1'),
                    
                    html.Div([
                        html.Div([
                            'Assets Composition',
                            html.Div([
                                html.I(className='fa fa-times-circle chartHeaderButton',id='close_btn_n2',style={'color':'red'}),
                                html.I(className='fa fa-minus-circle chartHeaderButton',id='hide_btn_n2',style={'color':'orange'}),
                                html.I(className='fa fa-repeat chartHeaderButton',style={'color':'#60f704'})   
                            ],style={'float':'right','width':'100px'})
                        ],className='chartHeader',style={}),
                        html.Div([
                            dcc.Graph(id='asset_pie',
                                figure={          
                                },
                                config={'displayModeBar': False},
                                style={'margin-top':'0px','overflow-y':'hidden','height':'270px','width':'300px','maxHeight':'300px','background':'white'}
                            )    
                        ],className='chartBody',style={},id='chartpanel_narrow_2'),
                    ],className='chartContainer',id='chart_narrow_2'),
                ],className='column6',style={'min-height':'100px','margin-left':'20px'}), #end of narrow chart column
                
                ],className='rowDash',style={'display':'inline-flex','overflow-y':'auto','height':'80%','width':'100%','padding-bottom':'100px'}),


],style={'display':'block','height':'98%','width':'100%','overflow':'hidden'})

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


######### Define Panel Control Buttons ###########
@app.callback(
    Output('chart_wide_1','style'),
    [Input('close_btn_w1','n_clicks')]    
)
def panel_display_change(click):
    trigger = dash.callback_context.triggered[0]
    close_style = {'display':'none'}
    if 'w1' in trigger['prop_id']:
        return close_style

    else:
        raise PreventUpdate()
    
@app.callback(
    Output('chart_wide_2','style'),
    [Input('close_btn_w2','n_clicks')]    
)
def panel_display_change(click):
    trigger = dash.callback_context.triggered[0]
    close_style = {'display':'none'}
    if 'w2' in trigger['prop_id']:
        return close_style

    else:
        raise PreventUpdate()
    
@app.callback(
    Output('chart_narrow_1','style'),
    [Input('close_btn_n1','n_clicks')]    
)
def panel_display_change(click):
    trigger = dash.callback_context.triggered[0]
    close_style = {'display':'none'}
    if 'n1' in trigger['prop_id']:
        return close_style

    else:
        raise PreventUpdate()
        
@app.callback(
    Output('chart_narrow_2','style'),
    [Input('close_btn_n2','n_clicks')]    
)
def panel_display_change(click):
    trigger = dash.callback_context.triggered[0]
    close_style = {'display':'none'}
    if 'n2' in trigger['prop_id']:
        return close_style

    else:
        raise PreventUpdate()

@app.callback(
    Output('chartpanel_wide_1','style'),
    [Input('hide_btn_w1','n_clicks')],
    [State('chartpanel_wide_1','style')]    
)
def panel_display_change(click,style):
    trigger = dash.callback_context.triggered[0]
    hide_style = {'display':'none'}
    show_style = {'padding-top':'15px'}
    if 'w1' in trigger['prop_id']:
        if style == {'display':'none'}:
            return show_style
        else:
            return hide_style

    else:
        raise PreventUpdate()  
        
@app.callback(
    Output('chartpanel_wide_2','style'),
    [Input('hide_btn_w2','n_clicks')],
    [State('chartpanel_wide_2','style')]    
)
def panel_display_change(click,style):
    trigger = dash.callback_context.triggered[0]
    hide_style = {'display':'none'}
    show_style = {'padding-top':'15px'}
    if 'w2' in trigger['prop_id']:
        if style == {'display':'none'}:
            return show_style
        else:
            return hide_style

    else:
        raise PreventUpdate()
        
@app.callback(
    Output('chartpanel_narrow_1','style'),
    [Input('hide_btn_n1','n_clicks')],
    [State('chartpanel_narrow_1','style')]    
)
def panel_display_change(click,style):
    trigger = dash.callback_context.triggered[0]
    hide_style = {'display':'none'}
    show_style = {}
    if 'n1' in trigger['prop_id']:
        if style == {'display':'none'}:
            return show_style
        else:
            return hide_style

    else:
        raise PreventUpdate()

@app.callback(
    Output('chartpanel_narrow_2','style'),
    [Input('hide_btn_n2','n_clicks')],
    [State('chartpanel_narrow_2','style')]    
)
def panel_display_change(click,style):
    trigger = dash.callback_context.triggered[0]
    hide_style = {'display':'none'}
    show_style = {}
    if 'n2' in trigger['prop_id']:
        if style == {'display':'none'}:
            return show_style
        else:
            return hide_style

    else:
        raise PreventUpdate()
    
    
    
    