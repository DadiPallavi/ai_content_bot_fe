import streamlit as st
import requests as rq

BACKEND_URL="http://127.0.0.1:8000"
st.set_page_config(
    page_title="AI content Generator",
    layout="wide"
)
st.title("AI Content Generator")
st.write("Genrate Blogs,LinkedIn Posts,Captions,Emails and more")
topic=st.text_input(
    "Enter topic"
)
technology=st.selectbox(
    "Select Technology",
    [
        "Python",
        "Java",
        "Html",
        "Css",
        "NodeJs"
    ]
)
content_type=st.selectbox(
    "Content Type",
    [
        "LinkedIn Post",
        "Blog",
        "Instagram Caption",
        "Twitter Post",
        "Email",
        "Youtube Description"
    ]
)
tone=st.selectbox(
    "Tone",
    [
        "Professional",
        "Technical",
        "Friendly",
        "Casual",
        "Marketing"
    ]
)
generate=st.button("Generate Content")
if generate:
    if topic=="":
        st.warning("please enter topic")
    else:
        with st.spinner("Generating Content...."):
            response=rq.post(
                f"{BACKEND_URL}/generate",
                params={
                    "topic":topic,
                    "technology":technology,
                    "content_type":content_type,
                    "tone":tone
                }
            )
            st.write("Status Code:",response.status_code)
            st.write("Response Text:",response.json()["content"])
            st.success("Content Generated Successfully")
            st.subheader("Generated Content")