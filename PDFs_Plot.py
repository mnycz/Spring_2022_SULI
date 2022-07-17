# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 09:36:39 2022

@author: kiern
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure

figure(figsize=(10,5))
data=pd.read_csv("/Users/kiern/OneDrive/Desktop/PDFs_NNPDF31NLO.csv ")
data2=pd.read_csv("/Users/kiern/OneDrive/Desktop/PDFs_uncer_NNPDF31NLO.csv  ")
data3=pd.read_csv("/Users/kiern/OneDrive/Desktop/PDFs_CT18NLO.csv ")
data4=pd.read_csv("/Users/kiern/OneDrive/Desktop/PDFS_uncer_CT18NLO.csv  ")
data5=pd.read_csv("/Users/kiern/OneDrive/Desktop/PDFs_JAM22.csv ")
data6=pd.read_csv("/Users/kiern/OneDrive/Desktop/PDFS_uncer_JAM22.csv  ")
data7=pd.read_csv("/Users/kiern/OneDrive/Desktop/PDFs_PDF4LHC21_40.csv ")
data8=pd.read_csv("/Users/kiern/OneDrive/Desktop/PDFS_uncer_PDF4LHC21_40.csv  ")
data9=pd.read_csv("/Users/kiern/OneDrive/Desktop/PDFs_NNPDF40NLO.csv ")
data10=pd.read_csv("/Users/kiern/OneDrive/Desktop/PDFs_uncer_NNPDF40NLO.csv  ")


fig, ax = plt.subplots()

plt.xlabel("Bin Number #",fontsize=14)
plt.ylabel("",fontsize=14)

#plt.plot(data["bin_num "], data[" Rc "]/data[" Rc "], 'r',label="Rc")
#plt.plot(data3["bin_num "], data3[" Rc "]/data3[" Rc "], 'r',label="Rc")

#plt.hlines(y=1.000, xmin=0, xmax=22, linestyles='-',lw=0.8,color="k")


lower=(data[" Rs "].to_numpy()-((data[" Rs "].to_numpy())*(data2[" Rs "].to_numpy())))*(1.0/(data[" Rs "].to_numpy()))
upper=(data[" Rs "].to_numpy()+((data[" Rs "].to_numpy())*(data2[" Rs "].to_numpy())))*(1.0/(data[" Rs "].to_numpy()))

lower2=(data3[" Rs "].to_numpy()-((data3[" Rs "].to_numpy())*(data4[" Rs "].to_numpy())))*(1.0/(data3[" Rs "].to_numpy()))
upper2 = (data3[" Rs "].to_numpy()+((data3[" Rs "].to_numpy())*(data4[" Rs "].to_numpy())))*(1.0/(data3[" Rs "].to_numpy()))

lower3=(data5[" Rs "].to_numpy()-((data5[" Rs "].to_numpy())*(data6[" Rs "].to_numpy())))*(1.0/(data5[" Rs "].to_numpy()))
upper3 = (data5[" Rs "].to_numpy()+((data5[" Rs "].to_numpy())*(data6[" Rs "].to_numpy())))*(1.0/(data5[" Rs "].to_numpy()))


lower4=(data7[" Rs "].to_numpy()-((data7[" Rs "].to_numpy())*(data8[" Rs "].to_numpy())))*(1.0/(data7[" Rs "].to_numpy()))
upper4= (data7[" Rs "].to_numpy()+((data7[" Rs "].to_numpy())*(data8[" Rs "].to_numpy())))*(1.0/(data7[" Rs "].to_numpy()))


lower5=(data9[" Rs "].to_numpy()-((data9[" Rs "].to_numpy())*(data10[" Rs "].to_numpy())))*(1.0/(data9[" Rs "].to_numpy()))
upper5= (data9[" Rs "].to_numpy()+((data9[" Rs "].to_numpy())*(data10[" Rs "].to_numpy())))*(1.0/(data9[" Rs "].to_numpy()))

#plt.fill_between(data["bin_num "],lower,upper,color='blue',alpha=0.25,label="Rv Error NN")

plt.fill_between(data["bin_num "],lower2,upper2,color='green',alpha=0.5,label="Rs Error CT18NLO")

plt.fill_between(data["bin_num "],lower3,upper3,color='purple',alpha=0.25,label="Rs Error JAM22")

#plt.fill_between(data["bin_num "],lower4,upper4,color='purple',alpha=0.25,label="Rv Error LHC")

plt.plot(data["bin_num "],lower,color="b",label="Rs Error NNPDF31NLO")
plt.plot(data["bin_num "],upper,color="b")

plt.plot(data["bin_num "],lower5,color="0",label="Rs Error NNPDF40NLO")
plt.plot(data["bin_num "],upper5,color="0")

plt.plot(data["bin_num "],lower4,color="red",label="Rs Error PDF4LHC21")
plt.plot(data["bin_num "],upper4,color="red")



for i in range(23):
    
    print(lower[i])
    
#plt.yscale("log")
plt.title("Rs Uncertainty ")
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.grid()
plt.legend( loc='upper left',bbox_to_anchor=(0.01,1),prop={'size':10},ncol=1)
plt. savefig("ALL_Rs.pdf", format="pdf", bbox_inches="tight") 
print(data)