#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 21:43:14 2020

@author: kangningli
"""


import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from dash_table.Format import Sign
import dash_table.FormatTemplate as FormatTemplate

import pandas as pd
import datetime

from src import report_plot, page_table, calculations
from app import app



def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()])


def get_header(app):
    header = html.Div([
                html.Div([
                    html.Img(src=app.get_asset_url("squirrel_icon.png"),className="reportLogo"),
                ],className="reportRow"),
                html.Div([
                    html.Div([
                        html.H5("Squirrel Family Finance Monthly Report",id='report_title',className='reportH5')],
                            className="seven columns main-title",
                        ),
                        html.Div([
                            dcc.Link(
                                "Full View",
                                href="/squirrel/FinancialReport",
                                className="full-view-link",)
                        ],className="five columns",),
                ],className="twelve columns",style={"padding-left": "0"}),
            ],className="reportRow")
    return header


def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                "Overview",
                href="/squirrel/FinancialReport/overview",
                className="reportTabFirst",
            ),
            dcc.Link(
                "Asset Details",
                href="/squirrel/FinancialReport/AssetDetails",
                className="reportTab",
            ),
            dcc.Link(
                "Investment Performance",
                href="/squirrel/FinancialReport/Investment",
                className="reportTab",
            ),
            dcc.Link(
                "News & Reviews",
                href="/squirrel/FinancialReport/newsreviews",
                className="reportTab",
            ),
        ],
        className="reportMenuRow",
    )
    return menu


layout_1 = html.Div(id='page_report_1', className='reportPage', children=[
                html.Div([Header(app)]),
                #sub page
                html.Div([
                    # Row 3
                    html.Div([
                        html.Div([
                            html.H5("Account Summary",className='reportH5',style={'color':'#000000','font-size':'1.6rem'}),
                            html.Br([]),
                            html.P([
                                'This monthly report demonstrates your asset values with consolidated performance details, including but not limited to charts, tables, as well as balance sheet. \
                                 This overview provides a snapshot of your financial status, displaying all of your accounts.'
                            ],style={"color": "#000000"},className="reportRow reportP"),
                            html.P([],id='acct_sum_text',
                            style={"color": "#000000"},className="reportRow reportP"),
                        ],className="product")
                    ],className="reportRow"),
                                    
                    # Row 4
                    html.Div([
                        html.Div([
                            html.H6("Net Worth 12 Month Trend",className="subtitle padded"),
                            dcc.Graph(
                                id="asset_12m_trend",
                                figure={},
                                config={"displayModeBar": False},),
                            
                        ],className="six columns",),
                        
                        html.Div([
                            html.H6("Net Worth Contribution",className="subtitle padded",),
                            dcc.Graph(
                                        id="graph_net_worth_waterfall",
                                        figure={},
                                        config={"displayModeBar": False}),
                                ],className="six columns"),
                        ],className="reportRow",style={"margin-bottom": "35px"}),
                    
                    # Row 5
                    html.Div([
                        html.Div([
                            html.H6(["Personal Balance Sheet"], className="subtitle padded"),
                            html.Table(id='balance_sheet_table',style={'border-spacing': 0,'font-size':'12px'})
                        ],className="six columns",),
                        
                            html.Div([
                                html.H6("Asset Liquidity",className="subtitle padded"),
                                dash_table.DataTable(
                                    id='asset_liquidity_table1',
                                    columns=[{'name':'Account','id':'Account'},
                                             {'name':'Liquidity','id':'Liquidity'},
                                             {            
                                                'id': 'Amount',
                                                'name': 'Amount',
                                                'type': 'numeric',
                                                'format': FormatTemplate.money(0)
                                                }
                                            ],
                                    style_cell={'textAlign': 'left'},
                                    style_as_list_view=True,
                                    style_header={'backgroundColor':'#025b99','color':'white','fontWeight':'bold'}
                                    
                                ),
                                dash_table.DataTable(
                                    id='asset_liquidity_table2',
                                    columns=[{'name':'Account','id':'Account'},
                                             {'name':'Liquidity','id':'Liquidity'},
                                             {            
                                                'id': 'Amount',
                                                'name': 'Amount',
                                                'type': 'numeric',
                                                'format': FormatTemplate.percentage(1).sign(Sign.positive)
                                                }
                                            ],
                                    style_cell={'textAlign': 'left'},
                                    style_header = {'display': 'none','margin-top':0,'height':'1px','font-size':'1px'},
                                    style_as_list_view=True,
                                    style_data_conditional=[
                                                            {
                                                                'if': {'row_index': 0},
                                                                'backgroundColor': '#025b99',
                                                                'color': 'white',
                                                                'fontWeight': 'bold'
                                                            },
                                                        ]
                                    
                            ),
                                
                            ],className="six columns",),
                        
                        ],className="reportRow"),
                        html.Div(['1'],style={'margin-left':'95mm','bottom':'15px','position':'absolute'}) 
                ],className='reportSubpage')
           ],style={})

                                                                  
                                    
layout_2 = html.Div(id='page_report_2', className='reportPage',
         children=[
            html.Div([Header(app)]),
            html.Div([
                # Row 3
                    html.Div([
                        html.Div([
                            html.H6(["Asset Allocation"], className="subtitle padded"),
                            dcc.Graph(
                                        id="asset_allocation_graph",
                                        figure={},
                                        config={"displayModeBar": False}),
                            
                        ],className="six columns",),
                        html.Div([
                            html.H6("Historical Liquid Asset",className="subtitle padded",),
                            dash_table.DataTable(
                                    id='hist_liq_asset_table',
                                    columns=[{'name':'Date','id':'Date'},
                                             {            
                                                'id': 'Amount',
                                                'name': 'Amount',
                                                'type': 'numeric',
                                                'format': FormatTemplate.money(0)}
                                            ],
                                    style_as_list_view=True,
                                    style_cell={'textAlign': 'left','font-size':'14px','height':'20px'},
                                    style_table={'height': '250px', 'overflowY': 'auto','font-size':'14px'},
                                    style_header = {'display': 'none','margin-top':0,'height':'5px'},
                                    style_data_conditional=[
                                                            {
                                                                'if': {'row_index': 'odd'},
                                                                'backgroundColor': '#f0f0f0'
                                                            }
                                                        ],
                                    
                            ),
                            
                        ],className="six columns"),
                    ],className="reportRow",style={"margin-bottom": "35px"}),
                        
                    # Row 3
                    html.Div([
                        html.Div([
                            html.H6(["Asset Details"], className="subtitle padded"), 
                            dash_table.DataTable(
                                    id='asset_detail_table',
                                    columns=[{'name':' ','id':'Name'},
                                             {            
                                                'id': 'Amount',
                                                'name': 'Amount',
                                                'type': 'numeric',
                                                'format': FormatTemplate.money(0)},
                                             {            
                                                'id': 'Change',
                                                'name': 'Change',
                                                'type': 'numeric',
                                                'format': FormatTemplate.percentage(1).sign(Sign.positive)}
                                            ],                                    
                                    style_as_list_view=True,
                                    style_header={'backgroundColor':'#025b99','color':'white','fontWeight':'bold'},
                                    style_cell={'textAlign': 'left'},
                                    style_table={'height': '300px', 'width':'300px' ,'overflowY': 'auto','font-size':'12px'}
                                    
                                    
                            ),
                            
                        ],className="six columns",),
                        html.Div([
                            html.H6("Asset Top Movers",className="subtitle padded",),
                            dcc.Graph(
                                        id="top_mover_graph",
                                        figure={},
                                        config={"displayModeBar": False}),
                                ],className="six columns"),
                        
                        ],className="reportRow",style={"margin-bottom": "35px"}),
                        
                        # Row 4
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.H6("3-tier Asset Growth", className="subtitle padded"),
                                        dcc.Graph(
                                            id="tier_asset_growth_graph",
                                            figure={},
                                            config={"displayModeBar": False},
                                        ),
                                    ],
                                    className="twelve columns",
                                )
                            ],
                            className="reportRow",
                        ),
                
                ],className='reportSubpage'),
            
            ],style={})




layout_3 = html.Div(id='page_report_3', className='reportPage',
         children=[
            html.Div([Header(app)]),
            html.Div([
                # Row 3
                html.Div([
                    html.Div([
                        html.H5("Investment Portfolio Summary",className='reportH5',style={'color':'#000000','font-size':'1.6rem'}),
                        html.Br([]),
                        html.P([
                            "\
                        The investment page displays asset level performance by asset type and investment objective. \
                        With this report, you can identify the performances in various holding periods, as well as comparison against a benchmark. \
                        The current data aggregation logic considers transfer-in of new funds as part of investment return, which leads to overestimate of total return."],
                        style={"color": "#000000"},className="reportRow reportP"),
                    ],className="product")
                ],className="reportRow"),
            
                # Row 4
                html.Div(
                    [
                        html.Div(
                            [
                                html.H6("Investment Performance", className="subtitle padded"),
                                dcc.Graph(
                                    id="investment_graph",
                                    figure={},
                                    config={"displayModeBar": False},
                                ),
                            ],className="twelve columns")
                    ],className="reportRow"),
                
                html.Div(
                    [
                        html.Div(
                            [
                                html.H6("Recent Investment Returns - updated as of 5/31/2016", className="subtitle padded"),
                                dash_table.DataTable(
                                    id='investment_perf_table',
                                    columns=[{'name':'','id':''},
                                             {            
                                                'id': 'YTD',
                                                'name': 'YTD',
                                                'type': 'numeric',
                                                'format': FormatTemplate.percentage(1).sign(Sign.positive)},
                                             {            
                                                'id': '3-month',
                                                'name': '3-month',
                                                'type': 'numeric',
                                                'format': FormatTemplate.percentage(1).sign(Sign.positive)},
                                             {            
                                                'id': '6-month',
                                                'name': '6-month',
                                                'type': 'numeric',
                                                'format': FormatTemplate.percentage(1).sign(Sign.positive)},
                                             {            
                                                'id': '1-year',
                                                'name': '1-year',
                                                'type': 'numeric',
                                                'format': FormatTemplate.percentage(1).sign(Sign.positive)}
                                            ],  
                                    style_as_list_view=True,
                                    style_header={'backgroundColor':'#025b99','color':'white','fontWeight':'bold'},
                                    style_cell={'textAlign': 'left'},
                            ),
                            ],className="twelve columns")
                    ],className="reportRow"),
                    
            ],className='reportSubpage'),

            ],style={})





layout_4 = html.Div(id='page_report_4', className='reportPage',
         children=[
            html.Div([Header(app)]),
            #sub page
                html.Div([
                    # Row 1
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6("News", className="subtitle padded"),
                                    html.Br([]),
                                    html.Div([
                                        html.A("10/25/20    These money and investing tips can help you figure out which oortfolio moves to make now.",href='https://www.marketwatch.com/story/these-money-and-investing-tips-can-help-you-figure-out-which-portfolio-moves-if-any-to-make-now-2020-10-25?mod=investing',target='_blank',className='reportP'),
                                        html.Br([]),
                                        html.A("08/08/20    Considering overed-call writing for income? Beware the risks.", href='https://www.marketwatch.com/articles/considering-covered-call-writing-for-income-in-retirement-beware-the-risks-51596895201?mod=investing',target='_blank',className='reportP',style={'line-height':'2rem'}),
                                    ],style={"color": "#7a7a7a"}),
                                ],className="reportRow",),
                            html.Div([
                                html.H6("Reviews", className="subtitle padded"),
                                html.Br([]),
                                html.Div([
                                    html.Li("Account was created in 2015.",className='reportLi'),
                                    html.Li("On average, the investment account has returns that outperformed broader market index - S&P500"
                                    ,className='reportLi'),
                                    html.Li("The total asset has a significant allocation on illiquid assets, including 401k and real estate."
                                    ,className='reportLi'),
                                ],id="reviews-bullet-pts"),
                                
                            ],className="reportRow"),
                            html.Div([
                                html.H6("Reference", className="subtitle padded"),
                                html.Br([]),
                                html.Div([
                                        html.A("1. Color Admin Dashboard",href='https://seantheme.com/color-admin/admin/html/index.html',target='_blank',className='reportP'),
                                        html.Br([]),
                                        html.A("2. Dash Gallery - Calire Financial Report", href='https://dash-gallery.plotly.host/dash-financial-report/overview',target='_blank',className='reportP',style={'line-height':'2rem'}),
                                        html.Br([]),
                                        html.A("3. Dash User Guide", href='https://dash.plotly.com/',target='_blank',className='reportP',style={'line-height':'2rem'}),
                                    ],style={"color": "#7a7a7a"}),
                                
                            ],className="reportRow"),
                            
                        ],className="reportRow",)
                    
                ],className='reportSubpage')

           ],style={})


@app.callback(
    [Output('graph_net_worth_waterfall','figure'), 
     Output('asset_12m_trend','figure'),
     Output('asset_allocation_graph','figure'),
     Output('top_mover_graph','figure'),
     Output('tier_asset_growth_graph','figure'),
     Output('investment_graph','figure')],   
    [Input('url','pathname')],
    [State('date_selected','children')])
def update_summary_info(url,month_end):
    if '/squirrel/FinancialReport' in url:
        data = pd.read_csv('Records.csv')   
        
        networth_waterfall_fig = report_plot.waterfall(data, month_end)
        asset_12m_fig = report_plot.report_12m_asset(data, month_end, "Asset")
        asset_allocation_fig = report_plot.asset_allocation_pie(data, month_end, 'Total')
        top_mover_fig = report_plot.top_mover_bar(data, month_end)
        tier_asset_growth = report_plot.tier_stack_area(data, month_end)
        investment_fig = report_plot.investment_line(data, month_end)
        
        return networth_waterfall_fig, asset_12m_fig, asset_allocation_fig, top_mover_fig, tier_asset_growth, investment_fig
    
    else:
        raise PreventUpdate
        
@app.callback(
    [Output('asset_liquidity_table1','data'),
     Output('asset_liquidity_table2','data'),
     Output('asset_detail_table','data'),
     Output('hist_liq_asset_table','data'),
     Output('investment_perf_table','data')],  
    [Input('url','pathname')],
    [State('date_selected','children')])
def update_table_data(url,month_end):
    if '/squirrel/FinancialReport' in url:
        data = pd.read_csv('Records.csv')   
        
        liquidity_df = page_table.prep_liquid_table(data, month_end)
        liquidity_df1 = liquidity_df.iloc[0:-4,:]
        liquidity_df2 = liquidity_df.iloc[-4:,:]
        liquidity_table_data1 = liquidity_df1.to_dict('records')
        liquidity_table_data2 = liquidity_df2.to_dict('records')
        
        asset_details = page_table.prep_asset_detail(data, month_end)
        asset_details_data = asset_details.to_dict('records')
        
        hist_liq_asset = page_table.get_hist_asset_data(data, month_end)
        hist_liq_asset_data = hist_liq_asset.to_dict('records')
        
        invest_perf = page_table.prep_investment_perf_table(data, month_end)
        invest_perf_data = invest_perf.to_dict('records')
        
        return liquidity_table_data1, liquidity_table_data2, asset_details_data, hist_liq_asset_data, invest_perf_data
    
    else:
        raise PreventUpdate        
        
@app.callback(
    Output('balance_sheet_table','children'),
    [Input('url','pathname')],
    [State('date_selected','children')]
    )
def update_balance_sheet(url, month_end):
    if '/squirrel/FinancialReport' in url:
        data = pd.read_csv('Records.csv')
        
        return page_table.balance_sheet(data, month_end)
    
    else:
        raise PreventUpdate
        
        
@app.callback(
    Output('acct_sum_text','children'),
    [Input('url','pathname')],
    [State('date_selected','children')]    
    )
def update_acct_summary(url,month_end):
    if '/squirrel/FinancialReport' in url:
        data = pd.read_csv('Records.csv')
        net_worth, assets, liabilities = calculations.finance_metric_calc(data,month_end)
        
        date_time_obj = datetime.datetime.strptime(month_end, '%m/%d/%Y').date()
        
        prior_date = calculations.monthdelta(date_time_obj,1)        
        month = int(date_time_obj.strftime("%m"))
        if month <= 10 and month >1:
            report_date_prev = prior_date.strftime('%m/%d/%Y')[1:]
        else: 
            report_date_prev = prior_date.strftime('%m/%d/%Y')
        
        net_worth_prior,_,_ = calculations.finance_metric_calc(data,report_date_prev)

        text = f'As of {month_end}, your net worth is ${net_worth:,.1f}, comparing to ${net_worth_prior:,.1f} in prior month {report_date_prev}. \
                The net worth comprises of total assets of ${assets:,.0f} and total liability of ${liabilities:,.0f}. \
                '
        
        return text
    
    else:
        raise PreventUpdate

###### Update Page based on Menu #########

@app.callback(
    [Output('page_report_1','style'),
     Output('page_report_2','style'),
     Output('page_report_3','style'),
     Output('page_report_4','style')],
    [Input('url','pathname')])
def update_page_display(path):
    display_list = [{'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'}]
    if path == '/squirrel/FinancialReport/overview':
        display_list[0]={}
        return display_list
    elif path == '/squirrel/FinancialReport/AssetDetails':
        display_list[1]={}
        return display_list
    elif path == '/squirrel/FinancialReport/Investment':
        display_list[2]={}
        return display_list
    elif path == '/squirrel/FinancialReport/newsreviews':
        display_list[3]={}
        return display_list
    
    else:
        raise PreventUpdate()
