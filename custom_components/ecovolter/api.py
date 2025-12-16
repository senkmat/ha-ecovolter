import aiohttp
import asyncio


class EcoVolterApi:
    """Simple API client for EcoVolter."""

    def __init__(self, host: str, port: int = 80):
        self.host = host
        self.port = port

    async def async_test_connection(self) -> bool:
        """Test if EcoVolter is reachable."""
        url = f"http://{self.host}:{self.port}/"

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, timeout=5) as response:
                    return response.status == 200
        except (asyncio.TimeoutError, aiohttp.ClientError):
            return False
