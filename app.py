
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("raw.githubusercontent.com_iantonios_dsc205_refs_heads_main_bike_sharing.csv")


df['dteday'] = pd.to_datetime(df['dteday'])


df = df.set_index('dteday')

st.title('Bike Sharing Data Visualization')

#Line plot: Total Ridership Over Time
st.header('Total Ridership Over Time')
fig1, ax1 = plt.subplots()
ax1.plot(df.index, df['cnt'])
ax1.set_xlabel('Date')
ax1.set_ylabel('Total Ridership')
st.pyplot(fig1)

# Bar Plot: Total Ridership by Season
st.header('Total Ridership by Season')

# Map the season numbers to names
season_map = {1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Fall'}
df['season_name'] = df['season'].map(season_map)

season_totals = df.groupby('season_name')['cnt'].sum()

fig2, ax2 = plt.subplots()
ax2.bar(season_totals.index, season_totals.values)
ax2.set_xlabel('Season')
ax2.set_ylabel('Total Ridership')
st.pyplot(fig2)

#Line plot with Rolling Average Selector
st.header('Total Ridership with Rolling Average')

rolling_option = st.radio(
    "Select a Rolling Average Window:",
    ('None', '7-day average', '14-day average')
)

fig3, ax3 = plt.subplots()

if rolling_option == '7-day average':
    df['cnt_rolling'] = df['cnt'].rolling(window=7).mean()
    ax3.plot(df.index, df['cnt_rolling'], label='7-day Average')
elif rolling_option == '14-day average':
    df['cnt_rolling'] = df['cnt'].rolling(window=14).mean()
    ax3.plot(df.index, df['cnt_rolling'], label='14-day Average')
else:
    ax3.plot(df.index, df['cnt'], label='Daily Total')

ax3.set_xlabel('Date')
ax3.set_ylabel('Total Ridership')
ax3.legend()

import matplotlib.dates as mdates

# Format the x-axis
ax3.xaxis.set_major_locator(mdates.MonthLocator(interval=3))  # Show every 3rd month
ax3.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))  # Format as "Year-Month"
plt.xticks(rotation=45)  # Rotate x labels for better readability

st.pyplot(fig3)

#Line plot: Total Ridership by Week
st.header('Total Weekly Ridership')

weekly_totals = df['cnt'].resample('W').sum()

fig4, ax4 = plt.subplots()
ax4.plot(weekly_totals.index, weekly_totals.values)
ax4.set_xlabel('Week')
ax4.set_ylabel('Total Ridership')

import matplotlib.dates as mdates

# Format the x-axis
ax4.xaxis.set_major_locator(mdates.MonthLocator(interval=3))  # Show every 3rd month
ax4.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))  # Format as "Year-Month"
plt.xticks(rotation=45)  # Rotate x labels for better readability

st.pyplot(fig4)
