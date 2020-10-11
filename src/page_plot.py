# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 14:52:58 2020

@author: Xian&Kang
"""

import plotly.graph_objects as go
import pandas as pd
import numpy as np

import datetime

from src import calculations

def waterfall(df_in, date, interval):
    
    x_list, y_list, y_range = calculations.waterfall_data_prep(df_in, date)
    
    fig_waterfall = go.Figure()
    
    fig_waterfall.add_trace(go.Waterfall(
    name = 'networth', orientation = "v",
    measure = ["absolute", "relative", "relative", "relative", "relative", "relative", "relative", "relative", "total"],
    x = x_list,
    textposition = "outside",
    #text = ["", "+80", "", "-40", "-20", "Total"],
    y = y_list,
    connector = {"line":{"color":"rgb(63, 63, 63)"}},))
    
    #fig_waterfall.update_xaxes(showgrid=False, showline=True, linewidth=2, linecolor='#404b6b', mirror=True, tickfont=dict(family='sans-serif',color='#fffef9',size=14))
    fig_waterfall.update_yaxes(showgrid=True, showline=False, zeroline=False, gridcolor='#d5d7d8',
                               tickfont=dict(family='sans-serif',color='black',size=14),
                               range=y_range)
    
    
    fig_waterfall.update_layout(margin={'l':40,'b':0,'r':0,'t':20,}, yaxis={'type':'linear'},plot_bgcolor='white',paper_bgcolor='white',
                                height=250,width=580, hoverlabel=dict(
                                                                    bgcolor="white",
                                                                    font_size=16,
                                                                    font_family="Rockwell"
                                                                ))
    
    return fig_waterfall


def dash_line(df_in, report_date, asset_name):
    
    date_list, y_list, _=calculations.line_chart_data_prep(df_in, report_date, asset_name)
    
    
    fig_line = go.Figure()
    
    
    fig_line.add_trace(go.Scatter(x=date_list, y=y_list,
                    mode='lines',
                    name='lines'))
    
    #fig_waterfall.update_xaxes(showgrid=False, showline=True, linewidth=2, linecolor='#404b6b', mirror=True, tickfont=dict(family='sans-serif',color='#fffef9',size=14))
    fig_line.update_yaxes(showgrid=True, showline=False, zeroline=False, gridcolor='#d5d7d8',
                               tickfont=dict(family='sans-serif',color='black',size=14),
                               range=[min(y_list)*0.7,max(y_list)*1.3])
    
    
    fig_line.update_layout(margin={'l':40,'b':0,'r':0,'t':20,}, yaxis={'type':'linear'},plot_bgcolor='white',paper_bgcolor='white',
                                height=250,width=580, hoverlabel=dict(
                                                                    bgcolor="white",
                                                                    font_size=16,
                                                                    font_family="Rockwell"
                                                                ))
    
    fig_line.update_layout(xaxis={
                                    "autorange": True,
                                    "range": [
                                        "2015-01-31",
                                        "2020-01-31",
                                    ],
                                    "rangeselector": {
                                        "buttons": [
                                            {
                                                "count": 1,
                                                "label": "1Y",
                                                "step": "year",
                                                "stepmode": "backward",
                                            },
                                            {
                                                "count": 3,
                                                "label": "3Y",
                                                "step": "year",
                                                "stepmode": "backward",
                                            },
                                            {
                                                "count": 5,
                                                "label": "5Y",
                                                "step": "year",
                                            },
                                            {
                                                "count": 10,
                                                "label": "10Y",
                                                "step": "year",
                                                "stepmode": "backward",
                                            },
                                            {
                                                "label": "All",
                                                "step": "all",
                                            },
                                        ]
                                    },
                                    "showline": True,
                                    "type": "date",
                                    "zeroline": False,
                                },)
    
    
    return fig_line


def dash_stackbar(data, report_date):
    
    tier1_amount = data.loc[(data['Date']==report_date) & (data['Rollup1']=='Deposit'),'Amount'].sum()
    tier2_amount = data.loc[(data['Date']==report_date) & ((data['Rollup1']=='Investment')|(data['Rollup1']=='ESP')),'Amount'].sum()
    tier3_amount = data.loc[(data['Date']==report_date) & (data['Rollup3']=='Asset'),"Amount"].sum() - tier1_amount - tier2_amount
    
    fig_bar = go.Figure()
    fig_bar.add_trace(go.Bar(name='Illiquid',x=['Asset'], y=[tier3_amount]))
    fig_bar.add_trace(go.Bar(name='Investment',x=['Asset'], y=[tier2_amount]))
    fig_bar.add_trace(go.Bar(name='Cash',x=['Asset'], y=[tier1_amount]))
    
    # Change the bar mode
    fig_bar.update_layout(barmode='stack')
    fig_bar.update_layout(margin={'l':50,'b':40,'r':0,'t':20,}, yaxis={'type':'linear'},plot_bgcolor='white',paper_bgcolor='white',
                                height=280,width=290, hoverlabel=dict(bgcolor="white",font_size=16,font_family="Rockwell"),
                                )
    fig_bar.update_yaxes(tickfont=dict(family='sans-serif',color='black',size=14),
                         range=[0, (tier1_amount + tier2_amount + tier3_amount)*1.2])
    
    
    return fig_bar

def dash_pie(data, report_date, asset_class):
    
    labels_list, values_list = calculations.pie_chart_data_prep(data,report_date)
    if asset_class == 'Total':
        labels = labels_list
        values = values_list
    else:
        labels = labels_list[:-1]
        values = values_list[:-1]

    fig_pie = go.Figure()
    fig_pie.add_trace(go.Pie(
        labels=labels, values=values,hoverinfo='label+value+percent', textinfo='label+percent',
        hole=0.7,
        insidetextorientation='radial',
        marker={'colors': [
                '#565d89',
                '#727db6',
                '#959dc8',
                '#348fe2',
                '#286baa'],
                'line': {'color':'white', 'width': 1}},
        sort=False
    ))
    
    fig_pie.update_layout(margin={'l':50,'b':0,'r':40,'t':10,}, yaxis={'type':'linear'},plot_bgcolor='white',paper_bgcolor='white',
                          height=290,width=290,
                          hoverlabel=dict(bgcolor="white",font_size=16,font_family="Rockwell"),
                          annotations=[dict(text=asset_class, x=0.5, y=0.5, font_size=20, showarrow=False)],
                          )
    
    fig_pie.update(layout_showlegend=False)
    
    return fig_pie



