from langchain_core.tools import tool

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

result = multiply.invoke({
    "a": 10,
    "b": 5
})

print(result)

// output --> 50

# cmd to run --> python step5_tools.py