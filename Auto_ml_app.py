import streamlit as st
import pandas as pd
import os

############### import profiling capablities ##################################

import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

############### importing machine learning stuff here #########################

from pycaret.regression import setup, compare_models, pull, save_model

###############################################################################

with st.sidebar:
    st.title("Automated Machine Learning for Regression")
    choice = st.radio("Navigation",["Upload","Profiling","ML-Stuff","Download"])
    st.info("This app allows us to do automated ML Model training")

if os.path.exists("sourcedata.csv"):
    df = pd.read_csv("sourcedata.csv",index_col=None)
    
if choice == "Upload":
    st.title("Upload your File here.")
    file = st.file_uploader("Upload your dataset here.")
    if file:
        df = pd.read_csv(file,index_col=None)
        df.to_csv("sourcedata.csv",index=None)
        st.dataframe(df)

if choice == "Profiling":
    st.title("Automated EDA")
    profile_report = df.profile_report()
    st_profile_report(profile_report)
    
if choice == "ML-Stuff":
    st.title("ML bro is here..........")
    target = st.selectbox("Select your target here",df.columns)
    if st.button("Train Models"):
        setup(df,target=target,silent=True)
        setup_df = pull()
        st.info("Model training is going on.")
        st.dataframe(setup_df)
        best_model = compare_models()
        compare_df = pull()
        st.info("Here are some ML model")
        st.dataframe(compare_df)
        best_model
        save_model(best_model, "best_model")
    
if choice == "Download":
    with("best_model.pkl","rb") as f:
        st.download_button("Download File", f, "best_model.pkl")
    
    
    
    
    
    