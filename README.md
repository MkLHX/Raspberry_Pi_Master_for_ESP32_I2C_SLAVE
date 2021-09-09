# Raspberry_Pi_Master_for_ESP32_I2C_SLAVE
# This Python lib only works with the v0.2.0 of the c++ library https://github.com/gutierrezps/ESP32_I2C_Slave/releases/tag/v0.2.0

## use __**Raspberry pi as MASTER**__ of a __**ESP32 SLAVE**__ on __**i2c bus**__

### To use ESP32 as slave on i2c bus you have to use ESP32_I2C_Slave c++ library:
> platformio lib_deps = ESP32 I2C Slave <br>
> https://github.com/gutierrezps/ESP32_I2C_Slave

because the esp32-arduino framework not allowed you to use ESP32 as i2c slave.

The ESP32 I2C Slave library do the job on 2 ESP32 or Arduino + ESP32 but not with python master on raspberry pi.

So i convert parts of this library to python classes.

To use these classes you must need to install:

>pip install adafruit-blinka<br>
>pip install adafruit-extended-bus


Follow examples to read data from master RPI to slave ESP32:<br>
[example-read](/example/raspberry_pi_read_esp32.py)<br>
[example-write](/example/raspberry_pi_write_esp32.py)<br>
[example-slave-side](/example/esp32_slave_side.cpp)<br>


to install it use pip:
>pip install raspberrypi-esp32-i2c