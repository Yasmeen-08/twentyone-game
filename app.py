from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="21 Blackjack",
    page_icon="🃏",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit's own header/footer and remove padding so the game fills the page
st.markdown(
    """
    <style>
    #MainMenu, header, footer { visibility: hidden; height: 0; }
    [data-testid="stHeader"], [data-testid="stToolbar"],
    [data-testid="stDecoration"] { display: none; }
    .stApp { background: #04200f; }
    .block-container { padding: 0 !important; max-width: 100% !important; }
    iframe { border: none; display: block; }
    </style>
    """,
    unsafe_allow_html=True,
)

html = (Path(__file__).parent / "index.html").read_text(encoding="utf-8")
components.html(html, height=760, scrolling=True)