import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def create_daily_air_df(df):
    daily_air_df = df.resample(rule='ME', on='date').agg({
    "PM2_5": lambda x: x.unique().tolist(),
    "PM10": lambda x: x.unique().tolist()
    })

    daily_air_df = daily_air_df.reset_index()
    
    return daily_air_df

def create_daily_tmp_df(df):
    daily_tmp_df = df.resample(rule='ME', on='date').agg({
        "TEMP": "mean"
    })

    daily_tmp_df = daily_tmp_df.reset_index()

    return daily_tmp_df

guanyuan_all = pd.read_csv("./dashboard/guanyuan_all.csv")

guanyuan_all.sort_values(by="date", inplace=True)
guanyuan_all.reset_index(inplace=True)
guanyuan_all["date"] = pd.to_datetime(guanyuan_all["date"])

min_date = guanyuan_all["date"].min()
max_date = guanyuan_all["date"].max()

with st.sidebar:
    st.write("AIR Q")
    
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )
    st.write("The air quality data from the Guanyuan area records the concentration of pollutants such as PM2.5 and PM10, harmful particles that can cause health issues if inhaled in large quantities. This dataset is collected at specific time intervals, allowing for the analysis of air pollution trends over time.")

main_df = guanyuan_all[(guanyuan_all["date"] >= str(start_date)) & 
                (guanyuan_all["date"] <= str(end_date))]

daily_air_df = create_daily_air_df(main_df)
daily_tmp_df = create_daily_tmp_df(main_df)

st.header('Air Quality : Guanyuan 🌫️')

st.subheader('Air Quality')
 
col1, col2 = st.columns(2)
 
with col1:
    PM2_5_mean = main_df.PM2_5.mean()
    PM2_5_mean_r = round(PM2_5_mean, 1)
    st.metric("PM2.5 Mean", value=PM2_5_mean_r)
 
with col2:
    PM10_mean = main_df.PM10.mean()
    PM10_mean_r = round(PM10_mean, 1)
    st.metric("PM10 Mean", value=PM10_mean_r)

q_text = ''
if PM2_5_mean <= 15:
    q_text = "Good"
elif 15 < PM2_5_mean <= 35:
    q_text = "Moderate"
elif 35 < PM2_5_mean <= 55:
    q_text = "Unhealthy"
elif 55 < PM2_5_mean <= 150:
    q_text = "Very Unhealthy"
else: q_text = "Hazardous"
       
st.subheader(q_text)

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(daily_air_df["date"], [len(x) for x in daily_air_df["PM2_5"]], marker='o', linewidth=1, color="#6495ED") 
ax.plot(daily_air_df["date"], [len(x) for x in daily_air_df["PM10"]], marker='o', linewidth=1, color="#52A447") 
ax.set_title("Air Quality", loc="center", fontsize=20) 
ax.tick_params(axis='x', rotation=45, labelsize=10)

st.pyplot(fig)

st.subheader('Temperature')

tmp_mean = main_df.TEMP.mean()
tmp_mean_r = round(tmp_mean, 1)
st.metric("Temperature Mean", value=tmp_mean_r)

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(daily_air_df["date"], daily_tmp_df["TEMP"], marker='o', linewidth=1, color="#6495ED")
ax.set_title("Temperature", loc="center", fontsize=20)
ax.tick_params(axis='x', rotation=45, labelsize=10)

st.pyplot(fig)

st.subheader('Rainfall')

col1, col2 = st.columns(2)
 
with col1:
    rain_max = main_df.RAIN.max()
    rain_max_r = round(rain_max, 1)
    st.metric("Max Rain", value=rain_max_r)
 
with col2:
    rain_min = main_df.RAIN.min()
    rain_min_r = round(rain_min, 1)
    st.metric("Min Rain", value=rain_min_r)

st.caption("Copyright © 2024 Arkan Abdila Barts. All rights reserved.")