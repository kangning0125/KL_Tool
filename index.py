#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 21:42:39 2020

@author: kangningli
"""


import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from layout import app1, app2, utils

app.title='MaoLi - Kenny Li App'

app.config.suppress_callback_exceptions = True

app.layout = html.Div([dcc.Location(id='url',refresh=False),
                       utils.create_body])




if __name__ == '__main__':
    app.run_server(debug=True, port='8800')