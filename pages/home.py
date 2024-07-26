import streamlit as st

def app():
    st.title("Sistem Deteksi Dini Kanker Serviks")
    st.write("""
        Kanker serviks adalah jenis kanker yang terjadi di sel-sel leher rahim (serviks) - bagian bawah rahim yang terhubung ke vagina.
        Gejalanya meliputi nyeri panggul, nyeri bawah perut, keputihan yang tidak normal, pendarahan di luar siklus menstruasi, dan lain-lain.
             
        Di Indonesia kanker serviks masih menjadi penyakit kanker dengan jumlah penderita terbesar kedua setelah kanker payudara. Angka kejadian kasus baru kanker serviks sesuai data GLOBOCAN, 2018 untuk wanita di Indonesia berkisar 32.469 kasus (17.2%) dengan angka kematian 18.279 (8.8%).
    """)

    st.image("asset/JUMLAH-KASUS.jpg", use_column_width="always")

    st.write("""
Kanker yang terjadi karena infeksi Human papillomavirus (HPV) risiko tinggi ini, masih menjadi fokus edukasi untuk meningkatkan kesadaran di masyarakat, khususnya yang sudah aktif seksual untuk rutin melakukan tes deteksi dini.
    """)