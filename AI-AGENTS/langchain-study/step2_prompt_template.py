from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

# Load .env variables
load_dotenv()

# Create Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",   # change if needed
    temperature=0.7
)

# Create prompt template
prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple words"
)

# Fill placeholder
formatted_prompt = prompt.invoke({
    "topic": "Vector Databases"
})

# Send prompt to Gemini
response = llm.invoke(formatted_prompt)

# Print response
print(response.content)


# python step2_prompt_template.py