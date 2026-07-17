# Construction-AI_Planner

Lesson 1: Project Setup & First LLM Call
-----------------------------------------
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
pip install -r requirements.txt

Step4 : Create a .env file

Step 5: Create config.py

This file will load environment variables in one place, so the rest of the application doesn't need to know where they come from.

Step 6: Create app.py
----------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------
Lesson 2: Build the Planner Brain (It just build the planner in which Construction AI planner just think or plan what to do . It only make the decision, not answering or calculating)
----------------------------------------------------------------------------------------

Step 1 — Create the Project Structure
construction-ai-planner/

prompts/
    planner.py

models/
    planner_models.py

planner.py(Later moved in agent/planner.py)

Step 2 — Create the Planner Model

We want the LLM to return structured data, not paragraphs.
.models/planner_models.py

Instead of getting:

I think you should search the document.

we get:

{
  "route": "rag",
  "tool_name": null,
  "reason": "Project-specific information."
}

Step 3 — Planner Prompt
prompts/planner.py

Step 4 - Build the Planner
planner.py

step 5 - Test IT
app.py
------------------------------------------------------------------------------------------

-------------------------------------------------------------------------------------------
Lesson 3: Building the Tool Node:
Point to Remember: at this lesson the planner still doesn't know how to calculate things. 
It only knows which tool to use.
------------------------------------------------------------------------------------------
Step 1 - Create a Better Tool Structure
tools/
│
├── __init__.py
├── base.py
├── concrete.py
├── brick.py
├── weather.py
├── registry.py
└── executor.py

Step 2 — Create the First Tool - concrete tool
tools/concrete.py

Step 3 — Brick Estimator
tools/brick.py

Step 4 — Weather Tool
tools/weather.py
app.py

Step 5 — Tool Registry
tools/registry.py

Imagine six months from now.

we'll have:

Concrete Tool
Steel Tool
BOQ Tool
Weather Tool
OCR Tool
Excel Tool
Cost Tool
Schedule Tool

We don't want a giant if/elif chain.
Instead, we build a registry.

Step 6 — Tool Executor(Running Tools)
tools/executor.py
This gives us a single entry point for running tools.


Step 7 — Improve the Planner Output
models/planner_models.py

Our current planner returns:

{
    "route": "tool",
    "tool_name": "calculator"
}

That's not enough.

The executor doesn't know what inputs to pass.

Instead, update PlannerDecision:
---------------------------------------------------------------------------

------------------------------------------------------------------------
Lesson 4 - – Build the Tool Agent
An AI agent is a component that can reason, decide, act, and return a result.
-----------------------------------------------------------------

Lesson 4.1 - Tool Selection Agent(Under Tool Agent)
Step 1: Create the Tool Model
File: models/tool_model.py

Step 2: Create the Prompt
File: prompts/tool_selector.py

Step 3: Create the Tool Selector
File: agents/tool_selector.py

Step 4: Create the Tool Agent
File: agents/tool_agent.py

Step 5: Test It
Update app.py

Lesson 4.2 – Parameter Extraction Agent (Inside ToolAgent)

Step 1 – Create the Parameter Model
models/parameter_model.py


Step 2 – Create the Prompt
prompts/parameter_extractor.py

Step 3 – Create the Extractor
agents/parameter_extractor.py

Step 4 – Update ToolAgent
agents/tool_agent.py.

Step 5 – Test
Update app.py.

Lesson 4.3 – Execute the Tool
Step 1 – Verify executor.py

Step 2 – Verify registry.py

Step 3 – Update ToolAgent
Modify agents/tool_agent.py.

Step 4 – Test in app.py

Lesson 4.4 – AI Response Generator

Step 1 – Create the Prompt
prompts/tool_response.py

Step 2 – Create the Response Generator
agents/response_generator.py

Step 3 – Update ToolAgent
Modify agents/tool_agent.py


Step 4 – Update app.py
----------------------------------------------------------------------------------------

Lesson-5: Retrieval_Augmented Generation (Rag)

---------------------------------------------------------------------------------
lesson 5.1: Load PDF & Split into Chunks

Step 1 — Create a New Folder
data/constrcutin.pdf
rag/__init__.py, loader.py, splitter.py

Step 2 — rag/loader.py

Step 3 — Test the Loader
Create a temporary file: test_loader.py

Step 4 — Inspect One Document
print(documents[0])

Step 5 — Create the Splitter
rag/splitter.py

Step 6 — Test the Splitter
test_splitter.py

Step 7 — Inspect a Chunk
print(chunks[0].page_content)

Step 8 — Inspect Metadata
print(chunks[0].metadata)


Lesson 5.2: Embeddings
Step 1 — Create embeddings.py
rag/embeddings.py

Step 2 — Test It
test_embeddings.py

Lesson 5.3 : ChromaDB (Vector Database)
Step 1 - rag/
    vector_store.py  ## This does three things: Chunks -> Embeddings -> Store in Chroma

Step 2 — Create the Database
vector_db/build_vector_db.py


Lesson 5.4 – Retriever (Semantic Search)
Step 1 — Create rag/retriever.py

Step 2 — Test It
test_retriever.py


Lesson 5.5 – Build the RAG Agent

Step 1 – Create the Prompt
prompts/rag.py

