# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 14:50:31 2020

@author: Xian&Kang
"""
import pandas as pd
import numpy as np

import datetime
import calendar

def monthdelta(date, delta):
    '''
    delta could be 1,3,6,12.
    '''
    year = int(date.strftime("%Y"))
    month = int(date.strftime("%m"))
    if month <= delta:
        new_month = month-delta+12
        day = calendar.monthrange(year-1, new_month)[1]
        report_date_prev = datetime.datetime(year - 1, new_month, day)
    else:
        day = calendar.monthrange(year, month-delta)[1]
        report_date_prev = datetime.datetime(year, month - delta, day)
        
    return report_date_prev

def finance_metric_calc(data,report_date):
    assets = data.loc[((data['Date']==report_date) & (data['Rollup3'] == 'Asset')),'Amount'].sum()
    liabilities = data.loc[((data['Date']==report_date) & (data['Rollup3'] == 'Liability')),'Amount'].sum()
    net_worth = assets - liabilities    
    return net_worth, assets, liabilities

def waterfall_data_prep(data, report_date):
    date_time_obj = datetime.datetime.strptime(report_date, '%m/%d/%Y').date()

    year = int(date_time_obj.strftime("%Y"))
    month = int(date_time_obj.strftime("%m"))
    if month == 1:
        day = calendar.monthrange(year, month)[1]
        report_date_prev = datetime.date(year - 1, 12, day)
    else:
        day = calendar.monthrange(year, month-1)[1]
        report_date_prev = datetime.date(year, month -1, day)

    if month <= 10 and month >1:
        report_date_prev = report_date_prev.strftime('%m/%d/%Y')[1:]
    else: 
        report_date_prev = report_date_prev.strftime('%m/%d/%Y')

    x_list = [report_date_prev, "Deposit", 'Investment', "ESP", "401k", 'Real Estate', 'Mortgage','Loan',report_date]

    net_worth_prev = finance_metric_calc(data,report_date_prev)[0]
    net_worth_curr = finance_metric_calc(data,report_date)[0]
    y_list = [net_worth_prev]

    for i in x_list[1:-1]:
        delta_i = data.loc[((data['Date']==report_date) & (data['Rollup1'] == i)),'Amount'].sum() - data.loc[((data['Date']==report_date_prev) & (data['Rollup1'] == i)),'Amount'].sum()
        if i in ['Mortgage','Loan']:
            y_list.append(-delta_i)
        else:
            y_list.append(delta_i)

    y_list.append(net_worth_curr)
    y_range = [y_list[0]-5000,y_list[-1]+5000]
    
    return x_list, y_list, y_range

def line_chart_data_prep(data, report_date, account):
    data['Date'] = pd.to_datetime(data['Date'])
    date_time_obj = datetime.datetime.strptime(report_date, '%m/%d/%Y')
    last_index = data[data['Date']==date_time_obj].last_valid_index()
    
    data_cut = data.loc[:last_index,:]
    data_sp = data_cut.loc[data_cut['Rollup3']=='SP500',:]
    
    if account == 'Asset':
        data_asset = data_cut.loc[data_cut['Rollup3']=='Asset',:]
        data_pivot = pd.pivot_table(data_asset, values = 'Amount', index = ['Date'],
                      columns=['Rollup3'],aggfunc=np.sum)
        y_list = data_pivot[account].tolist()
    else :
        data_asset = data_cut.loc[data_cut['Rollup1']==account,:]
        data_pivot = pd.pivot_table(data_asset, values = 'Amount', index = ['Date'],
                      columns=['Rollup1'],aggfunc=np.sum)
        y_list = data_pivot[account].tolist()
        
    y_list_sp = data_sp['Amount'].tolist()
    date_list = data_pivot.index.tolist()
    
    return date_list, y_list, y_list_sp

def pie_chart_data_prep(data,report_date):
    data_cut = data.loc[(data['Date']==report_date) & (data['Rollup3']=='Asset'),:]
    data_pivot = pd.pivot_table(data_cut, values = 'Amount', index = ['Date'],
                               columns=['Rollup1'], aggfunc=np.sum)
    labels_list = data_pivot.columns.to_list()
    values_list = data_pivot.iloc[0].values.tolist()
    return labels_list, values_list

def prep_top_mover_data(data, report_date):
    date_time_obj = datetime.datetime.strptime(report_date, '%m/%d/%Y').date()

    year = int(date_time_obj.strftime("%Y"))
    month = int(date_time_obj.strftime("%m"))
    if month == 1:
        day = calendar.monthrange(year, month)[1]
        report_date_prev = datetime.date(year - 1, 12, day)
    else:
        day = calendar.monthrange(year, month-1)[1]
        report_date_prev = datetime.date(year, month -1, day)

    if month <= 10 and month >1:
        report_date_prev = report_date_prev.strftime('%m/%d/%Y')[1:]
    else: 
        report_date_prev = report_date_prev.strftime('%m/%d/%Y')

    data_prep = data.loc[((data['Date'] == report_date)|(data['Date'] == report_date_prev)),['Date','Item','Amount']]
    data_prep = data_prep.loc[data['Rollup3']=='Asset',:]
    data_curr = data_prep.loc[data['Date']==report_date,:]
    data_prev = data_prep.loc[data['Date']==report_date_prev,:]

    df_result = pd.merge(data_curr, data_prev, on='Item')
    df_result['Delta'] = abs(df_result['Amount_x'] - df_result['Amount_y'])
    df_result = df_result.sort_values(by=['Delta'],ascending=False)

    x_list = df_result['Item'].tolist()
    y_curr_list = df_result['Amount_x'].tolist()
    y_prev_list = df_result['Amount_y'].tolist()
    return x_list, y_curr_list, y_prev_list

def prep_tier_asset_data(data, report_date):
    data['Date'] = pd.to_datetime(data['Date'])
    date_time_obj = datetime.datetime.strptime(report_date, '%m/%d/%Y')
    last_index = data[data['Date']==date_time_obj].last_valid_index()

    data_cut = data.loc[:last_index,:]
    date_list = []
    tier1_list = []
    tier2_list = []
    tier3_list = []
    for d in np.unique(data_cut['Date']):
        tier1_amount = data.loc[(data['Date']==d) & (data['Rollup1']=='Deposit'),'Amount'].sum()
        tier2_amount = data.loc[(data['Date']==d) & ((data['Rollup1']=='Investment')|(data['Rollup1']=='ESP')),'Amount'].sum()
        tier3_amount = data.loc[(data['Date']==d) & (data['Rollup3']=='Asset'),"Amount"].sum() - tier1_amount - tier2_amount
        date_list.append(d)
        tier1_list.append(tier1_amount)
        tier2_list.append(tier2_amount)
        tier3_list.append(tier3_amount)
    
    date_list = pd.to_datetime(date_list)
    #date_list = [date_obj.strftime('%m-%d-%Y') for date_obj in date_list]
        
    return date_list, tier1_list, tier2_list, tier3_list


