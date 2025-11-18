
# Litra Glow USB Protocol Documentation

**Author:** RKaushik

This document outlines the reverse-engineered USB HID protocol for the Logitech Litra Glow.

## Device Information

- **Vendor ID:** `0x046d` (Logitech)
- **Product ID:** `0xc900` (Litra Glow)
- **Usage Page:** `0xff43`

## HID Commands

All commands are sent as a 20-byte HID report.

### Turn On

- **Command:** `[0x11, 0xff, 0x04, 0x1c, 0x01]`

### Turn Off

- **Command:** `[0x11, 0xff, 0x04, 0x1c, 0x00]`

### Get Status

- **Command:** `[0x11, 0xff, 0x04, 0x01]`
- **Response:** The device returns a 20-byte report. The power status is in byte 4 (1 for on, 0 for off).

### Set Brightness

- **Command:** `[0x11, 0xff, 0x04, 0x4c, <brightness_high>, <brightness_low>]`
- **Value:** The brightness is a 16-bit integer (big-endian) representing the lumen value (20-250).

### Set Temperature

- **Command:** `[0x11, 0xff, 0x04, 0x9c, <temp_high>, <temp_low>]`
- **Value:** The temperature is a 16-bit integer (big-endian) representing the Kelvin value (2700-6500).
