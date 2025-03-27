import asyncio
from typing import is_protocol
from bleak import BleakScanner, BleakClient


async def scan_ble_devices():
    """Scan for nearby BLE devices."""
    devices = await BleakScanner.discover()
    print("Found devices:")
    for i, device in enumerate([d for d in devices if d.name]):
        print(f"  {i}:{device.name} - {device.address}")
    return devices


async def read_ble_characteristic(address, characteristic_uuid):
    """Connect to a BLE device and read a characteristic."""
    async with BleakClient(address) as client:
        if client.is_connected:
            print(f"Connected to {address}")
            value = await client.read_gatt_char(characteristic_uuid)
            print(f"Characteristic Value: {value}")

            print(
                " Make loop that continuously reads data.. maybe in a different function because it will make your lives so much easier. Up to you tho"
            )


async def main():
    # Scan for devices
    divices = await scan_ble_devices()

    # Replace with your device's MAC address (Linux/macOS) or UUID (Windows)
    device_address = "94:B5:55:C7:C0:66"  # Change this
    characteristic_uuid = "abcdef01-1234-5678-1234-56789abcdef0"  # Change to your characteristic UUID

    assert device_address in [d.address for d in divices], "device not found"
    # Read characteristic
    await read_ble_characteristic(device_address, characteristic_uuid)


# Run the program
asyncio.run(main())
