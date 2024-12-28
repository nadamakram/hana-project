import streamlit as st
from supabase import create_client, Client
from dotenv import load_dotenv
import os 
import importlib.util
from st_login_form import login_form

load_dotenv()

st.set_page_config(
    page_title="Login تسجيل الدخول",
    page_icon="🔑",
    layout="centered"
)

# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    return create_client(url, key)

supabase = init_connection()


client = login_form()

if st.session_state["authenticated"]:
    if st.session_state["username"]:
        st.success(f"Welcome {st.session_state['username']}")
        st.query_params["pages"] = 'chatbot'
        st.switch_page("pages/chatbot.py")
    else:
        st.success("Welcome guest")
        st.query_params["pages"] = 'chatbot'
        st.switch_page("pages/chatbot.py")
        ...
else:
    st.error("Not authenticated")