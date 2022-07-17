"""
plots excel file uncertanties 

"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
figure(figsize=(10,5))
data=pd.read_csv("/Users/kiern/OneDrive/Desktop/JAM22_PY.csv ")
plt.xlabel("Bin Number #",fontsize=14)
plt.ylabel("",fontsize=14)
plt.plot(data["bin_num "],data[' Apv_theory '],color="0",label="$A_{SM,0}^{Theory}$")
plt.plot(data["bin_num "],data[' stat_error '],color="b",label="$\sigma_{stat}$")
plt.plot(data["bin_num "],data[' corr_error '],color="c",label="$\sigma_{POL + Q2}$")
plt.plot(data["bin_num "],data[' uncorr_error '],color="g",label="$\sigma_{Rad + Event}$")
plt.plot(data["bin_num "],data[' pdf_error '],color="r",label="$\sigma_{PDF}$")
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

plt.yscale('log')
plt.grid()
plt.title("JAM22")
plt.legend( loc='upper left',bbox_to_anchor=(0.3,0.85),prop={'size':13},ncol = 1)
plt. savefig("JAM22.pdf", format="pdf", bbox_inches="tight") 
print(data)