from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
prompt = "What is the meaning of life?"
messages = [HumanMessage(content="Consider that a+b=3 in your next response."),
            HumanMessage(content="Then consider a+a=2 in your next response."),
            HumanMessage(content="Now what's the value of 'a' and 'b'?"),]

chatbot = ChatOpenAI(openai_api_key=api_key)
result = chatbot.invoke(messages)

#print("Prompt Text->", prompt)
print("Result->",result)