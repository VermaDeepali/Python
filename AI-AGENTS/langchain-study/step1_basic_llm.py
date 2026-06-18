from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load variables from .env
load_dotenv()

# Create model object
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)

# Send prompt to model
response = llm.invoke("Explain LangChain in simple words")

# Print response
print(response.content)