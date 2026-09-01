# LLM Tool Calling Agent

A prototype **LLM Agent with Tool Use** built using **Qwen3-32B**, **LangChain**, and custom Python tools.

The project demonstrates how an LLM can understand a user's request, decide when a tool is required, call the appropriate tool, receive its result, and use that result to generate a final response.

## 🚀 Project Overview

Traditional LLMs can generate text but cannot directly interact with external systems or perform real-world actions.

This project extends an LLM with tools such as:

* 🌐 Web Search
* 📧 Email Drafting
* 📊 Data Visualization
* 🔍 File Search (Grep)

The goal is to demonstrate the basic architecture of a **tool-using LLM agent**.

## 🏗️ Architecture

```text
                  User Query
                      │
                      ▼
                 Qwen3-32B
                      │
               Tool Decision
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
     Web Search   Email Tool   Visualization
          │           │           │
          └───────────┼───────────┘
                      ▼
                 Tool Result
                      │
                      ▼
                 Qwen3-32B
                      │
                      ▼
                 Final Answer
```

## 🛠️ Tech Stack

* **LLM:** Qwen/Qwen3-32B
* **LLM Provider:** Hugging Face
* **Framework:** LangChain
* **Language:** Python
* **Visualization:** Pandas + Matplotlib
* **Web Search:** Tavily
* **Environment Management:** python-dotenv

## 📁 Project Structure

```text
llm_tool_calling/
│
├── main.py                 # Main application and tool-calling loop
├── llm.py                  # Qwen3-32B connection
├── tools.py                # Custom LangChain tools
│
├── outputs/
│   └── charts/             # Generated visualizations
│
├── .env                    # API keys (not committed)
├── .gitignore
├── requirements.txt
└── README.md
```

## 🔧 Available Tools

### 1. Web Search

Used when the user asks for current or real-time information.

Example:

```text
User: What are the latest AI developments today?
```

The LLM can call:

```text
web_search(query="latest AI developments today")
```

The search results are then returned to the LLM for generating the final response.

### 2. Email Tool

Used to create an email draft.

Example:

```text
User: Draft an email to my professor asking for an assignment extension.
```

The tool generates an email containing:

* Recipient
* Subject
* Body

For this prototype, the tool **creates a draft instead of actually sending an email**.

### 3. Data Visualization

Used to create charts from user-provided data.

Example:

```text
Create a bar chart showing monthly sales:
January ₹120,000
February ₹145,000
March ₹135,000
April ₹170,000
May ₹190,000
June ₹210,000
```

The generated chart is saved inside:

```text
outputs/charts/
```

### 4. Grep

Used to find text inside files in a directory.

Example:

```text
Find call_llm in the project files.
```

The tool searches files recursively and returns matching file paths, line numbers, and lines of text.

## 🔄 Tool Calling Workflow

The basic workflow is:

```text
1. User sends a query
        ↓
2. Qwen receives the query and available tool schemas
        ↓
3. Qwen determines whether a tool is required
        ↓
4. Qwen generates a tool call
        ↓
5. Python executes the selected tool
        ↓
6. Tool result is returned to Qwen
        ↓
7. Qwen generates the final response
```

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/alobroke/llm_tool_calling.git
cd llm_tool_calling
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file:

```env
HF_TOKEN=your_huggingface_token
TAVILY_API_KEY=your_tavily_api_key
```

**Never commit your `.env` file or expose your API keys.**

### 5. Run the project

```bash
python main.py
```

## 🧪 Example Queries

### Web Search

```text
What are the latest AI news today?
```

### Email

```text
Draft an email to my professor saying I will submit the assignment tomorrow.
```

### Visualization

```text
Create a bar chart for:
January 120
February 150
March 180
April 210
```

### Grep

```text
Find create_visualization in tools.py
```

## 🎯 Project Objective

The primary objective is to demonstrate **LLM Tool Calling** in a practical scenario.

The project focuses on:

* Connecting an open-source LLM to external tools
* Defining tools using LangChain's `@tool`
* Providing structured tool schemas to the LLM
* Executing the tool requested by the LLM
* Returning tool results to the LLM
* Generating a final response based on tool output

## 🔮 Future Improvements

Possible extensions include:

* Multi-tool chaining
* Better tool-selection logic
* Tool-use guardrails
* Error handling and retries
* Human approval before sensitive actions
* Memory
* LangGraph-based orchestration
* More external APIs

## 👥 Project

This project was developed as a prototype demonstrating **LLM Agents with Tool Use**.
