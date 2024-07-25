import streamlit as st
from md.predict_cervical_cancer import predict_cervical_cancer

def app():
    st.header("Prediksi Kanker Serviks")
    age = st.number_input("Umur", min_value=0, max_value=120, value=25)
    age_at_first_menstruation = st.number_input("Umur Awal Menstruasi", min_value=0, max_value=20, value=12)
    pelvic_pain = st.radio("Nyeri Panggul", options=[1, 2], format_func=lambda x: "Tidak" if x == 1 else "Ya")
    lower_abdomen_pain = st.radio("Nyeri Bawah Perut", options=[1, 2], format_func=lambda x: "Tidak" if x == 1 else "Ya")
    weight_loss = st.radio("Berat Badan Turun", options=[1, 2], format_func=lambda x: "Tidak" if x == 1 else "Ya")
    fatigue = st.radio("Kelelahan", options=[1, 2], format_func=lambda x: "Tidak" if x == 1 else "Ya")
    discharge_color = st.selectbox("Warna Keputihan", options=[1, 2, 3], format_func=lambda x: "Putih Susu" if x == 1 else "Kuning" if x == 2 else "Hijau")
    bleeding_outside_cycle = st.radio("Pendarahan di Luar Siklus", options=[1, 2], format_func=lambda x: "Flek" if x == 1 else "Banyak")
    bleeding_duration = st.selectbox("Lama Pendarahan", options=[1, 2, 3], format_func=lambda x: "< 7 Hari" if x == 1 else "7 – 14 Hari" if x == 2 else "> 14 Hari")
    abdominal_mass = st.radio("Benjolan di Perut", options=[1, 2], format_func=lambda x: "Tidak" if x == 1 else "Ya")

    if st.button("Hasil Prediksi"):
        result = predict_cervical_cancer(age, age_at_first_menstruation, pelvic_pain, lower_abdomen_pain, weight_loss, fatigue, discharge_color, bleeding_outside_cycle, bleeding_duration, abdominal_mass)
        st.subheader("Hasil Prediksi:")
        st.write(result)
