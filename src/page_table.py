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
    change_list = [(a_i - b_i)/b_i if b_i != 0 else 0 for a_i, b_i in zip(y_curr_list, y_prev_list) ]
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


def balance_sheet(data, report_date):
    
    data_cut = data.loc[data['Date']==report_date,:]
    data_pivot = pd.pivot_table(data_cut, values = 'Amount', index = ['Date'],
                               columns=['Rollup1'], aggfunc=np.sum)
    
    deposit=data_pivot['Deposit'].values.tolist()[0]
    investment=data_pivot['Investment'].values.tolist()[0]
    esp=data_pivot['ESP'].values.tolist()[0]
    i401k=data_pivot['401k'].values.tolist()[0]
    re_amount=data_pivot['Real Estate'].values.tolist()[0]
    mortgage=data_pivot['Mortgage'].values.tolist()[0]
    loan=data_pivot['Loan'].values.tolist()[0]
    
    liq_total = deposit + investment
    long_total = esp + i401k + re_amount
    liability_total = mortgage + loan
    net_worth = liq_total + long_total - liability_total
    
    total_asset = liq_total + long_total
    total_liability = mortgage + loan + net_worth
    
    balance_sheet=[html.Thead([
                       html.Tr(children=[
                           html.Th('Assets',scope="col",colSpan="2", className='financialstat_head1'),
                           html.Th('Liabilities & Equity',scope="col",colSpan="2", className='financialstat_head1'),
                           
                       ])
                    ],style={'border-spacing': 0}),
                   
                   html.Tfoot([
                       html.Tr(children=[
                           html.Th('Total', scope='row', className='financialstat_total'),
                           html.Th(f"{total_asset:,.0f}", scope='col', className='financialstat_value_total'),
                           html.Th(' ', scope='row', className='financialstat_total'),
                           html.Th(f"{total_liability:,.0f}", scope='col', className='financialstat_value_total'),
                       ])
                       
                    ]),
                   
                   html.Tbody(children=[
                       html.Tr(children=[
                           html.Td('Liquid Assets', colSpan='2', className='financialstat_heading'), 
                           html.Td('Liabilities', colSpan='2', className='financialstat_heading'),    
                           
                       ]),
                       
                       html.Tr(children=[
                           html.Td('Deposits', className='financialstat_item'), 
                           html.Td(f"{deposit:,.0f}", className='financialstat_value_item'),
                           html.Td('Loans', className='financialstat_item'), 
                           html.Td(f"{loan:,.0f}", className='financialstat_value_item'),
                           
                       ]),
                       
                       html.Tr(children=[
                           html.Td('Investments', className='financialstat_item'), 
                           html.Td(f"{investment:,.0f}", className='financialstat_value_item'),
                           html.Td('Mortgage', className='financialstat_item'), 
                           html.Td(f"{mortgage:,.0f}", className='financialstat_value_item'),
                           
                       ]),
                       
                       
                       html.Tr(children=[
                           html.Td('Sub Total', className='financialstat_subtotal'),
                           html.Td(f"{liq_total:,.0f}", className='financialstat_value_subtotal'),
                           html.Td('Sub Total', className='financialstat_subtotal'),
                           html.Td(f"{liability_total:,.0f}", className='financialstat_value_subtotal'),
                           
                       ]),
                       
                       html.Tr(children=[
                           html.Td('Long-term Assets', colSpan='2', className='financialstat_heading'), 
                           html.Td('Equity', colSpan='2', className='financialstat_heading'),    
                           
                       ]),
                       
                       html.Tr(children=[
                           html.Td('Employee Stock', className='financialstat_item'), 
                           html.Td(f"{esp:,.0f}", className='financialstat_value_item'),
                           html.Td('Net Worth', className='financialstat_item'), 
                           html.Td(f"{net_worth:,.0f}", className='financialstat_value_item'),
                           
                       ]),
                       
                       html.Tr(children=[
                           html.Td('Real Estate', className='financialstat_item'), 
                           html.Td(f"{re_amount:,.0f}", className='financialstat_value_item') 
                       ]),
                       
                       html.Tr(children=[
                           html.Td('401k', className='financialstat_item'), 
                           html.Td(f"{i401k:,.0f}", className='financialstat_value_item') 
                       ]),
                       
                       html.Tr(children=[
                           html.Td('Sub Total', className='financialstat_subtotal'),
                           html.Td(f"{long_total:,.0f}", className='financialstat_value_subtotal'),
                       ]),
                       
                       
                   ],className='financialstat')
                   
    ]
    
    return balance_sheet

