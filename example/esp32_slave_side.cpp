/**
 * @file esp32_slave_side.cpp
 * @author MkLHX https://github.com/MkLHX
 * @brief 
 * @date 2021-04-20
 * 
 * @copyright Copyright (c) 2021
 * this is an example of esp32 slave side c++ code 
 */

#include <Arduino.h>
#ifndef Wire
#include <Wire.h>
#endif
#ifndef WireSlave
#include <WireSlave.h>
#endif

void receiveEvent(int numBytes);
void requestEvent(void);

byte i2cAddr = 0x21 // or wathever
int howManyBytesReceived;
uint8_t registerCode;

void receiveEvent(int numBytes)
{

    Serial.print(F("---> recieved "));
    Serial.print(numBytes);
    howManyBytesReceived = numBytes;
    Serial.println(F(" events on i2c bus"));
    registerCode = WireSlave.read();
}

void requestEvent(void)
{
    Serial.print(F("---> request register value: "));
    Serial.print(registerCode, DEC);
    Serial.print(F(" / 0x0"));
    Serial.println(registerCode, HEX);
    
    // switch case for multiple i2c registers
    switch (registerCode)
    {
    case 0x00:
    {
        Serial.print("case of register 0x00");
        // return value about register 0x00 uint8_t format
        const uint8_t device_type = 0x00;
        WireSlave.write(device_type);
        break;
    }
    case 0x01:
    {
        Serial.print("case of register 0x01");
        // return value about register 0x01 uint8_t format
        const uint8_t device_firmware = 10; // send 10 divide by 10 to get the real value
        WireSlave.write(device_firmware);
        break;
    }
    default {
        Serial.print("UNKNOW REGISTER: ");
        Serial.println(registerCode);
    }
    }
}

void setup()
{
    Serial.begin(115200);
    bool ready = WireSlave.begin(I2C_SDA_PIN, I2C_SCL_PIN, i2cAddr);
    if (!ready)
    {
        Serial.println(F("I2C slave init failed"));
        while (true)
            delay(100);
    }
    WireSlave.onReceive(receiveEvent); // receive register value
    WireSlave.onRequest(requestEvent); // send register value
}

void loop()
{
    // your other logic than i2c here
    WireSlave.update();
    delay(5); // cadencing loop to allow other i2c device interrupt
}
