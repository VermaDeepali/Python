import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load variables from .env
load_dotenv()

# Create model object
llm = ChatOpenAI(
    model="openai/gpt-4o-mini",   # or another model
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

# Send prompt to model
response = llm.invoke("Explain LangChain in simple words")

# Print response
print(response.content)


# cmd to run --> python step1_basic_llm.py