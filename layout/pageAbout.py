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

app_intro = 'The Squirrel family finance planner is a dashboard developed in Python and hosted on Heroku. The main purpose of this app is to create an idea on how to \
            manage personal wealth and visualize the monthly data in a better way. With various types of graphs and tables, this app converts plain numbers into vivid description of your financial health. \
                Meanwhile, the codes are published in Github for your future reference, if you are interested in creating your own dashboard project.'

kenny_intro = 'Kenny is a quantitative analyst in Capital One. His profession is focused in model risk, interest rate risk, and asset-liability management, \
                with interests and experiences in data science and machine learning.'
xian_intro = 'Xian has master degree in Information System and has been working in data engineering for 4 years. She has comprehensive skill package in data visulization, data engineering, and data science.'


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

layout = html.Div(id='page_about',
         children=[
            html.Div([
                html.Div(['About Us'],className='rowHeader'),
                html.Div(
                    html.Div(children=app_intro,style={'margin':'10px'}),className='columnCard',style={'height':'100px','margin':'0px'}
                )
            
            ],className='rowDash'),
            html.Div([
                html.Div(['Developers'],className='rowHeader'),
                html.Div([
                    html.Div([ # developer #1 card
                        html.Img(src=app.get_asset_url('kennyli_pic.png'),style={'padding':'20px','width':'200px','height':'200px'}),
                        html.Div([
                            html.Div([
                                html.H4(['Kenny Li',],style={'color':'#010108b3','margin-top':'15px','width':'80px'}),
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
                                html.H4(['Xian Cui'],style={'color':'#010108b3','margin-top':'15px','width':'80px'}),
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
                html.Div(['Release Notes'],className='rowHeader'),
                html.Div([
                    html.Div(children=release_note_v100,style={'margin-left':'20px'}), #v1.0 release note 
                    html.Div(children=release_note_v018,style={'margin-left':'20px'}), #v0.18 release note 
                    html.Div(children=release_note_v017,style={'margin-left':'20px'}) #v0.17 release note 
                ],className='columnCard',style={'height':'240px','overflow-y':'auto'})
                
                ],className='rowDash')

],style={'display':'block','height':'93%','width':'100%','overflow':'auto'})


