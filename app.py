import streamlit as st

def page_start():
    if st.session_state.x:
        with st.sidebar:
            st.header("Application menu")
            st.write("Yoou are signed on")
        st.title("You are logged in")
        st.switch_page()


def authenticate_user():
    if name == 'a' and passwd == 'a':
        st.session_state.x = True
        st.switch_page("pages/chartDisplay.py")
    else:
        st.write("Login failed. Try again")
        st.session_state.x = False


if "x" not in st.session_state:
    st.session_state.x = False


st.set_page_config(
    page_title="Multi-Domain Intelligence App",
)
   
if st.session_state.x:
    with st.sidebar:
        st.header("Application menu")
        st.write("You are signed on")

else:
    st.title("Hello")
    st.write("This will be shown on the page!")
    name = st.text_input("username")
    passwd = st.text_input("password", type="password")
    if st.button("login"):
        authenticate_user()

with st.expander("see application details"):
    st.write("This is a test screen")
    st.write("Hi")