import asyncio

from fastmcp.client.client import Client # Corrected import

async def main():
    # Initialize the client
    # The client library is designed to handle session IDs automatically.
    client = Client("http://127.0.0.1:8000/mcp/")

    try:
        # Use the client as an asynchronous context manager
        async with client: # <-- ADDED THIS LINE
            # Call the 'add' tool
            result = await client.call_tool(name="add", arguments={"a": 5, "b": 3})
            print(f"Result of add(5, 3): {result.data}")

            # Call another tool
            result_sub = await client.call_tool(name="subtract", arguments={"a": 10, "b": 4})
            print(f"Result of subtract(10, 4): {result_sub.data}")

            # Test division by zero
            # This should raise an exception on the client side if the server returns an error
            result_div_zero = await client.call_tool(name="divide", arguments={"a": 10, "b": 0})
            print(f"Result of divide(10, 0): {result_div_zero.data}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # client.close() is handled by the async with block's __aexit__
        # but if you had logic that could run outside the 'async with',
        # explicitly calling client.close() might be needed there.
        # For this simple script, the 'async with' handles cleanup.
        pass

if __name__ == "__main__":
    asyncio.run(main())