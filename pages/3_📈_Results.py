import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import plotly.figure_factory as ff

from PIL import Image
from chembl_webresource_client.new_client import new_client as ch

st.set_page_config(
    page_title="Results",
    page_icon="📈",
    layout="centered"
)

hide_menu = """
<style>
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: visible;
}

footer:after {
    content: 'Developed by Kasen Zhaniya, Shakibaeva Zhanara and Sultanov Danial';
    display: block;
    position: relative;
    color: grey;
    padding: px;
    top: 3px;
}

</style>
"""

st.markdown(hide_menu, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>📊 Results</h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.success("The influence of the studied preparations on the germination of wheat seeds on the 3rd and 7th days")

    labs = ['Water', 'KN-2 (0.01)', 'KN-2 (0.001)', 'b-CD (0.01)', 'b-CD (0.001)', 'ЖЖ-5 (0.01)', 'ЖЖ-5 (0.001)']
    energy = [84, 90, 88, 82, 82, 88, 90]
    germ = [80, 88, 86, 78, 84, 94, 98]

    df = pd.DataFrame({"Germination Energy": energy, "Lab Germination": germ}, index=labs)
    st.bar_chart(df, x=labs, height=0)

with col2:
    st.success("Morphological characteristics of wheat seedlings in the application of the studied preparations")

    labs = ['Water', 'KN-2 (0.01)', 'KN-2 (0.001)', 'b-CD (0.01)', 'b-CD (0.001)', 'ЖЖ-5 (0.01)', 'ЖЖ-5 (0.001)']
    roots = [3.6, 3, 3.67, 3.48, 3.85, 3.46, 5.13]
    rlen = [1.25, 1.22, 2.16, 1.61, 0.74, 1.39, 2.36]
    slen = [1.33, 2.92, 3.18, 4.29, 2.87, 2.68, 5.8]

    df2 = pd.DataFrame({"Root Number": roots, "Root Length": rlen, 'Sprout Length': slen}, index=labs)
    st.bar_chart(df2, x=labs)

st.write("""---""")

st.markdown("<h1 style='text-align: center;'>Current Usage</h1>", unsafe_allow_html=True)

c1, c2 = st.columns(2)

with c1:
    image = Image.open('./images/galamilk.png')
    st.image(image, width=300, caption='On-site Galamilk')

with c2:
    st.markdown("##### So far, our substance has been tested on the <a href='https://www.instagram.com/galamilk_qazaqstan/?hl=en'>**Galamilk**</a> goat farm, which also produces wheat for goat feed", unsafe_allow_html=True)
    st.title('')
    st.info("#### Our substance, used at 1 gram per 10 liters of water, significantly enhanced wheat growth and germination compared to other stimulants at the farm")
