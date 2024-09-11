import aiohttp
import asyncio
from datetime import timedelta
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.event import async_track_time_interval
from homeassistant.helpers.network import get_url

from .const import DOMAIN, PRUSA_CONNECT_API_URL

async def initialize_integration(hass: HomeAssistant, config):
    instance_url = get_url(hass)
    camera_entity_id = config.get("camera_entity_id")
    upload_interval = config.get("upload_interval")
    api_token = config.get("api_token")
    camera_id = config.get("camera_id")

    session = async_get_clientsession(hass)

    async def upload_image_to_prusa_connect():
        """Capture an image from the camera and upload it to Prusa Connect."""
        state = hass.states.get(camera_entity_id)
        if state is None:
            print("Invalid camera entity ID.")
            return
        
        if api_token is None or camera_id is None:
            print("API config values are not set.")
            return

        image_url = f"{instance_url}{state.attributes['entity_picture']}"
        
        try:
            async with session.get(image_url) as response:
                if response.status != 200:
                    print(f"Failed to fetch image from camera: {response.status}")
                    return
                
                image_data = await response.read()
                
                headers = {
                    "token": api_token,
                    "fingerprint": camera_id,
                    "Content-Type": "image/jpg",
                    "Content-Length": str(len(image_data))
                }
                
                async with session.put(PRUSA_CONNECT_API_URL, headers=headers, data=image_data) as upload_response:
                    if upload_response.status == 200:
                        response_text = await upload_response.text()
                        print(f"Image uploaded successfully to Prusa Connect: {upload_response.status} - {response_text}")
                    else:
                        error_text = await upload_response.text()
                        print(f"Failed to upload image: {upload_response.status} - {error_text}")

        except aiohttp.ClientError as e:
            print(f"Error uploading image to Prusa Connect: {e}")

    async def periodic_upload():
        """Wrapper to schedule periodic upload."""
        while True:
            await upload_image_to_prusa_connect()
            await asyncio.sleep(upload_interval)

    # Schedule periodic upload if validation passes
    hass.loop.create_task(periodic_upload())

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the integration using YAML configuration."""
    if DOMAIN not in config:
        return True
    await initialize_integration(hass, config[DOMAIN])
    return True

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry):
    """Set up the integration using UI config entry."""
    await initialize_integration(hass, config_entry.data)
    return True

