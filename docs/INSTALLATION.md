
# Detailed Installation Guide

**Author:** RKaushik

This guide provides detailed step-by-step instructions for installing the Litra Glow macOS Shortcuts Controller.

## 1. Install Python 3

macOS comes with Python pre-installed. You can verify this by opening the Terminal app and running:

```bash
python3 --version
```

If you see a version number (e.g., `Python 3.9.6`), you are ready to proceed. If not, you can install Python from the official website: [python.org](https://www.python.org/downloads/macos/)

## 2. Install `hidapi`

The `hidapi` library is required for USB HID communication. Install it using `pip3`:

```bash
pip3 install hidapi
```

## 3. Clone the Repository

Clone this repository to your local machine using `git`:

```bash
git clone https://github.com/rkaushikethz/litra-macos-shortcuts.git
cd litra-macos-shortcuts
```

## 4. Make the Script Executable

Navigate to the repository directory and make the `litra_control.py` script executable:

```bash
chmod +x litra_control.py
```

## 5. Create a Symbolic Link

Create a symbolic link to the script in `/usr/local/bin` to make it accessible from anywhere in the terminal:

```bash
sudo ln -s "$(pwd)/litra_control.py" /usr/local/bin/litra-control
```

You may be prompted to enter your password.

## 6. Verify the Installation

Connect your Litra Glow to your computer and run the following command:

```bash
litra-control status
```

If the installation was successful, you will see the current status of your Litra Glow.
