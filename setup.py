import os
import pathlib
from setuptools import setup, find_packages

# Package meta-data.
NAME = "raspberrypi-esp32-i2c"
DESCRIPTION = "use Raspberry Pi as master on ESP32 i2c \
    slave when use ESP32 i2c Slave c++ library"
URL = "https://github.com/MkLHX/Raspberry_Pi_Master_for_ESP32_I2C_SLAVE"
EMAIL = "mickael@lehoux.net"
AUTHOR = "Mickael Lehoux"
REQUIRES_PYTHON = ">=3.6.0"
VERSION = "0.0.2"

# What packages are required for this module to be executed?
REQUIRED = [
    # 'requests', 'maya', 'records',
]

# What packages are optional?
EXTRAS = {
    # 'fancy feature': ['django'],
}

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

# Load the package's version.py module as a dictionary.
about = {}
if not VERSION:
    with open(os.path.join(here, "version.py")) as f:
        exec(f.read(), about)
else:
    about["__version__"] = VERSION

setup(
    name=NAME,
    version=about["__version__"],
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=URL,
    license="MIT",
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=REQUIRES_PYTHON,
    project_urls={  # Optional
        "Source": "https://github.com/MkLHX/\
            Raspberry_Pi_Master_for_ESP32_I2C_SLAVE",
        "Bug Reports": "https://github.com/MkLHX/\
            Raspberry_Pi_Master_for_ESP32_I2C_SLAVE/issues",
    },
    keywords="i2c driver python hardware diy iot raspberry pi",
)
