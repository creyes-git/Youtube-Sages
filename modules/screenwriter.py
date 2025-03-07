from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv


load_dotenv() # Load the .env file


# Initializing the LLM
llm = ChatGroq(model = "llama-3.3-70b-versatile",
               temperature = 1.5,
               max_tokens = 20000,
               timeout = None,
               max_retries = 2,
               stop_sequences = None)
    

# This library stores the conversation history in streamlit memory, allowing the agent to mantain context during the conversation
system_message = ("Eres un guionista profesional con experiencia en la elaboración de guiones atractivos para videos de YouTube"
                  "Su papel es ayudar al usuario a crear narrativas convincentes y responder preguntas sobre su guión"
                  "Por favor, utilice el contexto y el tema proporcionados para informar sus respuestas sobre la historia y el guión"
                  "Si una pregunta cae fuera del ámbito de la escritura de guiones, responde con 'No soy un experto' y luego responde"
                  "Solo responde en ESPANOL"
                  "\n\n"
                  "{input}")

qa_prompt = ChatPromptTemplate.from_messages([MessagesPlaceholder(variable_name = "chat_history"),
                                                                 ("human", "{input}"),
                                                                 ("system", system_message)])


# Create the CHAIN with the prompt and LLM
chain = qa_prompt | llm


memory = StreamlitChatMessageHistory()
memory.add_message(SystemMessage(content = system_message)) # Start the conversation with the system message


def talk_with_screenwriter(user_input : str):
    
    memory.add_message(HumanMessage(content = user_input))
    
    response = chain.invoke({"input": user_input, "chat_history": memory.messages})
    
    memory.add_message(AIMessage(content = response.content))
    
    return response.content
    

def clear_memory():
    
    memory.clear()
    memory.add_message(SystemMessage(content = system_message))