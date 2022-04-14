# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 18:55:20 2022

@author: bhupe
"""

import pairsselection
import pandas as pd
import pairs_split_prediction
import numpy as np
import matplotlib.pyplot as plt
import sklearn.metrics as metrics
import seaborn as sns
import random
from sklearn.ensemble import RandomForestRegressor
import plot_vehicle_pair
import matplotlib.backends.backend_pdf
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score


#Loading the dataset.
df_new = pd.read_csv("D:\STUDY MATERIALS\SEMESTER-4\DAB 402 CAPSTONE PROJECT\Internal Project\i80_processed.csv")

#Filtering the vehicle pairs with higher than 30sec of data. 
df = df_new[df_new["Time_per_pair"] > 30]

df = df.drop(['nextframeAcc','nextframesvel','nextframeposition'], axis=1)


df["Reaction_time_1.0_acc"]=df.groupby(["LF_pairs"],as_index=False)["sacc"].shift(-10)
df["Reaction_time_1.0_position"]=df.groupby(["LF_pairs"],as_index=False)["Local.Y"].shift(-10)
df["Reaction_time_1.0_vel"]=df.groupby(["LF_pairs"],as_index=False)["svel"].shift(-10)


#df = df.drop(['Reaction_time_0.3'], axis=1)



df = df[df["Reaction_time_1.0_acc"].notna()]
#Random Pairs selections
my_pairs=pairsselection.training_pairs(df)
print(len(my_pairs))


#Train and Test datasets
data70 = pd.DataFrame()
data30 = pd.DataFrame()

data70 = df[df['LF_pairs'].isin(my_pairs)]

data30 = df[~df['LF_pairs'].isin(my_pairs)]

#Features and Target varibales for RF model.

X_train = data70[["frspacing",'dV','svel','dA']]
y_train= data70['Reaction_time_1.0_acc']

#Random Forest model

RFReg = RandomForestRegressor(n_estimators = 150,n_jobs=-1)

#Fitting the model.
RFReg.fit(X_train,y_train)

#training score.
RFReg.score(X_train,y_train)

#Feature importance for the model.
RFReg.feature_importances_

#Ploting the feature importance.
plt.barh(X_train.columns,RFReg.feature_importances_)

# len(data30['LF_pairs'].unique())


#pairs split
c, b = pairs_split_prediction.data_in_parts(data30,0,150)
print(b)



#Predicted acceleration
target_variable = 'Reaction_time_1.8_acc'
F = pairs_split_prediction.prediction(data30, b, target_variable, RFReg)


# #Appending all the results into one list.
#FDS = FDS + F
# r2 = r2 + rscore
# MAE = MAE + Mae 



#Merging the datasets into all the list.
#Final_out = plot_vehicle_pair.merging_dataset(F)

F.to_csv("result_dataset_1.8_acc.csv")

# print(Final_out)

# path = "output_plots.pdf"
# PLotting the graph
#plot_vehicle_pair.plot_pred_acc_vehicle_pairs(Final_out,path)

# #MAE score
# mae_score = mean_absolute_error(F['Reaction_time_0.4_acc'], F['pacc'])
# r2_scores = r2_score(F['Reaction_time_0.4_acc'], F['pacc'])


# pdf = matplotlib.backends.backend_pdf.PdfPages("output_plots.pdf")
# for d in FDS:
#     fig, ax = plt.subplots()
#     sns.set(rc = {'figure.figsize':(15,8)})
#     sns.lineplot(data = d[['pacc','acc_after5sec']]).set(title='Observed acceleration vs the predicted acceleration plot for_Vehicle_pair_'+d['LF_pairs'].unique()+'.')
#     plt.legend(labels=["pacc","observered acceleration"])
#     pdf.savefig(fig)
#     print(d['LF_pairs'].unique())
# pdf.close()

