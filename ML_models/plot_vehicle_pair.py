# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 21:47:55 2022

@author: bhupe
"""

import pandas as pd
import matplotlib.backends.backend_pdf
import seaborn as sns
import matplotlib.pyplot as plt

def merging_dataset(F_df):
    x = pd.DataFrame()
    for d in range(0,len(F_df)-1):
        x = F_df[0]
        Final_out = pd.concat([x,F_df[d+1]])
    return Final_out
        

def plot_pred_acc_vehicle_pairs(F_df,path):
    
    pdf = matplotlib.backends.backend_pdf.PdfPages(path)
    
    for d in F_df:
        fig, ax = plt.subplots()
        sns.set(rc = {'figure.figsize':(15,8)})
        sns.lineplot(data = d[['pacc','acc_after5sec']]).set(title='Observed acceleration vs the predicted acceleration plot for_Vehicle_pair_'+d['LF_pairs'].unique()+'.')
        plt.legend(labels=["pacc","observered acceleration"])
        pdf.savefig(fig)
        print(d['LF_pairs'].unique())
    pdf.close()
    
    return 'file created!!!'
