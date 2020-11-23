"""
@file Unpacker.py
@author Mickael Lehoux <https://github.com/MkLHX>
@brief Class to allow raspberry I2C Master to deal with ESP32
using ESP32 Slave I2C library
@date 2020-09-25

The ESP32 Slave I2C library
use packing and upacking classes to format data
On python side we need to DECODE data from i2c

format:
    [0]: start byte (0x02)
    [1]: packet length
    [2]: data[0]
    [3]: data[1]
    ...
    [n+1]: data[n-1]
    [n+2]: CRC8 of packet length and data
    [n+3]: end byte (0x04)
based on:
https://github.com/gutierrezps/ESP32_I2C_Slave/blob/master/src/WireUnpacker.h
https://github.com/gutierrezps/ESP32_I2C_Slave/blob/master/src/WireUnpacker.cpp
"""
from Raspberry_Pi_Master_for_ESP32_I2C_SLAVE.crc8 import Crc8


class Unpacker:
    error_codes = {
        "INVALID_CRC": 1,
        "INVALID_LENGTH": 2,
        "INVALID_START": 5,
        "INVALID_END": 6,
    }
    error_decodes = {
        1: "INVALID_CRC",
        2: "INVALID_LENGTH",
        3: "INVALID_START",
        4: "INVALID_END",
    }

    def __init__(self):
        self._debug = False
        self.reset()

    @property
    def debug(self):
        return self._debug

    @debug.setter
    def debug(self, d):
        self._debug = d

    def __enter__(self):
        """Context manager enter function."""
        # Just return this object so it can be used in a with statement, like
        # with Unpacker() as unpacker:
        #     # do stuff!
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit function, ensures resources are cleaned up."""
        return False  # Don't suppress exceptions.

    def __del__(self):
        """Clean up any resources instance."""
        return False

    def get_last_error(self):
        """
        @brief get the last error code and message
        @return list [error_code, error_text]
        """
        return self._last_error, self.error_decodes[self._last_error]

    def read(self):
        """
        @brief return i2c values from slave
        @return list buffer
        """
        return self._buffer

    def write(self, data: list):
        """
        @brief get the i2c data from slave
        check if start, end and crc8 bytes are correct
        remove start, length, crc8 and end bytes
        """
        if self._debug:
            print("Data to unpack: ", data)
        if data[0] != self._frame_start:
            self._last_error = self.error_codes["INVALID_START"]
            raise Exception("ERROR: Unpacker invalid start byte")
        if data[-1] != self._frame_end:
            self._last_error = self.error_codes["INVALID_END"]
            raise Exception("ERROR: Unpacker invalid end byte")

        # check if provided crc8 is good
        # ignore crc and end bytes
        payload_range = len(data) - 2
        crc8 = Crc8()
        # ignore start, length
        crc = crc8.calc(data[2:payload_range])
        if crc != data[-2]:
            self._last_error = self.error_codes["INVALID_CRC"]
            raise Exception("ERROR: Unpacker invalid crc8")

        self._buffer = data[2:-2]

    def reset(self):
        self._frame_start = 0x02
        self._frame_end = 0x04
        self._buffer = []
        self._last_error = None
