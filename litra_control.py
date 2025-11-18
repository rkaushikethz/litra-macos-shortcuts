#!/usr/bin/env python3
"""
Logitech Litra Glow Command-Line Controller

Control your Logitech Litra Glow light from the command line,
designed for integration with macOS Shortcuts.

Author: RKaushik
License: MIT
"""

import sys
import argparse
from typing import Optional

from litra import (
    get_device,
    find_litra_devices,
    turn_on_command,
    turn_off_command,
    get_status_command,
    set_brightness_command,
    set_temperature_command,
    parse_status_response,
    validate_brightness,
    validate_temperature,
    percentage_to_lumen,
    format_status
)


# Exit codes
EXIT_SUCCESS = 0
EXIT_DEVICE_NOT_FOUND = 1
EXIT_INVALID_PARAMETER = 2
EXIT_COMMUNICATION_ERROR = 3


def cmd_on() -> int:
    """Turn the light on."""
    device = get_device()
    if not device:
        print("Error: Litra Glow device not found. Please check USB connection.", file=sys.stderr)
        return EXIT_DEVICE_NOT_FOUND
    
    try:
        with device:
            if device.write(turn_on_command()):
                print("Light turned ON")
                return EXIT_SUCCESS
            else:
                print("Error: Failed to send command to device", file=sys.stderr)
                return EXIT_COMMUNICATION_ERROR
    except Exception as e:
        print(f"Error: Communication failed - {e}", file=sys.stderr)
        return EXIT_COMMUNICATION_ERROR


def cmd_off() -> int:
    """Turn the light off."""
    device = get_device()
    if not device:
        print("Error: Litra Glow device not found. Please check USB connection.", file=sys.stderr)
        return EXIT_DEVICE_NOT_FOUND
    
    try:
        with device:
            if device.write(turn_off_command()):
                print("Light turned OFF")
                return EXIT_SUCCESS
            else:
                print("Error: Failed to send command to device", file=sys.stderr)
                return EXIT_COMMUNICATION_ERROR
    except Exception as e:
        print(f"Error: Communication failed - {e}", file=sys.stderr)
        return EXIT_COMMUNICATION_ERROR


def cmd_toggle() -> int:
    """Toggle the light on/off."""
    device = get_device()
    if not device:
        print("Error: Litra Glow device not found. Please check USB connection.", file=sys.stderr)
        return EXIT_DEVICE_NOT_FOUND
    
    try:
        with device:
            # Get current status
            if not device.write(get_status_command()):
                print("Error: Failed to get device status", file=sys.stderr)
                return EXIT_COMMUNICATION_ERROR
            
            response = device.read()
            if not response:
                print("Error: Failed to read device status", file=sys.stderr)
                return EXIT_COMMUNICATION_ERROR
            
            status = parse_status_response(response)
            if 'error' in status:
                print(f"Error: {status['error']}", file=sys.stderr)
                return EXIT_COMMUNICATION_ERROR
            
            # Toggle based on current state
            if status['power'] == 'on':
                command = turn_off_command()
                new_state = "OFF"
            else:
                command = turn_on_command()
                new_state = "ON"
            
            if device.write(command):
                print(f"Light toggled {new_state}")
                return EXIT_SUCCESS
            else:
                print("Error: Failed to send command to device", file=sys.stderr)
                return EXIT_COMMUNICATION_ERROR
    except Exception as e:
        print(f"Error: Communication failed - {e}", file=sys.stderr)
        return EXIT_COMMUNICATION_ERROR


def cmd_brightness(value: str, is_percentage: bool = False) -> int:
    """Set the brightness."""
    try:
        brightness_value = int(value)
    except ValueError:
        print(f"Error: Invalid brightness value '{value}'. Must be an integer.", file=sys.stderr)
        return EXIT_INVALID_PARAMETER
    
    # Convert percentage to lumens if needed
    if is_percentage:
        if brightness_value < 0 or brightness_value > 100:
            print("Error: Brightness percentage must be between 0 and 100", file=sys.stderr)
            return EXIT_INVALID_PARAMETER
        brightness_lumen = percentage_to_lumen(brightness_value)
        print(f"Setting brightness to {brightness_value}% ({brightness_lumen} lumens)")
    else:
        brightness_lumen = brightness_value
        is_valid, error_msg = validate_brightness(brightness_lumen)
        if not is_valid:
            print(f"Error: {error_msg}", file=sys.stderr)
            return EXIT_INVALID_PARAMETER
    
    device = get_device()
    if not device:
        print("Error: Litra Glow device not found. Please check USB connection.", file=sys.stderr)
        return EXIT_DEVICE_NOT_FOUND
    
    try:
        with device:
            if device.write(set_brightness_command(brightness_lumen)):
                print(f"Brightness set to {brightness_lumen} lumens")
                return EXIT_SUCCESS
            else:
                print("Error: Failed to send command to device", file=sys.stderr)
                return EXIT_COMMUNICATION_ERROR
    except Exception as e:
        print(f"Error: Communication failed - {e}", file=sys.stderr)
        return EXIT_COMMUNICATION_ERROR


