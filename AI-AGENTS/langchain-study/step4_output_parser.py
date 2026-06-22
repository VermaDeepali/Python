import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatOpenAI(
    model="openai/gpt-4o-mini",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url=os.getenv("OPENROUTER_BASE_URL")
)

prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple words"
)

parser = StrOutputParser()

chain = prompt | llm | parser

response = chain.invoke({
    "topic": "Node.js Event Loop"
})

print(response)

# cmd to run --> python step4_output_parser.py