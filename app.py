#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 21:38:03 2020

@author: kangningli
"""


import dash



app = dash.Dash(__name__,external_stylesheets=[ '/assets/font-awesome.min.css','/assets/font-awesome.css' ] ,suppress_callback_exceptions=True)
server = app.server



