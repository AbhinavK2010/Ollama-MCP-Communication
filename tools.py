from fastmcp.server.registry import register
from mcp.tools.python_tool import PythonObjectTool
from calculator import Calculator

register(
    PythonObjectTool(
        name="calculator",
        object=Calculator()
    )
)
