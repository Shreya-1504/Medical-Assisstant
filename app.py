#streamlit is for creating the app
#nltk is working with the text
#we use pipeline to install pretrained models from hugging face
#distilgpt is the text generation model 
#it takes time since it uses many parameters.first time it takes ore time since it downloads the models
import streamlit as st
import nltk
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#download necessary nltk data
nltk.download('punkt') #downloads data like punctuation rules
nltk.download('stopwords')

#load apretrained hugging face model
chatbot = pipeline("text-generation", model="distilgpt2")
def healthcare_chatbot(user_input):
    user_input = user_input.lower()  

    if "symptom" in user_input:
        return "please consult Doctor for accurate advice"
    elif "appointment" in user_input:
        return "Would you like to schedule appointment with doctor"
    elif "medication" in user_input:
        return "It is important to take prescribed medicines regularly"
    else:
        response=chatbot(user_input,max_length=500,num_return_sequences=1)
        #max_length of chatbot response
        #num_return_sequences is used to to tell how many responses/answers we want
        return response[0]['generated_text']
        #response has many things,it has probability values as well,but we only th first thing and in that we need generated text

def main():
    st.title("AI Health Assistant 🤖💊")
    st.write("Welcome! Ask me health-related questions.")

    # Maintain chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_area("How can I assist you?", height=100)

    if st.button("Submit"):
        if user_input:
            st.session_state.chat_history.append(("User", user_input))
            with st.spinner("Processing your query, please wait..."):
                response = healthcare_chatbot(user_input)
            st.session_state.chat_history.append(("Chatbot", response))

    # Display chat history
    for role, text in st.session_state.chat_history:
        st.write(f"**{role}:** {text}")
main()