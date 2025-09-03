from pymongo import MongoClient
from pymongo.operations import SearchIndexModel
import time
from app.config import settings


# Create a vector search index in mongodb atlas
def create_vector_index():
    # Create your index model, then create the search index
    index_name = "vector_index"
    search_index_model = SearchIndexModel(
        definition={
            "fields": [
                {
                    "type": "vector",
                    "numDimensions": 768,
                    "path": "embedding",
                    "similarity": "cosine",
                }
            ]
        },
        name=index_name,
        type="vectorSearch",
    )
    # Connect to your Atlas cluster
    client = MongoClient(settings.atlas_connection_string)
    collection = client["rag-atlas"]["starter"]

    collection.create_search_index(model=search_index_model)

    # Wait for initial sync to complete

    print("Polling to check if the index is ready. This may take up to a minute.")

    predicate = None

    if predicate is None:
        predicate = lambda index: index.get("queryable") is True

    while True:
        indices = list(collection.list_search_indexes(index_name))
        if len(indices) and predicate(indices[0]):
            break
        time.sleep(5)

    print(index_name + " is ready for querying.")
