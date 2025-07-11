import asyncio
import os
from langchain_ollama.chat_models import ChatOllama
from mcp_use import MCPAgent, MCPClient
from fastmcp.client.client import Client as FastMCPClient # Import the FastMCP client directly if needed for configuration

# Define the URL of your already running MCP server
MCP_SERVER_URL = "http://127.0.0.1:8000/mcp/"

async def main():
    # Configure the MCPClient to connect to your running server
    # The 'servers' key should point to existing server URLs.
    # Note: mcp_use's MCPClient is typically used when you *manage* the server's lifecycle
    # or have multiple servers. If you just need to connect to one pre-existing server,
    # you might alternatively use FastMCPClient directly as shown in your client.py.
    # However, for MCPAgent, mcp_use.MCPClient is the expected type.
    
    # We will configure it to connect to an external server.
    # The 'servers' key within MCPClient.from_dict is for existing URLs.
    config = {
        "mcpServers": {
            "calculator_server": { # A descriptive name for your server
                "url": MCP_SERVER_URL
            }
        }
    }
    client = MCPClient.from_dict(config) # This will connect to the specified URL
    
    # Initialize the Ollama LLM
    llm = ChatOllama(model="mistral", base_url="http://localhost:11434")
    
    # Wire the LLM to the client
    agent = MCPAgent(llm=llm, client=client, max_steps=20)

    # Give prompt to the agent
    print("Sending prompt to the agent...")
    result = await agent.run("I would like you to add number 4 with number 6")
    print("\n🔥 Result:", result)

    # Always clean up running MCP sessions
    await client.close_all_sessions()

if __name__ == "__main__":
    asyncio.run(main())