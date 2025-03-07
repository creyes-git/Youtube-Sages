from modules.screenwriter import memory
from modules.voice_actor import cartesia_text_to_speech
import streamlit as st


st.set_page_config(page_title = "Hayek&You", page_icon = "🧑‍🏫", layout = "centered", initial_sidebar_state = "expanded")


with st.sidebar:

    upload_script = st.file_uploader(label = "Upload Script", 
                                     type = "txt", 
                                     key = "upload_script", 
                                     accept_multiple_files = False,
                                     help = "Upload your script in TXT format to use it with the Voice Actor")
    
    st.write("\n") # Space Line
    
    placeholder = st.empty()
    if upload_script:
        memory_script = placeholder.button(label = "Use In-Memory Script",
                                           key = "memory_script", 
                                           disabled = True)
        
    else:
        memory_script = placeholder.button(label = "Use In-Memory Script", 
                                           type = "primary", 
                                           key = "memory_script", 
                                           icon = "🧠",
                                           use_container_width = True,
                                           help = "Use the script in the conversation history, if available")
        
    st.write("---") # Space Line
    
    voice_speed = st.slider(label = "Voice Speed", 
                            min_value = 0.01, 
                            max_value = 0.5, 
                            value = 0.1, 
                            step = 0.01,
                            key = "voice_speed",
                            on_change = None,
                            help = "Adjust the speed of the voice")
    
    st.write("\n") # Space Line
    st.write("\n") # Space Line
    st.write("\n") # Space Line
    st.write("\n") # Space Line
    st.write("\n") # Space Line
    
    create_speech = st.button(label = "Create Speech", 
                              type = "primary",
                              key = "create_speech", 
                              icon = "🎙️",
                              use_container_width = True,
                              help = "Convert the text to speech using the script and save it to a .mp3 file")
    

if upload_script:
    script = upload_script.read().decode("utf-8")
    st.write(script)
    
if memory_script:
    try:
        script = str(list(filter(lambda msg: msg.type == "ai", memory.messages))[-1].content)
        st.title("Your Script:")
        st.write(script)
    except:
        st.warning("No script found in the conversation history. Go with the Screenwriter to start.", icon = "⚠️")
        

with st.spinner("Creating Speech..."):        
    if create_speech:
        
        text = str(list(filter(lambda msg: msg.type == "ai", memory.messages))[-1].content)
        
        speech = cartesia_text_to_speech(text = text, speed = voice_speed)
            
        audio = st.audio(speech.content, format = "audio/mpeg")
        
        with open(r"assets\audio\my_speech.mp3", "wb") as f:
            f.write(speech.content)
            
        st.success("Speech created successfully!", icon = "✅")
        st.balloons()
        
        if audio:
            with st.sidebar:
                st.download_button(label = "Download Speech", 
                                   data = open(r"C:\Users\creyes\Desktop\LLM_Learning\Youtube-Guru\assets\audio\my_speech.mp3", "rb").read(),
                                   file_name = "my_speech.mp3",
                                   mime = "audio/mpeg",
                                   icon = "📥",
                                   key = "download_speech",
                                   use_container_width = True)
       
    