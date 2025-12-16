"""EcoVolter integration."""

from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry

from .const import DOMAIN

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the EcoVolter component (YAML mode)."""
    # YAML setup není podporován
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up EcoVolter from a config entry."""
    hass.data.setdefault(DOMAIN, {})
    # Sem později vložíme API klienta
    return True
