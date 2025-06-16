from strands import Agent
from strands.models.ollama import OllamaModel
from strands_tools import shell

from mcp import stdio_client, StdioServerParameters
from strands.tools.mcp import MCPClient

import logging

# Enables Strands debug log level
logging.getLogger("strands").setLevel(logging.DEBUG)

# Sets the logging format and streams logs to stderr
logging.basicConfig(
    format="%(levelname)s | %(name)s | %(message)s",
    handlers=[logging.StreamHandler()]
)

stdio_mcp_client = MCPClient(lambda: stdio_client(StdioServerParameters(command="python", args=["/Users/fzhu/gradle/ai/strands/develocitymcp.py"])))


# SYSTEM_PROMPT = """
# You are a highly skilled shell agent, designed to assist users with command-line interface (CLI) tasks on their operating system. You have access to a wide range of shell commands and tools, including ls, cd, mkdir, rm, find, grep, sed, awk, bash, python, and more.

# When a user requests a task, follow these steps:
# 1. Analyze the task and plan the necessary shell commands step-by-step.
# 2. If multiple commands are needed, outline the sequence clearly.
# 3. For potentially destructive commands (e.g., rm, mv), confirm with the user before proceeding.
# 4. If a task cannot be performed with shell commands, politely explain the limitations.

# Your goal is to help users complete CLI tasks efficiently and safely.
# """

SYSTEM_PROMPT = """
You are an expert in develocity builds. You are given a question and you need to answer it.
"""



# Create an Ollama model instance
ollama_model = OllamaModel(
    host="http://localhost:11434",  # Ollama server address
    model_id="qwen3:latest"         # Specify the model
)

with stdio_mcp_client:

    tools = stdio_mcp_client.list_tools_sync()
# Create an agent using the Ollama model
    agent = Agent(model=ollama_model, tools=tools, system_prompt=SYSTEM_PROMPT)

    # Use the agent to list files
    use_agent = agent("get the last 4 builds and retrieve each build detail using the build id retrieved one by one")
    print(use_agent)
