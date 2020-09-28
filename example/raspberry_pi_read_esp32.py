from Adafruit_PureIO.smbus import SMBus  # pip install adafruit-blinka
from Raspberry_Pi_Master_for_ESP32_I2C_SLAVE.packer import Packer
from Raspberry_Pi_Master_for_ESP32_I2C_SLAVE.unpacker import Unpacker
import time


slave_address = 0x04  # slave address is 4
register = 0x01  # register to read is 0x01


def read_from_rpi_to_esp32():
    try:
        # prepare the data
        with Packer() as packer:
            packer.write(register)
            packer.end()

        # change 1 of SMBus(1) to bus number on your RPI
        with SMBus(1) as smbus:
            smbus.write_bytes(register, bytearray(packer.read()))
        time.sleep(0.3)  # wait i2c process the request
        raw_read = smbus.read_bytes(register, 5)
        print(list(raw_read))  # the raw read contains the data format first, length, data, crc8, end bytes

        # let's clean the data
        with Unpacker as unpacker:
            unpacker.write(raw_read)
            read = unpacker.read()
        return read
    except Exception as e:
        print("ERROR: {}".format(e))
