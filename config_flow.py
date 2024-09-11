from homeassistant import config_entries
import voluptuous as vol
import uuid

from .const import DOMAIN, PRUSA_CONNECT_API_URL

CONFIG_SCHEMA = vol.Schema(
    {
        vol.Required("camera_entity_id"): str,
        vol.Required("upload_interval", default=60): int,
        vol.Required("api_token"): str,
        vol.Required("camera_id", default=str(uuid.uuid4())): str,
    }
)

class PrusaConnectConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for PrusaConnect Webcam Uploader."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            return self.async_create_entry(title="PrusaConnect Webcam Uploader", data=user_input)

        return self.async_show_form(step_id="user", data_schema=CONFIG_SCHEMA)
