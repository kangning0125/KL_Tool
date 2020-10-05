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

kenny_intro = 'Kenny is a quantitative analyst in Model Validation Group of Capital One. His profession is focused in bank\'s balance sheet management in areas of market risks.'
xian_intro = 'Xian is a very beautiful and smart lady. She works in Vanda Pharmaceutical company.'



layout = html.Div(id='page_about',
         children=[
            html.Div([
                html.Div(['About Us'],className='rowHeader'),
                html.Div(['this is a container of introduction'],className='columnCard',style={'height':'50px'})
            
            ],className='row'),
            html.Div([
                html.Div(['Developers'],className='rowHeader'),
                html.Div([
                    html.Div([ # developer #1 card
                        html.Img(src=app.get_asset_url('kennyli_pic.png'),style={'padding':'20px','width':'50%','height':'100%'}),
                        html.Div([
                            html.Div([
                                html.H4(['Kenny Li',],style={'color':'#010108b3','margin-top':'15px','width':'80px'}),
                                html.A(href='https://www.linkedin.com/in/kangning-li-cpa-frm-24488956/',className='fab fa-linkedin', target='_blank',
                                       style={'display':'inline','margin-top':'15px','text-decoration':'none','color':'#0077b5','font-weight':'900'})                                
                            ],style={'height':'10%','display':'inline-flex'}),
                            html.P(children=[kenny_intro],style={'height':'50%','margin-block-start':'0em','margin-block-end':'0em'}),
                            html.Div([
                                html.I(className='fas fa-envelope',style={'display':'inline','margin-right':'5px','padding-top':'3px'}),
                                html.P(['kangning0125@gmail.com'],style={'margin':0})
                            ],style={'height':'25%','display':'inline-flex','margin-top':'10px'}),
                        ],style={'display':'block','width':'50%','height':'100%'})
                    ],style={'display':'inline-flex','width':'48%','height':'100%','margin-left':'4px'}), # end of developer #1 card
                    html.Div([ # developer #2 card
                        html.Img(src=app.get_asset_url('xian_pic.png'),style={'padding':'20px','width':'50%','height':'100%'}),
                        html.Div([
                            html.Div([
                                html.H4(['Xian Cui'],style={'color':'#010108b3','margin-top':'15px','width':'80px'}),
                                html.A(href='https://www.linkedin.com/in/xian-cui-3039a646/',className='fab fa-linkedin', target='_blank',
                                       style={'display':'inline','margin-top':'15px','text-decoration':'none','color':'#0077b5','font-weight':'900'})                                
                            ],style={'height':'10%','display':'inline-flex'}),
                            html.P(children=[xian_intro],style={'height':'50%','margin-block-start':'0em','margin-block-end':'0em'}),
                            html.Div([
                                html.I(className='fas fa-envelope',style={'display':'inline','margin-right':'5px','padding-top':'3px'}),
                                html.P(['xiancui2007@gmail.com'],style={'margin':0})
                            ],style={'height':'25%','display':'inline-flex','margin-top':'10px'}),
                        ],style={'display':'block','width':'50%','height':'100%'})
                    ],style={'display':'inline-flex','width':'48%','height':'100%','margin-left':'4px'}), # end of developer #2 card
                ],className='columnCard',style={'display':'block','height':'200px'})
                
                ],className='row'),
            html.Div([
                html.Div(['Release Notes'],className='rowHeader'),
                html.Div(['this is a container of release notes'],className='columnCard',style={'height':'100px'})
                
                ],className='row')

],style={'display':'block','height':'100%','width':'100%'})


