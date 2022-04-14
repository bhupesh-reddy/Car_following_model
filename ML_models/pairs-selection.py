# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 19:05:15 2022

@author: bhupe
"""
import random

def training_pairs(data):
    random.seed(2109)
    pairs = data["LF_pairs"].unique()
    pairs = pairs.tolist()
    v = round(len(pairs)*0.7)
    pairs = random.sample(pairs, v)
    return pairs
