import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()  # Load .env file

llm = ChatOpenAI(
    model="gpt-5",
    api_key=os.getenv("OPENAI_API_KEY")
)

response = llm.invoke("Tell me a joke")

print(response.content)


# in .env file add your OPENAI_API_KEY 
