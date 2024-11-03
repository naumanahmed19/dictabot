from core.config import openai, pc
from utils.langchain import split_text

with open('./assets/document.txt', 'r') as file:
    documents = file.read()

# upcert data to picone database

def upsert_data(identifier, text):
    """
    Upserts the given data to the Pinecone database.

    Parameters:
    identifier (str): The id for the user item
    text (str): The text for which to generate embeddings and upsert to Pinecone.

    Returns:
    None
    """
    data = generate_embeddings(identifier,text)
    pc.upsert(
        vectors=data,
    )
    print('Data pushed to Pinecone')

#Generate embeddings for each sentence

def generate_embeddings(identifier, text):
    """
    Generates embeddings for each chunk of the given text.

    Parameters:
    identifier (str): The id for the user item
    text (str): The text for which to generate embeddings.

    Returns:
    data (list): The embeddings generated for the given text.
    """
    text_chunks = split_text(text)
    data = []
    for i, chunk in enumerate(text_chunks):
        response = openai.embeddings.create(
            input= chunk.page_content,
            model= "text-embedding-3-small",
            encoding_format = "float",
        )
        data.append({
            "id": f"item#{identifier}_chunk_{i}",
            "values": response.data[0].embedding,
            "metadata": {
                "content": chunk.page_content,
            }
        })
        print("Embeddings generated successfully")
        return data





# upsert_data('1',documents)


# Search for similar documents

def search_similar_documents(text):
    """
    Searches for similar documents in the Pinecone database.

    Parameters:
    text (str): The text to search for similar documents.

    Returns:
    results (list): The list of similar documents.
    """
    embeddings = generate_embeddings("search", text)
    response = pc.query(
        vectors=embeddings,
        top_k=5,
    )
    results = []
    for result in response.results:
        results.append(result.metadata['content'])
    return results



# create speach to text using openai whisper api
def speach_to_text():