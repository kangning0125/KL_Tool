#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 23:05:23 2020

@author: kangningli
"""

import dash_html_components as html
import dash_core_components as dcc
import dash
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc

from app import app
from layout import app2, pageHome, pageDashboard, pageReport, pageAbout
from layout import pageHomeCN, pageDashboardCN, pageReportCN, pageAboutCN


menu_en = [
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
            ],style={'margin-left':'5px'})]

menu_cn = [
            html.Div(['目录'],style={'font-size':'larger','font-weight':'bold','margin-top':'20px','margin-bottom':'10px','padding-left':'20px'}),    
            html.Div([
                html.Div([
                    html.I(className='fa fa-home',style={'display':'inline','margin-right':'10px'}),
                    dcc.Link('主页',id='menu_home',href='/squirrel_cn/home',style={'display':'inline','text-decoration':'none','color': '#b7b1b1'}),
                    ],className='menu_item'),
                html.Div([
                    html.I(className='fa fa-bar-chart',style={'display':'inline','margin-right':'10px'}),
                    dcc.Link('本月汇总',id='menu_item1',href='/squirrel_cn/dashboard',style={'display':'inline','text-decoration':'none','color': '#b7b1b1'}),
                    ],className='menu_item'),
                
                html.Div([
                    html.I(className='fa fa-file-text-o',style={'display':'inline','margin-right':'13px'}),
                    dcc.Link('财富报告',id='menu_item4',href='/squirrel_cn/FinancialReport',style={'display':'inline','text-decoration':'none','color': '#b7b1b1'}),
                    ],className='menu_item'),
                
                html.Div([
                    html.I(className='fa fa-paint-brush',style={'display':'inline','margin-right':'10px'}),
                    dcc.Link('录入',id='menu_item2',href='/squirrel_cn/logging',style={'display':'inline','text-decoration':'none','color': '#b7b1b1'}),
                    ],className='menu_item'),
                
                html.Div([
                    html.I(className='fa fa-address-card',style={'display':'inline','margin-right':'9px'}),
                    dcc.Link('关于我们',id='menu_item3',href='/squirrel_cn/aboutus',style={'display':'inline','text-decoration':'none','color': '#b7b1b1'}),
                    ],className='menu_item'),
                
                html.Div(['© 2020 李康宁 & 崔宪'],style={'bottom':'15px','position':'absolute'})  
            ],style={'margin-left':'5px'})]



create_body = html.Div(id='page-content',
    children=[
    # header row
    html.Div([
        html.Div([
            html.Div([
                html.Img(src=app.get_asset_url('squirrel_icon.png'),style={'width':100,'height':'100%','padding-left':'20px'}) #https://pnglibs.com/images/bt/squirrel-clipart-transparent-background-6.png
            ],style={'text-align':'center','width':'150px'}),
            html.Div(['Squirrel'],className='appHeader',style={'width':'70px'}),
            html.Div(['The family finance planner'],className='appHeader',style={'border-left':'2px solid #f4682b','padding-left':'5px','margin-top':'10px','padding-top':'25px'}),
            dbc.ButtonGroup(
                [dbc.Button("中文", className="btn-primary", id='button_cn'), dbc.Button("English",className="btn-primary",id='button_en')],className='btn-lang'),
        ],style={'display':'inline-flex','vertical-align':'bottom','height':'100%','margin-left':0,'width':'100%','min':''}),
    ],className='headerRow'),
    # end of header row
    # display
    html.Div(id='page_display',
        children=[
        html.Div(id='menu',className='Menu',
                children=menu_en),
         html.Div(id='dashboard_display_en',style={'display':'inline-block','width':'80%','vertical-align':'text-top','margin-top':0,'height':'95%','margin-left':'20px','overflow':'auto'}), 
         html.Div(id='dashboard_display_cn',style={'display':'none','width':'80%','vertical-align':'text-top','margin-top':0,'height':'95%','margin-left':'20px','overflow':'auto'}),
         html.Div('1/31/2019',id='date_selected',style={'display':'none'}),
         html.Div('1/31/2019',id='date_selectedCN',style={'display':'none'})
        ],style={'display':'inline'},)                       
                           
    ], className='wrapper',style={'margin':0})



@app.callback(
            Output('dashboard_display_en','children'),
            [Input('url','pathname')]        
)
def display_page(path):
    if path == '/squirrel/home':
        return pageHome.layout
    elif path == '/squirrel/dashboard':
        return pageDashboard.layout
    elif path == '/squirrel/logging':
        return app2.layout
    elif '/squirrel/FinancialReport' in path:
        return [pageReport.layout_1, pageReport.layout_2, pageReport.layout_3, pageReport.layout_4]
    elif path == "/squirrel/aboutus":
        return pageAbout.layout
    else:
        raise PreventUpdate
        
@app.callback(
            Output('dashboard_display_cn','children'),
            [Input('url','pathname')]        
)
def display_cn_page(path):
    if path == '/squirrel_cn/home':
        return pageHomeCN.layout
    elif path == '/squirrel_cn/dashboard':
        return pageDashboardCN.layout
    elif path == '/squirrel_cn/logging':
        return app2.layout
    elif '/squirrel_cn/FinancialReport' in path:
        return [pageReportCN.layout_1, pageReportCN.layout_2, pageReportCN.layout_3, pageReportCN.layout_4]
    elif path == "/squirrel_cn/aboutus":
        return pageAboutCN.layout
    else:
        raise PreventUpdate
    
    
@app.callback(
            [Output('menu','children'),
             Output('dashboard_display_en','style'),
             Output('dashboard_display_cn','style'),
             Output('url','pathname')],
            [Input('button_en','n_clicks'),
             Input('button_cn','n_clicks')],
            [State('url','pathname')]
)
def change_menu(en_click, cn_click, url):
    
    trigger = dash.callback_context.triggered[0]
    display = {'display':'inline-block','width':'80%','vertical-align':'text-top','margin-top':0,'height':'95%','margin-left':'20px','overflow':'auto'}
    hide = {'display':'none','width':'80%','vertical-align':'text-top','margin-top':0,'height':'95%','margin-left':'20px','overflow':'auto'}
    url_en = '/squirrel/home'
    url_cn = '/squirrel_cn/home'
        
    if en_click is None and cn_click is None:
        if 'cn' in url:
            return [menu_cn,hide,display,url_cn]
        else:
            raise PreventUpdate
    else:
        
        if 'button_cn' in trigger['prop_id']:
            return [menu_cn,hide,display,url_cn]
        elif 'button_en' in trigger['prop_id']:
            return [menu_en,display,hide,url_en]        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    