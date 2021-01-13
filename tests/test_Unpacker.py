# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import sys
import unittest
from Raspberry_Pi_Master_for_ESP32_I2C_SLAVE.unpacker import Unpacker


class TestPacker(unittest.TestCase):
    def test_unpacker(self):
        value_to_unpack = [2, 6, 12, 1, 19, 4]
        unpacked = None
        with Unpacker() as unpacker:
            unpacker.write(value_to_unpack)
            unpacked = unpacker.read()
        expected = [12, 1]
        self.assertIsNotNone(unpacked)
        self.assertTrue(type(unpacked).__name__ == "list")
        self.assertEqual(expected, unpacked)


if __name__ == "__main__":
    unittest.main()
