"""
@file Packer.py
@author Mickael Lehoux <https://github.com/MkLHX>
@brief Class to allow raspberry I2C Master to deal with ESP32
using ESP32 Slave I2C library
@date 2020-09-18

The ESP32 Slave I2C library
use packing and upacking classes to format data
On python side we need to ENCODE data before send them through i2c

Packet format:
    [0]: start byte (0x02)
    [1]: packet length
    [2]: data[0]
    [3]: data[1]
    ...
    [n+1]: data[n-1]
    [n+2]: CRC8 of packet length and data
    [n+3]: end byte (0x04)
based on:
https://github.com/gutierrezps/ESP32_I2C_Slave/blob/master/src/WirePacker.h
https://github.com/gutierrezps/ESP32_I2C_Slave/blob/master/src/WirePacker.cpp
"""
from Raspberry_Pi_Master_for_ESP32_I2C_SLAVE.crc8 import Crc8


class Packer:
    PACKER_BUFFER_LENGTH = (
        128  # because ESP Slave I2C library wait for buffer[128] size
    )

    def __init__(self):
        self._debug = False
        self._buffer = [0] * self.PACKER_BUFFER_LENGTH
        self._index = 0
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
        # with Packer() as packer:
        #     # do stuff!
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit function, ensures resources are cleaned up."""
        self.reset()
        return False  # Don't suppress exceptions.

    def __del__(self):
        """Clean up any resources instance."""
        return False

    def read(self):
        """
        Read the next available packet byte. At each call,
        the value returned by available() will be decremented.
        @return int -1 if no bytes to read / byte value
        """
        if not self._is_written:
            raise Exception(
                "You need to finish process by using packer.end() method before read buffer"
            )
        return self._buffer

    def write(self, data: int):
        """
        @brief write data in prepared buffer
        @param int data
        """
        if self._debug:
            print("Data to unpack: ", data)
        if self._is_written:  # allow write after .end()
            self._is_written = False
        self._buffer[self._index] = data
        self._index += 1

    def end(self):
        """
        @brief Closes the packet. After that, use avaiable() and read()
        to get the packet bytes.
        """
        self._index += 1  # add field for CRC byte
        self._buffer[self._index] = self._frame_end
        self._index += 1
        self._total_length = self._index
        self._buffer[1] = self._total_length

        # ignore crc and end bytes
        payload_range = self._total_length - 2

        # ignore start and length bytes [2:payload_range]
        crc = Crc8()
        _crc8 = crc.calc(self._buffer[2:payload_range])

        self._buffer[self._index - 2] = _crc8
        self._is_written = True

    def reset(self):
        """
        @brief Reset the packing process.
        """
        self._frame_start = 0x02
        self._frame_end = 0x04
        self._buffer[0] = self._frame_start
        self._index = 2  # keep field for total lenght on index 1
        self._is_written = False
