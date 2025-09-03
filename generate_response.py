import os
import json
import re

from huggingface_hub import InferenceClient
from get_query_results import get_query_results
from app.config import settings


# generate response using LLM using the retrieved documents as context
def call_llm(body):
    # Build the query dynamically using the input body
    video_title = body.get("video_title", "")
    description = body.get("description", "")
    include_emojis = body.get("include_emojis", "")
    video_type = body.get("video_type", "")
    hashtags = body.get("generate_hashtags", "")

    # Improved prompt for generating YouTube video titles in JSON format
    query = f"""
    [INST]
    You are an expert YouTube title creator with over 10 years of experience in crafting high-retention, high-CTR (click-through rate) titles.
    Your task is to generate 3 unique, compelling YouTube video titles, each accompanied by 3 relevant hashtags, based on the information provided below.

    Please ensure:
    - Titles are creative, engaging, and optimized for YouTube search and click-through.
    - Hashtags are relevant, trending, and help increase discoverability.
    - If 'Include Emojis' is 'yes', add appropriate emojis to the titles.
    - If 'Generate hashtags' is 'no', leave the hashtags array empty.
    - The output is a valid, minified JSON array (no comments, no trailing commas, no escape codes), directly usable in code.

    Input Information:
    - Possible Title: {video_title}
    - Video Type: {video_type}
    - Description: {description}
    - Include Emojis: {include_emojis}
    - Generate Hashtags: {hashtags}

    Example Output:
    [
      {{
        "title": "Your First Compelling Title",
        "hashtags": ["#example1", "#example2", "#example3"]
      }},
      {{
        "title": "Another Engaging Title",
        "hashtags": ["#tag1", "#tag2", "#tag3"]
      }},
      {{
        "title": "Third Attention-Grabbing Title",
        "hashtags": ["#tagA", "#tagB", "#tagC"]
      }}
    ]

    Only return the JSON array as shown above.
    [/INST]
    """

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

    # Try to extract the JSON array from the output string
    output_text = output.choices[0].message.content

    # Use regex to find the first JSON array in the output
    match = re.search(r"\[\s*{.*?}\s*\]", output_text, re.DOTALL)
    if match:
        json_str = match.group(0)
        try:
            extracted_json = json.loads(json_str)
        except Exception:
            # If parsing fails, fallback to returning the string
            extracted_json = json_str
    else:
        # If no JSON array found, fallback to returning the whole output
        extracted_json = output_text

    return extracted_json


if __name__ == "__main__":
    call_llm()