def cmd_temperature(value: str) -> int:
    """Set the color temperature."""
    try:
        temperature = int(value)
    except ValueError:
        print(f"Error: Invalid temperature value '{value}'. Must be an integer.", file=sys.stderr)
        return EXIT_INVALID_PARAMETER
    
    is_valid, error_msg = validate_temperature(temperature)
    if not is_valid:
        print(f"Error: {error_msg}", file=sys.stderr)
        return EXIT_INVALID_PARAMETER
    
    device = get_device()
    if not device:
        print("Error: Litra Glow device not found. Please check USB connection.", file=sys.stderr)
        return EXIT_DEVICE_NOT_FOUND
    
    try:
        with device:
            if device.write(set_temperature_command(temperature)):
                print(f"Temperature set to {temperature}K")
                return EXIT_SUCCESS
            else:
                print("Error: Failed to send command to device", file=sys.stderr)
                return EXIT_COMMUNICATION_ERROR
    except Exception as e:
        print(f"Error: Communication failed - {e}", file=sys.stderr)
        return EXIT_COMMUNICATION_ERROR


def cmd_status() -> int:
    """Get the current device status."""
    device = get_device()
    if not device:
        print("Error: Litra Glow device not found. Please check USB connection.", file=sys.stderr)
        return EXIT_DEVICE_NOT_FOUND
    
    try:
        with device:
            if not device.write(get_status_command()):
                print("Error: Failed to send status request", file=sys.stderr)
                return EXIT_COMMUNICATION_ERROR
            
            response = device.read()
            if not response:
                print("Error: Failed to read device status", file=sys.stderr)
                return EXIT_COMMUNICATION_ERROR
            
            status = parse_status_response(response)
            print(format_status(status))
            return EXIT_SUCCESS
    except Exception as e:
        print(f"Error: Communication failed - {e}", file=sys.stderr)
        return EXIT_COMMUNICATION_ERROR


def cmd_list() -> int:
    """List all connected Litra devices."""
    devices = find_litra_devices()
    
    if not devices:
        print("No Litra Glow devices found")
        return EXIT_DEVICE_NOT_FOUND
    
    print(f"Found {len(devices)} Litra Glow device(s):")
    for i, device in enumerate(devices, 1):
        print(f"\n{i}. {device['product']}")
        print(f"   Manufacturer: {device['manufacturer']}")
        print(f"   Serial: {device['serial_number']}")
    
    return EXIT_SUCCESS


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="Control Logitech Litra Glow light from the command line",
        epilog="Author: RKaushik | License: MIT"
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Command to execute')
    
    # On command
    subparsers.add_parser('on', help='Turn the light on')
    
    # Off command
    subparsers.add_parser('off', help='Turn the light off')
    
    # Toggle command
    subparsers.add_parser('toggle', help='Toggle the light on/off')
    
    # Brightness command
    brightness_parser = subparsers.add_parser('brightness', help='Set brightness')
    brightness_parser.add_argument('value', help='Brightness value (20-250 lumens or 0-100%%)')
    brightness_parser.add_argument('-p', '--percentage', action='store_true',
                                   help='Interpret value as percentage (0-100)')
    
    # Temperature command
    temperature_parser = subparsers.add_parser('temperature', help='Set color temperature')
    temperature_parser.add_argument('value', help='Temperature in Kelvin (2700-6500, multiples of 100)')
    
    # Status command
    subparsers.add_parser('status', help='Get current device status')
    
    # List command
    subparsers.add_parser('list', help='List all connected Litra devices')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return EXIT_SUCCESS
    
    # Execute command
    if args.command == 'on':
        return cmd_on()
    elif args.command == 'off':
        return cmd_off()
    elif args.command == 'toggle':
        return cmd_toggle()
    elif args.command == 'brightness':
        return cmd_brightness(args.value, args.percentage)
    elif args.command == 'temperature':
        return cmd_temperature(args.value)
    elif args.command == 'status':
        return cmd_status()
    elif args.command == 'list':
        return cmd_list()
    else:
        parser.print_help()
        return EXIT_SUCCESS


if __name__ == '__main__':
    sys.exit(main())
