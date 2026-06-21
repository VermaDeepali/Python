import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# LLM
llm = ChatOpenAI(
    model="openai/gpt-4o-mini",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url=os.getenv("OPENROUTER_BASE_URL")
)

# Prompt template
prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple words"
)

# Chain prompt -> llm
chain = prompt | llm

# Invoke chain
response = chain.invoke({
    "topic": "AWS Lambda"
})

print(response.content)

# cmd to run --> python step3_chain.py