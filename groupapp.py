import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import folium



# Page configuration
st.set_page_config(page_title="AI and Automation Takeover", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
slide = st.sidebar.radio(
    "Go to",
    [
        "Layoffs and Workforce Dynamics",
        "Automation Growth",
        "AI Advancement",
        "AI Accuracy on Knowledge Tests",
        "Countries Leading the AI Revolution",
        "Industries Most at Risk"
    ]
)

# Page content logic
st.title("Artificial Intelligence and Automation Takeover")


if slide == "Layoffs and Workforce Dynamics":
    st.header("Dataset 1: Matplotlib Visualization")
    
    fig, ax = plt.subplots()
    x = np.arange(0, 10)
    y = x ** 2
    ax.plot(x, y, marker='o')
    ax.set_title("Matplotlib Line Plot")
    st.pyplot(fig)
    
elif slide == "Automation Growth":
    st.header("Dataset 2: Plotly Visualization")
    
    df = pd.DataFrame({
        'x': np.random.rand(50),
        'y': np.random.rand(50),
        'size': np.random.randint(10, 100, 50)
    })
    fig = px.scatter(df, x='x', y='y', size='size', title="Plotly Scatter Plot")
    st.plotly_chart(fig)
    
elif slide == "AI Advancement":
    st.header("Dataset 3: Folium Map Visualization")
    
    m = folium.Map(location=[37.7749, -122.4194], zoom_start=12)
    folium.Marker(location=[37.7749, -122.4194], popup="San Francisco").add_to(m)
    
    st.components.v1.html(m._repr_html_(), height=500)


# Footer
st.markdown("---")
st.markdown("Created by Tyler Gaudino, Logan Caraballo, and Jose Nieves © 2025")