from modules.screenwriter import talk_with_screenwriter, clear_memory, memory
import streamlit as st
import os


st.set_page_config(page_title = "Hayek&You", page_icon = "🧑‍🏫", layout = "centered", initial_sidebar_state = "expanded")


def save_to_script(response):
        
    if os.path.exists(r"assets\temp\script.txt"):
        os.remove(r"assets\temp\script.txt")
        
    with open(r"assets\temp\script.txt", "w") as f:
        f.write(f"{response}")


with st.sidebar:

    new_chat = st.button(label = "New Chat", 
                         type = "primary", 
                         key = "new_chat", 
                         icon = "✍🏼",
                         use_container_width = True,
                         help = "Start a new chat and clear the conversation history")
    
    
    #placeholder = st.empty()
    #if new_chat:
    #    dowload_script = placeholder.download_button(label = "Get Script!", 
    #                                                 data = "",
    #                                                 icon = "📥",
    #                                                 use_container_width = True,
    #                                                 disabled = True) 
    #else:    
    #    dowload_script = placeholder.download_button(label = "Get Script!", 
    #                                                 type = "secondary", 
    #                                                 key = "get_script",
    #                                                 data = open(r"C:\Users\creyes\Desktop\LLM_Learning\Youtube-Guru\assets\temp\script.txt"),
    #                                                 icon = "📥",
    #                                                 mime = "text/plain",
    #                                                 use_container_width = True,
    #                                                 help = "Get the last conversation messages as the final script")
        
    
# Buttons actions        
if new_chat:
    clear_memory()


for msg in memory.messages:
    if msg.type == "human":
        st.chat_message("human", avatar = r"C:\Users\creyes\Desktop\LLM_Learning\Youtube-Guru\assets\images\human_avatar.svg").write(msg.content)
    elif  msg.type == "ai":
        st.chat_message("ai", avatar = r"C:\Users\creyes\Desktop\LLM_Learning\Youtube-Guru\assets\images\ai_avatar.svg").write(msg.content)


with st.spinner("Thinking..."):
    if user_input := st.chat_input(placeholder = "Your message..."):
        
        st.chat_message("human", avatar = r"C:\Users\creyes\Desktop\LLM_Learning\Youtube-Guru\assets\images\human_avatar.svg").write(user_input)
        response = talk_with_screenwriter(user_input)
        #save_to_script(response)# Keep saving the AI response as a script to a file 
        st.chat_message("ai", avatar = r"C:\Users\creyes\Desktop\LLM_Learning\Youtube-Guru\assets\images\ai_avatar.svg").write(response)