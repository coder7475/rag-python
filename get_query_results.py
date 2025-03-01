# Define a function to run vector search queries
from pymongo import MongoClient
from get_embeddings import get_embedding

import pprint


def get_query_results(query):
    """Gets results from a vector search query."""

    query_embedding = get_embedding(query)
    pipeline = [
        {
            "$vectorSearch": {
                "index": "vector_index",
                "queryVector": query_embedding,
                "path": "embedding",
                "exact": True,
                "limit": 5,
            }
        },
        {"$project": {"_id": 0, "text": 1}},
    ]
    # Connect to your Atlas cluster
    client = MongoClient(
        "mongodb+srv://rag:V0oyZYxieV05mPKL@cluster0.xjslrno.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    )
    collection = client["rag_db"]["test"]

    results = collection.aggregate(pipeline)

    array_of_results = []
    for doc in results:
        array_of_results.append(doc)
    return array_of_results


# Test the function with a sample query

pprint.pprint(get_query_results("AI technology"))

