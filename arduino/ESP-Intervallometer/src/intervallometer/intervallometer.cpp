#include "Arduino.h"
#include <BLEDevice.h>
#include "./intervallometer.h"

#pragma region constructor
IntervalloMeter::IntervalloMeter(short int shotPin, short int autofocusPin, BLECharacteristic *bleShots){
    this->shotPin = shotPin;
    this->autoFocusPin = autofocusPin;
    this->autofocusDelay = autofocusDelay;
    this->bleShots = bleShots;

    this->isAutofocus = true;

    pinMode(shotPin, OUTPUT);
    pinMode(autofocusPin, OUTPUT);
}
#pragma endregion

void IntervalloMeter::loop(){
    if (this->status != IntervallometerStatus::IDLE && this->shots > 0 && (millis() - time_now >= this->delay || this->shots == this->originalShots)){

        switch (this->status)
        {
        case IntervallometerStatus::Intervallometer:
            SingleShot(this->shotDelay);
            break;
        
        case IntervallometerStatus::BulbIntervallometer:
            SingleShot(this->wait);
            break;
        
        default:
            break;
        }

        // notify BLE Client
        this->bleShots->setValue(String(this->shots).c_str());
        this->bleShots->notify();
        this->time_now = millis();
        this->shots--;
    }
}


void IntervalloMeter::setProgram(Program program){
    this->shots = program.shots;
    this->originalShots = program.shots;
    this->delay = program.delay * 1000;
    this->wait = program.wait * 1000;
    this->isAutofocus = program.useAutofocus;
    this->autofocusDelay = program.autofocusDelay * 1000;
    this->status = program.status;

    switch (this->status)
    {
    case IntervallometerStatus::SingleShot:
        SingleShot(this->shotDelay);
        this->status = IntervallometerStatus::IDLE;
        break;
    
    case IntervallometerStatus::Bulb:
        SingleShot(this->wait);
        this->status = IntervallometerStatus::IDLE;
        break;

    case IntervallometerStatus::TimerBulb:
        Arduino_h::delay(this->delay);
        SingleShot(this->wait);
        this->status = IntervallometerStatus::IDLE;
        break;
    
    default:
        break;
    }
}

#pragma region private methods
void IntervalloMeter::SingleShot(long unsigned int waitTime){
    digitalWrite(this->autoFocusPin, HIGH);
    if(this->isAutofocus){
        Arduino_h::delay(this->autofocusDelay);
    }

    digitalWrite(this->shotPin, HIGH);
    Arduino_h::delay(waitTime);
    digitalWrite(this->shotPin, LOW);
    digitalWrite(this->autoFocusPin, LOW);
}

#pragma endregion