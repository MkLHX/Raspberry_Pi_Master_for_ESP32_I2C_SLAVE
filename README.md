# Raspberry_Pi_Master_for_ESP32_I2C_SLAVE
## use <u><b>Raspberry pi as MASTER</b></u> of a <u><b>ESP32 SLAVE</b></u> on <u><b>i2c bus</b></u>

### To use ESP3 as slave on i2c bus you have to use ESP32_I2C_Slave c++ library:
> platformio lib_deps = ESP32 I2C Slave
> https://github.com/gutierrezps/ESP32_I2C_Slave

because the esp32-arduino framework not allowed you to use ESP32 as i2c slave.

The ESP32 I2C Slave library do the job on 2 ESP32 or Arduino + ESP32 but not with python master on raspberry pi.

So i convert parts of this library to python classes.

To use these classes you must need to install:

>pip install adafruit-blinka<br>
>pip install adafruit-extended-bus


Follow examples to read data from master RPI to slave ESP32:<br>
[example-read](/example/raspberry_pi_read_esp32.py)<br>
[example-write](/example/raspberry_pi_write_esp32.py)


to install it use pip:
>pip install raspberrypi-esp32-i2c