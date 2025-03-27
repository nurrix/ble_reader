import asyncio
from bleak import BleakScanner


async def scan_ble_devices():
    """Scan for nearby BLE devices and list their addresses."""
    print("Scanning for BLE devices...")
    devices = await BleakScanner.discover()

    for device in [d for d in devices if d.name]:
        print(f"Device: {device.name} | Address: {device.address}")


# Run the scanner
asyncio.run(scan_ble_devices())
