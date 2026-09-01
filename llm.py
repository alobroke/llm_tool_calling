import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()



HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

if not HUGGINGFACEHUB_API_TOKEN:
    raise ValueError("HUGGINGFACEHUB_API_TOKEN not found in .env")

MODEL_NAME = "Qwen/Qwen3-32B"

client = InferenceClient(
    api_key=HUGGINGFACEHUB_API_TOKEN
)




def call_llm(messages, tools=None):

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        tools=tools if tools else None,
        tool_choice="auto" if tools else None,
        temperature=0.5,
        max_tokens=1500
    )

    return response.choices[0].message