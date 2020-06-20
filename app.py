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
    show_raw_data = st.checkbox("Show raw data " , False)
    if show_raw_data:
        st.write(df)

search = st.text_input("Enter student id")
if search != "":
    search_result = df.query("ID == @search")
    st.table(search_result)

# filter by GPA
if st.sidebar.checkbox("Do you want to filter by  GPA" , False):
    GPA1 = st.sidebar.slider("GPA for semester 1" ,  0 ,  4)
    GPA2 = st.sidebar.slider("GPA for semester 2" , 0 , 4)
    GPA3 = st.sidebar.slider("GPA cumulative for Level 1" , 0 , 4)
    if st.sidebar.button("Filter"):
        df = df.query("GPA >= @GPA1 and GPA2 >= @GPA2 and GPA_LevelOne >= @GPA3")
        st.sidebar.title("Filter is applied")
        st.header("Filterd Data: this filter applied to over all application function")
        st.write(df)
        
    else:
        st.sidebar.title("No filter is applied")



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

# Compare between subjects
if st.sidebar.checkbox("Compare between Subjects" , False):
    st.header("Compare between subjects")
    headers = list(df)
    subjects = list(filter(lambda x: x not in ["ID" ,"GPA" , "GPA2" , "GPA_LevelOne" , "Name"] , headers ))
    options = st.sidebar.multiselect("Pick" , subjects , default =["English", "Computer"])
    dic ={}
    dicp={}
    for option in options:
        dic[option] = df[option].value_counts()
        dicp[option] = df[option].value_counts(normalize=True) * 100

    comparsion = pd.DataFrame(dic)
    comparsionp = pd.DataFrame(dicp)

    st.write(comparsion)
    st.write(comparsionp)
    comparsion.plot(kind="bar"  )
    plt.xlabel("Mark")
    plt.ylabel("Count")

    st.pyplot()
    comparsionp.plot(kind="bar")
    plt.xlabel("Mark")
    plt.ylabel("Count Perecentage")

    st.pyplot()
    sns.heatmap(comparsion)
    plt.xlabel("Mark")
    plt.ylabel("Count Perecentage")

    st.pyplot()
    sns.heatmap(comparsionp)
    plt.xlabel("Mark")
    plt.ylabel("Count")

    st.pyplot()







