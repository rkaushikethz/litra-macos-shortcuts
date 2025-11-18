'''
# Logitech Litra Glow macOS Shortcuts Controller

**Author:** RKaushik  
**License:** MIT

This command-line tool allows you to control your Logitech Litra Glow light on macOS and integrate it with the Shortcuts app for easy automation.

## Features

- Turn the Litra Glow on and off
- Set brightness in lumens or percentage
- Set color temperature in Kelvin
- Get the current status of the device
- Designed for seamless integration with macOS Shortcuts

## Prerequisites

- macOS 10.15 (Catalina) or higher
- Python 3 (usually pre-installed on macOS)
- Logitech Litra Glow connected via USB

## Installation

1.  **Install Dependencies:**

    Open the Terminal app and run the following command to install the required `hidapi` library:

    ```bash
    pip3 install hidapi
    ```

2.  **Clone the Repository:**

    ```bash
    git clone https://github.com/rkaushikethz/litra-macos-shortcuts.git
    cd litra-macos-shortcuts
    ```

3.  **Install the CLI Tool:**

    Run the following command to make the script executable and create a symbolic link in `/usr/local/bin` for easy access from anywhere:

    ```bash
    chmod +x litra_control.py
    sudo ln -s "$(pwd)/litra_control.py" /usr/local/bin/litra-control
    ```

4.  **Verify Installation:**

    Test that the tool is working by running:

    ```bash
    litra-control status
    ```

    If your Litra Glow is connected, you should see its current status.

## Usage

### Command-Line

- **Turn On:** `litra-control on`
- **Turn Off:** `litra-control off`
- **Toggle:** `litra-control toggle`
- **Set Brightness (Lumens):** `litra-control brightness 150`
- **Set Brightness (Percentage):** `litra-control brightness 75 -p`
- **Set Temperature:** `litra-control temperature 4500`
- **Get Status:** `litra-control status`
- **List Devices:** `litra-control list`

### macOS Shortcuts Integration

You can control your Litra Glow from the Shortcuts app by using the "Run Shell Script" action.

**Example: Create a "Turn On Litra" Shortcut**

1.  Open the **Shortcuts** app.
2.  Create a new shortcut.
3.  Add the **Run Shell Script** action.
4.  In the script box, enter:

    ```
    /usr/local/bin/litra-control on
    ```

5.  Save the shortcut with a name like "Turn On Litra". You can now run this shortcut with Siri or from the Shortcuts widget.

For more detailed instructions, see the [Shortcuts Guide](./docs/SHORTCUTS_GUIDE.md).

## Troubleshooting

- **Device Not Found:** Ensure your Litra Glow is securely connected to a USB port. Try a different port if necessary. Run `litra-control list` to see if the device is detected.
- **Permission Denied:** If you get a permission error when running `litra-control`, make sure you have made the script executable (`chmod +x litra_control.py`).

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
'''
