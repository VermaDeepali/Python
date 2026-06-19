from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load variables from .env
load_dotenv()

# Create model object
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.7
)

# Send prompt to model
response = llm.invoke("Explain LangChain in simple words")

# Print response
print(response.content)