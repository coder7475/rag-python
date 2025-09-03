# Start

environment

```
python3 -m venv venv
```

activate

```
source venv/

Install:
```

pip install -r requirements.txt

````

# Pipeline

1. Ingest Data:

```python
python3 ingest_data.py
````

2. create vector index:

```py
python3 create_vector_index.py
```

3. Generate Response to a query(prompt):

```python3
python3 generate_response.py
```

Here’s a **README.md** draft tailored for your project based on the structure of your app and what you’ve shared 👇

```markdown
# 📚 FastAPI Vector Search App

A FastAPI application that ingests PDF documents, chunks them into embeddings, stores them in MongoDB Atlas, and provides endpoints to query and generate responses using an LLM.

---

## 🚀 Features

- FastAPI-based backend with auto-generated Swagger docs.
- Ingests PDF files and chunks them into ~400-character segments.
- Creates a **vector search index** in MongoDB Atlas.
- Generates responses from an LLM (e.g., OpenAI/Hugging Face).
- Configurable via environment variables.

---

## 📂 Project Structure
```

.
├── app
│ ├── config.py # Configuration and environment variables
│ ├── **init**.py
│ └── main.py # FastAPI entrypoint
├── create_vector_index.py # MongoDB Atlas vector index creation
├── generate_response.py # Call to LLM for generating responses
├── get_embeddings.py # Generate embeddings from text
├── get_query_results.py # Query MongoDB Atlas vector store
├── ingest_data.py # Ingest & chunk PDF documents
├── README.md # Project documentation
├── requirements.txt # Python dependencies
└── venv # Virtual environment (not committed)

````

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/fastapi-vector-app.git
cd fastapi-vector-app
````

### 2. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configuration

Create a `.env` file in the project root with your settings:

```env
APP_NAME=FastAPI Vector Search
APP_VERSION=0.1.0
DEBUG=True
HOST=127.0.0.1
PORT=8000

DATABASE_URL=mongodb+srv://<user>:<password>@cluster.mongodb.net/db
SECRET_KEY=your-secret-key
API_PREFIX=/api

OPENAI_API_KEY=your-openai-key
```

---

## ▶️ Running the App

### Option 1: With Uvicorn

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Option 2: Directly with Python

```bash
python app/main.py
```

---

## 📡 API Endpoints

| Method | Endpoint        | Description                              |
| ------ | --------------- | ---------------------------------------- |
| GET    | `/`             | Root health check                        |
| GET    | `/info`         | Show app info from environment variables |
| GET    | `/env-test`     | Verify environment variables             |
| GET    | `/ingest-data`  | Ingest and chunk PDF into embeddings     |
| GET    | `/create-index` | Create MongoDB Atlas vector index        |
| GET    | `/prompt`       | Generate a response using the LLM        |

Docs are auto-generated:

- Swagger UI → [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc → [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🛠️ Development Notes

- Runs on **FastAPI + Uvicorn**.
- Requires **MongoDB Atlas** with vector index support.
- Supports **OpenAI/HuggingFace LLMs** for generating responses.
- Extendable for custom embeddings & retrieval-augmented generation.

---

## 📜 License

MIT License. Feel free to use and modify.

---

## 👨‍💻 Author

Developed by **\[Robiul Hossain]**
