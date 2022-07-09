from dataclasses import dataclass
from turtle import onclick
import streamlit as st
import pandas as pd

st.title('Corona Virus ')
st.write("Informasi Corona dari Twitter. Nama dan nama pengguna telah diberi kode untuk menghindari masalah privasi.")


df = pd.read_excel('coronavirus.xlsx')


info = df
if st.button("Lihat Data"):
    st.write(info)

#menghitung jumlah Location
jdata = df.Location.shape

# Memilih Location
st.write("Terdapat", jdata, "Location tweet coronavirus dari pengguna twitter")
Local = st.selectbox("Pilih Lokasi", df.Location.unique())

# Menampilkan dataframe dari Location yang pilih
st.write(df[(df.Location == Local)])

#menghitung jumlah tweet dari Location
st.write(Local, "Memiliki", "Tweet")

# radio button untuk melihat status kesehatan
status = st.radio("Pilih Status Kesehatan", df.Sentiment.unique())

st.write(df[df.Sentiment == status])
