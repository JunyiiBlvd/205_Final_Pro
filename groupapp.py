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
        "Automation Growth and AI Progression",
        "AI Advancement",
        "AI Accuracy on Knowledge Tests",
        "Countries Leading the AI Revolution",
        "Industries Most at Risk"
    ]
)

# Page content logic
st.title("Artificial Intelligence and Automation Takeover")


if slide == "Layoffs and Workforce Dynamics":
    st.header("Layoffs and Workforce Dynamics")
    st.write("Explore layoff trends and workforce dynamics in the age of AI and automation.")


    # Load dataset
    layoffs_df = pd.read_csv('Layoff_Trend_Analyzed_30_Years_Final.csv')

    # Preview data
    st.write("Raw Data Sample:", layoffs_df.head())

    # Cleaning:
    # 1. Filter to only 2010–2024
    layoffs_df = layoffs_df[layoffs_df['Year'] >= 2010]

    # 2. Drop rows where critical data for graphing is missing
    layoffs_df = layoffs_df.dropna(subset=['Layoffs', 'Year'])

    # 3. Optional: Handle missing industry/company names separately if needed

    # 4. Make sure 'year' is an integer
    layoffs_df['Year'] = layoffs_df['Year'].astype(int)

    # Summarize layoffs and global events
    layoffs_summary = layoffs_df.groupby('Year').agg({
        'Layoffs': 'sum',
        'Global_Event': lambda x: ', '.join(x.dropna().unique())  # Combine unique events for that year
    }).reset_index()

    # Create a line plot with large scatter markers for each year
    fig = px.line(
        layoffs_summary,
        x='Year',
        y='Layoffs',
        title='Total Layoffs per Year (2010–2024)',
        labels={'Layoffs': 'Number of Layoffs in Thousands', 'Year': 'Year'},
        markers=True,  # This adds markers at each data point on the line
    )

    # Customize the scatter markers to make them bigger
    fig.update_traces(
        marker=dict(
            size=12,  # Adjust size of the markers (bubbles)
            color='rgb(255, 0, 0)',  # Optional: Change marker color
            opacity=0.8,  # Optional: Adjust opacity for a more transparent effect
            line=dict(width=2, color='DarkSlateGrey')  # Optional: Add border around the bubbles
        ),
        hovertemplate="<b>Year: %{x}</b><br>Layoffs: %{y}<br>Global Event: %{customdata[0]}<br>"  # Display global event on hover
    )

    # Add the global event data as custom data to be displayed when hovering over the markers
    fig.update_traces(customdata=layoffs_summary[['Global_Event']].values)

    # Show the plot
    st.plotly_chart(fig, use_container_width=True)
    
    
elif slide == "Automation Growth and AI Progression":

    st.header("Countries Leading the AI Revolution")
    st.write("Use the radio buttons below to switch between different global metrics related to AI and automation.")

# --- Load Patents Dataset ---
    patents_df = pd.read_csv("artificial-intelligence-patents-submitted-per-million.csv")

# Clean and standardize column names
    patents_df = patents_df.rename(columns={
        'Entity': 'Country',
        'Patent applications per 1 million people - Field: All': 'Value'
    })

# Drop NaNs and filter recent years
    patents_df = patents_df.dropna(subset=['Value'])



    investment_df = pd.read_csv("private-investment-in-artificial-intelligence-cset.csv")
# Clean and standardize column names
    investment_df = investment_df.rename(columns={
        'Entity': 'Country',
        'Estimated investment - Field: All': 'Value'
    })


    robots_df = pd.read_csv("industrial-robots-annual-installations-total-operational.csv")
# Clean and standardize column names
    robots_df = robots_df.rename(columns={
        'Entity': 'Country',
        'Annual industrial robots installed': 'Value'
    })

# --- Radio Button UI ---
    dataset_choice = st.radio(
        "Select dataset to view:",
        ('AI Patent Applications', 'Private Investment in AI', 'Industrial Robots Installed')
    )

# --- Select dataset to visualize ---
    if dataset_choice == 'AI Patent Applications':
        display_df = patents_df
        title = f"AI-Related Patent Applications per Million"
    elif dataset_choice == 'Private Investment in AI':
        display_df = investment_df
        title = "Private Investment in AI by Country"
    else:
        display_df = robots_df
        title = "Industrial Robots Installed by Country"

    available_years = sorted(display_df['Year'].dropna().unique())
    selected_year = st.slider("Select Year", int(min(available_years)), int(max(available_years)), int(max(available_years)))

    # --- Filter by selected year ---
    year_df = display_df[display_df['Year'] == selected_year]

    vmin = year_df['Value'].min()
    vmax = year_df['Value'].max()

# --- Plot Heatmap ---
    fig = px.choropleth(
         year_df,
        locations="Country",
        locationmode="country names",
        color="Value",
        color_continuous_scale="Reds",
        range_color=(vmin, vmax),
        title=f"{title} ({selected_year})"
    )

    st.plotly_chart(fig, use_container_width=True, height=1000)
    
elif slide == "AI Advancement":
    st.header("Dataset 3: Folium Map Visualization")
    
    m = folium.Map(location=[37.7749, -122.4194], zoom_start=12)
    folium.Marker(location=[37.7749, -122.4194], popup="San Francisco").add_to(m)
    
    st.components.v1.html(m._repr_html_(), height=500)


# Footer
st.markdown("---")
st.markdown("Created by Tyler Gaudino, Logan Caraballo, and Jose Nieves © 2025")