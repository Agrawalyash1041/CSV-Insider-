import pandas as pd
import numpy as np
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report


st.set_page_config(
    page_title='CSV Insider/Overview',
    page_icon= '📊',
    layout= "wide",
    initial_sidebar_state= "auto"
)

st.title("Overiew of Data using Pandas Profiling 🔍")
st.subheader('Introduction')
st.write("""Welcome to our website, where we are thrilled to introduce you to our free CSV Analyzer powered by Pandas Profiling. 
         If you've ever found yourself grappling with complex datasets, fret not! Our user-friendly tool simplifies the process by providing comprehensive insights at the click of a button.
         Using our website is a breeze. Simply upload your CSV file, and with a single click on the "Generate report" button, our analyzer springs into action. Within moments, 
         you'll receive a comprehensive analysis of your data, complete with descriptive statistics, data types, missing value assessments, correlations, and much more.""")

uploaded_file = st.file_uploader("Select or Drop your CSV Files here",type='csv')
# Pandas Profiling Report
if uploaded_file is not None:
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True, minimal=True,dark_mode= True)
    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**Pandas Profiling Report**')
    st_profile_report(pr)


    