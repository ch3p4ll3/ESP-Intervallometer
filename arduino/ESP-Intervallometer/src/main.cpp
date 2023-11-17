#include <Arduino.h>
#include <BLEDevice.h>
#include <BLEServer.h>
#include <BLEUtils.h>

#include "./characteristicsCallbacks/characteristicsCallbacks.cpp"
#include "./intervallometer/intervallometer.h"

#define SERVICE_UUID "4fafc201-1fb5-459e-8fcc-c5c9c331914b"
#define DELAY_CHARACTERISTICS_UUID "beb5483e-36e1-4688-b7f5-ea07361b26a8"
#define SHOTS_CHARACTERISTICS_UUID "5bd6d6d5-8d8a-43c1-9626-ae6b45b5dfa6"
#define WAIT_CHARACTERISTICS_UUID "fe8cb5c3-db5c-4de7-9e2c-fb7dec9f469b"
#define AUTOFOCUS_CHARACTERISTICS_UUID "29292731-e87e-4834-a5dc-6f18b3535cd6"
#define AUTOFOCUS_DELAY_CHARACTERISTICS_UUID "0cc3228d-d3fc-4d62-93dd-8e1396d5544c"
#define STATUS_CHARACTERISTICS_UUID "1f85fe39-fe80-4bfe-8df0-a8a893d22dc1"

#define BLE_SERVER_NAME "ESP-Intervallometer"

#pragma region global variables
BLECharacteristic DelayCharacteristics(DELAY_CHARACTERISTICS_UUID, BLECharacteristic::PROPERTY_READ | BLECharacteristic::PROPERTY_WRITE);
BLECharacteristic ShotsCharacteristics(SHOTS_CHARACTERISTICS_UUID, BLECharacteristic::PROPERTY_NOTIFY | BLECharacteristic::PROPERTY_READ | BLECharacteristic::PROPERTY_WRITE);
BLECharacteristic WaitCharacteristics(WAIT_CHARACTERISTICS_UUID, BLECharacteristic::PROPERTY_READ | BLECharacteristic::PROPERTY_WRITE);
BLECharacteristic AutofocusCharacteristics(AUTOFOCUS_CHARACTERISTICS_UUID, BLECharacteristic::PROPERTY_READ | BLECharacteristic::PROPERTY_WRITE);
BLECharacteristic AutofocusDelayCharacteristics(AUTOFOCUS_DELAY_CHARACTERISTICS_UUID, BLECharacteristic::PROPERTY_READ | BLECharacteristic::PROPERTY_WRITE);
BLECharacteristic StatusCharacteristics(STATUS_CHARACTERISTICS_UUID, BLECharacteristic::PROPERTY_READ | BLECharacteristic::PROPERTY_WRITE);

IntervalloMeter intervallometer(2, 4, &ShotsCharacteristics);

Program intervallometerProgram;
static int taskCore = 1
#pragma endregion

#pragma region function declarations
void initBLE();
void setCallbacks();
void setDefaults();
void coreTask( void * pvParameters );
#pragma endregion

void coreTask( void * pvParameters ){
    while(true){
        intervallometer.loop();
    }
}

class StatusCallback : public BLECharacteristicCallbacks
{
  void onWrite(BLECharacteristic *pCharacteristic)
  {
    String rxValue = pCharacteristic->getValue().c_str();

    int status = rxValue.toInt();

    intervallometerProgram.status = static_cast<IntervallometerStatus>(status);
    intervallometer.setProgram(intervallometerProgram);
  }
};

void setup()
{
  initBLE();
  setCallbacks();
  setDefaults();

  xTaskCreatePinnedToCore(
                    coreTask,   /* Function to implement the task */
                    "coreTask", /* Name of the task */
                    10000,      /* Stack size in words */
                    NULL,       /* Task input parameter */
                    0,          /* Priority of the task */
                    NULL,       /* Task handle. */
                    taskCore);  /* Core where the task should run */

  Serial.begin(9600);
}

void loop()
{
}

void initBLE()
{
  BLEDevice::init(BLE_SERVER_NAME);

  // Create the BLE Server
  BLEServer *pServer = BLEDevice::createServer();

  // Create the BLE Service
  BLEService *intervallometerService = pServer->createService(SERVICE_UUID);

  intervallometerService->addCharacteristic(&DelayCharacteristics);
  intervallometerService->addCharacteristic(&ShotsCharacteristics);
  intervallometerService->addCharacteristic(&WaitCharacteristics);
  intervallometerService->addCharacteristic(&AutofocusCharacteristics);
  intervallometerService->addCharacteristic(&AutofocusDelayCharacteristics);
  intervallometerService->addCharacteristic(&StatusCharacteristics);

  // Start the service
  intervallometerService->start();

  // Start advertising
  BLEAdvertising *pAdvertising = BLEDevice::getAdvertising();
  pAdvertising->addServiceUUID(SERVICE_UUID);
  pServer->getAdvertising()->start();
}

void setCallbacks()
{
  DelayCharacteristics.setCallbacks(new DelayCallback(&intervallometerProgram));
  ShotsCharacteristics.setCallbacks(new ShotsCallback(&intervallometerProgram));
  WaitCharacteristics.setCallbacks(new WaitCallback(&intervallometerProgram));
  AutofocusCharacteristics.setCallbacks(new AutofocusCallback(&intervallometerProgram));
  AutofocusDelayCharacteristics.setCallbacks(new AutofocusDelayCallback(&intervallometerProgram));
  StatusCharacteristics.setCallbacks(new StatusCallback());
}

void setDefaults(){
  DelayCharacteristics.setValue("1");
  ShotsCharacteristics.setValue("1");
  WaitCharacteristics.setValue("1");
  AutofocusCharacteristics.setValue("0");
  AutofocusDelayCharacteristics.setValue("1500");
  StatusCharacteristics.setValue("0");
}
