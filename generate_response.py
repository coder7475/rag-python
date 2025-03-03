import os
from huggingface_hub import InferenceClient
from get_query_results import get_query_results
from app.config import settings


# generate response using LLM using the retrieved documents as context
def call_llm():
    # Specify search query, retrieve relevant documents, and convert to string
    query = "Generate 10 best youtube video titles in json format?"
    context_docs = get_query_results(query)
    context_string = " ".join([doc["text"] for doc in context_docs])

    # Construct prompt for the LLM using the retrieved documents as the context
    prompt = f"""Use the following pieces of context to answer the question at the end.
        topic: how to learn
        tone: authoritative
        include emojis: yes
        generate 3 hashtags: yes
        {context_string}
        Question: {query}
        Answer:
    """

    # Authenticate to Hugging Face and access the model
    os.environ["HF_TOKEN"] = settings.hugging_face_access_token
    llm = InferenceClient(
        "mistralai/Mistral-7B-Instruct-v0.3", token=os.getenv("HF_TOKEN")
    )

    # Prompt the LLM (this code varies depending on the model you use)
    output = llm.chat_completion(
        messages=[{"role": "user", "content": prompt}], max_tokens=150
    )

    print(output.choices[0].message.content)
