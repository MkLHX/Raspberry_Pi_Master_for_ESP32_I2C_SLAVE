# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import sys
import unittest
from Raspberry_Pi_Master_for_ESP32_I2C_SLAVE.packer import Packer


class TestPacker(unittest.TestCase):
    def test_packer(self):
        packer = Packer()
        packer.write(127)
        packer.end()
        packed = [i for i in packer.read() if i != 0]
        expected = [2, 5, 127, 185, 4]
        self.assertIsNotNone(packed)
        self.assertTrue(type(packed).__name__ == "list")
        self.assertEqual(expected, packed)


if __name__ == "__main__":
    unittest.main()
