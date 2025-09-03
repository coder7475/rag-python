# 🎥 YouTube Video Title Generator

Generate engaging, clickworthy YouTube video titles (with optional emojis and hashtags) powered by **FastAPI**, **MongoDB Atlas Vector Search**, and **LLMs**.

---

## 🚀 Features

- Generate optimized YouTube video titles from descriptions.
- Optionally add emojis and relevant hashtags.
- Ingest PDF data and create embeddings for vector search.
- Uses MongoDB Atlas **vector search index** with cosine similarity.
- FastAPI backend with auto-generated API docs.

---

## 📂 Project Structure

```

.
├── app
│ ├── config.py # Configuration and environment variables
│ ├── **init**.py
│ └── main.py # FastAPI entrypoint
├── create_vector_index.py # MongoDB Atlas vector index creation
├── generate_response.py # LLM response generation
├── get_embeddings.py # Embedding generation helper
├── get_query_results.py # Query MongoDB Atlas with embeddings
├── ingest_data.py # Ingest & chunk PDF data
├── requirements.txt # Python dependencies
└── README.md # Project documentation

```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/youtube-title-generator.git
cd youtube-title-generator
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configuration

Create a `.env` file in the root directory:

```env
APP_NAME=YouTube Title Generator
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

## ▶️ Usage

### 1. Ingest Data

```bash
python3 ingest_data.py
```

### 2. Create Vector Index

```bash
python3 create_vector_index.py
```

### 3. Generate Response from Query

```bash
python3 generate_response.py
```

Or run the FastAPI app:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

---

## 📡 API Endpoints

| Method | Endpoint        | Description                        |
| ------ | --------------- | ---------------------------------- |
| GET    | `/`             | Root health check                  |
| GET    | `/info`         | Show app info from env             |
| GET    | `/ingest-data`  | Ingest & chunk PDF into embeddings |
| GET    | `/create-index` | Create MongoDB Atlas vector index  |
| POST   | `/prompt`       | Generate YouTube title & hashtags  |

### Example `/prompt` Request

```json
{
  "video_title": "How to Learn",
  "description": "You need to manage time, prioritize tasks, and take notes",
  "include_emojis": "yes",
  "video_type": ".mp4",
  "generate_hashtags": "yes"
}
```

### Example Response

```json
{
  "message": "Prompt generated successfully!",
  "output": [
    {
      "title": "📅 Master Time Management: Prioritize Tasks & Take Notes",
      "hashtags": ["#TimeManagement", "#Productivity", "#YouTubeTips"]
    },
    {
      "title": "📝 Learn the Secrets to Effective Note-Taking",
      "hashtags": ["#Notetaking", "#StudyTips", "#YouTubeTutorial"]
    },
    {
      "title": "🎯 Boost Your Productivity: Prioritize & Organize Your Tasks",
      "hashtags": ["#ProductivityHacks", "#TaskManagement", "#YouTubeLifeHacks"]
    }
  ]
}
```

## 📖 API Documentation

Interactive API documentation is available and auto-generated:

- **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)  
  Explore and test all endpoints with an intuitive interface.

- **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)  
  Browse comprehensive, well-structured API reference documentation.

---

## 🛠️ Development Notes

- Runs on **FastAPI + Uvicorn**.
- Requires **MongoDB Atlas** with vector index support.
- Uses **HuggingFace LLMs** for text generation.
- Extendable for custom embeddings and retrieval-augmented generation (RAG).

---

## 📜 License

MIT License. Feel free to use and modify.

---

## 👨‍💻 Author

Developed by [**Robiul Hossain**](https://github.com/coder7475)
