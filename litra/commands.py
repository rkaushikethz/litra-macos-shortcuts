"""
Logitech Litra Glow HID Command Generation

Author: RKaushik
License: MIT
"""

from typing import List


def turn_on_command() -> List[int]:
    """
    Generate command to turn the Litra Glow on.
    
    Returns:
        List of command bytes
    """
    return [0x11, 0xff, 0x04, 0x1c, 0x01]


def turn_off_command() -> List[int]:
    """
    Generate command to turn the Litra Glow off.
    
    Returns:
        List of command bytes
    """
    return [0x11, 0xff, 0x04, 0x1c, 0x00]


def get_status_command() -> List[int]:
    """
    Generate command to get the current device status.
    
    Returns:
        List of command bytes
    """
    return [0x11, 0xff, 0x04, 0x01]


def set_brightness_command(brightness_lumen: int) -> List[int]:
    """
    Generate command to set brightness in lumens.
    
    Args:
        brightness_lumen: Brightness value in lumens (20-250)
        
    Returns:
        List of command bytes
    """
    # Convert brightness to 16-bit big-endian
    brightness_high = (brightness_lumen >> 8) & 0xFF
    brightness_low = brightness_lumen & 0xFF
    
    return [0x11, 0xff, 0x04, 0x4c, brightness_high, brightness_low]


def set_temperature_command(temperature_kelvin: int) -> List[int]:
    """
    Generate command to set color temperature in Kelvin.
    
    Args:
        temperature_kelvin: Temperature value in Kelvin (2700-6500)
        
    Returns:
        List of command bytes
    """
    # Convert temperature to 16-bit big-endian
    temp_high = (temperature_kelvin >> 8) & 0xFF
    temp_low = temperature_kelvin & 0xFF
    
    return [0x11, 0xff, 0x04, 0x9c, temp_high, temp_low]


def parse_status_response(response: List[int]) -> dict:
    """
    Parse the status response from the device.
    
    Args:
        response: Raw response bytes from device
        
    Returns:
        Dictionary with status information
    """
    if not response or len(response) < 5:
        return {'error': 'Invalid response'}
    
    status = {
        'power': 'on' if response[4] == 1 else 'off',
        'brightness_lumen': None,
        'temperature_kelvin': None
    }
    
    # Parse brightness if available (bytes 5-6)
    if len(response) >= 7:
        brightness = (response[5] << 8) | response[6]
        if brightness > 0:
            status['brightness_lumen'] = brightness
    
    # Parse temperature if available (bytes 7-8)
    if len(response) >= 9:
        temperature = (response[7] << 8) | response[8]
        if temperature > 0:
            status['temperature_kelvin'] = temperature
    
    return status
