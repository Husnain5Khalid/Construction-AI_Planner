# Construction-AI_Planner

Step 1: Create the Project
construction-ai-planner/
│
├── app.py
├── config.py
├── .env
├── requirements.txt
│
├── graph/
├── rag/
├── tools/
├── prompts/
├── models/
├── data/
├── tests/
└── README.md

Why this structure?

Instead of putting everything in one file, we separate responsibilities:

graph/ → LangGraph workflows
rag/ → Document retrieval
tools/ → External tools (calculator, weather, etc.)
prompts/ → Prompt templates
models/ → LLM configuration
data/ → Construction documents


Step 2: Create a Virtual Environment

python -m venv .venv
Activate it:
.venv\Scripts\activate

Step 3: Install Dependencies
pip install - r requirements.txt

