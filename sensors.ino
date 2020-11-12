#include <SHT1x.h>

#define dataPin 11
#define clockPin 10

SHT1x sht1x(dataPin, clockPin);

void setup(){
    Serial.begin(9600);
    byte a;
}

void loop(){
    if (Serial.available()>0){
        Serial.readBytes(byte, 1);
        if (byte==0){
            out=sht1x.readTemperatureC();
        }
        else if (byte==1){
            out=sht1x.readHumidity();
        }
        else if (byte==2){
            out=0;
        }
        Serial.write(out, 4)
    }
}
