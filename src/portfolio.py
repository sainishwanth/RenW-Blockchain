import streamlit as st
import pandas as pd


def portfolio(df):
    st.table(df)
