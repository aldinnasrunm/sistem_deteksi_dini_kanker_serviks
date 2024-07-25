import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Sistem Deteksi Dini Kanker Serviks",
    page_icon="❤️",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

st.title("Sistem Deteksi Dini Kanker Serviks")
selected = option_menu(
    menu_title=None,
    options=['Home', 'Berita', 'Prediksi'],
    icons=['house', 'newspaper', 'calculator'],
    default_index=0,
    orientation='horizontal',
)

if selected == "Home":
    import pages.home as home
    home.app()
   
elif selected == "Berita":
    import pages.berita as berita
    berita.app()  

elif selected == "Prediksi":
    import pages.prediksi as prediksi
    prediksi.app()  



footer = """<style>.footer {position: fixed;left: 0;bottom: 0;width: 100%;background-color: #000;color: white;text-align: center;}</style><div class='footer'><br><p>Copyright Informatika UMS 2024</p></div>"""
st.markdown(footer, unsafe_allow_html=True)