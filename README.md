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

planner.py

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













