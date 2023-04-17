# EDA_app
Automated Machine Learning for Regression
This is a Streamlit web application for automated machine learning for regression tasks. The application provides an easy-to-use interface for uploading data, performing automated exploratory data analysis (EDA), training machine learning models, and downloading the best-performing model.

Requirements
This application requires the following libraries to be installed:

Streamlit
Pandas
Pandas-Profiling
Streamlit-Pandas-Profiling
PyCaret
These can be installed using the following command:

How to Use
To run the application, navigate to the directory where the code is saved and run the following command in the terminal:

The web application will open in your default browser.

The user can perform the following tasks in the application:

Upload
The user can upload their dataset by selecting the Upload option from the sidebar. Once uploaded, the data will be saved in a CSV file named sourcedata.csv in the same directory.

Profiling
The user can perform automated exploratory data analysis (EDA) on the uploaded dataset by selecting the Profiling option from the sidebar. The Pandas-Profiling library is used to generate an interactive report that provides insights into the data.

ML-Stuff
The user can train machine learning models on the uploaded dataset by selecting the ML-Stuff option from the sidebar. The PyCaret library is used to perform automated machine learning. The user needs to select the target variable and click on the Train Models button to start training. Once the training is completed, the best-performing model will be saved as a .pkl file named best_model.pkl in the same directory.

Download
The user can download the best-performing model by selecting the Download option from the sidebar. The user needs to click on the Download File button to download the best_model.pkl file.
