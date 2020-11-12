#include <SHT1x.h>

#define dataPin 11
#define clockPin 10

SHT1x sht1x(dataPin, clockPin);

String a="temp";
String b="hum";
float temp, hum;

void setup() {
  Serial.begin(9600);
}

void loop() {
  
  if (Serial.available() > 0) {
    temp=(float)sht1x.readTemperatureC();
       
    hum=(float)sht1x.readHumidity();

        
    String data = Serial.readStringUntil('\n');
    if (a==data){
      Serial.print(temp);
    }
    else if (b==data){
      Serial.print(hum);
    }
    else {
      Serial.print("0");
    }
  }
}