"""
Logitech Litra Glow USB HID Device Communication

Author: RKaushik
License: MIT
"""

import hid
from typing import Optional, List


class LitraDevice:
    """Represents a Logitech Litra Glow device connected via USB."""
    
    # Device identification
    VENDOR_ID = 0x046d
    PRODUCT_ID_GLOW = 0xc900
    USAGE_PAGE = 0xff43
    
    # Device specifications
    MIN_BRIGHTNESS_LUMEN = 20
    MAX_BRIGHTNESS_LUMEN = 250
    MIN_TEMPERATURE_KELVIN = 2700
    MAX_TEMPERATURE_KELVIN = 6500
    TEMPERATURE_STEP = 100
    
    def __init__(self, device_path: Optional[bytes] = None):
        """
        Initialize a Litra device connection.
        
        Args:
            device_path: Optional specific device path to connect to
        """
        self.device = None
        self.device_path = device_path
        
    def connect(self) -> bool:
        """
        Connect to a Litra Glow device.
        
        Returns:
            True if connection successful, False otherwise
        """
        try:
            if self.device_path:
                self.device = hid.Device(path=self.device_path)
            else:
                # Find and connect to first available Litra Glow
                self.device = hid.Device(self.VENDOR_ID, self.PRODUCT_ID_GLOW)
            
            return True
        except (IOError, OSError) as e:
            return False
    
    def disconnect(self):
        """Close the device connection."""
        if self.device:
            self.device.close()
            self.device = None
    
    def write(self, data: List[int]) -> bool:
        """
        Write data to the device.
        
        Args:
            data: List of bytes to write
            
        Returns:
            True if write successful, False otherwise
        """
        if not self.device:
            return False
        
        try:
            # Pad data to 20 bytes as required by the device
            padded_data = data + [0x00] * (20 - len(data))
            self.device.write(bytes(padded_data))
            return True
        except (IOError, OSError):
            return False
    
    def read(self, length: int = 20) -> Optional[List[int]]:
        """
        Read data from the device.
        
        Args:
            length: Number of bytes to read
            
        Returns:
            List of bytes read, or None if read failed
        """
        if not self.device:
            return None
        
        try:
            data = self.device.read(length, timeout=1000)
            return list(data) if data else None
        except (IOError, OSError):
            return None
    
    def __enter__(self):
        """Context manager entry."""
        self.connect()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.disconnect()


def find_litra_devices() -> List[dict]:
    """
    Find all connected Litra Glow devices.
    
    Returns:
        List of device info dictionaries
    """
    devices = []
    
    try:
        for device_info in hid.enumerate(LitraDevice.VENDOR_ID, LitraDevice.PRODUCT_ID_GLOW):
            if device_info.get('usage_page') == LitraDevice.USAGE_PAGE:
                devices.append({
                    'path': device_info['path'],
                    'serial_number': device_info.get('serial_number', 'Unknown'),
                    'manufacturer': device_info.get('manufacturer_string', 'Logitech'),
                    'product': device_info.get('product_string', 'Litra Glow')
                })
    except Exception:
        pass
    
    return devices


def get_device() -> Optional[LitraDevice]:
    """
    Get a connected Litra Glow device.
    
    Returns:
        LitraDevice instance if found and connected, None otherwise
    """
    device = LitraDevice()
    if device.connect():
        return device
    return None
