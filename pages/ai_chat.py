import streamlit as st
from app.services.ai_service import generate_ai_response

st.set_page_config(page_title="AI Chat")

#security check
if not st.session_state.get('logged_in', False):
    st.error("Access denied. Please log in to use the AI assistant.")
    st.page_link("pages/login.py", label="Go to login page")
    st.stop()

st.header("AI Intelligence Assistant")
st.subheader(f"Ask the AI anything (Logged in as: {st.session_state['role']})")

#initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hello! I am an expert in Cybersecurity, Data Analysis, and IT Operations. How can I assist you?"}
    ]

#Display chat history
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#user input section
if prompt := st.chat_input("Enter your query here..."):
    #Add user message
    st.session_state["messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    #Generate AI response
    with st.spinner("Thinking..."):
        ai_response = generate_ai_response(
            user_prompt=prompt,
            user_role=st.session_state['role']
        )
    
    #AI response
    st.session_state["messages"].append({"role": "assistant", "content": ai_response})
    with st.chat_message("assistant"):
        st.markdown(ai_response)