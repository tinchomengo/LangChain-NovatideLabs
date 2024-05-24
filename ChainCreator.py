from langchain.chat_models import ChatOpenAI
from langchain.chat_models import ollama
from langchain.prompts import ChatPromptTemplate
from langchain.schema import BaseOutputParser
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

chatbot = ChatOpenAI(openai_api_key=api_key)
secondChatbot = ollama.OllamaChat()

class JSONParser(BaseOutputParser):
    def parse(self, text: str):
        return text.strip().split(", ")

template = "You are a helpful assistant that generates comma-separated lists. A user will pass in a category and you should generate 5 objects in that category, in a comma-separated list. ONLY return a comma-separated list, nothing more."
human_template = "{text}"

prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("user", human_template)
])
secondPrompt = "What is the meaning of life?"
secondResult = secondChatbot.invoke(prompt)

chain = prompt | chatbot | JSONParser()
result = chain.invoke({"text": "animals"})
print("Result 1->", result)
print("Result 2->", secondResult)