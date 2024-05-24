from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

chatbot = ChatOpenAI(openai_api_key=api_key)

template = "You translate from {source_language} to {target_language}."
human_template = "{text}"

prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("user", human_template)
])

messages = prompt.format_messages(source_language="English", target_language="Italian", text="Hello, how are you?")

result = chatbot(messages)

print("Result->", result.content)