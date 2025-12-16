import aiohttp
import asyncio

class EcoVolterApi:
    """Simple API client for EcoVolter."""

    def __init__(self, host: str, port: int = 80):
        self.host = host
        self.port = port

    async def async_test_connection(self):
        """Test if the wallbox is reachable."""
        url = f"http://{self.host}:{self.port}/status"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, timeout=5) as resp:
                    if resp.status == 200:
                        return True
        except asyncio.TimeoutError:
            return False
        except Exception:
            return False
        return False
