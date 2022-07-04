#include <Servo.h>
Servo myservo1,myservo2;

int angle[2];
String data;
int above =10;
int below= 9;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(10);
  myservo1.attach(below);
  myservo2.attach(above);
//  myservo3.attach(2);
//  myservo4.attach(3);
//  myservo5.attach(4);
//  myservo6.attach(5);
//  myservo7.attach(6);
//  myservo8.attach(7);
  myservo1.write(130);
  myservo2.write(90);
  delay(10);
}

void loop() {

if (Serial.available() > 0) {
       data = Serial.readString(); 
       //Serial.println(data);
       for (int i=0 ; i<2;i++){
        int index = data.indexOf(",");
        angle[i]= atol(data.substring(0,index).c_str());
        data= data.substring(index+1);
        
       }
       for(int i=0;i<2;i++)
       {
          Serial.println(angle[i]);
       }
 }
       
//       myservo1.write(angle[0]);
//       myservo2.write(angle[1]);
//       myservo3.write(angle[2]);
//       myservo4.write(angle[3]);
//       myservo5.write(angle[4]);
//       myservo6.write(angle[5]);
//       myservo7.write(angle[6]);
//       myservo8.write(angle[7]);
  
     
     
}
