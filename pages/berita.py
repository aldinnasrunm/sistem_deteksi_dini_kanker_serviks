import streamlit as st
from PIL import Image
import requests
from asset.news_data import news

def resize_to_square(image, size):
    width, height = image.size
    if width == height:
        return image.resize((size, size), Image.LANCZOS)
    elif width > height:
        new_width = int(size * width / height)
        resized_img = image.resize((new_width, size), Image.LANCZOS)
        left = (new_width - size) / 2
        return resized_img.crop((left, 0, left + size, size))
    else:
        new_height = int(size * height / width)
        resized_img = image.resize((size, new_height), Image.LANCZOS)
        top = (new_height - size) / 2
        return resized_img.crop((0, top, size, top + size))


def app():
    st.header("Berita Kanker Serviks")
    st.markdown("""<br>""", unsafe_allow_html=True)
    for article in news:
        col1, col2 = st.columns([1, 3])
        with col1:
            response = requests.get(article['image'], stream=True)
            img = Image.open(response.raw)
            square_img = resize_to_square(img, 150)
            st.image(square_img, width=150)
        with col2:
            st.markdown(f"""
                <a href="{article['link']}" target="_blank" style="text-decoration: none; color: inherit;">
                    <h3>{article['title']}</h3>
                    <p>{article['content']}</p>
                </a>
            """, unsafe_allow_html=True)
            st.caption(f"Sumber: {article['src']}")
        st.write("---")

