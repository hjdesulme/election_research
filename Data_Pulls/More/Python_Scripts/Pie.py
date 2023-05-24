#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat June 8 22:58:00 2019

@author: handell
"""

import plotly.plotly as py
import plotly.graph_objs as go

labels = ['Hillary Clinton: (United States)','Bernie Sanders: (United States)']
values = [3765,3808]

trace = go.Pie(labels=labels, values=values)

py.iplot([trace], filename='Candidate-Democratic-Primary-United_States-Cumulative')