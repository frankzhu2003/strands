import os
import httpx
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

import logging
# Enables Strands debug log level
logging.getLogger("develocitymcp").setLevel(logging.DEBUG)

# Sets the logging format and streams logs to stderr
logging.basicConfig(
    format="%(levelname)s | %(name)s | %(message)s",
    handlers=[logging.StreamHandler()]
)

# Load environment variables from .env file
load_dotenv()

DEVELOCITY_URL = os.getenv("DEVELOCITY_URL")
DEVELOCITY_API_KEY = os.getenv("DEVELOCITY_API_KEY")

mcp = FastMCP("DevelocityMCP")


def get_headers():
    return {
        "Authorization": f"Bearer {DEVELOCITY_API_KEY}",
        "Accept": "application/json"
    }

@mcp.tool()
def get_latest_builds(count: int ) -> str:
    """
    Get the latest N build IDs from the Develocity API.
    """
    try:
        url = f"{DEVELOCITY_URL}/api/builds?reverse=true&maxBuilds={count}"
        logging.info(f"Fetching builds from {url}")
        resp = httpx.get(url, headers=get_headers(), timeout=10)
        resp.raise_for_status()
        builds = resp.json()
        if not builds:
            return "No builds found."
        build_ids = [build.get("id") for build in builds if build.get("id")]
        return f"Latest {count} build IDs: {build_ids}"


    except Exception as e:
        return f"Error fetching build IDs: {e}"

@mcp.tool()
def get_build_detail_by_id(build_id: str) -> str:
    """
    Get build details by build ID from the Develocity API.
    """
    try:
        url = f"{DEVELOCITY_URL}/api/builds/{build_id}"
        resp = httpx.get(url, headers=get_headers(), timeout=10)
        resp.raise_for_status()
        build = resp.json()
        return f"Build details for {build_id}: {build}"
    except Exception as e:
        return f"Error fetching build details: {e}"

@mcp.tool()
def get_build_dependencies_by_id(build_id: str) -> str:
    """
    Get build dependencies by build ID from the Develocity API.
    """
    try:
        url = f"{DEVELOCITY_URL}/api/builds/{build_id}/gradle-dependencies"
        resp = httpx.get(url, headers=get_headers(), timeout=10)
        resp.raise_for_status()
        dependencies = resp.json()
        return f"Build dependencies for {build_id}: {dependencies}"
    except Exception as e:
        return f"Error fetching build dependencies: {e}"

@mcp.tool()
def get_build_attributes_by_id(build_id: str) -> str:
    """
    Get build attributes by build ID from the Develocity API.
    """
    try:
        url = f"{DEVELOCITY_URL}/api/builds/{build_id}/gradle-attributes"
        resp = httpx.get(url, headers=get_headers(), timeout=10)
        resp.raise_for_status()
        attributes = resp.json()
        return f"Build attributes for {build_id}: {attributes}"
    except Exception as e:
        return f"Error fetching build attributes: {e}"

if __name__ == "__main__":
    mcp.run()
