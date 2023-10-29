- [ESP-DSLR-Trigger](#esp-dslr-trigger)
  - [How it works](#how-it-works)
  - [How to make your intervallometer](#how-to-make-your-intervallometer)
  - [Build and upload the project](#build-and-upload-the-project)
    - [Using VSCode Extension](#using-vscode-extension)
    - [Build and upload manually](#build-and-upload-manually)
  - [Intervallometer Status](#intervallometer-status)
  - [GATT server](#gatt-server)
    - [Characteristics UUIDs](#characteristics-uuids)

# ESP-DSLR-Trigger
The ESP-DSLR-Trigger project is a simple and easy-to-use system for controlling a DSLR camera using a Bluetooth Low Energy (BLE) device. The project uses the ESP32 microcontroller, which is a popular choice for developing BLE devices.

The ESP-DSLR-Trigger project exposes a single GATT server with a single service. It can be used to trigger the DSLR camera to take a picture, start or stop a bulb exposure, or start or stop an intervallometer.

The ESP-DSLR-Trigger project also includes a web UI that can be used to connect to the GATT server and manage it easily. The web UI allows you to connect to the GATT server, read and write the values of the characteristics, and start and stop bulb exposures, intervallometers, and timers.

## How it works
This simple intervalometer is based on an esp-32. The client connects to the esp bluetooth and sends commands via BLE and the ESP will manage the shooting of your DSLR autonomously!

## How to make your intervallometer
I bought [this](https://www.amazon.it/GIn-Telecomando-Scatto-Remoto-fotocamere/dp/B00DJ6FZ8E/ref=sr_1_37?__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=meike+nikon+d3200&qid=1595268319&sr=8-37)
remote shutter release for my Nikon. I opened it and welded cables in the slats where, if pressed the button, it made contact. After finding the common I made this small scheme and connected the optocoupler to pin 2 of the [ESP32](https://www.amazon.it/Sviluppo-ESP-WROOM-32-ESP-32S-Bluetooth-Antenna/dp/B071JR9WS9/ref=sr_1_4?__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=esp32&qid=1595268549&sr=8-4)  


Scheme
![](scheme.jpg)

Internal connections 
![](internal.jpg)

## Build and upload the project
### Using VSCode Extension
To use the PlatformIO IDE extension for Visual Studio Code, you will need to have the following installed:

* Visual Studio Code
* The [PlatformIO IDE](https://platformio.org/install/ide?install=vscode) extension for Visual Studio Code

Once you have installed the necessary software, you can follow these steps to build and upload a PlatformIO project using the Visual Studio Code extension:

1. Clone the ESP-DSLR-Trigger project from GitHub:

```
git clone https://github.com/ch3p4ll3/ESP-DSLR-Trigger.git
```
1. Open Visual Studio Code.
2. Click on the "File" menu and select "Open Folder".
3. Select the folder that contains the PlatformIO project (`ESP-DSLR-Trigger/arduino/ESP-Intervallometer`).
4. The PlatformIO IDE extension will automatically detect your PlatformIO project and open it in Visual Studio Code.
5. To build the project, click on the "Build" button in the PlatformIO IDE extension's toolbar.
6. To upload the project to your board, click on the "Upload" button in the PlatformIO IDE extension's toolbar.


### Build and upload manually
To build and upload the ESP-DSLR-Trigger project, you will need to have the PlatformIO IDE installed. Once you have installed the PlatformIO IDE, you can follow these steps:

1. Clone the ESP-DSLR-Trigger project from GitHub:

```
git clone https://github.com/ch3p4ll3/ESP-DSLR-Trigger.git
```

2. Open the ESP-DSLR-Trigger project in the PlatformIO IDE:

```
cd ESP-DSLR-Trigger/arduino/ESP-Intervallometer
platformio open
```

3. Select the board that you will be using:

```
platformio boards
```

In the "Boards" dialog box, select the board that you will be using and click on the "Close" button.

4. Build the project:

```
platformio build
```

The PlatformIO IDE will compile and link your code to create a firmware image.

5. Upload the project to your board:

```
platformio upload
```

The PlatformIO IDE will upload the firmware image to your board.

Once you have uploaded the project to your board, you can start using it to control your DSLR camera using a BLE device!


## Intervallometer Status
The Intervallometer can have different states:

|        Status        |  Value  |                                           Description                                                     |
| ---------------------| ------- | --------------------------------------------------------------------------------------------------------- |
| IDLE                 |    0    | The ESP-DSLR-Trigger is in idle state. It is not currently taking any pictures.                           |
| SingleShot           |    1    | The ESP-DSLR-Trigger is in single shot mode. It takes a single picture.                                   |
| Bulb                 |    2    | The ESP-DSLR-Trigger is in bulb mode. It starts a bulb exposure.                                          |
| TimerBulb            |    3    | The ESP-DSLR-Trigger is in timer bulb mode. It is taking a bulb exposure after a certain ammount of time  |
| Intervallometer      |    4    | The ESP-DSLR-Trigger is in intervallometer mode. It is taking pictures at regular intervals.              |
| BulbIntervallometer  |    5    | The ESP-DSLR-Trigger is in bulb intervallomater mode. It is taking bulb exposures at regular intervals.   |

The Intervallometer Status is used to control the behavior of the ESP-DSLR-Trigger project. For example, when the ESP-DSLR-Trigger is in single shot mode, it will take a single picture. When the ESP-DSLR-Trigger is in intervallometer mode, it will take pictures at regular intervals.

The Intervallometer status enum is also used to indicate the current state of the ESP-DSLR-Trigger project to GATT clients. GATT clients can read the Status characteristic to determine the current state of the ESP-DSLR-Trigger project.

## GATT server
A GATT server is a Bluetooth Low Energy (BLE) device that exposes data to other BLE devices, known as GATT clients. GATT stands for Generic Attribute Profile, and it is the protocol that BLE devices use to communicate with each other.

GATT servers organize their data into services and characteristics. A service is a collection of related characteristics, and a characteristic is a single piece of data. For example, a GATT server for a fitness tracker might have a service for heart rate data, with characteristics for the current heart rate, the average heart rate, and the maximum heart rate.

GATT clients can read and write data from GATT servers. They can also subscribe to notifications from GATT servers, which means that they will be notified whenever the value of a characteristic changes.

### Characteristics UUIDs
|            Name             |                    UUID                 |     Type    | What it's used for |
| --------------------------- | ----------------------------------------| ----------- | ------------------ |
| DELAY_CHARACTERISTICS_UUID  | `beb5483e-36e1-4688-b7f5-ea07361b26a8`    | `R`/`W`     | Sets the delay between shots |
| SHOTS_CHARACTERISTICS_UUID  | `5bd6d6d5-8d8a-43c1-9626-ae6b45b5dfa6`    | `R`/`W`/`N` | Sets the number of shots to be taken, the counter is scaled with each shot taken and clients are notified |
| WAIT_CHARACTERISTICS_UUID   | `fe8cb5c3-db5c-4de7-9e2c-fb7dec9f469b`    | `R`/`W`     | Sets the time to wait for BULB poses |
| STATUS_CHARACTERISTICS_UUID | `1f85fe39-fe80-4bfe-8df0-a8a893d22dc1`    | `R`/`W`     | Sets the type of shot: Single Shot, Bulb, Intervallometer, Bulb Intervallometer, Timer Bulb |