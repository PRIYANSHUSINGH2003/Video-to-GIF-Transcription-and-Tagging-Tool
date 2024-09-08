import streamlit as st
import requests

st.set_page_config(page_title="Video to GIF Tool", layout="wide")

# User Authentication and Subscription status
st.title("Video to GIF Transcription Tool")
st.sidebar.title("Login/Signup")

# Check if user is logged in
if 'user_token' not in st.session_state:
    email = st.text_input("Enter Email")
    password = st.text_input("Enter Password", type="password")
    if st.button("Login"):
        response = requests.post("http://localhost:8000/login", data={"email": email, "password": password})
        st.session_state.user_token = response.json().get("token")
else:
    st.write("Welcome back!")
    if st.button("Logout"):
        del st.session_state.user_token

# GIF Creation Interface
if st.session_state.get("user_token"):
    st.write("Upload a video to create a GIF")
    video_file = st.file_uploader("Choose a video file", type=["mp4"])
    if st.button("Generate GIF"):
        # Send request to FastAPI backend to generate GIF
        files = {"file": video_file}
        headers = {"Authorization": f"Bearer {st.session_state.user_token}"}
        response = requests.post("http://localhost:8000/generate_gif/", files=files, headers=headers)
        st.write(response.json())
