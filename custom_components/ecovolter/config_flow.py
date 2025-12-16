from homeassistant import config_entries
import voluptuous as vol

from .const import DOMAIN
from .api import EcoVolterApi


class EcoVolterConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for EcoVolter."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}

        if user_input is not None:
            # Test connection k wallboxu
            api = EcoVolterApi(user_input["host"], user_input.get("port", 80))
            connected = await api.async_test_connection()
            if not connected:
                errors["host"] = "cannot_connect"
                # Zobrazíme formulář znovu s chybou
                schema = vol.Schema(
                    {
                        vol.Required("host"): str,
                        vol.Optional("port", default=80): int,
                    }
                )
                return self.async_show_form(
                    step_id="user",
                    data_schema=schema,
                    errors=errors,
                )

            # Pokud je spojení OK, vytvoříme entry
            return self.async_create_entry(
                title=f"EcoVolter ({user_input['host']})",
                data=user_input,
            )

        # První zobrazení formuláře
        schema = vol.Schema(
            {
                vol.Required("host"): str,
                vol.Optional("port", default=80): int,
            }
        )

        return self.async_show_form(
            step_id="user",
            data_schema=schema,
            errors=errors,
        )
