#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 14:10:19 2018

@author: emmaworthington
"""

import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
from datetime import datetime

year = np.array((1957, 1981, 1992, 1998, 2004))
amoc = np.array((22.9, 18.7, 19.4, 16.1, 14.8))

fig1 = plt.figure(figsize=(10, 10))
plt.scatter(year, amoc, s=300)
plt.tick_params(labelsize=20)
plt.ylim((0, 30))
plt.xlabel('Year of hydrographic section', fontsize=24)
plt.ylabel('AMOC [Sv]\n(net transport 0 - 1000 m)', fontsize=24)
plt.tight_layout()
fig1.savefig('../figures/bryden2005.png', format='png', dpi=1000, 
        bbox_inches='tight', transparent=False)

# Plot MAR MOC
output_dir = '/Users/emmaworthington/OneDrive/PhD/Data/rapid/'
moc_transports = xr.open_dataset(
        output_dir + 'netcdf-moc_transports/moc_transports.nc')
amoc = moc_transports['moc_mar_hc10'].values
amoc_time = moc_transports['time'].values

x_05 = datetime(2005, 1, 1)
x_07 = datetime(2007, 1, 1)
x_09 = datetime(2009, 1, 1)
x_11 = datetime(2011, 1, 1)
x_13 = datetime(2013, 1, 1)
x_15 = datetime(2015, 1, 1)
x_17 = datetime(2017, 1, 1)

fig2 = plt.figure(figsize=(10, 10))
plt.plot(amoc_time, amoc)
plt.xlim((amoc_time[0], amoc_time[-1]))
plt.tick_params(labelsize=20)
plt.xticks(
        (x_05, x_07, x_09, x_11, x_13, x_15, x_17),
        ('2005', '2007', '2009', '2011', '2013', '2015', '2017'),
        fontsize=20)
plt.xlabel('Year', fontsize=24)
plt.ylabel('AMOC [Sv]', fontsize=24)
plt.tight_layout()
fig2.savefig('../figures/amoc.png', format='png', dpi=1000, 
        bbox_inches='tight', transparent=False)