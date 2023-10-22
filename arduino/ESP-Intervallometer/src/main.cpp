#include <Arduino.h>
#include <BLEDevice.h>
#include <BLEServer.h>
#include <BLEUtils.h>

#include "./intervallometer/intervallometer.h"

#define SERVICE_UUID "91bad492-b950-4226-aa2b-4ede9fa42f59"
#define DELAY_CHARACTERISTICS_UUID ""
#define SHOTS_CHARACTERISTICS_UUID ""
#define WAIT_CHARACTERISTICS_UUID ""
#define STATUS_CHARACTERISTICS_UUID ""

#define BLE_SERVER_NAME "ESP-Intervallometer"

#pragma region global variables
BLECharacteristic DelayCharacteristics(DELAY_CHARACTERISTICS_UUID, BLECharacteristic::PROPERTY_NOTIFY | BLECharacteristic::PROPERTY_READ | BLECharacteristic::PROPERTY_WRITE);
BLECharacteristic ShotsCharacteristics(SHOTS_CHARACTERISTICS_UUID, BLECharacteristic::PROPERTY_NOTIFY | BLECharacteristic::PROPERTY_READ | BLECharacteristic::PROPERTY_WRITE);
BLECharacteristic WaitCharacteristics(WAIT_CHARACTERISTICS_UUID, BLECharacteristic::PROPERTY_NOTIFY | BLECharacteristic::PROPERTY_READ | BLECharacteristic::PROPERTY_WRITE);
BLECharacteristic StatusCharacteristics(STATUS_CHARACTERISTICS_UUID, BLECharacteristic::PROPERTY_NOTIFY | BLECharacteristic::PROPERTY_READ | BLECharacteristic::PROPERTY_WRITE);

IntervalloMeter intervallometer(2);
#pragma endregion

#pragma region function declarations
void initBLE();
#pragma endregion

void setup() {
  initBLE();
  Program prog;
  prog.delay = 5;
  prog.shots = 5;
  prog.wait = 5;
  prog.status = IntervallometerStatus::SingleShot;

  intervallometer.setProgram(prog);
}

void loop() {
  intervallometer.loop();
}


void initBLE(){
  BLEDevice::init(BLE_SERVER_NAME);

  // Create the BLE Server
  BLEServer *pServer = BLEDevice::createServer();

  // Create the BLE Service
  BLEService *intervallometerService = pServer->createService(SERVICE_UUID);

  intervallometerService->addCharacteristic(&DelayCharacteristics);
  intervallometerService->addCharacteristic(&ShotsCharacteristics);
  intervallometerService->addCharacteristic(&WaitCharacteristics);
  intervallometerService->addCharacteristic(&StatusCharacteristics);
  
  // Start the service
  intervallometerService->start();

  // Start advertising
  BLEAdvertising *pAdvertising = BLEDevice::getAdvertising();
  pAdvertising->addServiceUUID(SERVICE_UUID);
  pServer->getAdvertising()->start();
}
