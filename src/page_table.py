#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 18:27:58 2020

@author: kangningli
"""
import dash_html_components as html
import dash_core_components as dcc

import pandas as pd
import numpy as np
import datetime


def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table

def get_hist_asset_data(data, report_date):
    data['Date'] = pd.to_datetime(data['Date'])
    date_time_obj = datetime.datetime.strptime(report_date, '%m/%d/%Y')
    last_index = data[data['Date']==date_time_obj].last_valid_index()

    data_cut = data.loc[:last_index,:]

    data_cut = data_cut.loc[((data_cut['Rollup1'] == 'Deposit')| (data_cut['Rollup1'] == 'Investment')),['Date','Amount']]

    data_pivot = pd.pivot_table(data_cut, values = 'Amount', index = ['Date'],
                          aggfunc=np.sum)
    data_pivot = data_pivot.reset_index()
    data_final = data_pivot.sort_values(by='Date', ascending=False)
    data_final['Date'] = data_final['Date'].dt.strftime('%m/%d/%Y')
    
    if data_final.shape[0] > 6:
        data_final = data_final[:6]
        
    return data_final