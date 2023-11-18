#pragma once
#include <BLEDevice.h>
#include "Arduino.h"

enum IntervallometerStatus {IDLE, SingleShot, Bulb, TimerBulb, Intervallometer, BulbIntervallometer };


struct Program{
    IntervallometerStatus status;
    long unsigned int shots;
    long unsigned int delay;  // delay between a shot
    long unsigned int wait;  // time to wait for a bulb photo
    unsigned int autofocusDelay;
    bool useAutofocus;
};


class IntervalloMeter{
    private:
        bool isAutofocus;
        short int shotPin;
        short int autoFocusPin;
        unsigned int autofocusDelay;
        int shotDelay = 100;

        long unsigned int time_now = millis();
        long unsigned int shots;
        long unsigned int originalShots;
        long unsigned int delay;
        long unsigned int wait;

        BLECharacteristic *bleShots;

        void SingleShot(long unsigned int waitTime);
        void Delay(long unsigned int waitTime);

    public:
        IntervallometerStatus status = IntervallometerStatus::IDLE;

        IntervalloMeter(short int shotPin, short int autofocusPin, BLECharacteristic *bleShots);

        void setProgram(Program program);

        void loop();
};