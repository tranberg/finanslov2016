# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
Hvor mange dronninger kan DK forsørge for ulandsbistanden?

Data: kategori 063201 og 063202 fra http://www.oes-cs.dk/olapdatabase/finanslov/index.cgi
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
    ax.tick_params(color=color, labelcolor=color)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

years = range(2014, 2020)
yearNames = ['R2014', 'B2015', 'F2016', 'BO2017', 'BO2018', 'BO2019']
path = 'data/'
a = pd.read_csv(path + '2016-expenses.csv', sep=';')
af = pd.read_csv(path + 'bilateral-afrika.csv', sep=';')
la = pd.read_csv(path + 'bilateral-latin-asien.csv', sep=';')

# Index of countries in data loaded above
africaDict = {
    'Etiopien': 103,
    'Niger': 104,
    'Zimbabwe': 105,
    'Somalia': 106,
    'Sydsudan': 107,
    'Tanzania': 108,
    'Kenya': 109,
    'Uganda': 110,
    'Mozambique': 111,
    'Ghana': 112,
    'Benin': 113,
    'Burkina Faso': 114,
    'Zambia': 115,
    'Mali': 116
}
latinAsiaDict = {
    'Pakistan': 119,
    'Myanmar': 120,
    'Cambodja': 121,
    'Indonesien': 122,
    'Palæstina': 123,
    'Afganistan': 124,
    'Bangladesh': 125,
    'Nepal': 126,
    'Bhutan': 127,
    'Vietnam': 128,
    'Nicaragua': 130,
    'Bolivia': 131
}

queen = []
for year in years:
    if year == 2019:
        queen.append(a[str(year) + ' '][0])
    else:
        queen.append(a[str(year)][0])

afNames = list(af[af.columns[0]])
latinAsiaNames = list(la[la.columns[0]])

africaData = af[af.columns[1:]].as_matrix()
latinAsiaData = la[la.columns[1:]].as_matrix()

afNorm = np.divide(africaData, queen)
laNorm = np.divide(latinAsiaData, queen)

plt.figure(figsize=(7, 8))
ax = plt.subplot(111)
plt.pcolormesh(afNorm, cmap='Blues')
plt.colorbar(label="Antal dronninger")
ax.xaxis.set_tick_params(width=0)
ax.yaxis.set_tick_params(width=0)
ax.set_xticks(np.linspace(0, 5, 6))
ax.set_xticklabels([' ' + yearNames[i] for i in range(len(years))], ha='left', va='top', fontsize=11)
ax.set_yticks(np.linspace(0.5, 14.5, 15))
ax.set_yticklabels(afNames, fontsize=13)
plt.axis([0, 6, 0, 15])
plt.title(u'Ulandsbistand (Afrika) normeret til udgifter på Dronningen')
plt.savefig('img/queen-afrika.png', bbox_inches='tight')

plt.figure(figsize=(7, 8))
ax = plt.subplot(111)
plt.pcolormesh(laNorm, cmap='Blues')
plt.colorbar(label="Antal dronninger")
ax.xaxis.set_tick_params(width=0)
ax.yaxis.set_tick_params(width=0)
ax.set_xticks(np.linspace(0, 5, 6))
ax.set_xticklabels([' ' + yearNames[i] for i in range(len(years))], ha='left', va='top', fontsize=11)
ax.set_yticks(np.linspace(0.5, 14.5, 15))
ax.set_yticklabels(latinAsiaNames, fontsize=13)
plt.axis([0, 6, 0, 14])
plt.title(u'Ulandsbistand (Latinamerika, Asien) normeret til udgifter på Dronningen')
plt.savefig('img/queen-latin.png', bbox_inches='tight')

queenSum = sum(queen)
afSum = np.sum(africaData, 1)
laSum = np.sum(latinAsiaData, 1)

plt.figure()
ax = plt.subplot(111)
plt.bar(range(15), afSum / queenSum, color='#337AB7', edgecolor='#337AB7')
ax.yaxis.grid(True)
ax.xaxis.set_tick_params(width=0)
ax.set_xticks(np.linspace(.6, 14.6, 15))
ax.set_xticklabels(afNames, rotation=60, ha='right', va='top', fontsize=11)
plt.axis([0, 14.8, -.5, 3.5])
simpleaxis(ax)
plt.title(u'Ulandsbistand til Afrika normeret til udgifter på Dronningen')
plt.savefig('img/queen-afrika-total.png', bbox_inches='tight')

plt.figure()
ax = plt.subplot(111)
plt.bar(range(14), laSum / queenSum, color='#337AB7', edgecolor='#337AB7')
ax.yaxis.grid(True)
ax.xaxis.set_tick_params(width=0)
ax.set_xticks(np.linspace(.6, 13.6, 14))
ax.set_xticklabels(latinAsiaNames, rotation=60, ha='right', va='top', fontsize=11)
plt.axis([0, 13.8, -.5, 2.5])
simpleaxis(ax)
plt.title(u'Ulandsbistand til Latinamerika/Asien normeret til udgifter på Dronningen')
plt.savefig('img/queen-latin-total.png', bbox_inches='tight')
