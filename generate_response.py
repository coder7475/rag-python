import os
from huggingface_hub import InferenceClient
from get_query_results import get_query_results
from app.config import settings


# generate response using LLM using the retrieved documents as context
def call_llm():
    # Specify search query, retrieve relevant documents, and convert to string
    query = """[INST] You are a YouTube title expert with 10 years of experience in crafting high-retention, high-CTR (click-through rate) titles. 
    Your task is to generate 10 compelling youtube video titles with 3 hashtags each and convert it into a valid JSON object based on the given information:

        possible video title: How to Learn
        Description: You need to manage time, priotirize tasks, take notes
        Include emojis: yes

    Generate the JSON object without any escape code, make sure its valid and usable in code:
    [/INST]"""

    context_docs = get_query_results(query)
    context_string = " ".join([doc["text"] for doc in context_docs])

    # Construct prompt for the LLM using the retrieved documents as the context
    prompt = f"""Use the following pieces of context to answer the question at the end.
        {context_string}
        Question: {query}
    """

    # Authenticate to Hugging Face and access the model
    os.environ["HF_TOKEN"] = settings.hugging_face_access_token
    llm = InferenceClient(
        "mistralai/Mistral-7B-Instruct-v0.3", token=os.getenv("HF_TOKEN")
    )

    # Prompt the LLM (this code varies depending on the model you use)
    output = llm.chat_completion(
        messages=[{"role": "user", "content": prompt}], max_tokens=300
    )
    print(output.choices[0].message.content)

    return output.choices[0].message.content


if __name__ == "__main__":
    call_llm()
