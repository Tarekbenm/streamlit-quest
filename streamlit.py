import streamlit as st
st.write("Hello Wilders, welcom to my application")
import pandas as pd
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/weather2019.csv"
df_weather = pd.read_csv(link)
st.write(df_weather)

st.line_chart(df_weather['MAX_TEMPERATURE_C'])
