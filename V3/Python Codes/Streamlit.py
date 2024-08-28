import streamlit as st
import pandas as pd


df = pd.read_excel(".\Software Vacancy Clean.xlsx")
df["Skills"] = df["Skills"].apply(lambda x: x.replace("[", "").replace("]", "").replace("'",''))
df_for_view = df[["Name","Company","Location","Type_of_Employment","Education_degree","Category","Skills","Mean_Salary"]]

category = {df_for_view["Skills"]}

st.markdown("#### Data Example")
st.dataframe(df_for_view)
st.sidebar.selectbox("Select you'r category",df_for_view)