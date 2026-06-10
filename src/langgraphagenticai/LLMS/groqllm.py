import os
import streamlit as st
from langchain_groq import ChatGroq
"""
This .py file get the input from our UI (like the GROQ API Key) and the model we want to use and then initialize the Groq LLM with those inputs.
"""
class GroqLLM:
    """
    This user_controls_input is coming from our user input where we gather all the necessary information from 
    the user. You can trace it back to main.py and then main.py will point you to loadui.py where we have the LoadStreamlitUI class that is responsible 
    for loading the UI and gathering user inputs. So pretty much we are passing all the user inputs from the UI to this GroqLLM class to initialize our 
    LLM model with those inputs but in this case it will be our GROQ API Key and the GROQ model we want to use.
    """
    def __init__(self,user_controls_input):
        self.user_controls_input=user_controls_input
    def get_llm_model(self):
        try:
            groq_api_key=self.user_controls_input['GROQ_API_KEY']
            selected_groq_model=self.user_controls_input['selected_groq_model']
            if groq_api_key=='' and os.environ["GROQ_API_KEY"] =='':
                st.error("Please Enter the Groq API KEY")

            llm = ChatGroq(api_key =groq_api_key, model=selected_groq_model)

        except Exception as e:
            raise ValueError(f"Error Occurred with Exception : {e}")
        return llm