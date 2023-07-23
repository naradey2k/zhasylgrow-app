import matplotlib.pyplot as plt
import streamlit as st
import matplotlib.image as mpimg

st.set_page_config(
    page_title="Home page",
    page_icon="👋",
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

st.markdown("# 👋 Welcome to ZhasylGrow - efficient and environmentally friendly plant growth stimulator")
st.markdown(hide_menu, unsafe_allow_html=True)


st.write("""---""")
st.markdown(
    """
    \n
    ### Select on the left panel what you want to explore:

    - With 🔭 General Info, you will have a short description of the project, its goals and advantages
    
    - With 🎨 Methods, you will explore scientific content of our project

    - With 📈 Results, you will explore the results and differences between other approaches

    - With 🚚 Buy Product, you could buy our product to use and test on our product
    \n  
    
    """
)
