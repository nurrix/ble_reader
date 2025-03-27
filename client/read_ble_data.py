import asyncio
from bleak import BleakScanner, BleakClient

async def scan_ble_devices():
    """Scan for nearby BLE devices."""
    devices = await BleakScanner.discover()
    for device in devices:
        print(f"Found device: {device.name} - {device.address}")

async def read_ble_characteristic(address, characteristic_uuid):
    """Connect to a BLE device and read a characteristic."""
    async with BleakClient(address) as client:
        if await client.is_connected():
            print(f"Connected to {address}")
            value = await client.read_gatt_char(characteristic_uuid)
            print(f"Characteristic Value: {value}")

async def main():
    # Scan for devices
    await scan_ble_devices()
    
    # Replace with your device's MAC address (Linux/macOS) or UUID (Windows)
    device_address = "XX:XX:XX:XX:XX:XX"  # Change this
    characteristic_uuid = "12345678-1234-5678-1234-56789abcdef0"  # Change to your characteristic UUID
    
    # Read characteristic
    await read_ble_characteristic(device_address, characteristic_uuid)

# Run the program
asyncio.run(main())
