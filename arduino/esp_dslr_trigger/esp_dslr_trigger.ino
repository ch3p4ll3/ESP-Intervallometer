#include "BluetoothSerial.h" //Header File for Serial Bluetooth, will be added by default into Arduino

BluetoothSerial ESP_BT; //Object for Bluetooth

#define shotPin 2

int period, shots, wait;
unsigned long time_now, wait_time;
int run = -1; //-1 stop, 0 intervallometer, 1 bulb, 2 timer bulb, 3 bulb intervallometer

void parser(String);
void split(String, char, String[]);
void intervallometer();
void timerBulb();
void bulbIntervallometer();


void setup() {
    pinMode(shotPin, OUTPUT);
    Serial.begin(115200); //Start Serial monitor in 115200
    ESP_BT.begin("ESP32_Shutter_Control"); //Name of your Bluetooth Signal
    Serial.println("Bluetooth Device is Ready to Pair");
}


void loop() {
    String message;

    if (ESP_BT.available()){
            while(ESP_BT.available()){
                message += char(ESP_BT.read());
        }

        Serial.println(message);
        parser(message);
    }

    switch(run){
        case -1:
        if (digitalRead(shotPin))
            digitalWrite(shotPin, LOW);
            break;

        case 0:
            intervallometer();
            break;

        case 1:
            digitalWrite(shotPin, HIGH);
            break;

        case 2:
            timerBulb();
            break;
        
        case 3:
            bulbIntervallometer();
            break;

        default:
            if (digitalRead(shotPin))
                digitalWrite(shotPin, LOW);
            break;
    }
}


void intervallometer(){
    if((millis() - time_now) % period == 0 && run == 0 && shots > 0){
        digitalWrite(shotPin, HIGH);
        delay(100);
        digitalWrite(shotPin, LOW);
        shots--;
        Serial.println(shots);
        ESP_BT.println(shots);
    }

    if (shots <= 0 && run == 0){
        run = -1;
        ESP_BT.println("Finished");
    }
}


void bulbIntervallometer(){
    String message;
    
    if(run == 3 && shots > 0){
        if ((millis() - time_now) % period == 0) {
            digitalWrite(shotPin, HIGH);
            wait_time = millis();
            while ((millis() - wait_time) <= wait && run == 3){
                if (ESP_BT.available()){
                    while(ESP_BT.available()){
                        message += char(ESP_BT.read());
                    }

                    Serial.println(message);
                    parser(message);
                }
            }

            digitalWrite(shotPin, LOW);
            shots--;
            time_now = millis();
            delay(1);
            Serial.println(shots);
            ESP_BT.println(shots);
        }
    }

    else if (shots <= 0 && run == 0){
        run = -1;
        ESP_BT.println("Finished");
    }
}


void timerBulb(){
    if (!digitalRead(shotPin))
        digitalWrite(shotPin, HIGH);

    if ((millis() - time_now) >= period && run == 2){
        run = -1;
        ESP_BT.println("Finished");
    }
}


void split(String data, char separator, String ar[10]){
    int count = 0;

    for (int i=0; i<data.length(); i++){
        if (data[i] == separator){
            count++;
        }

        else{
            ar[count] = ar[count] + data[i];
        }
    }
}


void parser(String c){
    String tmp[10];
    split(c, '#', tmp);

    if (tmp[0] == "intervallometer"){
        period = tmp[1].toInt()*1000;
        shots = tmp[2].toInt();
        time_now = millis();
        run = 0;
    }

    else if (tmp[0] == "bulbIntervallometer") {
        period = tmp[1].toInt()*1000;
        shots = tmp[2].toInt();
        wait = tmp[3].toInt()*1000;
        time_now = millis();
        run = 3;
    }

    else if (tmp[0] == "Bulb"){
        run = 1;
        ESP_BT.println("Bulb Started");
    }

    else if (tmp[0] == "timerBulb"){
        period = tmp[1].toInt()*1000;
        ESP_BT.print("Bulb mode on for ");
        ESP_BT.print(period/1000);
        ESP_BT.println(" seconds");
        time_now = millis();
        run = 2;
    }

    else if (tmp[0] == "singleShot"){
        digitalWrite(shotPin, HIGH);
        delay(100);
        digitalWrite(shotPin, LOW);
    }

    else if (tmp[0] == "stop"){
        run = -1;
        ESP_BT.println("Stopped");
    }

    else
        ESP_BT.println("Error, wrong command");
}