import asyncio
from dedalus_labs import AsyncDedalus, DedalusRunner
from dotenv import load_dotenv

load_dotenv()


async def main():
    # Initialize Dedalus client
    # Set DEDALUS_API_KEY in your environment first
    client = AsyncDedalus()

    # Create a runner
    runner = DedalusRunner(client)

    # Connect to your MCP server by its slug: dlopezvsr/mcp-playground
    response = await runner.run(
        input="What tools are available?",  # Your query
        model="openai/gpt-4o",  # Choose your LLM
        mcp_servers=["dlopezvsr/mcp-playground"],  # ← Your server!
    )

    print("Response:", response.final_output)


if __name__ == "__main__":
    # First, install the SDK:
    # pip install dedalus-labs

    # Then set your API key:
    # export DEDALUS_API_KEY="your-api-key-here"
    # Get it from: https://dedaluslabs.ai

    asyncio.run(main())
