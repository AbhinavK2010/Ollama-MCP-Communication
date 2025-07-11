# Ollama-MCP-Communication
Linking Ollama, to a locally built MCP from scratch 

Project: Multi-Agent Communication Protocol (MCP) Calculator with Ollama Integration

Project Summary:
This project establishes a foundational implementation of a Multi-Agent Communication Protocol (MCP) server, designed from the ground up to expose a standard calculator's functionalities as callable tools. It further illustrates the seamless integration of a Large Language Model (LLM), specifically Ollama utilizing the Mistral model, to intelligently interpret natural language requests and execute these exposed MCP tools.

The primary objective is to demonstrate a robust and modular architecture for extending LLM capabilities through external tool invocation. This architectural separation offers several key advantages:
- Scalability: Independent operation of the LLM and tool server allows for distributed deployment and scaling.
- Modularity: New tools can be integrated into the MCP server without requiring modifications or retraining of the LLM.
- Enhanced Functionality: LLMs, while proficient in natural language understanding, benefit from external tools for precise computational tasks or specific interactions with external systems.

Project Components:
1.  calculator.py:
    - This file defines the Calculator class, which encapsulates fundamental arithmetic operations: add, subtract, multiply, and divide.
    - It serves as the core logic provider for the computational tools subsequently exposed by the MCP server.

2.  server.py:
    - This script functions as the MCP server application.
    - It leverages the FastMCP library to instantiate an MCP server, designated as "Calculator Server".
    - The add, subtract, multiply, and divide methods of the Calculator class are exposed as callable tools via the @mcp.tool() decorator.
    - The server is configured to operate over HTTP on http://127.0.0.1:8000.

3.  client.py:
    - This asynchronous client demonstrates direct programmatic interaction with the FastMCP server.
    - It illustrates the invocation of exposed tools (add, subtract, divide) and incorporates error handling for scenarios such as division by zero.
    - This client is valuable for independent verification of server functionality.

4.  olaama_client.py:
    - This component represents the core LLM integration.
    - It utilizes the langchain-ollama library to establish a connection with a local Ollama instance running the "mistral" model.
    - mcp_use.MCPAgent and mcp_use.MCPClient are employed to bridge the LLM with the MCP server.
    - The MCPAgent enables the LLM to intelligently select and invoke the calculator tools based on natural language prompts (e.g., "I would like you to add number 4 with number 6").
    - The configuration within olaama_client.py is set to connect to an MCP server assumed to be already operational at http://127.0.0.1:8000/mcp/.

Setup and Execution Guidelines:
To execute this project, Python 3.8 or a later version, along with pip, is required.

1.  Project File Placement:
    Ensure that all project files (calculator.py, server.py, client.py, olaama_client.py) are located within the same directory.

2.  Dependency Installation:
    The use of a Python virtual environment is strongly recommended to manage project dependencies.

    # Create a virtual environment
    python -m venv myenv

    # Activate the virtual environment
    # On macOS/Linux:
    source myenv/bin/activate
    # On Windows (Command Prompt):
    myenv\Scripts\activate
    # On Windows (PowerShell):
    myenv\Scripts\Activate.ps1

    # Install required Python packages
    pip install fastmcp langchain-ollama mcp-use

3.  Ollama Configuration:
    Verify that Ollama is installed and operational on your system. The "mistral" model must also be available.

    # Initiate the Ollama service (if not already active)
    ollama serve

    # Download the Mistral model
    ollama pull mistral

    Confirm that Ollama is listening on http://1
