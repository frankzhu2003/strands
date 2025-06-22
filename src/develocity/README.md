# Develocity MCP Server

This directory contains the MCP server for interacting with the Develocity API.

## Docker

A `Dockerfile` is provided to run the server in a containerized environment.

### Prerequisites

- Docker installed and running.

### Building the Image

To build the Docker image, run the following command from the root of the `strands` project:

```sh
docker build --build-arg DEVELOCITY_API_KEY=<your_api_key> --build-arg DEVELOCITY_URL=<your_develocity_url> -t develocity-mcp-server -f src/develocity/Dockerfile src/develocity
```

### Running the Container

The server requires the `DEVELOCITY_URL` and `DEVELOCITY_API_KEY` environment variables to be set. You can pass them to the `docker run` command:

```sh
docker run -p 8000:8000 develocity-mcp-server
``` 