import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

from PIL import Image
from chembl_webresource_client.new_client import new_client as ch

st.set_page_config(
    page_title="Methods",
    page_icon="🎨",
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

names = {
    "Name": ["Morpholine", "Carbon Disulfide", "Propargyl Bromide", "B-Cyclodextrin"],
}    

st.markdown("<h1 style='text-align: center;'>🔎 Objects of Study</h1>", unsafe_allow_html=True)

df = pd.DataFrame(names)
c1, c2 = st.columns(2)

with c1:
    edited_df = st.data_editor(
        df,
        column_config={
            "name": "Name",
        },
        disabled=["Name"],
        hide_index=True,
        width=400,
        key='1'
    )

image_df = pd.DataFrame(
    {
        "apps": [
            "https://www.ebi.ac.uk/chembl/api/data/image/CHEMBL276518.svg",
            "https://www.ebi.ac.uk/chembl/api/data/image/CHEMBL1365180.svg",
            "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Propargyl_bromide.svg/220px-Propargyl_bromide.svg.png",
            "https://www.ebi.ac.uk/chembl/api/data/image/CHEMBL415690.svg",
        ],
    }
)

with c2:
    st.data_editor(
        image_df,
        column_config={
            "apps": st.column_config.ImageColumn(
                "Image", help="Streamlit app preview screenshots"
            )
        },
        hide_index=True,
        width=500,
        key='2'
    )


st.write("""---""")

st.markdown("<h1 style='text-align: center;'>One Pot Method</h1>", unsafe_allow_html=True)

image = Image.open('./images/work.png')

col1, col2 = st.columns([6, 4])

with col1:
    st.image(image)

with col2:
    st.title("")
    st.title("")
    st.info("""
            1. We add **carbon disulfide to morpholine** in an alkaline medium; stir at room temp.
            2. In the same vessel we add **propargyl** bromide. Mix for two hours.
            3. The resulting substance is filtered, washed with solvents.
        """)

with st.expander("ℹ️ - Why we use B-Cyclodextrin?"):
    st.success("""
        1. Increasing the solubility of the substance in water
        2. Increased chemical and physical stability
        3. Masking the smell of the drug
        4. The transformation of a liquid substance into an amorphous powder
        \n
    """)        

st.write("""---""")    

st.markdown("<h1 style='text-align: center;'>Methods of Studying Bio-Activity</h1>", unsafe_allow_html=True)
st.warning("""
        Before planting, the cuttings are kept in solutions with concentrations of **0.01%, 0.001%**,
        according to the experimental scheme, with an exposure of 6 hours when the ends of the cuttings are immersed in the solution
    """)

methods = {
    "Name": ["Water", "KN-2 Analogue (0.01%)", "KN-2 Analogue (0.001%)", "B-Cyclodextrin (0.01%)", "B-Cyclodextrin (0.001%)"],
}    

df = pd.DataFrame(methods)
cc1, cc2 = st.columns(2)

with cc1:
    edited_df = st.data_editor(
        df,
        column_config={
            "name": "Name",
        },
        disabled=["Name"],
        hide_index=True,
        width=400,
        key='3'
    )

res_df = pd.DataFrame(
    {
        "apps": [
            "https://i.imgur.com/IIWiAYp.jpeg",
            "https://i.imgur.com/H5smDwm.jpeg",
            "https://i.imgur.com/ZHrH8mc.jpeg",
            "https://i.imgur.com/Y0hGB3R.jpeg",
            "https://i.imgur.com/ibo4RED.jpeg",
        ],
    }
)

with cc2:
    st.data_editor(
        res_df,
        column_config={
            "apps": st.column_config.ImageColumn(
                "Image", help="Streamlit app preview screenshots"
            )
        },
        hide_index=True,
        width=500,
        key='4'
    )
