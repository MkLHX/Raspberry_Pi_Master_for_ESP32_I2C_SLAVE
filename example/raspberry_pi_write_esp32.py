from Adafruit_PureIO.smbus import SMBus  # pip install adafruit-blinka
from Raspberry_Pi_Master_for_ESP32_I2C_SLAVE.packer import Packer
from Raspberry_Pi_Master_for_ESP32_I2C_SLAVE.unpacker import Unpacker
import time


slave_address = 0x04  # slave address is 4
register = 0x01  # register to write is 0x01
value = 0x04


def write_from_rpi_to_esp32():
    try:
        # change 1 of SMBus(1) to bus number on your RPI
        smbus = SMBus(1)
        # prepare the data
        packed = None
        with Packer() as packer:
            packer.write(register)
            packer.write(value)
            packer.end()
            packed = packer.read()
        smbus.write_bytes(register, bytearray(packed))
    except Exception as e:
        print("ERROR: {}".format(e))
