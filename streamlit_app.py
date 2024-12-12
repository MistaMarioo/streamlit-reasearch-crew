import streamlit as st
from main import ResearchCrew  # Import the ResearchCrew class from main.py
import os

st.title('Email Creator by Marketing.MBA')
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
os.environ["SERPER_API_KEY"] = st.secrets["SERPER_API_KEY"]
os.environ["ANTHROPIC_API_KEY"] = st.secrets["ANTHROPIC_API_KEY"]
os.environ["PERPLEXITY_API_KEY"] = st.secrets["PRPLEXITY_API_KEY"]

with st.sidebar:
    st.header('Enter Email Details')
    topic = st.text_input("Main topic:")
    targetgroup_information = st.text_area("Target Group Information:")
    key_points = st.text_area("Key Points or Specific Information Needed:")
    email_type = st.radio("Select Email-Type", ["Content Email", "Pitch Email", "Content Email with Pitch"], index=0, format_func=lambda x: x, disabled=False, horizontal=False, label_visibility="visible")

if st.button('Write Email'):
    if not topic or not targetgroup_information or not key_points or not email_type:
        st.error("Please fill all the fields.")
    else:
        inputs = f"Research Topic: {topic}\nTarget Group Information: {targetgroup_information}\nKey Points: {key_points}\nEmail Type: {email_type}"
        research_crew = ResearchCrew(inputs)
        result = research_crew.run()
        st.subheader("Results:")
        st.write(result)
