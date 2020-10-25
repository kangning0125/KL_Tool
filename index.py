#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 21:42:39 2020

@author: kangningli
"""


import dash_core_components as dcc
import dash_html_components as html


from app import app, server
from layout import utils

app.title='Squirrel - A family finance planner app'

app.config.suppress_callback_exceptions = True

app.layout = html.Div([dcc.Location(id='url',refresh=False),
                       utils.create_body])




if __name__ == '__main__':
    app.run_server(debug=True, port='8800')