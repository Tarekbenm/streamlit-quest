import streamlit as st
st.write("Hello Wilders, welcom to my application")
import pandas as pd
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/weather2019.csv"
df_weather = pd.read_csv(link)
st.write(df_weather)

st.line_chart(df_weather['MAX_TEMPERATURE_C'])

import seaborn as sns
viz_correlation = sns.heatmap(df_weather.drop("OPINION", axis=1 ).corr(), 
								center=0,
								cmap = "vlag"
								)

st.pyplot(viz_correlation.figure)
st.clear_cache()

