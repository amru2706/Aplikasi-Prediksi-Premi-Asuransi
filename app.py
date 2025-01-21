import streamlit as st
import pickle
import numpy as np

# Load Model
model = pickle.load(open('model_uas.pkl', 'rb'))

# Judul Aplikasi
st.title("Aplikasi Prediksi Premi Asuransi")
st.write("**Nama**: Muhammad Amrullah | **NIM**: 2021230014")
st.markdown("Aplikasi ini digunakan untuk memprediksi besar premi asuransi berdasarkan 5 input.")

# Input Data Pengguna
age = st.number_input("Usia (tahun):", min_value=0, max_value=120, value=25, step=1)
sex = st.selectbox("Jenis Kelamin:", ["Laki-laki", "Perempuan"])
bmi = st.number_input("Indeks Massa Tubuh (BMI):", min_value=10.0, max_value=50.0, value=25.0, step=0.1)
children = st.number_input("Jumlah Anak yang Ditanggung:", min_value=0, max_value=10, value=0, step=1)
smoker = st.selectbox("Apakah Perokok?", ["Ya", "Tidak"])

# Konversi Input
sex = 0 if sex == "Laki-laki" else 1
smoker = 1 if smoker == "Ya" else 0

# Tombol Prediksi
if st.button("Prediksi Premi"):
    # Konversi Input ke Array
    input_features = np.array([[age, sex, bmi, children, smoker]])
    
    # Prediksi Premi
    prediction = model.predict(input_features)[0]
    
    # Menampilkan Hasil Prediksi
    st.success(f"Estimasi Premi Asuransi: ${prediction:,.2f}")
