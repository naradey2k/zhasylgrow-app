import matplotlib.pyplot as plt
import streamlit as st
import matplotlib.image as mpimg

st.set_page_config(
    page_title="General Info",
    page_icon="🔭",
    layout="centered"
)

desc1 = """Plant growth stimulants based on dithiocarbamates have already shown their high biological activity, however, due to the content of benzene rings, they have **CONCEROGENIC EFFECTS** and can be **HAZARDOUS TO HEALTH**"""
desc2 = """Environmentally friendly solution to the issue of agriculture will enable the sustainable development of agriculture, an important sector of the economy of Kazakhstan"""

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

st.markdown("<h1 style='text-align: center;'>🌳ZhasylGrow</h1>", unsafe_allow_html=True)
st.success("Our main goal is to obtain a new, more efficient and environmentally friendly plant growth stimulator")
st.image(f'./images/tree.jpg')

st.write("""---""")

st.markdown("<h1 style='text-align: center;'>Description</h1>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.warning(desc1)
with col2:
    st.warning(desc2)

st.write("""---""")

st.markdown("<h1 style='text-align: center;'>Advantages</h1>", unsafe_allow_html=True)
st.success("The project complies with all the principles of **GREEN CHEMISTRY**, as our final product has non-toxic by-products **water** and **sodium bromide**")

col1, col2, col3 = st.columns(3)
with col1:
    st.info("Stronger biological activity on spring wheat germination than **Water** and **Akpenol-Alpha (KN-2)** analog")
with col2:
    st.info("Cost-effective, highest germination at **0.001 g per 100 ml water**")   
with col3:
    st.info("Efficient **one-pot system**, eliminating intermediate stages")
