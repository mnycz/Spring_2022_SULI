# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 13:17:10 2022

@author: kiern
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.pyplot import figure

figure(figsize=(10,5))
data=pd.read_csv("/Users/kiern/OneDrive/Desktop/PDFs_PDF4LHC21_40.csv ")
data2=pd.read_csv("/Users/kiern/OneDrive/Desktop/PDFs_uncer_PDF4LHC21_40.csv  ")

d=data[" D "].to_numpy()
u=data[" U "].to_numpy()


derr=data2[" D "].to_numpy()
uerr=data2[" U "].to_numpy()

val=d/u
derr_1=(derr/d)**2
uerr_1=(uerr/u)**2
sum=derr_1+uerr_1
sqrt_sum=np.sqrt(sum)
uncer=val*sqrt_sum



plt.plot(data["bin_num "], val/val, 'r',label="d/u")
#plt.plot(data["bin_num "], val, '--',label="d/u")
lower=((val-(uncer))*(1.0/(val)))
upper=((val+(uncer))*(1.0/(val)))


for i in range(len(lower)):
    print("--------")
    print(val[i])
    print(uncer[i])
    print(lower[i])
    print(upper[i])
    print("-------")


plt.fill_between(data["bin_num "],lower,upper,color='blue',alpha=0.25,label="d/u Error PDF4LHC21")


plt.title("PDF4LHC21 d/u Uncertainty ")
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.grid()
plt.legend( loc='upper left',bbox_to_anchor=(0.4,1.02),prop={'size':11})
plt. savefig("PDF4LHC21_d_over_u_Uncer.pdf", format="pdf", bbox_inches="tight") 