import os
from dotenv import load_dotenv
from openai import OpenAI
from pinecone import Pinecone


# Load environment variables from .env file
load_dotenv()

# Create an OpenAI client
client = OpenAI()
client.api_key = os.getenv('OPENAI_API_KEY')
openai = client


# Create a Pinecone client
pcClient = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))
pc = pcClient.Index("mynotes")
