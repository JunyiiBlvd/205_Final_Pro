import streamlit as st # type: ignore
import pandas as pd # type: ignore
import plotly.graph_objects as go # type: ignore

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
