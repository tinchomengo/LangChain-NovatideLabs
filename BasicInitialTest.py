from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
prompt = "What is the meaning of life?"
chatbot = ChatOpenAI(openai_api_key=api_key)
result = chatbot.invoke(prompt)
print("Prompt Text->", prompt)
print("Result->",result)