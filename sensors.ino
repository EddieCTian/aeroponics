#include <SHT1x.h>

#define dataPin 11
#define clockPin 10

SHT1x sht1x(dataPin, clockPin);

char a;

void setup(){
    Serial.begin(9600);

}

void loop(){
    if (Serial.available()>0){
        a = Serial.read();
        if (a=='0'){
            Serial.print(sht1x.readTemperatureC(), 2);
        }
        else if (a=='1'){
            Serial.print(sht1x.readHumidity(), 2);
        }
/*        else if (a=='2'){
            some spooky ph code tbd
        }
*/
    }
}
