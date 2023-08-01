from langchain.agents import create_pandas_dataframe_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os
import streamlit as st
import pandas as pd

def main():
    load_dotenv()

    # Load the OpenAI API key from the environment variable
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print("OPENAI_API_KEY is not set")
        exit(1)
    else:
        print("OPENAI_API_KEY is set")
    st.set_page_config(page_title="CSV Insider/OPEN AI",page_icon="📊",layout='wide')
    st.header('Interact and Extract Insights from Your Data with OpenAI')
    st.subheader("Introduction")
    st.write(""" This powerful tool allows you to leverage the capabilities of OpenAI to analyze and explore your CSV files effortlessly. 
    Gone are the days of manual data manipulation and complex coding. With CSV Query, you can now ask questions directly to your data and receive intelligent answers powered by 
    OpenAI's advanced natural language processing. Whether you're a data analyst, researcher, or simply curious about your data, CSV Query provides an intuitive interface to interact 
    with your CSV files, enabling you to uncover valuable insights with ease. Let's dive in and discover the potential that awaits within your data. """)
    Uploaded_file = st.file_uploader("Upload and Drop your files here",type=["csv"])


    if Uploaded_file is not None:
        data = pd.read_csv(Uploaded_file)
        st.write("Data Preview:")
        st.dataframe(data.head())
        agent = create_pandas_dataframe_agent(OpenAI(temperature=0),data,verbose=True) 

        query = st.text_input("Please enter your Question :") 

        if st.button("Find the Answer"):
           answer = agent.run(query)
           st.write("Answer:")
           st.write(answer)

if __name__ =="__main__" :
    main()

