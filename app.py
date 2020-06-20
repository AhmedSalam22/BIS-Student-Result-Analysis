import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Business Information System Level 1 -- Students result analysis")

file_uploader = st.file_uploader("Upload your Excel file" , type="xlsx")

@st.cache(persist= True)
def load_data(PATH):
    df = pd.read_excel(PATH)
    return df

if file_uploader != None:
    df = load_data(file_uploader)
    if st.checkbox("Show raw data " , False):
        st.write(df)

search = st.text_input("Enter student id")
if search != "":
    search_result = df.query("ID == @search")
    st.table(search_result)