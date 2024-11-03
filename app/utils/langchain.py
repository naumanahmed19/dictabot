from langchain_text_splitters import RecursiveCharacterTextSplitter

# Import LangChain and split the document using recursive splitter
def split_text(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=20,
        length_function=len,
        is_separator_regex=False,
    )
    return splitter.create_documents([text])
