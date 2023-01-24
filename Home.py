#Library
import pandas as pd
import streamlit as st
import plotly.express as px
from streamlit_option_menu import option_menu
import subprocess
import sys

# Create Localhost to host website
st.set_page_config(page_title='BPS Provinsi Sumatera Barat',
                   page_icon=":bar_chart:",
                   layout='wide')

st.title("title lom ada")
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)
