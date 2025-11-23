from langsmith import traceable
from langchain_huggingface import HuggingFaceEndpoint
from langchain.chains import RetrievalQA
from app.core.config import settings
from app.modules.storage import get_vectorstore
from app.prompts.templates import get_prompt

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    task="text-generation",   # ✅ force correct API
    temperature=0.3,
    huggingfacehub_api_token=settings.HUGGINGFACEHUB_API_TOKEN,
    model_kwargs={"max_length": 512}
)


@traceable(name="Financial_Analysis_Run") # <--- LangSmith Tracking
def run_financial_analysis(query: str):
    """
    Executes the RAG pipeline with full observability.
    """
    # 1. Get Retriever
    vectorstore = get_vectorstore()
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    
    # 2. Build Chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        chain_type_kwargs={"prompt": get_prompt()}
    )
    
    # 3. Invoke
    result = qa_chain.invoke({"query": query})
    return result['result']# RAG Logic & Generation
