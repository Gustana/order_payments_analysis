from st_pages import Page, show_pages
import streamlit as st
import os
import sys

# Get the directory of main.py
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory (data) to the Python path
parent_dir = os.path.join(current_dir, '..')
sys.path.append(parent_dir)

from data import data

show_pages(
    [
        Page("main.py", "Home"),
        Page("eda.py", "EDA"),
        Page('analysis_res.py', 'Analysis Result')
    ]
)

st.title('Order Payment Analysis')
st.divider()

st.subheader("Introduction")


st.text('The purpose of this project is to make analysis related to order payments.')

df = data.getDataFrame()

st.dataframe(
    df.loc[:, df.columns != 'order_id'].head()
)

st.markdown(
f'''
There are 5 columns on the dataset:
- Payment Sequential -> Number of payment that has been made sequentially
- Payment Type -> Category of payment: Credit Card, Boleto, Voucher, Debit Card, Undefined
- Payment Installment -> Number of debt payment
- Payment Value -> The amount of payment
'''
)