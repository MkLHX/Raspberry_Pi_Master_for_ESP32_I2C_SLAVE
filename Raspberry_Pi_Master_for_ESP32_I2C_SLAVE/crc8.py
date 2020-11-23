"""
@file Crc8.py
@author Mickael Lehoux <https://github.com/MkLHX>
@brief build CRC8 in python
@date 2020-09-18
based on:
https://github.com/gutierrezps/ESP32_I2C_Slave/blob/master/src/WireCrc.h
"""


class Crc8:
    def __init__(self):
        self._seed = 0
        self._debug = False

    def __enter__(self):
        """Context manager enter function."""
        # Just return this object so it can be used in a with statement, like
        # with Crc8() as crc8:
        #     # do stuff!
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit function, ensures resources are cleaned up."""
        return False  # Don't suppress exceptions.

    def calc(self, data):
        crc = self._seed
        for _byte in data:
            extract = _byte
            for j in range(8, 0, -1):
                _sum = (crc ^ extract) & 0x01
                crc >>= 1
                if _sum:
                    crc ^= 0x8C
                extract >>= 1
        return crc
