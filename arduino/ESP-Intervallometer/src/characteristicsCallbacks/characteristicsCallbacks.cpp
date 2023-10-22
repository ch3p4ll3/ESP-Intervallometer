#include "Arduino.h"
#include "../intervallometer/intervallometer.h"
#include <BLEDevice.h>

class DelayCallback : public BLECharacteristicCallbacks
{
  public:
    Program *program;

    DelayCallback(Program *program){
      this->program = program;
    }
  
    void onWrite(BLECharacteristic *pCharacteristic)
    {
      String rxValue = pCharacteristic->getValue().c_str();

      int delay_time = rxValue.toInt();

      this->program->delay = delay_time;
    }
};


class ShotsCallback : public BLECharacteristicCallbacks
{
  public:
    Program *program;

    ShotsCallback(Program *program){
      this->program = program;
    }
  
    void onWrite(BLECharacteristic *pCharacteristic)
    {
      String rxValue = pCharacteristic->getValue().c_str();

      int delay_time = rxValue.toInt();

      this->program->shots = delay_time;
    }
};

class WaitCallback : public BLECharacteristicCallbacks
{
  public:
    Program *program;

    WaitCallback(Program *program){
      this->program = program;
    }
  
    void onWrite(BLECharacteristic *pCharacteristic)
    {
      String rxValue = pCharacteristic->getValue().c_str();

      int delay_time = rxValue.toInt();

      this->program->wait = delay_time;
    }
};