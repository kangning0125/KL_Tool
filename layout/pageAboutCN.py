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

app_intro = '我们开发松鼠记账的初衷是尝试构建一个基于Python与Dash的网页版应用，并且融入当前流行的Dashboard设计理念。这个应用的主要功能和创意是\
            打造一个管理个人财务和将单纯数据进行可视化的平台。我们希望能够通过不同类型与格式的图表和表格，将枯燥的财务数字转换为直观并易于理解的页面。\
            我们还将继续增加新的功能与图表，同时将编程代码更新开放在Github上面。感兴趣的朋友可以通过下方的LinkedIn或者Email联系我们，一起交流探讨。'

kenny_intro = '我目前就职于美国的Capital One银行，从事模型风险、市场利率风险的管理工作，在此之前我在KPMG从事金融市场相关的咨询工作。我对Python、网页设计、机器学习和数据可视化有着浓厚的兴趣。我还喜爱各种吃和旅游以及视频制作。'
xian_intro = '从乔治华盛顿大学取得信息管理硕士后，我先加入面向数据分析和数据库编程相关的IT咨询公司。目前在Vanda制药公司担任临床数据经理，主要负责管理临床数据并负责临床数据库的设计与搭建。硕士期间的学习加上这些年的工作经验，让我\
                积累了丰富的数据可视化、数据工程、数据科学等知识与经验。'

release_note_v017=[ 
    html.H5(['V0.17 - beta'],style={'margin-block-start': '1em','margin-block-end': '0em'}),
    html.P(['- Lauches the testing version of the app on Heroku;'],style={'margin-block-start': '0.2em','margin-block-end': '0em'}),
    html.P(['- Lauches the dashboard page; All the contents are linked to date selector on Home page;'],style={'margin-block-start': '0.2em','margin-block-end': '0em'}),
    html.P(['- Added headings and frameworks for report page.'],style={'margin-block-start': '0.2em','margin-block-end': '0em'})
]

release_note_v018=[ 
    html.H5(['V0.18 - beta'],style={'margin-block-start': '1em','margin-block-end': '0em'}),
    html.P(['- Tested write and load data file function on Heroku;'],style={'margin-block-start': '0.2em','margin-block-end': '0em'}),
    html.P(['- Updated responsive design formatting for various screen sizes;'],style={'margin-block-start': '0.2em','margin-block-end': '0em'}),
    html.P(['- Pre-v1 release debug and UAT.'],style={'margin-block-start': '0.2em','margin-block-end': '0em'})
]

release_note_v100=[ 
    html.H5(['V1.0'],style={'margin-block-start': '1em','margin-block-end': '0em'}),
    html.P(['- Lauches the public version of the app on Heroku;'],style={'margin-block-start': '0.2em','margin-block-end': '0em'}),
    html.P(['- Created versions in English and Chinese;'],style={'margin-block-start': '0.2em','margin-block-end': '0em'}),
    html.P(['- Fixed a few bugs in beta.'],style={'margin-block-start': '0.2em','margin-block-end': '0em'})
]

layout = html.Div(id='page_aboutCN',
         children=[
            html.Div([
                html.Div(['关于我们'],className='rowHeader'),
                html.Div(
                    html.Div(children=app_intro,style={'margin':'10px'}),className='columnCard',style={'height':'100px','margin':'0px'}
                )
            
            ],className='rowDash'),
            html.Div([
                html.Div(['开发人员'],className='rowHeader'),
                html.Div([
                    html.Div([ # developer #1 card
                        html.Img(src=app.get_asset_url('kennyli_pic.png'),style={'padding':'20px','width':'200px','height':'200px'}),
                        html.Div([
                            html.Div([
                                html.H4(['李康宁',],style={'color':'#010108b3','margin-top':'15px','width':'80px'}),
                                html.A(href='https://www.linkedin.com/in/kangning-li-cpa-frm-24488956/',className='fa fa-linkedin-square', target='_blank',
                                       style={'display':'inline','margin-top':'15px','text-decoration':'none','color':'#0077b5','font-weight':'900'})                                
                            ],style={'height':'10%','display':'inline-flex'}),
                            html.P(children=[kenny_intro],style={'height':'70%','margin-block-start':'0em','margin-block-end':'0em'}),
                            html.Div([
                                html.I(className='fa fa-envelope',style={'display':'inline','margin-right':'5px','padding-top':'3px'}),
                                html.P(['kangning0125@gmail.com'],style={'margin':0})
                            ],style={'height':'25%','display':'inline-flex','margin-top':'10px'}),
                        ],style={'display':'block','width':'50%','height':'100%'})
                    ],style={'display':'inline-flex','width':'48%','height':'100%','margin-left':'4px'}), # end of developer #1 card
                    html.Div([ # developer #2 card
                        html.Img(src=app.get_asset_url('xian_pic.png'),style={'padding':'20px','width':'200px','height':'200px'}),
                        html.Div([
                            html.Div([
                                html.H4(['崔宪'],style={'color':'#010108b3','margin-top':'15px','width':'80px'}),
                                html.A(href='https://www.linkedin.com/in/xian-cui-3039a646/',className='fa fa-linkedin-square', target='_blank',
                                       style={'display':'inline','margin-top':'15px','text-decoration':'none','color':'#0077b5','font-weight':'900'})                                
                            ],style={'height':'10%','display':'inline-flex'}),
                            html.P(children=[xian_intro],style={'height':'70%','margin-block-start':'0em','margin-block-end':'0em'}),
                            html.Div([
                                html.I(className='fa fa-envelope',style={'display':'inline','margin-right':'5px','padding-top':'3px'}),
                                html.P(['xiancui2007@gmail.com'],style={'margin':0})
                            ],style={'height':'25%','display':'inline-flex','margin-top':'10px'}),
                        ],style={'display':'block','width':'50%','height':'100%'})
                    ],style={'display':'inline-flex','width':'48%','height':'100%','margin-left':'4px'}), # end of developer #2 card
                ],className='columnCard',style={'display':'block','height':'270px'})
                
                ],className='rowDash'),
            html.Div([
                html.Div(['更新日志'],className='rowHeader'),
                html.Div([
                    html.Div(children=release_note_v100,style={'margin-left':'20px'}), #v1.0 release note 
                    html.Div(children=release_note_v018,style={'margin-left':'20px'}), #v0.18 release note 
                    html.Div(children=release_note_v017,style={'margin-left':'20px'}) #v0.17 release note 
                ],className='columnCard',style={'height':'240px','overflow-y':'auto'})
                
                ],className='rowDash')

],style={'display':'block','height':'98%','width':'100%'})


