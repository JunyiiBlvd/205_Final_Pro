import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

projection = pd.read_csv('https://raw.githubusercontent.com/JunyiiBlvd/205_Final_Pro/refs/heads/master/employment-projections.csv')

projection.rename(columns = {projection.columns[1]: 'Percent change'}, inplace = True)

st.write('Raw Data Set:', projection.head())

colors = ['green' if i >= 0 else 'red' for i in projection['Percent change']]

fig = plt.figure(figsize = (12,6))
ax = fig.add_subplot()
ax.bar(projection['Occupation'], projection['Percent change'], color = colors)
ax.set_xlabel('Occupation')
ax.set_ylabel('Percent Change')
ax.set_ylim(-10,20)
ax.set_title("Employment projections per occupations 2023-2033")
ax.set_xticklabels(projection['Occupation'],rotation = 45, ha = 'right')
#ax.hlines(y= 0, color = 'black')
st.pyplot(fig)