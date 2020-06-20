import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Business Information System Level 1 -- Students result analysis")

file_uploader = st.file_uploader("Upload your Excel file" , type="xlsx")

def convert_string_to_float(x):
    try:
        x = float(x)
    except:
        x = -1 
    return x

@st.cache(persist= True)
def load_data(PATH):
    df = pd.read_excel(PATH)
    df["GPA"] = df["GPA"].apply(convert_string_to_float)
    return df

if file_uploader != None:
    df = load_data(file_uploader)
    if st.checkbox("Show raw data " , False):
        st.write(df)

search = st.text_input("Enter student id")
if search != "":
    search_result = df.query("ID == @search")
    st.table(search_result)

# Show summary 
if st.sidebar.checkbox("Do you want a summary of GPA" , False):
    GPA_summary =df[["GPA" , "GPA2" , "GPA_LevelOne"]].query("GPA != -1").describe()
    st.table(GPA_summary)

    # box plot 
    print(df.info())
    GPA_summary.plot(kind="box")
    plt.ylim(-1, 5)
    st.pyplot()
    
    sns.distplot(df["GPA"])
    st.pyplot()
    sns.distplot(df["GPA2"])
    st.pyplot()
    sns.distplot(df["GPA_LevelOne"])
    st.pyplot()

  

  




