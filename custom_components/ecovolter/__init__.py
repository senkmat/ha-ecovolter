"""EcoVolter integration."""

from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry

from .const import DOMAIN
from .api import EcoVolterApi


async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the EcoVolter component (YAML mode)."""
    # YAML setup není podporován
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up EcoVolter from a config entry."""

    hass.data.setdefault(DOMAIN, {})

    host = entry.data.get("host")
    port = entry.data.get("port", 80)

    # vytvoříme API klienta
    api = EcoVolterApi(host, port)
    hass.data[DOMAIN][entry.entry_id] = api

    # test spojení s wallboxem
    connected = await api.async_test_connection()
    if not connected:
        # pokud se nepodaří připojit, vyhodíme chybu, HA to zobrazí uživateli
        raise Exception(f"Cannot connect to EcoVolter at {host}:{port}")

    return True
