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


import pandas as pd

from app import app

layout = html.Div([
            #row 1
            html.Div([
                html.Div([
                    html.Div([
                        html.I(className='fa fa-book')
                    ],style={'width':'25%','max-width':'250px','float':'left','padding-right':'15px','padding-left':'30px','font-size':'180px','line-height':'200px'}),
                    
                    html.Div([
                        html.H1('松鼠个人记账',className='homeHeaderMain'),
                        html.P('持续更新中 · 数据可视化 · 编码全部开放',className='homeHeaderSub'),
                        
                        html.Div([
                            dcc.Link("本月汇总", href='/squirrel_cn/dashboard' ,id='go_dash_btnCN', className="homeButton"), 
                            html.A("Github",href='https://github.com/kangning0125/KL_Tool', target='_blank',className="homeButton")
                                 
                        ],className='homeButtonContainer'),
                        
                    ],style={'width':'70%','float':'left','padding-right':'15px','padding-left':'15px','height':'100%'})
                    
                ],style={'display':'block','box-sizing':'border-box','position':'relative','z-index':2,'width':'100%',
                         'padding-left':'15px','padding-right':'15px','margin-left':'auto','margin-right':'auot','color':'#fff'})
                         
            ],className="rowHome",style={"margin-bottom": "0px",'min-height':'300px','max-height':'500px'}),
            
            #row 2
            html.Div([
                html.H3('提示: 选择日期来查看其他月份记录:',style={'color':'black', 'font-size':'14px','padding-left':'40px'}),
                dcc.Dropdown(
                    id='date-selectorCN',
                    options=[],
                    value='1/31/2019',
                    style={'width':'150px','margin-left':'20px','color':'black'}
                ),
                #html.Div(id='date-display-value',style={'color':'black'}),
            ],className="rowHome",style={"display":'inline-flex','background':'#f5f5f5', 'width':'100%','max-height':'50px','padding-top':'10px','padding-bottom':'10px'}),
            
            #row 3
            html.Div([
                html.Div([
                    html.P(['松鼠记账是一个试验性平台，以家庭账本为案例，用于展示Dash, CSS网页格式，开放式编程环境以及图形可视化等一系列概念。'],
                           style={'color':'#333', 'font-weight':'300', 'line-height': "1.6rem",'font-size':'24px','padding-left':'40px','padding-right':'20px'}),
                    html.Div([
                        html.Div([
                            html.I('  全部代码分享在Github',className='fa fa-github', style={'color':'inherit','font-weight':500,'line-height':'1.5rem','font-size':'23px','margin-top':'10px','margin-bottom':'10px'}),
                            html.H4('The codes for this app are shared on Github for your reference.', style={'color':'inherit','line-height':'1.1rem','font-size':'14px'})
                        ],className='homeIconContainer'),
                        
                        html.Div([
                            html.I('  无限拓展可能',className='fa fa-arrows-alt', style={'color':'inherit','font-weight':500,'line-height':'1.5rem','font-size':'23px','margin-top':'10px','margin-bottom':'10px'}),
                            html.H4('Dash provides combination of web page design and Python programming. Users can achieve and visualize unlimited ideas.', style={'color':'inherit','line-height':'1.1rem','font-size':'14px'})
                        ],className='homeIconContainer'),
                        
                        html.Div([
                            html.I('  100% 开源编程语言',className='fa fa-file-code-o', style={'color':'inherit','font-weight':500,'line-height':'1.5rem','font-size':'23px','margin-top':'10px','margin-bottom':'10px'}),
                            html.H4('All packages used in the development are 100% free.', style={'color':'inherit','line-height':'1.1rem','font-size':'14px'})
                        ],className='homeIconContainer'),
                        
                        html.Div([
                            html.I('  通过CSS与Python设计页面',className='fa fa-css3', style={'color':'inherit','font-weight':500,'line-height':'1.5rem','font-size':'23px','margin-top':'10px','margin-bottom':'10px'}),
                            html.H4('Web styles can be specified in CSS or directly in Python, depneding on user\'s preference.', style={'color':'inherit','line-height':'1.1rem','font-size':'14px'})
                        ],className='homeIconContainer'),
                        
                        html.Div([
                            html.I('  响应式网页设计',className='fa fa-desktop', style={'color':'inherit','font-weight':500,'line-height':'1.5rem','font-size':'23px','margin-top':'10px','margin-bottom':'10px'}),
                            html.H4('The layout of elements are designed responsively for different devices and screen sizes.', style={'color':'inherit','line-height':'1.1rem','font-size':'14px'})
                        ],className='homeIconContainer'),
                        
                        html.Div([
                            html.I('  可与云数据链接',className='fa fa-cloud-upload', style={'color':'inherit','font-weight':500,'line-height':'1.5rem','font-size':'23px','margin-top':'10px','margin-bottom':'10px'}),
                            html.H4('Heroku provides addons to connect with salesforce.com, which provides cloud solution for datawarehouse.', style={'color':'inherit','line-height':'1.1rem','font-size':'14px'})
                        ],className='homeIconContainer'),
                        
                        
                        
                    ],style={'margin-top':'20px','display':'block','height':'500px'})
                ],style={'margin-right':'0px','margin-left':'0px','width':'100%','display':'block','box-sizing':'border-box'})
            ],className="rowHome",style={"margin-bottom": "0px",'background':'#ffffff','min-height':'55%','border-bottom-left-radius':'10px','border-bottom-right-radius':'10px'}),

    ],style={'height':'100%'})

@app.callback(
    Output('date-selectorCN', 'options'),
    [Input('url', 'pathname')])
def display_value(path):
    if path == '/squirrel_cn/home':
        data = pd.read_csv('Records.csv')
        dates = data['Date'].tolist()
        date_list1 = set()
        date_list = [x for x in dates if not (x in date_list1 or date_list1.add(x))]
        
        return [{'label': i, 'value': i} for i in date_list[12:]]
    else:
        raise PreventUpdate

@app.callback(
    Output('date_selectedCN','children'),
    [Input('date-selectorCN', 'value')])
def display_value1(value):
    return value




