#include "SoftwareSerial.h"
#include "stdlib.h"

void setup() {
  Serial.begin(115200);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(2, OUTPUT);
  digitalWrite(2, HIGH);
}
int num1 = 0, num2 = 0;
void loop() {
  char buff[100] = {0};
  char data;
  int i = 0;
  if(Serial.available() == 8) {
    for (i = 0; i < 8; i++) {
      buff[i] = Serial.read();
    }
    num1 = 1*(buff[3]-'0')+10*(buff[2]-'0')+100*(buff[1]-'0')+1000*(buff[0]-'0');
    num2 = 1*(buff[7]-'0')+10*(buff[6]-'0')+100*(buff[5]-'0')+1000*(buff[4]-'0');
  }
  
  while(num1 != 0 && num2 != 0)
  {
    
    digitalWrite(6, HIGH);
    delayMicroseconds(num1);
    digitalWrite(6, LOW);
    delayMicroseconds(num1);

    digitalWrite(5, HIGH);
    delayMicroseconds(num2);
    digitalWrite(5, LOW);
    delayMicroseconds(num2);
    
    if(Serial.available()) break;
  }   
}
