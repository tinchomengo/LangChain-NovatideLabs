import requests
#from langchain_community.llms import OpenAI
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')

llm = OpenAI(api_key=openai_api_key, max_tokens=500)

def get_pokemon_info(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    return response.json()

template = "Tell me about the Pokémon {pokemon_name}."
prompt = PromptTemplate(template=template, input_variables=["pokemon_name"])

def create_prompt_text(template, input_data):
    print("here")
    return template.format(pokemon_name=input_data["pokemon_name"])

pokemon_name = "pikachu"

prompt_text = create_prompt_text(prompt, {"pokemon_name": pokemon_name})
print("Prompt Text->", prompt_text)

ai_response = llm.invoke(prompt_text)

print("AI Response:", ai_response)

pokemon_info = get_pokemon_info(pokemon_name)
#print("Pokémon Information:", pokemon_info)
