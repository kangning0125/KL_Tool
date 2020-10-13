#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 18:27:58 2020

@author: kangningli
"""
import dash_html_components as html


import pandas as pd
import numpy as np
import datetime

from src import calculations

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

def prep_asset_detail(data, report_date):
    name_list, y_curr_list, y_prev_list = calculations.prep_top_mover_data(data, report_date)
    change_list = [a_i - b_i for a_i, b_i in zip(y_curr_list, y_prev_list)]
    df = {'col1': [1, 2], 'col2': [3, 4]}
    df = pd.DataFrame(data={'Name': name_list, 'Amount': y_curr_list, 'Change': change_list})
    df.drop(df[df['Amount'] < 10].index, inplace = True)
    return df


def prep_investment_perf_table(data, report_date):
    data['Date'] = pd.to_datetime(data['Date'])
    date_time_obj = datetime.datetime.strptime(report_date, '%m/%d/%Y')
    last_index = data[data['Date']==date_time_obj].last_valid_index()
    data_cut = data.loc[:last_index,:]
    data_cut = data_cut.loc[((data_cut['Rollup1']=='Investment') | (data_cut['Rollup1']=='Benchmark')),: ]

    data_pivot = pd.pivot_table(data_cut, values = 'Amount', index = ['Date'],
                              columns=['Rollup1'],aggfunc=np.sum)
    data_pivot = data_pivot.reset_index()

    report_date_timeobj = datetime.datetime.strptime(report_date, '%m/%d/%Y')
    report_year = report_date_timeobj.year

    inv_curr = data_pivot.loc[data_pivot['Date']==report_date_timeobj,['Investment']].values[0][0]
    sp_curr = data_pivot.loc[data_pivot['Date']==report_date_timeobj,['Benchmark']].values[0][0]

    year_end = datetime.datetime(report_year-1, 12, 31)
    inv_year_end = data_pivot.loc[data_pivot['Date']==year_end,['Investment']].values[0][0]
    sp_year_end = data_pivot.loc[data_pivot['Date']==year_end,['Benchmark']].values[0][0]

    M3_end = calculations.monthdelta(report_date_timeobj, 3)
    inv_M3_end = data_pivot.loc[data_pivot['Date']==M3_end,['Investment']].values[0][0]
    sp_M3_end = data_pivot.loc[data_pivot['Date']==M3_end,['Benchmark']].values[0][0]

    M6_end = calculations.monthdelta(report_date_timeobj, 6)
    inv_M6_end = data_pivot.loc[data_pivot['Date']==M6_end,['Investment']].values[0][0]
    sp_M6_end = data_pivot.loc[data_pivot['Date']==M6_end,['Benchmark']].values[0][0]

    M12_end = calculations.monthdelta(report_date_timeobj, 12)
    inv_M12_end = data_pivot.loc[data_pivot['Date']==M12_end,['Investment']].values[0][0]
    sp_M12_end = data_pivot.loc[data_pivot['Date']==M12_end,['Benchmark']].values[0][0]

    YTD_return_inv = (inv_curr - inv_year_end)/inv_year_end
    M3_return_inv = (inv_curr - inv_M3_end)/inv_M3_end
    M6_return_inv = (inv_curr - inv_M6_end)/inv_M6_end
    M12_return_inv = (inv_curr - inv_M12_end)/inv_M12_end
    YTD_return_sp = (sp_curr - sp_year_end)/sp_year_end
    M3_return_sp = (sp_curr - sp_M3_end)/sp_M3_end
    M6_return_sp = (sp_curr - sp_M6_end)/sp_M6_end
    M12_return_sp = (sp_curr - sp_M12_end)/sp_M12_end

    investment_perf_df = pd.DataFrame(data={'':['Investment','S&P 500 Index'],
                                            'YTD':[YTD_return_inv,YTD_return_sp],
                                            '3-month':[M3_return_inv,M3_return_sp],
                                            '6-month':[M6_return_inv,M6_return_sp],
                                            '1-year':[M12_return_inv,M12_return_sp]})
    return investment_perf_df

def prep_liquid_table(data, report_date):
    data_cut = data.loc[((data['Date']==report_date)&(data['Rollup3']=='Asset')),: ]

    data_pivot = pd.pivot_table(data_cut, values = 'Amount', index = ['Date'],
                              columns=['Rollup1'],aggfunc=np.sum)
    data_pivot = data_pivot.reset_index()

    total_asset = 0
    for i in data_pivot.columns.tolist()[1:]:
        total_asset += data_pivot[i][0]

    high_ratio=(data_pivot['Deposit'][0]+data_pivot['Investment'][0])/total_asset
    med_ratio=(data_pivot['ESP'][0]+data_pivot['401k'][0])/total_asset
    low_ratio=data_pivot['Real Estate'][0]/total_asset



    liquidity_df = pd.DataFrame(data={'Account':['Deposit','Investment','ESP','401k','Real Estate','','','',''],
                                     'Liquidity':['High','High','Medium','Medium','Low','Ratio','High','Medium','Low'],
                                     'Amount':[data_pivot['Deposit'][0],data_pivot['Investment'][0],data_pivot['ESP'][0],data_pivot['401k'][0],data_pivot['Real Estate'][0],'',high_ratio,med_ratio,low_ratio]})
    return liquidity_df

