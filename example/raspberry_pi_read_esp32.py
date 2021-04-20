from Adafruit_PureIO.smbus import SMBus  # pip install adafruit-blinka
from Raspberry_Pi_Master_for_ESP32_I2C_SLAVE.packer import Packer
from Raspberry_Pi_Master_for_ESP32_I2C_SLAVE.unpacker import Unpacker
import time


slave_address = 0x04  # slave address is 4
register = 0x01  # register to read is 0x01


def read_from_rpi_to_esp32():
    try:
        smbus = SMBus(1)
        # prepare the data
        packed = None
        with Packer() as packer:
            packer.write(register)
            packer.end()
            packed = packer.read()

        # change 1 of SMBus(1) to bus number on your RPI
        raw_list = None
        smbus.write_bytes(register, bytearray(packed))
        time.sleep(0.3)  # wait i2c process the request
        raw_list = list(smbus.read_bytes(register, 5))  # the read_bytes contains the data format: first, length, data, crc8, end bytes
        print(raw_list)

        # let's clean received data
        unpacked = None
        with Unpacker as unpacker:
            unpacker.write(raw_list)
            unpacked = unpacker.read()

        return unpacked

    except Exception as e:
        print("ERROR: {}".format(e))
