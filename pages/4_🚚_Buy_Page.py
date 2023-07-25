import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import time

from PIL import Image
from chembl_webresource_client.new_client import new_client as ch

st.set_page_config(
    page_title="Buy Page",
    page_icon="🚚",
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
    content: 'Developed by Kasen Zhaniya, Shakibaeva Zhanara';
    display: block;
    position: relative;
    color: grey;
    padding: px;
    top: 3px;
}

</style>
"""

st.markdown(hide_menu, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>🚚 Buy Section</h1>", unsafe_allow_html=True)

name = st.text_input("Input your First and Last Names: ", placeholder='Nurtasov Kairat')
address = st.text_input("Input your E-mail Address: ", placeholder='admin@gmail.com')
phone = st.text_input("Input your Phone Number: ", placeholder='+7 (707) 123 45-67')

a, b = st.columns([4, 1])

button = b.button("Send Request", use_container_width=True)

if button:
    time.sleep(1)
    st.toast('Sending...')
    time.sleep(1)
    st.toast('Done!', icon='🎉')
