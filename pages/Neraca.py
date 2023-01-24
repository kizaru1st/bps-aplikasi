import pandas as pd
import streamlit as st
import plotly.express as px
import subprocess
import sys
from streamlit_option_menu import option_menu

excel_file = 'UHH.xlsx'
sheet_name = 'DATA'

selected = option_menu(
    menu_title=None,
    options=["UHH", "HLS", "RLS", "Perkapita"],
    icons=['house', 'gear', 'book', 'envelope'],
    menu_icon="cast",
    default_index=0,
    orientation='horizontal',
)

if selected == "UHH":
    df = pd.read_excel(excel_file, sheet_name=sheet_name,
                       engine="openpyxl", usecols='A:D')

    st.title("Data UHH Pada Tahun 2020 - 2022")
    st.dataframe(df, width=1200)
    st.text("")

    st.sidebar.header("Filter: ")
    tahun = st.sidebar.selectbox(
        "Pilih tahun: ",
        ["2020", "2021", "2022"]
    )

    if(tahun == "2020"):
        st.bar_chart(df, x="Kabupaten/Kota", y="2020")

    elif(tahun == "2021"):
        st.bar_chart(df, x="Kabupaten/Kota", y="2021")

    elif(tahun == "2022"):
        st.bar_chart(df, x="Kabupaten/Kota", y="2022")
