int FL = A0;
int FR = A1;
int BL = A2;
int BR = A3;
//int ledPin = 13; the LED is connected to digital pin 13
int FLv, FRv, BLv, BRv; 
char situation[] = "llll";
void setup() { 
  pinMode (13, OUTPUT);
  Serial.begin(9600);
}

void loop() { 
  FLv = analogRead(FL);
  FRv = analogRead(FR);
  BLv = analogRead(BL);
  BRv = analogRead(BR);
  
  if(FLv>750)
    situation[0]='h';
  if(FRv>750)
    situation[1]='h';
  if(BLv>750)
    situation[2]='h';
  if(BRv>750)
    situation[3]='h';
  
  Serial.print(situation);
  situation[0] = 'l';
  situation[1] = 'l';
  situation[2] = 'l';
  situation[3] = 'l';
}