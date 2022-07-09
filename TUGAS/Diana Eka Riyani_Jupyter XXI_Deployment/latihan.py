import streamlit as st

st.title('Data Travel')

st.write("Data ini dikumpulkan sebagai bagian dari studi perjalanan yang dilakukan oleh mahasiswa Statistika.")

if(st.button("About Data")):
    st.text("Data ini didapatkan dari Kaggle")

data = pd.read_csv('TravelStudy.csv')

show_data = st.checkbox("Show Dataframe")
if show_data:
    st.write(data)

info = data.shape
if st.button("Lihat Total Data"):
    st.write(info)

st.text("Variabel dijelaskan di bawah ini:")

DomInt = st.radio("Apakah kamu mahasiswa internasional atau domestik?", data.DomInt.unique())
st.write(data[data.DomInt == DomInt])

DayBoarding = st.radio("Apakah kamu seorang siswa harian atau asrama?", data.DayBoarding.unique())
st.write(data[data.DayBoarding == DayBoarding])

Countries = st.slider("Berapa banyak negara yang pernah kamu kunjungi?", 0, 50)
st.write(data[data.Countries == Countries])

Languages = st.selectbox("Berapa banyak bahasa yang kamu kuasai?", data.Languages.unique())
st.write(data[data.Languages == Languages])