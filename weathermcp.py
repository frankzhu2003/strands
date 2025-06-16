import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("WeatherMCP")

@mcp.tool()
def get_weather(latitude: float, longitude: float) -> str:
    """
    Get weather information for a given latitude and longitude using the US National Weather Service API.
    """
    points_url = f"https://api.weather.gov/points/{latitude},{longitude}"
    headers = {"User-Agent": "WeatherMCP/1.0"}
    try:
        points_resp = httpx.get(points_url, headers=headers, timeout=10)
        points_resp.raise_for_status()
        points_data = points_resp.json()
        forecast_url = points_data["properties"].get("forecast")
        if not forecast_url:
            return "Forecast URL not found in API response."
        forecast_resp = httpx.get(forecast_url, headers=headers, timeout=10)
        forecast_resp.raise_for_status()
        forecast_data = forecast_resp.json()
        periods = forecast_data["properties"].get("periods", [])
        if not periods:
            return "No forecast periods found."
        next_period = periods[0]
        return f"Weather for {next_period['name']}: {next_period['detailedForecast']}"
    except Exception as e:
        return f"Error fetching weather: {e}"

if __name__ == "__main__":
    mcp.run()
