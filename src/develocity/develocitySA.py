from strands import Agent
from strands.models.ollama import OllamaModel

from mcp import stdio_client, StdioServerParameters
from strands.tools.mcp import MCPClient

import logging
import os
from dotenv import load_dotenv

# Enables Strands debug log level
logging.getLogger("strands").setLevel(logging.DEBUG)

# Sets the logging format and streams logs to stderr
logging.basicConfig(
    format="%(levelname)s | %(name)s | %(message)s",
    handlers=[logging.StreamHandler()]
)

# Load environment variables from .env file
load_dotenv()

GITHUB_PERSONAL_ACCESS_TOKEN = os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN")
 
GITHUB_REPO_NAME = os.getenv("GITHUB_REPO_NAME")

LastBuildId = ''
BuildDetail = ''

stdio_github_mcp_client = MCPClient(lambda: stdio_client(StdioServerParameters(command="docker", 
                                                                               args=["run", "-i", "--rm", 
                                                                                     "-e", "GITHUB_PERSONAL_ACCESS_TOKEN=" + GITHUB_PERSONAL_ACCESS_TOKEN,
                                                                                     "-e", "GITHUB_TOOLSETS=repos,issues", 
                                                                                     "ghcr.io/github/github-mcp-server"])))

stdio_mcp_client = MCPClient(lambda: stdio_client(StdioServerParameters(command="python", 
                                                                        args=["/Users/fzhu/gradle/ai/strands/src/develocity/develocitymcp.py"])))

# Create an Ollama model instance
ollama_model = OllamaModel(
    host="http://localhost:11434",  # Ollama server address
    model_id="qwen3:latest"         # Specify the model
)

SYSTEM_PROMPT = """
You are an expert in develocity builds. You are given a question and you need to answer it.
"""

with stdio_mcp_client:

    tools = stdio_mcp_client.list_tools_sync()
    # Create an agent using the Ollama model
    agent = Agent(model=ollama_model, tools=tools, system_prompt=SYSTEM_PROMPT)

    # Use the agent to list files
    use_agent = agent(f"get the last 1 build detail and return both the build id and the build detail in a structured format, e.g., 'ID: <id>\nDETAIL: <detail>'")
    print(use_agent)
    # Convert AgentResult to string to get the response content
    response_str = str(use_agent)
    lines = response_str.strip().split('\n')
    print(f"the lines are {lines}")
    
    capture_detail = False
    build_detail_lines = []
    for line in lines:
        if line.startswith('ID:'):
            LastBuildId = line.replace('ID:', '').strip()
        elif line.startswith('DETAIL:'):
            build_detail_lines.append(line.replace('DETAIL:', '').strip())
    BuildDetail = '\n'.join(build_detail_lines)
    print(f"the last build id is {LastBuildId}")
    print(f"the build detail is {BuildDetail}")


SYSTEM_PROMPT = """
You are an expert in Github. You are given a task and you need to complete it in the github repository {GITHUB_REPO_NAME}.
"""
with stdio_github_mcp_client:

    tools = stdio_github_mcp_client.list_tools_sync()
# Create an agent using the Ollama model
    agent = Agent(model=ollama_model, tools=tools, system_prompt=SYSTEM_PROMPT)

    # Use the agent to list files
    use_agent = agent(f"create a new issue in the github repository {GITHUB_REPO_NAME} with the LastBuildId {LastBuildId} as the title and the build detail {BuildDetail} as the body.")
    print(use_agent)
