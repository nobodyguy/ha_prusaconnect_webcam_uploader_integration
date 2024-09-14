# PrusaConnect Webcam Uploader

The **PrusaConnect Webcam Uploader** integration for Home Assistant allows you to periodically upload images from a configured Home Assistant Camera entity to Prusa Connect.

## Features

- Uploads images from a Home Assistant Camera entity to Prusa Connect at a configurable interval.
- Easy configuration through the Home Assistant user interface.

## Installation

1. Install [HACS](https://hacs.xyz/) (Home Assistant Community Store) if you haven't already.
2. Add this repository to HACS as a custom repository:
   - Go to **HACS** > **Integrations**.
   - Click on the three dots in the upper-right corner and select **Custom repositories**.
   - Enter the URL: `https://github.com/nobodyguy/ha_prusaconnect_webcam_uploader_integration`.
   - Choose **Integration** as the category.
3. Search for **PrusaConnect Webcam Uploader** in HACS and install the integration.
4. Restart Home Assistant.

Alternatively, you can manually copy the `prusaconnect_webcam_uploader` folder to your `custom_components` directory.

## Configuration
Click on the button below.

[![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=prusaconnect_webcam_uploader)

Or configure the integration manually:

1. Go to **Configuration** > **Integrations** in Home Assistant.
2. Click on the **Add Integration** button.
3. Search for **PrusaConnect Webcam Uploader** and click on it to configure.
4. Fill in the configuration parameters.

### Configuration Parameters

| Parameter          | Type   | Required | Default                                | Description                                                                 |
|--------------------|--------|----------|----------------------------------------|-----------------------------------------------------------------------------|
| `camera_entity_id` | string | Yes      | N/A                                    | The entity ID of the Home Assistant Camera entity to use for image capture. |
| `upload_interval`  | int    | Yes      | 60                                     | The interval in seconds at which images will be uploaded.                  |
| `api_token`        | string | Yes      | N/A                                    | Your Camera API token obtained from your printer's Camera tab on https://connect.prusa3d.com/.                                               |
| `camera_id`        | string | Yes      | Randomly generated UUID | A unique Camera fingerprint used for Prusa Connect Camera API.                       |

## Usage

After configuring the integration, the images from the selected camera entity will be automatically uploaded to Prusa Connect at the specified interval. You can monitor the upload status in the Home Assistant log.

## Issues

If you encounter any issues or have feature requests, please open an issue on the [GitHub repository](https://github.com/username/ha_prusaconnect_webcam_uploader_integration/issues).

## Contributing

Contributions are welcome! Please open a pull request with any changes or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.


## TODO
* Resize image (max 16MB)
* Options Flow - https://developers.home-assistant.io/docs/config_entries_options_flow_handler
* Configurable PrusaLink enum sensor that should trigger snapshoting - https://developers.home-assistant.io/docs/integration_listen_events
