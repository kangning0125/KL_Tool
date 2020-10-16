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
    html.H3('Select Date'),
    dcc.Dropdown(
        id='date-selector',
        options=[],
        value='1/31/2019',
    ),
    html.Div(id='date-display-value'),
])

@app.callback(
    Output('date-selector', 'options'),
    [Input('url', 'pathname')])
def display_value(path):
    if path == '/squirrel/home':
        data = pd.read_csv('Records.csv')
        dates = data['Date'].tolist()
        date_list1 = set()
        date_list = [x for x in dates if not (x in date_list1 or date_list1.add(x))]
        
        return [{'label': i, 'value': i} for i in date_list[12:]]
    else:
        raise PreventUpdate

@app.callback(
    [Output('date-display-value', 'children'),
    Output('date_selected','children')],
    [Input('date-selector', 'value')])
def display_value1(value):
    return ['You have selected "{}"'.format(value),value]