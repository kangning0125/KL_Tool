# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 14:52:58 2020

@author: Xian&Kang
"""

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

import datetime

from src import calculations

def waterfall(df_in, date):
    
    x_list, y_list, y_range = calculations.waterfall_data_prep(df_in, date)
    
    fig_waterfall = go.Figure()
    
    fig_waterfall.add_trace(go.Waterfall(
    name = 'networth', orientation = "v",
    measure = ["absolute", "relative", "relative", "relative", "relative", "relative", "relative", "relative", "total"],
    x = x_list,
    textposition = "outside",
    y = y_list,
    connector = {"line":{"color":"rgb(63, 63, 63)"}},))
    
    fig_waterfall.update_xaxes(autorange=True, showline=True, title="")
    fig_waterfall.update_yaxes(autorange=False, range=y_range,
                            gridcolor="rgba(127, 127, 127, 0.2)",
                            mirror=False,
                            nticks=4,
                            showgrid=True,
                            showline=True,
                            linewidth=1,
                            ticklen=5,
                            ticks='outside',
                            #title="",
                            type="linear",
                            zeroline=False,
                            zerolinewidth=4,)
    
    
    fig_waterfall.update_layout(margin={'l':10,'b':10,'r':0,'t':20,}, yaxis={'type':'linear'},plot_bgcolor='white',paper_bgcolor='white',
                                height=200,width=330, autosize=False,hovermode='closest')
    
    return fig_waterfall

def report_12m_asset(data, report_date, asset_name):
    
    date_list, y_list, _=calculations.line_chart_data_prep(data, report_date, asset_name)
    
    fig_asset = go.Figure()
    
    fig_asset.add_trace(go.Scatter(x=date_list[-12:],y=y_list[-12:],line={"color": "#067cc1"}, mode="lines", name="Total Asset",))
    
    fig_asset.update_layout(margin={'l':50,'b':20,'r':20,'t':20,}, yaxis={'type':'linear'},plot_bgcolor='white',paper_bgcolor='white',
                                height=200,width=340, autosize=False,hovermode='closest', showlegend=True,font={"family": "Raleway", "size": 10},
                                legend={
                                        "x": -0.0277108433735,
                                        "y": -0.142606516291,
                                        "orientation": "h",
                                    },)
    
    fig_asset.update_xaxes(autorange=True,
                            linecolor="rgb(0, 0, 0)",
                            linewidth=1,
                            showgrid=False,
                            showline=True,
                            title= "",
                            type="date",)
    
    fig_asset.update_yaxes(autorange=True,
                            gridcolor="rgba(127, 127, 127, 0.2)",
                            linecolor='black',
                            mirror=False,
                            nticks=6,
                            showgrid=True,
                            showline=True,
                            linewidth=1,
                            ticklen=5,
                            ticks='outside',
                            #title="",
                            type="linear",
                            zeroline=False,
                            zerolinewidth=4,)
    
    return fig_asset


def investment_line(df_in, report_date):
    
    date_list, y_list, sp_list=calculations.line_chart_data_prep(df_in, report_date, 'Investment')
    

    fig_line = make_subplots(specs=[[{"secondary_y": True}]])
    
    
    fig_line.add_trace(go.Scatter(x=date_list, y=y_list, mode='lines', line={"color": "#067cc1"},
                    name='Investment'),
                      secondary_y=False)
    
    fig_line.add_trace(go.Scatter(x=date_list, y=sp_list, mode='lines', line={"color": "#b5b5b5"},
                    name='S&P 500 Index'),
                       secondary_y=True)
    
    fig_line.update_yaxes(secondary_y=False,showgrid=True, showline=True, zeroline=False, gridcolor='#d5d7d8',
                               tickfont=dict(family='sans-serif',color='black',size=14),
                               range=[min(y_list)*0.7,max(y_list)*1.3])
    
    fig_line.update_yaxes(secondary_y=True,showgrid=False, showline=True, zeroline=False, gridcolor='#d5d7d8',
                               tickfont=dict(family='sans-serif',color='black',size=14),
                               range=[min(sp_list)*0.7,max(sp_list)*1.3])
    
    
    fig_line.update_layout(margin={'l':30,'b':30,'r':30,'t':30,}, yaxis={'type':'linear'},plot_bgcolor='white',paper_bgcolor='white',
                                height=200,width=700, font={"family": "Raleway", "size": 10},showlegend=True,
                                hoverlabel=dict(bgcolor="white",font_size=10,font_family="Rockwell"))
    
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

def top_mover_bar(data, report_date):
    
    x_list, y_curr_list, y_prev_list = calculations.prep_top_mover_data(data, report_date)
    
    fig_bar = go.Figure()
        
    fig_bar.add_trace(go.Bar(x=x_list[0:4], y=y_prev_list[0:4], name="Previous Month",
                            marker={
                                "color": "#dddddd",
                                "line": {
                                    "color": "rgb(255, 255, 255)",
                                    "width": 2},
                            },
                                                        
                        ),)
    
    fig_bar.add_trace(go.Bar(x=x_list[0:4], y=y_curr_list[0:4], name="Current Month",
                            marker={
                                "color": "#97151c",
                                "line": {
                                    "color": "rgb(255, 255, 255)",
                                    "width": 2},
                            },
                                                        
                        ),)
    
    # Change the bar mode
    fig_bar.update_layout(barmode='group')
    fig_bar.update_layout(margin={'l':10,'b':10,'r':0,'t':20,}, yaxis={'type':'linear'},plot_bgcolor='white',paper_bgcolor='white',
                                height=200,width=330, bargap=0.35,font={"family": "Raleway", "size": 10},hovermode="closest",
                                legend={"x": -0.0228945952895, "y": -0.189563896463,"orientation": "h","yanchor": "top",}
                                )
    fig_bar.update_yaxes(tickfont=dict(family='sans-serif',color='black',size=14), autorange=True, zeroline=False, showgrid=True, showline=True, linewidth=1)
    fig_bar.update_xaxes(autorange= True, range = [-0.5, 4.5], showline= True,
                         title="",type = "category")
    
    return fig_bar


def asset_allocation_pie(data, report_date, asset_class):
    
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
                          height=200,width=330,
                          hoverlabel=dict(bgcolor="white",font_size=16,font_family="Rockwell"),
                          annotations=[dict(text=asset_class, x=0.5, y=0.5, font_size=20, showarrow=False)],
                          )
    
    fig_pie.update(layout_showlegend=False)
    
    return fig_pie

def tier_stack_area(data, report_date):
    date_list, tier1_list, tier2_list, tier3_list = calculations.prep_tier_asset_data(data, report_date)
    y_range = [max(tier3_list)*0.8, (max(tier1_list)+max(tier2_list)+max(tier3_list))*1.05]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=date_list[-12:], y=tier3_list[-12:],
        name='Tier 3',
        hoverinfo='x+y',
        mode='lines',
        line=dict(width=0.5, color='#4c9cc2'),
        stackgroup='one' # define stack group
    ))
    fig.add_trace(go.Scatter(
        x=date_list[-12:], y=tier2_list[-12:],
        name='Tier 2',
        hoverinfo='x+y',
        mode='lines',
        line=dict(width=0.5, color='#3275b1'),
        stackgroup='one'
    ))
    fig.add_trace(go.Scatter(
        x=date_list[-12:], y=tier1_list[-12:],
        name='Tier 1',
        hoverinfo='x+y',
        mode='lines',
        line=dict(width=0.5, color='#427d9a'),
        stackgroup='one'
    ))

    fig.update_layout(margin={'l':30,'b':30,'r':30,'t':30,}, yaxis={'type':'linear'},plot_bgcolor='white',paper_bgcolor='white',
                                height=200,width=700, autosize=True, font={"family": "Raleway", "size": 10},hovermode="closest",
                                legend={"orientation": "v","yanchor": "top",}
                                )
    
    fig.update_yaxes(tickfont=dict(family='sans-serif',color='black',size=14), range=y_range, zeroline=False, showgrid=True, showline=True, gridcolor='#676d72',linecolor='#4c5359', linewidth=1)
    fig.update_xaxes(range=[date_list[-12],date_list[-1]], showline= False, linecolor='#3c444a',linewidth=1, showgrid=False, gridcolor='#676d72',
                         title="",type = "date")
    
    return fig

