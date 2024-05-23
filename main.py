import requests
#from langchain_community.llms import OpenAI
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from the environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')

# Initialize the OpenAI language model with max_tokens parameter
llm = OpenAI(api_key=openai_api_key, max_tokens=500)  # Adjust max_tokens as needed

# Define a function to get Pokémon information from PokeAPI
def get_pokemon_info(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    return response.json()

# Define a prompt template for the Pokémon query
template = "Tell me about the Pokémon {pokemon_name}."
prompt = PromptTemplate(template=template, input_variables=["pokemon_name"])

# Function to create the prompt text
def create_prompt_text(template, input_data):
    print("here")
    return template.format(pokemon_name=input_data["pokemon_name"])

# Define the Pokémon name
pokemon_name = "pikachu"

# Create the prompt text
prompt_text = create_prompt_text(prompt, {"pokemon_name": pokemon_name})
print("Prompt Text->", prompt_text)

# Get the AI's response using the language model
ai_response = llm.invoke(prompt_text)  # Use invoke method instead of __call__

# Print the AI response
print("AI Response:", ai_response)

# Get the Pokémon information using the PokeAPI
pokemon_info = get_pokemon_info(pokemon_name)
#print("Pokémon Information:", pokemon_info)
