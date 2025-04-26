import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import folium


st.set_page_config(page_title="AI and Automation Takeover", layout="wide")

col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    st.markdown("### Team Members")
    st.write("Jose")
    st.write("Logan")
    st.write("Tyler")

with col2:
    st.title("Artificial Intelligence and Automation Takeover")

with col3:
    
    st.write("")

st.markdown("---")  


slide = st.sidebar.radio("Select Visualization Slide", ["Slide 1", "Slide 2", "Slide 3"])


if slide == "Slide 1":
    st.header("Dataset 1: Matplotlib Visualization")
    
    fig, ax = plt.subplots()
    x = np.arange(0, 10)
    y = x ** 2
    ax.plot(x, y, marker='o')
    ax.set_title("Matplotlib Line Plot")
    st.pyplot(fig)
    
elif slide == "Slide 2":
    st.header("Dataset 2: Plotly Visualization")
    
    df = pd.DataFrame({
        'x': np.random.rand(50),
        'y': np.random.rand(50),
        'size': np.random.randint(10, 100, 50)
    })
    fig = px.scatter(df, x='x', y='y', size='size', title="Plotly Scatter Plot")
    st.plotly_chart(fig)
    
elif slide == "Slide 3":
    st.header("Dataset 3: Folium Map Visualization")
    
    m = folium.Map(location=[37.7749, -122.4194], zoom_start=12)
    folium.Marker(location=[37.7749, -122.4194], popup="San Francisco").add_to(m)
    
    st.components.v1.html(m._repr_html_(), height=500)

st.markdown("---")


st.header("Dataframe Preview")
st.write("This area will display your datasets as dataframes once they are ready.")
dummy_df = pd.DataFrame({
    "Column A": np.random.randint(0, 100, 10),
    "Column B": np.random.rand(10)
})
st.dataframe(dummy_df)
