"""
Utility functions for Litra Glow control

Author: RKaushik
License: MIT
"""

from typing import Tuple


def validate_brightness(brightness: int, min_val: int = 20, max_val: int = 250) -> Tuple[bool, str]:
    """
    Validate brightness value.
    
    Args:
        brightness: Brightness value to validate
        min_val: Minimum allowed brightness
        max_val: Maximum allowed brightness
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not isinstance(brightness, int):
        return False, f"Brightness must be an integer, got {type(brightness).__name__}"
    
    if brightness < min_val or brightness > max_val:
        return False, f"Brightness must be between {min_val} and {max_val} lumens"
    
    return True, ""


def validate_temperature(temperature: int, min_val: int = 2700, max_val: int = 6500) -> Tuple[bool, str]:
    """
    Validate temperature value.
    
    Args:
        temperature: Temperature value to validate
        min_val: Minimum allowed temperature
        max_val: Maximum allowed temperature
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not isinstance(temperature, int):
        return False, f"Temperature must be an integer, got {type(temperature).__name__}"
    
    if temperature < min_val or temperature > max_val:
        return False, f"Temperature must be between {min_val}K and {max_val}K"
    
    if temperature % 100 != 0:
        return False, f"Temperature must be a multiple of 100 (e.g., 2700, 2800, ...)"
    
    return True, ""


def percentage_to_lumen(percentage: int, min_lumen: int = 20, max_lumen: int = 250) -> int:
    """
    Convert brightness percentage to lumens.
    
    Args:
        percentage: Brightness percentage (0-100)
        min_lumen: Minimum brightness in lumens
        max_lumen: Maximum brightness in lumens
        
    Returns:
        Brightness in lumens
    """
    if percentage < 0:
        percentage = 0
    elif percentage > 100:
        percentage = 100
    
    lumen_range = max_lumen - min_lumen
    return min_lumen + int((percentage / 100.0) * lumen_range)


def lumen_to_percentage(lumen: int, min_lumen: int = 20, max_lumen: int = 250) -> int:
    """
    Convert brightness lumens to percentage.
    
    Args:
        lumen: Brightness in lumens
        min_lumen: Minimum brightness in lumens
        max_lumen: Maximum brightness in lumens
        
    Returns:
        Brightness percentage (0-100)
    """
    if lumen < min_lumen:
        return 0
    elif lumen > max_lumen:
        return 100
    
    lumen_range = max_lumen - min_lumen
    return int(((lumen - min_lumen) / lumen_range) * 100)


def format_status(status: dict) -> str:
    """
    Format status dictionary as human-readable string.
    
    Args:
        status: Status dictionary from parse_status_response
        
    Returns:
        Formatted status string
    """
    if 'error' in status:
        return f"Error: {status['error']}"
    
    lines = [f"Power: {status['power'].upper()}"]
    
    if status.get('brightness_lumen'):
        brightness = status['brightness_lumen']
        percentage = lumen_to_percentage(brightness)
        lines.append(f"Brightness: {brightness} lumens ({percentage}%)")
    
    if status.get('temperature_kelvin'):
        lines.append(f"Temperature: {status['temperature_kelvin']}K")
    
    return "\n".join(lines)
