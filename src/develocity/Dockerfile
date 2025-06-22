# Dockerfile
# Use an official Python runtime as a parent image
FROM python:3.12-slim-bookworm

# Install uv using the official distroless image.
# Pinning to a specific version (e.g., :0.6.11) is recommended for reproducibility.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set build arguments for environment variables
ARG DEVELOCITY_API_KEY
ARG DEVELOCITY_URL

# Set environment variables in the container
ENV DEVELOCITY_API_KEY=$DEVELOCITY_API_KEY
ENV DEVELOCITY_URL=$DEVELOCITY_URL

# Set the working directory in the container
WORKDIR /app

# Copy the dependency definition
COPY pyproject.toml .
COPY uv.lock ./

# Install dependencies using uv sync.
# Leverages Docker layer caching via --mount=type=cache.
# --frozen ensures installs match the lock file (if provided and copied). Remove if no lock file.
# --no-install-project skips installing the local project code in this layer, optimizing caching.
# NOTE: This command relies on 'pyproject.toml' correctly listing dependencies, including 'mcp'.
# Ensure the 'mcp' package is resolvable based on your project setup (see pyproject.toml notes).
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project


# Copy the application code
COPY develocitymcp.py .

# Install the project itself using uv sync.
# This step makes your 'shellserver' project available in the environment managed by uv.
# Use --frozen if you have a lock file copied.
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen

# Run the server
CMD ["uv", "run", "develocitymcp.py"] 