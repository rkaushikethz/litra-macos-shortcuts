"""
Logitech Litra Glow Control Library

Author: RKaushik
License: MIT
"""

from .device import LitraDevice, find_litra_devices, get_device
from .commands import (
    turn_on_command,
    turn_off_command,
    get_status_command,
    set_brightness_command,
    set_temperature_command,
    parse_status_response
)
from .utils import (
    validate_brightness,
    validate_temperature,
    percentage_to_lumen,
    lumen_to_percentage,
    format_status
)

__version__ = "1.0.0"
__author__ = "RKaushik"
__all__ = [
    'LitraDevice',
    'find_litra_devices',
    'get_device',
    'turn_on_command',
    'turn_off_command',
    'get_status_command',
    'set_brightness_command',
    'set_temperature_command',
    'parse_status_response',
    'validate_brightness',
    'validate_temperature',
    'percentage_to_lumen',
    'lumen_to_percentage',
    'format_status'
]
