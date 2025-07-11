from calculator import Calculator
from fastmcp import FastMCP # Only import FastMCP

mcp = FastMCP("Calculator Server") # No explicit transport here, FastMCP will handle it

calc = Calculator()

@mcp.tool()
def add(a: int, b: int) -> int:
    return calc.add(a, b)

@mcp.tool()
def subtract(a: int, b: int) -> int:
    return calc.subtract(a, b)

@mcp.tool()
def multiply(a: int, b: int) -> int:
    return calc.multiply(a, b)

@mcp.tool()
def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return calc.divide(a, b)

if __name__ == "__main__":
    # Specify transport as a string "http" directly in the run method
    mcp.run(transport="http", host="127.0.0.1", port=8000)