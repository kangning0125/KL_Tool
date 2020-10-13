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

from app import app

layout = html.Div([
    html.H3('Test Input Function'),
    dcc.Dropdown(
        id='app-dropdown',
        options=[]
    ),
    html.Div(id='app-display-value'),
    
    html.Div(dcc.Input(id='input-on-submit', type='text')),
    html.Button('Submit', id='submit-val', n_clicks=0),
    
])

@app.callback(
    Output('app-dropdown', 'options'),
    [Input('url', 'pathname'),
     Input('submit-val','n_clicks')],
    [State('input-on-submit','value')])
def display_value(path, n_clicks, string):
    if path == '/squirrel/logging' and n_clicks is not None:
        print(n_clicks)
        if string is None:
            pass
        else:
            with open('input_test.csv','a') as fd:
                fd.write(string)
            fd.close()
        
        data = pd.read_csv('input_test.csv')
        return [{'label': i, 'value': i} for i in data['Item']]
    else:
        raise PreventUpdate

@app.callback(
    Output('app-display-value', 'children'),
    [Input('app-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)