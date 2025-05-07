import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go



# Page configuration
st.set_page_config(page_title="The Race for Intelligence", layout="wide")

# Define all slide names in order
slides = [
    "Layoffs and Workforce Dynamics",
    "Countries Leading the AI Revolution",
    "Annual Industrial Robots Installed",
    "AI Accuracy on Knowledge Tests",
    "Industries Most at Risk"
]
# --- Session State Navigation Logic ---
if "current_slide" not in st.session_state:
    st.session_state.current_slide = slides[0]

# Sidebar navigation (sync with session)
st.sidebar.title("Navigation")
st.session_state.current_slide = st.sidebar.radio(
    "Go to",
    slides,
    index=slides.index(st.session_state.current_slide)
)

# Assign current slide
slide = st.session_state.current_slide

##################################DATA SHOWS THAT AI INVESTMENTS AND PATENTS ARE SKEWED TOWARDS USA WHILE AUTOMATION IS SKEWED TOWARDS CHINA############################

# Page content logic
st.title("The Race for Intelligence")

############################################################################################################################################################################
def s1():
    st.header("Layoffs and Workforce Dynamics")
    st.write("Explore layoff trends and workforce dynamics in the age of AI and automation.")


    # Load dataset
    layoffs_df = pd.read_csv('Layoff_Trend_Analyzed_30_Years_Final.csv')
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
def s1_1(file_path, top_n):
    df = clean_employment_data(file_path)

    top_jobs = df.sort_values("Percent change, 2023-33", ascending=False).head(top_n)

    fig = px.bar(
        top_jobs,
        x="Percent change, 2023-33",
        y="Occupation",
        orientation="h",
        title=f"Top {top_n} Fastest Growing Occupations (2023–2033)",
        labels={"Percent change, 2023-33": "Growth (%)", "Occupation": "Occupation"},
    )
    fig.update_layout(yaxis={'categoryorder': 'total ascending'})
    st.plotly_chart(fig, use_container_width=True)
def s1_2(file_path):
    df = clean_employment_data(file_path)
    # Normalize bubble size (projected employment)
    df["Normalized size"] = (
        (df["Projected employment, 2033"] - df["Projected employment, 2033"].min()) /
        (df["Projected employment, 2033"].max() - df["Projected employment, 2033"].min())
        ) * 60  # 60 is your max bubble size

    fig = px.scatter(
    df,
    x="Employment, 2023",
    y="Percent change, 2023-33",
    size="Normalized size",
    hover_name="Occupation",
    title="2023 Employment vs. Growth Rate (Normalized Bubble Size)",
    labels={
        "Employment, 2023": "Employment in 2023",
        "Percent change, 2023-33": "Percent Change (2023–2033)",
        "Projected employment, 2033": "2033 Employment"
    },
    size_max=60  # still useful to cap largest bubble
)
    st.plotly_chart(fig, use_container_width=True)



def clean_employment_data(file_path):
    df = pd.read_csv(file_path)

    def clean_col(col):
        col = col.replace('\xa0', ' ')
        col = col.replace('–', '-')
        col = col.strip()
        return col

    df.columns = [clean_col(col) for col in df.columns]

    # Drop rows missing growth data
    df = df.dropna(subset=['Percent change, 2023-33'])

    # Drop the "Total, all occupations" row
    df = df[df["Occupation"] != "Total, all occupations"]

    # Convert numeric columns that may have commas
    cols_to_convert = [
        "Employment, 2023",
        "Percent change, 2023-33",
        "Projected employment, 2033"
    ]

    for col in cols_to_convert:
        if col in df.columns:
            df[col] = df[col].astype(str).str.replace(",", "")
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df
    
############################################################################################################################################################################
def s2():
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
############################################################################################################################################################################
def s3():
    st.title("Annual Industrial Robots Installed Over Time by Entity")

# Load and sort data
    df = pd.read_csv('annual-industrial-robots-installed.csv')
    df = df.sort_values('Year')

# Identify unique entities and sorted years
    entities = df['Entity'].unique()
    years = sorted(df['Year'].unique())

# Create initial empty traces for each entity
    initial_traces = [
        go.Scatter(x=[], y=[], mode='lines+markers', name=ent)
        for ent in entities
    ]

# Build the figure with Play button
    fig = go.Figure(
        data=initial_traces,
        layout=go.Layout(
            xaxis=dict(range=[years[0], years[-1]], title='Year'),
            yaxis=dict(
                range=[
                    df['Annual industrial robots installed'].min(),
                    df['Annual industrial robots installed'].max()
                ],
                title='Robots Installed'
            ),
            updatemenus=[dict(
                type='buttons',
                showactive=False,
                y=1.05,
                x=1.15,
                xanchor='right',
                yanchor='top',
                buttons=[dict(
                    label='Play',
                    method='animate',
                    args=[None, {
                        'frame': {'duration': 1000, 'redraw': True},
                        'transition': {'duration': 300},
                        'fromcurrent': True
                    }]
                )]
            )]
        ),
        frames=[
            go.Frame(
                data=[
                    go.Scatter(
                        x=df[(df['Entity'] == ent) & (df['Year'] <= year)]['Year'],
                        y=df[(df['Entity'] == ent) & (df['Year'] <= year)]['Annual industrial robots installed'],
                        mode='lines+markers',
                        name=ent
                    )
                    for ent in entities
                ],
                name=str(year)
            )
            for year in years
        ]
    )

# Add slider below to show progress
    fig.update_layout(
        sliders=[dict(
            steps=[
                dict(
                    method='animate',
                    args=[[str(year)], {
                        'mode': 'immediate',
                        'frame': {'duration': 1000, 'redraw': True},
                        'transition': {'duration': 300}
                    }],
                    label=str(year)
                )
                for year in years
            ],
            transition={'duration': 0},
            x=0,
            y=-0.1,
            currentvalue={'prefix': 'Year: ', 'font': {'size': 16}},
            len=1.0
        )]
    )

    # Render in Streamlit
    st.plotly_chart(fig, use_container_width=True)

def s4():
    df = pd.read_csv("AI-VS-Human.csv")

    # Create line chart
    fig = px.line(
        df,
        x="Year",
        y="Perfomance relative to the human baseline (100%)",
        color="Task",
        markers=True,
        title="AI Task Performance Over Time (Relative to Human Baseline = 100%)",
        labels={"Perfomance relative to the human baseline (100%)": "Performance (%)", "Year": "Year", "Task": "Task"},
    )

    # Add horizontal baseline at 100%
    fig.add_shape(
        type="line",
        x0=df["Year"].min(),
        x1=df["Year"].max(),
        y0=100,
        y1=100,
        line=dict(color="Red", dash="dash"),
    )

    fig.update_layout(legend_title="Task")

    # Display in Streamlit
    st.plotly_chart(fig, use_container_width=True)
############################################################################################################################################################################
if slide == "Layoffs and Workforce Dynamics":
    s1()
    s1_1('employment-projections.csv', 10)
    s1_2('employment-projections.csv')
elif slide == "Countries Leading the AI Revolution":
    s2()
elif slide == "Annual Industrial Robots Installed":
    s3()
elif slide == "AI Accuracy on Knowledge Tests":
    s4()
elif slide == "Industries Most at Risk":
    s4()

# --- Next Button ---
current_index = slides.index(slide)
if current_index < len(slides) - 1:
    if st.button("Next"):
        st.session_state.current_slide = slides[current_index + 1]
        st.rerun()


# Footer
st.markdown("---")
st.markdown("Created by Tyler Gaudino, Logan Caraballo, and Jose Nieves © 2025")