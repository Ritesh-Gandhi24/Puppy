
#include <Servo.h>
int FL = A5;
int FR = A4;
int BL = A3;
int BR = A2;
//int ledPin = 13; the LED is connected to digital pin 13
int FLv, FRv, BLv, BRv; 
byte situation;

Servo myservo_7, myservo_6;

void setup() { 
  pinMode (13, OUTPUT);
  Serial.begin(9600);
  Serial.setTimeout(10);
  myservo_7.attach(7);
  myservo_6.attach(6);
}

void loop() { 
  situation=0b00000000;
  analogWrite(FL,0);
  analogWrite(FR,0);
  analogWrite(BL,0);
  analogWrite(BR,0);
  FLv = analogRead(FL);
  FRv = analogRead(FR);
  BLv = analogRead(BL);
  BRv = analogRead(BR);
  
//  Serial.print(FLv);
//  Serial.print(' ');
//
//   Serial.print(FRv);
//  Serial.print(' ');
//
//   Serial.print(BLv);
//  Serial.print(' ');
//
//   Serial.print(BRv);
//  Serial.println(' ');

  myservo_7.write(90);
  myservo_6.write(90);
  
  if(FLv>300)
    situation= situation | 0b00001000;
  if(FRv>300)
    situation= situation | 0b00000100;
  if(BLv>300)
    situation= situation | 0b00000010;
  if(BRv>300)
    situation= situation | 0b00000001;
  
  Serial.println(situation);
}
