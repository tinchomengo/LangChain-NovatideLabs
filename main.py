from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

chatbot = ChatOpenAI(openai_api_key=api_key)
result = chatbot.invoke("What is the meaning of a human person?")
print(result)