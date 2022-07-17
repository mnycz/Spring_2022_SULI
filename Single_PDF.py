import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure

figure(figsize=(10,5))
data=pd.read_csv("/Users/kiern/OneDrive/Desktop/PDFs_NNPDF40NLO.csv ")
data2=pd.read_csv("/Users/kiern/OneDrive/Desktop/PDFs_uncer_NNPDF40NLO.csv  ")


fig, ax = plt.subplots()

plt.xlabel("Bin Number #",fontsize=14)
plt.ylabel("",fontsize=14)



plt.plot(data["bin_num "], data[" Rc "]/data[" Rc "], 'r',label="Rc")
lower=(data[" Rc "].to_numpy()-((data[" Rc "].to_numpy())*(data2[" Rc "].to_numpy())))*(1.0/(data[" Rc "].to_numpy()))
upper=(data[" Rc "].to_numpy()+((data[" Rc "].to_numpy())*(data2[" Rc "].to_numpy())))*(1.0/(data[" Rc "].to_numpy()))


plt.fill_between(data["bin_num "],lower,upper,color='blue',alpha=0.25,label="Rc Error NNPDF40NLO")


plt.title("NNPDF40NLO Rc Uncertainty ")
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.grid()
plt.legend( loc='upper left',bbox_to_anchor=(0.4,1.02),prop={'size':11})
plt. savefig("NNPDF40NLO_Rc_Uncer.pdf", format="pdf", bbox_inches="tight") 
