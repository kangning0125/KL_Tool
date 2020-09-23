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

layout = html.Div(id='page_about',
         children=[
            html.Div([
                html.Div(['About Us'],className='columnHeader'),
                html.Div(['this is a container of introduction'],className='columnCard')
            
            ],className='row'),
            html.Div([],className='row')

])


