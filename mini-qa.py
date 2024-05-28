import os
from dotenv import load_dotenv
from langchain_community.vectorstores.cassandra import Cassandra
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain_community.llms import openai
from langchain_openai import OpenAI
from langchain_openai import OpenAIEmbeddings

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

from astrapy import DataAPIClient
from astrapy.constants import VectorMetric
from astrapy.ids import UUID
from astrapy.exceptions import InsertManyException


from datasets import load_dataset

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
ASTRA_DB_APPLICATION_TOKEN = os.getenv('ASTRA_DB_APPLICATION_TOKEN')
ASTRA_DB_API_ENDPOINT = os.getenv('ASTRA_DB_API_ENDPOINT')

llm = OpenAI(api_key=OPENAI_API_KEY)
myEmbeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

# Initialize the client
client = DataAPIClient(ASTRA_DB_APPLICATION_TOKEN)
db = client.get_database_by_api_endpoint(
  "https://b0d3fe7f-952d-41c6-8087-c8753caac07b-us-east1.apps.astra.datastax.com"
)

print(f"Connected to Astra DB: {db.list_collection_names()}")

database = client.get_database(ASTRA_DB_API_ENDPOINT)
print(f"* Database: {database.info().name}\n")


# Create a new collection
collection = database.create_collection(
    "vector_test",
    dimension=5,
    metric=VectorMetric.COSINE,  # or simply "cosine"
    check_exists=False,
)
print(f"* Collection: {collection.full_name}\n")

# Insert some documents
documents = [
    {
        "_id": UUID("018e65c9-df45-7913-89f8-175f28bd7f74"),
        "text": "ChatGPT integrated sneakers that talk to you",
        "$vector": [0.1, 0.15, 0.3, 0.12, 0.05],
    },
    {
        "_id": UUID("018e65c9-e1b7-7048-a593-db452be1e4c2"),
        "text": "An AI quilt to help you sleep forever",
        "$vector": [0.45, 0.09, 0.01, 0.2, 0.11],
    },
    {
        "_id": UUID("018e65c9-e33d-749b-9386-e848739582f0"),
        "text": "A deep learning display that controls your mood",
        "$vector": [0.1, 0.05, 0.08, 0.3, 0.6],
    },
]
try:
    insertion_result = collection.insert_many(documents)
    print(f"* Inserted {len(insertion_result.inserted_ids)} items.\n")
except InsertManyException:
    print("* Documents found on DB already. Let's move on.\n")


# Perform a similarity search
query = [0.2, 0.15, 0.2, 0.11, 0.05]
results = collection.find(
    vector=query,
    limit=10,
)
print("Vector search results:")
for document in results:
    print("    ", document)

# Cleanup (if desired)
drop_result = collection.drop()
print(f"\nCleanup: {drop_result}\n")