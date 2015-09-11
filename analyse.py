# -*- coding: utf-8 -*-
"""
Created on Wed Sep 09 17:02:15 2015

@author: Alexis Eidelman
"""

from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dates

import load

pb = (df.avant_date_signature < datetime(2012, 1, 1, 0, 0)) | \
     (df.avant_date_signature >= datetime(2015, 10, 1, 0, 0))
df = df[~pb]
# => remove 223 lines and 90 000€ de montants

cond_avantage = (df.conv_objet == '') | (df.conv_objet.isnull())
av = df[df.ligne_type == '[A]']  # 4052619 lignes
conv = df[df.ligne_type == '[C]']  # 1634478 lignes

df.ligne_type.value_counts()

##
av.avant_montant_ttc.sum()
pd.DatetimeIndex(av.avant_date_signature)
date = pd.DatetimeIndex(av.avant_date_signature.tolist())

mois = 12*(date.year - date.year.min()) + date.month

av.groupby(mois)['avant_montant_ttc'].sum().plot(kind='bar')

date_label = [str(2012 + x) + '-' + str(y) for x in range(4) for y in range(1,13)]
idx = pd.date_range('2012-10-01', '2015-10-01', freq='M')

#fig, ax = plt.subplots()
#ax.plot_date(idx.to_pydatetime(), montant_total_par_mois, 'v-')
#
#montant_total_par_mois = av.groupby(mois)['avant_montant_ttc'].sum()
#montant_total_par_mois.plot(kind='bar', xticks=idx)
#fig = plt.figure(figsize=(16,12))
## Add a subplot
ax = fig.add_subplot(111)
montant_total_par_mois.plot(kind='bar', ax=ax, xticks=date_label[10:-2])
# ax.set_xticklabels(date_label[10:-2])

cond_regard_citoyens = (av.avant_date_signature >= datetime(2012, 1, 1, 0, 0)) & \
    (av.avant_date_signature < datetime(2014, 7, 1, 0, 0))


rgd_cit = av[cond_regard_citoyens]
rgd_cit.avant_montant_ttc.sum()/1e6
df.avant_montant_ttc.sum()/1e6
# => 440 M€
