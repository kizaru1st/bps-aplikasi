import pandas as pd
import streamlit as st
import plotly.express as px
import subprocess
import sys
from streamlit_option_menu import option_menu

excel_filebuku = 'Book1.csv.xlsx'
sheet_namebuku = 'Book1'
sheet_mostread = 'MostRead'
sheet_mostrequest = 'MostRequest'

excel_filepengunjung ='PengunjungPST.xlsx'
sheet_namebukupengunjung = 'Sheet1'

selected = option_menu(
    menu_title=None,
    options=["Data Buku", "Data Pengunjung"],
    icons=['book','person'],
    menu_icon="cast",
    default_index=0,
    orientation='horizontal',
)

if selected == "Data Buku":
    
    buku = st.sidebar.selectbox(
        "Pilih Aksi: ",
        ["Create Data Buku", "Lihat Data Buku Paling Sering Dibaca", "Lihat Data Buku Paling Sering Diminta"]
    )

    if(buku == "Create Data Buku"):
        st.title("Create a New Data")
        df = pd.read_excel("Book1.csv.xlsx")
        st.header("Data Buku")


        id_book = st.text_input("ID Buku")
        judul = st.text_input("Judul Buku")
        st.write(df)
        hide_st_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    header {visibility: hidden;}
                    </style>
                        """
        st.markdown(hide_st_style, unsafe_allow_html=True)

    elif(buku == "Lihat Data Buku Paling Sering Dibaca"):
        df = pd.read_excel(excel_filebuku, sheet_name=sheet_mostread,
                       engine="openpyxl", usecols='A:D')

        st.title("Data Buku Paling Sering Dibaca di Perpustakaan BPS")
        st.dataframe(df, width=1200)
        st.text("")

    elif(buku == "Lihat Data Buku Paling Sering Diminta"):
        df = pd.read_excel(excel_filebuku, sheet_name=sheet_mostrequest,
                       engine="openpyxl", usecols='A:D')

        st.title("Data Buku Paling Sering Diminta di Perpustakaan BPS")
        st.dataframe(df, width=1200)
        st.text("")


if selected == "Data Pengunjung":
    df = pd.read_excel(excel_filepengunjung, sheet_name=sheet_namebukupengunjung,
                       engine="openpyxl", usecols='A:L')

    st.title("Data Pengunjung Perpustakaan BPS")
    st.dataframe(df, width=1200)
    st.text("")
    hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                    """
    st.markdown(hide_st_style, unsafe_allow_html=True)
