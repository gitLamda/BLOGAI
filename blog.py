# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 09:57:37 2024

@author: User
"""

import streamlit as st
import google.generativeai as genai
from apikey import google_gemin_api

genai.configure(api_key = google_gemin_api)
# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

# title of the app
st.title('BLOG.AI')

# create subheader
st.subheader('Create blogs with your new AI Blog companion!')

with st.sidebar:
    st.title('Enter Blog Details')
    blog_title = st.text_input('Blog Title')
    keywords = st.text_input('Blog Keywords')
    num_words = st.slider('Number of Words', min_value= 250, max_value = 1000, step = 50)
    submit_button = st.button('Generate Blog')
    prompt_parts = [f"Generate a comprehensive engaging blog post relevant to the given title \"{blog_title}\" and {keywords}\". Make sure to incorporate these {keywords} in the blog post. The blog be approximately {num_words} in length, suitable for an online audience. Ensure the content is original, informative and maintains a consistent tone throughout."]                
    
    response = model.generate_content(prompt_parts)
if submit_button:
    st.write(response.text)