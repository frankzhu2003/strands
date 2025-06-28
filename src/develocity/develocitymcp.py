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
def get_builds(max_builds: int, include_attributes: bool, include_dependencies: bool, from_build_id: str, advanced_query: str) -> str:
    """
    Get the latest N builds from the Develocity API.
    N has a limit of 10.
    When N is greater than 10, another call to this function should be made where 'from_build_id' is the build ID of the oldest build in the current set.
    This can be repeated until the desired number of builds is fetched.

    Included in the response is a list of builds.
    At the top level of each build is: id, available at, build tool type, build tool version, build agent version, and models.

    Additional build attributes can be included in the response by calling this function with "include_attributes" equal to "true".
    These attributes may vary between build tools, but will generally include information like: build start time, build duration, project name, requested tasks/goals/targets, build outcome (e.g., passed or failed), whether the failure was due to tests/compile/lint (verification), whether the failure was due to toolchain issues (non-verification), tags, custom values, Develocity settings, build tool-specific options, and details about the environment.
    If these additional build attributes aren't required, it's better to call with "include_attributes" equal to "false" for faster and smaller responses.
    Custom values and tags are user-defined data.
    Custom values are key-value pairs where tags are a simple value.
    Common custom values are (exactly as written in quotes): "Git branch", "Git commit id", "Git repository", "CI provider"
    Common tags are: either "CI" or "LOCAL", the Git branch, the OS (exactly "Linux", "Mac OS X", or "Windows*"), and whether the working directory had modifications (exactly "Dirty")

    The dependencies of a build can be included in the response by calling this function with "include_dependencies" equal to "true".
    A build dependency includes: namespace (i.e., "group"), name (i.e., "artifact"), version, and purl or "package URL" (e.g., "pkg:maven/{namespace}/{name}@{version}")
    If build dependencies aren't required, it's better to call with "include_dependencies" equal to "false" for faster and smaller responses.

    The API also supports an optional advanced query parameter.
    Each query can be made from one or more terms separated by spaces.
    Each term is a field name and search pattern: fieldName:pattern.
    For example, project:my-project, will include only build scans for my-project in the response.
    Terms can be combined using boolean "and" and "or" operators, and grouped using parentheses: user:dylan or (tag:CI and value:"Git branch=master")
    Terms can also be negated using "-": project:my-project -tag:local
    Another example: user:dylan or not (tag:CI and value:"Git branch=master")
    Supported fields are (exactly as written in quotes): "user", "project", "requested" (e.g., tasks/goals/targets), "buildTool", "value" (i.e., custom value), "tag"
    """
    try:
        url=f"{DEVELOCITY_URL}/api/builds?reverse=true&maxBuilds={max_builds}"
        if include_attributes:
            url=url + "&models=gradle-attributes&models=maven-attributes&models=bazel-attributes&models=npm-attributes&models=python-attributes&models=sbt-attributes"
        if include_dependencies:
            url=url + "&models=gradle-dependencies&models=maven-dependencies"
        if from_build_id:
            url=url + f"&fromBuild={from_build_id}"
        if advanced_query:
            url=url + f"&query={advanced_query}"
        logging.info(f"Fetching builds from {url}")
        resp = httpx.get(url, headers=get_headers(), timeout=10)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return f"Error fetching build IDs: {e}"

@mcp.tool()
def get_configured_repositories_for_build(build_id: str) -> list:
    """
    Get the configured repositories (e.g., Maven repositories) by build ID from the Develocity Export API.
    """
    try:
        url = f"{DEVELOCITY_URL}/build-export/v2/build/{build_id}/events?eventTypes=Repository"
        resp = httpx.get(url, headers=get_headers(), timeout=30)
        resp.raise_for_status()
        return resp.text
    except Exception as e:
        return [f"Error fetching build repository: {e}"]

@mcp.tool()
def get_failure_details_for_build(build_id: str) -> list:
    """
    Get the failure details by build ID from the Develocity Export API.
    """
    try:
        url = f"{DEVELOCITY_URL}/build-export/v2/build/{build_id}/events?eventTypes=ExceptionData"
        resp = httpx.get(url, headers=get_headers(), timeout=30)
        resp.raise_for_status()
        return resp.text
    except Exception as e:
        return [f"Error fetching build repository: {e}"]

if __name__ == "__main__":
    print("Starting Develocity MCP server")
    mcp.run()
