from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

chatbot = ChatOpenAI(openai_api_key=api_key)

def parse(text: str):
    return text.strip().split("answer =")

template = "You are a helpful assistant that solves math problems. Output the answer in the following format: answer = <answer here>. Make sure to output the answer in all lowercases and to have exactly one space and one equal sign following it."
human_template = "{problem}"

prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("user", human_template)
])

message = prompt.format_messages(problem="2x^2-5x+3=0")

result = chatbot(message)

parsed = parse(result.content)

steps, answer = parsed

print("Result->", answer)