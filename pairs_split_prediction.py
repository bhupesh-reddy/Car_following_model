# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 19:53:31 2022

@author: bhupe
"""

import warnings
import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score


warnings.filterwarnings('ignore')
def data_in_parts(data30,rangefrom,rangeto):
    a=data30['LF_pairs'].unique()
    b = a.tolist()
    b = b[rangefrom:rangeto]
    c= len(a)/30
    return c,b 


def prediction(data30,b,target_variable,RFReg):
    F_df = []
    r = []
    Q = pd.DataFrame()

    for i in b:

        Q = data30[data30['LF_pairs']== i]

        vel=np.zeros(Q.shape[0])
        local_y = np.zeros(Q.shape[0])
        frspacing = np.zeros(Q.shape[0])
        dv = np.zeros(Q.shape[0])
        pred_acc = np.zeros(Q.shape[0])
        dA = np.zeros(Q.shape[0])
    
        #adding first value of the vehicle
        vel[0]=Q.iloc[0]['svel']
        local_y[0] = Q.iloc[0]['Local.Y']
        frspacing[0] = Q.iloc[0]['frspacing']
   #check here
        dv[0] = Q.iloc[0]['dV']
        dA[0] = Q.iloc[0]['dA']    
        #pred_speed[0] = Q.iloc[0]['svel']
        pred_acc[0] = Q.iloc[1][target_variable]
     
    

#     #predicting first value of acceleration
            #check here
        pred_acc[1]= RFReg.predict(np.array([frspacing[0],dv[0],vel[0],dA[0]]).reshape(1,-1))
            

#     #calculating vel,frspacing,local.y,dv from the predicted acceleration.
            #check here
        vel[1] = vel[0]+(pred_acc[1]*0.1)
        dv[1] = vel[1] - Q.iloc[1]['PrecVehVel']

#     ## localy: s = ut + 0.5*a*t^2
        local_y[1] = local_y[0] + ((vel[0]*0.1)+ (0.5*pred_acc[1]*pow(0.1,2)))
        frspacing[1] = Q.iloc[1]['PrecVehLocalY'] - local_y[1] - Q.iloc[1]['PrecVehLength']
        dA[1] = Q.iloc[1]['dA']
    
    
        for j in range(2,len(Q)):
#         ########
#         #print(j)
#         ########
            vel[j] = vel[j-1]+(pred_acc[j]*0.1)
            dv[j] = vel[j] - Q.iloc[j]['PrecVehVel']
#         ########
#         ## localy: s = ut + 0.5*a*t^2
#         ########
            local_y[j] = local_y[j-1] + ((vel[j-1]*0.1)+ (0.5*pred_acc[j]*pow(0.1,2)))
            frspacing[j] = Q.iloc[j]['PrecVehLocalY'] - local_y[j] - Q.iloc[j]['PrecVehLength']
            dA
            if j == len(Q)-1:
                break
            pred_acc[j+1] = RFReg.predict(np.array([frspacing[j],dv[j],vel[j],dA[j]]).reshape(1, -1))
#         ########
#         #print(pred_acc)
#         ########
        Q['pacc']=pred_acc
        Q['pvel']=vel
        Q['pposition']= local_y
        Q['pdv']= dv
        Q['pfrspacing']=frspacing
        F_df.append(Q)
        result = pd.concat(F_df)
        #r.append(r2_score(Q[target_variable], Q['pacc']))
        
 
    return result
