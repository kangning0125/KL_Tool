# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 14:50:31 2020

@author: Xian&Kang
"""
import pandas as pd
import numpy as np


def finance_metric_calc(data,report_date):
    assets = data.loc[((data['Date']==report_date) & (data['Rollup3'] == 'Asset')),'Amount'].sum()
    liabilities = data.loc[((data['Date']==report_date) & (data['Rollup3'] == 'Liability')),'Amount'].sum()
    net_worth = assets - liabilities    
    return net_worth, assets, liabilities