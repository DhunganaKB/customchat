import streamlit as st
from langchain.chat_models import ChatOpenAI
import openai
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)

OPENAI_API_KEY=os.getenv('OPENAI_API_KEY')
openai.api_key=OPENAI_API_KEY

print(openai.api_key)

model_id='ft:gpt-3.5-turbo-0613:personal::87mitXcG'

st.title('Nobel Prize Chatbot (Science): 2023')
st.write('This app will answer about nobel laureates - 2023')

#st.write("**Your question goes here:**")

question = st.text_input("Your question goes here:", key="input")

if question:
    test_message=[{'role': 'system',
    'content': "As a dedicated journalist closely monitoring latest development in science and technology, you provide us with accurate and factual information regarding  the nobel prize 2023."},
    {'role': 'user', 'content': f'{question}'}]

    completion = openai.ChatCompletion.create(model=model_id,messages=test_message)

    answer = completion['choices'][0].message['content']

    st.write(answer)
