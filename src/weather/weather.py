import requests
from strands import Agent, tool
from strands.models.ollama import OllamaModel

@tool(
    name="get_weather",
    description="Get weather information for a given latitude and longitude using the US National Weather Service API.",
    inputSchema={
        "latitude": {"type": "number", "description": "Latitude of the location"},
        "longitude": {"type": "number", "description": "Longitude of the location"}
    }
)
def get_weather(latitude: float, longitude: float) -> str:
    """
    Fetches weather forecast from api.weather.gov for the given latitude and longitude.
    """
    # Step 1: Get the gridpoint office and grid X/Y
    points_url = f"https://api.weather.gov/points/{latitude},{longitude}"
    points_resp = requests.get(points_url, headers={"User-Agent": "StrandsWeatherAgent/1.0"})
    if points_resp.status_code != 200:
        return f"Failed to get grid info: {points_resp.text}"
    points_data = points_resp.json()
    forecast_url = points_data["properties"].get("forecast")
    if not forecast_url:
        return "Forecast URL not found in API response."
    # Step 2: Get the forecast
    forecast_resp = requests.get(forecast_url, headers={"User-Agent": "StrandsWeatherAgent/1.0"})
    if forecast_resp.status_code != 200:
        return f"Failed to get forecast: {forecast_resp.text}"
    forecast_data = forecast_resp.json()
    periods = forecast_data["properties"].get("periods", [])
    if not periods:
        return "No forecast periods found."
    # Return a summary of the next period
    next_period = periods[0]
    return f"Weather for {next_period['name']}: {next_period['detailedForecast']}"


# Create an Ollama model instance
ollama_model = OllamaModel(
    host="http://localhost:11434",  # Ollama server address
    model_id="qwen3:latest"         # Specify the model
)
# Create the agent and register the tool
agent = Agent(
    model=ollama_model, 
    tools=[get_weather],
    system_prompt="You are a helpful weather assistant. Use the get_weather tool to provide weather information based on latitude and longitude."
)



if __name__ == "__main__":
    # Example usage
    # lat = 38.8977  # Example: White House
    # lon = -77.0365
    print(agent(f"What is the weather at Atlanta, GA?"))
