import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain.agents import initialize_agent, AgentType

# Load environment variables from .env file
load_dotenv()


# -------------------------------
# Step 1: Create a Tool
# -------------------------------
# @tool converts a normal Python function into a LangChain tool
@tool
def multiply(a: int, b: int) -> int:
    """
    Multiply two numbers.
    This description helps the agent understand when to use this tool.
    """
    return a * b


# -------------------------------
# Step 2: Create LLM
# -------------------------------
# Using OpenRouter as OpenAI-compatible provider
llm = ChatOpenAI(
    model="openai/gpt-4o-mini",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url=os.getenv("OPENROUTER_BASE_URL")
)


# -------------------------------
# Step 3: Register Tools
# -------------------------------
# Agent gets access to tools through this list
tools = [multiply]


# -------------------------------
# Step 4: Create Agent
# -------------------------------
# ZERO_SHOT_REACT_DESCRIPTION means:
# - Agent uses tool descriptions
# - Agent reasons before acting
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True   # Shows internal reasoning steps
)


# -------------------------------
# Step 5: Ask Agent
# -------------------------------
# Agent decides whether tool is needed
response = agent.invoke(
    "What is 25 multiplied by 4?"
)


# -------------------------------
# Step 6: Print Final Response
# -------------------------------
print(response)