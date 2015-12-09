# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
Sum af ekstraudgifter i ændringsforslag i procent af total foreslået udgift på paragraf-niveau

Et ca. mål for hvor meget der hvert år har flyttet sig under forhandlingerne af finansloven
"""


def simpleaxis(ax):
    """
    Nicer figures with less framing
    """
    color = 'black'
    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)
    for spine in ['bottom', 'left']:
        ax.spines[spine].set_edgecolor(color)
        ax.spines[spine].set_zorder(20)
    ax.tick_params(color=color, labelcolor=color)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

path = 'data/'
years = range(2003, 2016)

changeList = []
totChangeList = []
for y in years:
    year = str(y)

    a = pd.read_csv(path + year + '.csv', sep=';')
    aa = pd.read_csv(path + year + 'A.csv', sep=';')

    b = a[year].astype(float).as_matrix()
    bb = aa[year].astype(float).as_matrix()

    expenses = b[np.where(b > 0)]
    totExpenses = sum(expenses)

    changes = bb[np.where(bb > 0)]
    totChanges = sum(changes)
    totChangeList.append(totChanges)

    change = totChanges / totExpenses
    changeList.append(change * 100)


plt.figure(figsize=(10, 6))
ax = plt.subplot(111)
plt.bar(range(len(years)), changeList, color='#337AB7', edgecolor='#337AB7', zorder=10)
ax.set_xticklabels([str(years[i]) for i in range(len(years))], rotation=60, ha='right', va='top', fontsize=13)
ax.set_xticks(np.linspace(.6, 12.6, 13))
ax.yaxis.grid(True)
ax.xaxis.set_tick_params(width=0)
plt.axis([0, 12.8, 0, 10])
plt.title(u'Sum af ekstraudgifter i ændringsforslag i procent af total foreslået udgift på paragraf-niveau')
plt.ylabel('%')
simpleaxis(ax)
plt.savefig('img/changes.png', bbox_inches='tight')
