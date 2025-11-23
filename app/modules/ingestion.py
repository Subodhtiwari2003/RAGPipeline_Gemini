from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_and_chunk_data(urls: list[str]):
    print(f"Loading data from {len(urls)} sources...")
    
    # 1. Load
    # 1. Load Data
    urls = [
    "https://finance.yahoo.com/quote/AAPL",
    "https://www.investing.com/equities/apple-computer-inc",
    "https://www.moneycontrol.com/india/stockpricequote/technology/infosys/IT"
    ]

    loader = WebBaseLoader(urls)
    docs = loader.load()
    
    # 2. Split
    # Chunk size 1000 is good for financial reports to keep context
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, 
        chunk_overlap=200
    )
    chunks = text_splitter.split_documents(docs)
    
    print(f"Generated {len(chunks)} chunks.")
    return chunks# Scrapes and chunks data
