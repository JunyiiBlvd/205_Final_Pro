import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

ai = pd.read_csv('https://raw.githubusercontent.com/JunyiiBlvd/205_Final_Pro/refs/heads/master/The%20Rise%20Of%20Artificial%20Intellegence2.csv')

ai['Organizations Using AI'] = ai['Organizations Using AI'].str.replace('%','')
ai['Organizations Planning to Implement AI'] = ai['Organizations Planning to Implement AI'].str.replace('%','')
ai['Organizations Believing AI Provides Competitive Edge'] = ai['Organizations Believing AI Provides Competitive Edge'].str.replace('%','')
ai['Medical Professionals Using AI for Diagnosis'] = ai['Medical Professionals Using AI for Diagnosis'].str.replace('%','')
ai['Global Expectation for AI Adoption (%)'] = ai['Global Expectation for AI Adoption (%)'].str.replace('%','')
ai['Expected Increase in Employee Productivity Due to AI (%)'] = ai['Expected Increase in Employee Productivity Due to AI (%)'].str.replace('%','')
ai['Net Job Loss in the US'] = ai['Net Job Loss in the US'].str.replace('%','')

st.write("data:", ai.head())

fig = px.line(
    ai,
    x = 'Year',
    y = ['AI Software Revenue(in Billions)',
         'Global AI Market Value(in Billions)'],
    markers = True,
    title = 'The Value of Aritifical Intelligence'
)

fig.update_layout(
    yaxis_title = 'Value (Billions $)',
    yaxis_range = [0,2000]
)

st.plotly_chart(fig)

fig1 = px.line(
    ai,
    x = 'Year',
    y = ['Organizations Using AI',
    'Organizations Planning to Implement AI',
    'Medical Professionals Using AI for Diagnosis',
    'Expected Increase in Employee Productivity Due to AI (%)'],
    title = 'AI in the Field',
    markers = True
)

fig1.update_layout(
    yaxis_title = 'Percentage (%)',
    yaxis_range = [0,70]
)

st.plotly_chart(fig1)

#fig2 = plt.figure()
#ax = fig2.add_subplot()
#ax.hist(ai['Year'], weights = ai['Net Job Loss in the US'], bins = len(ai['Year'].unique()))
#st.pyplot(fig2)

