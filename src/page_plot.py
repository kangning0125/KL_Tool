# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 14:52:58 2020

@author: Xian&Kang
"""

import plotly.graph_objects as go
import pandas as pd
import numpy as np

def waterfall(df_in, date, interval):
    
    fig_waterfall = go.Figure()
    
    fig_waterfall.add_trace(go.Waterfall(
    name = 'networth', orientation = "v",
    measure = ["absolute", "relative", "relative", "relative", "relative", "relative", "relative", "relative", "total"],
    x = ["12/31/2015", "Deposits", 'Investment', "ESP", "401k", 'Real Estate', 'Mortgage','Loan',"1/31/2016"],
    textposition = "outside",
    #text = ["", "+80", "", "-40", "-20", "Total"],
    y = [20, 40, 30, 10, 10, -10, -40, -20, 100],
    connector = {"line":{"color":"rgb(63, 63, 63)"}},))
    
    #fig_waterfall.update_xaxes(showgrid=False, showline=True, linewidth=2, linecolor='#404b6b', mirror=True, tickfont=dict(family='sans-serif',color='#fffef9',size=14))
    fig_waterfall.update_yaxes(showgrid=True, showline=False, zeroline=False, gridcolor='#d5d7d8',
                               tickfont=dict(family='sans-serif',color='black',size=14),
                               range=[0,200])
    
    
    fig_waterfall.update_layout(margin={'l':40,'b':0,'r':0,'t':20,}, yaxis={'type':'linear'},plot_bgcolor='white',paper_bgcolor='white',
                                height=250,width=580, hoverlabel=dict(
                                                                    bgcolor="white",
                                                                    font_size=16,
                                                                    font_family="Rockwell"
                                                                ))
    
    return fig_waterfall


def dash_line(df_in, date, asset_name, span):
    
    fig_line = go.Figure()
    
    N = 100
    random_x = np.linspace(0, 1, N)
    random_y0 = np.random.randn(N) + 5
    
    fig_line.add_trace(go.Scatter(x=random_x, y=random_y0,
                    mode='lines',
                    name='lines'))
    
    #fig_waterfall.update_xaxes(showgrid=False, showline=True, linewidth=2, linecolor='#404b6b', mirror=True, tickfont=dict(family='sans-serif',color='#fffef9',size=14))
    fig_line.update_yaxes(showgrid=True, showline=False, zeroline=False, gridcolor='#d5d7d8',
                               tickfont=dict(family='sans-serif',color='black',size=14),
                               range=[0,10])
    
    
    fig_line.update_layout(margin={'l':40,'b':0,'r':0,'t':20,}, yaxis={'type':'linear'},plot_bgcolor='white',paper_bgcolor='white',
                                height=250,width=580, hoverlabel=dict(
                                                                    bgcolor="white",
                                                                    font_size=16,
                                                                    font_family="Rockwell"
                                                                ))
    
    return fig_line


def dash_stackbar():
    fig_bar = go.Figure()
    fig_bar.add_trace(go.Bar(name='Tier3',x=['Asset'], y=[20]))
    fig_bar.add_trace(go.Bar(name='Tier2',x=['Asset'], y=[10]))
    fig_bar.add_trace(go.Bar(name='Tier1',x=['Asset'], y=[50]))
    
    # Change the bar mode
    fig_bar.update_layout(barmode='stack')
    fig_bar.update_layout(margin={'l':40,'b':0,'r':0,'t':20,}, yaxis={'type':'linear'},plot_bgcolor='white',paper_bgcolor='white',
                                height=280,width=290, hoverlabel=dict(
                                                                    bgcolor="white",
                                                                    font_size=16,
                                                                    font_family="Rockwell"
                                                                ))
    return fig_bar

def dash_pie():
    labels = ['A1','B2','C3','D4']
    values = [4500, 2500, 1053, 500]

    fig_pie = go.Figure()
    fig_pie.add_trace(go.Pie(
        labels=labels, values=values,hoverinfo='label+value+percent', textinfo='label+percent',
        marker={'colors': [
                'rgb(0, 204, 0)',
                'rgb(255, 255, 0)',
                'rgb(118, 17, 195)',
                'rgb(0, 48, 240)',
                # 'rgb(240, 88, 0)',
                # 'rgb(215, 11, 11)',
                # 'rgb(11, 133, 215)',
                # 'rgb(0, 0, 0)',
                # 'rgb(0, 0, 0)',
                # 'rgb(0, 0, 0)'
              ]},
        sort=False
    ))
    
    fig_pie.update_layout(margin={'l':40,'b':0,'r':0,'t':20,}, yaxis={'type':'linear'},plot_bgcolor='white',paper_bgcolor='white',
                                height=290,width=290, hoverlabel=dict(
                                                                    bgcolor="white",
                                                                    font_size=16,
                                                                    font_family="Rockwell"
                                                                ))
    fig_pie.update(layout_showlegend=False)
    
    return fig_pie



