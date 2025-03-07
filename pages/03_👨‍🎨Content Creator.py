from modules.content_creator import flux_schnell_create_image, flux_dev_create_image, flux_pro_create_image
import streamlit as st
from PIL import Image


st.set_page_config(page_title = "Hayek&You", page_icon = "🧑‍🏫", layout = "centered", initial_sidebar_state = "expanded")


with st.sidebar:
    
    model = st.radio(label = "Choose a Model:", 
                     options = ["Flux - Schnell", "Flux - Dev", "Flux - Pro"],
                     index = 1,
                     key = "model")
    
    st.write("---")
    
    if model == "Flux - Dev" or model == "Flux - Pro":
        reference_image = st.file_uploader(label = "Upload a reference image:", 
                                        type = ["jpg", "png", "jpeg"],
                                        key = "reference_image",
                                        help = "Upload a reference image to use as a starting point for the image generation")
    
    if model == "Flux - Schnell" or model == "Flux - Dev":
        num_images = st.slider(label = "Number of Images", 
                            min_value = 1, 
                            max_value = 4, 
                            value = 1, 
                            step = 1,
                            key = "num_images",
                            help = "Select the number of images to generate")
    
    if model == "Flux - Dev":
        prompt_strength = st.slider(label = "Prompt Strength", 
                                    min_value = 0.1, 
                                    max_value = 1.0, 
                                    value = 0.8, 
                                    step = 0.1,
                                    key = "prompt_strength",
                                    help = "Adjust the strength of the prompt to control the image generation")
    

# PROMPT INPUT
with st.form(key = "prompt_text_form", clear_on_submit = False):
    
    prompt = st.text_area(label = "", 
                          placeholder = "Enter your prompt here",
                          max_chars = 100,
                          height = 150,
                          key = "prompt")
    
    submit_button = st.form_submit_button(label = "Generate Image", 
                                          type = "primary", 
                                          use_container_width = True,
                                          help = "Generate the image based on the prompt")
    
    
    if submit_button and model == "Flux - Schnell":
        response = flux_schnell_create_image(prompt, num_images)
        for i in response:
            image = Image.open(i)
            st.image(image)
        
    elif submit_button and model == "Flux - Dev":
        response = flux_dev_create_image(prompt, num_images, reference_image, prompt_strength)
        for i in response:
            image = Image.open(i)
            st.image(image)
        
    elif submit_button and model == "Flux - Pro":
        response = flux_pro_create_image(prompt, reference_image)
        for i in response:
            image = Image.open(i)
            st.image(image)