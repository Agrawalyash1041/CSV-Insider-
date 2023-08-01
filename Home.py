import streamlit as st
from streamlit_lottie import st_lottie
import requests 

st.set_page_config(
    page_title='CSV Insider',
    page_icon= '📊',
    layout= "wide",
    initial_sidebar_state= "auto"
)

st.title('Unveiling Data Insights with CSV Insider')
st.sidebar.success('Navigate through pages Above 👆')

### Creating the Lottie File function
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

### Loading lottie file
lottie_excel = load_lottieurl("https://assets10.lottiefiles.com/private_files/lf30_D3Uxth.json")

# ---- HEADER SECTION ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
     st.subheader("""Hi, I am Yash Nitin Agrawal.""")
     st.write(
        """
        Welcome to My Website, where we're excited to introduce you to our innovative app that empowers users to gain valuable insights from CSV (Comma Separated Values) files. 
        With a powerful combination of Pandas profiling and cutting-edge language models, our app provides a comprehensive overview of your data while offering a unique question-answering experience.
        In today's data-driven world, the ability to extract meaningful insights from raw data is paramount. However, analyzing large datasets can be a daunting task, especially for those without a strong background in data science. 
        That's where our CSV Insights app comes in, bridging the gap between complex data analysis techniques and everyday users. """)
    with right_column:
       st_lottie(lottie_excel,height=250)
    st.write("")
    st.subheader("Part 1: Overviewing the Data using Pandas Profiling")
    st.write("""
    In the first part of our app, we leverage the renowned Pandas profiling library. With its cutting-edge capabilities, we offer you a detailed overview of your data like never before.
    Pandas profiling allows us to generate comprehensive reports that include statistical summaries, data types, missing values, correlations, distributions, and much more. 
    With just a few clicks, you can unlock a wealth of knowledge about your CSV file, enabling you to make informed decisions and uncover hidden patterns.""")
    st.write("")
    st.subheader("Part 2: OPEN AI for Question Data")
    st.write("""The second part of our app takes data analysis to the next level by harnessing the capabilities of Langchain and Open AI API. We have developed a powerful model that can answer your questions based on the data contained in your CSV file. Gone are the days of scrolling through rows and columns, trying to make sense of the numbers. 
    Simply input your queries, and our model will provide you with accurate and concise answers, enabling you to make informed decisions and drive impactful actions.""")
    st.write("")
    st.subheader("Disclaimer: The CSV Insights app is intended for informational purposes only and should not replace professional data analysis or domain expertise.")