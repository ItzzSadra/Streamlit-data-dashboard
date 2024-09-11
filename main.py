import streamlit as st
import pandas as pd
import matplotlib as pt

st.title("Simple Data Dashboard")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summery")
    st.write(df.describe())

    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select Column to filter by", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select Value", unique_values)

    filtred_df = df[df[selected_column] == selected_value]
    st.write(filtred_df)

else:
    st.write("Waiting on File Upload ....")