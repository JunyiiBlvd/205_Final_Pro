import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


def load_data():
    df = pd.read_csv('The Rise Of Artificial Intellegence2.csv')
    df = df.sort_values('Year')
    # Convert percent strings → floats
    pct_cols = [
        'Organizations Planning to Implement AI',
        'Organizations Using AI',
        'Global Expectation for AI Adoption (%)'
    ]
    for col in pct_cols:
        df[col] = df[col].str.rstrip('%').astype(float)
    return df

df       = load_data()
years    = df['Year'].astype(str)
planning = df['Organizations Planning to Implement AI']
using    = df['Organizations Using AI']
expect   = df['Global Expectation for AI Adoption (%)']

# 2. UI selector
choice = st.radio(
    "Choose a chart:",
    ("Implementation & Adoption", "Expectation ")
)

if choice == "Implementation & Adoption":
    # 3a. Grouped bar chart (side-by-side)
    x     = range(len(years))
    width = 0.4

    fig, ax = plt.subplots()
    ax.bar([i - width/2 for i in x], planning, width, label='Planning to Implement AI')
    ax.bar([i + width/2 for i in x], using,    width, label='Using AI ')

    # 4a. Styling
    ax.set_xticks(x)
    ax.set_xticklabels(years, rotation=45)
    ax.set_ylim(0, 100)  # clamp to 0–100%
    ax.set_xlabel('Year')
    ax.set_ylabel('Organizations (%)')
    ax.set_title('Percentage of Organizations Planning vs. Using AI')
    ax.legend()
    plt.tight_layout()
    st.pyplot(fig)

else:
    # 3b. Simple line chart
    fig, ax = plt.subplots()
    ax.plot(years, expect, marker='o', linestyle='-', label='Global Expectation for AI Adoption ')

    # 4b. Styling
    ax.set_xticklabels(years, rotation=45)
    ax.set_ylim(0, 100)
    ax.set_xlabel('Year')
    ax.set_ylabel('Expectation (%)')
    ax.set_title('Global Expectation for AI Adoption by Year')
    ax.legend()
    plt.tight_layout()
    st.pyplot(fig)
