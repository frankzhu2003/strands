# Develocity MCP Server

This directory contains the MCP server for interacting with the Develocity API.

## Docker

A `Dockerfile` is provided to run the server in a containerized environment.

### Prerequisites

- Docker installed and running.

### Building the Image

To build the Docker image, run the following command from this directory:

```sh
docker build -t frankzhu2003/develocitymcp .
```
### Pushing the Image

```sh
docker push frankzhu2003/develocitymcp
```

### Running the Develocity MCP Server in Agentic AI 

The server requires the `DEVELOCITY_URL` and `DEVELOCITY_API_KEY` environment variables to be set. 

For Claude Desktop, update the Claude's `claude_desktop_config.json` file, e.g. /Users/fzhu/Library/Application Support/Claude/claude_desktop_config.json

```
{
  "mcpServers": {
    "develocitymcp": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e",
        "DEVELOCITY_API_KEY",
        "-e",
        "DEVELOCITY_URL",
        "frankzhu2003/develocitymcp"
      ],
      "env": {
        "DEVELOCITY_URL": "https://YOUR-develocity-url",
        "DEVELOCITY_API_KEY": "YOUR-develocity-api-key"
      }
    },
    "github": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e",
        "GITHUB_PERSONAL_ACCESS_TOKEN",
        "ghcr.io/github/github-mcp-server"
      ],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "YOUR-github-token"
      }
    }
  }
}
``` 
