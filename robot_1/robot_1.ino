#include <servo.h>
Servo servoRight;
Servo servoLeft;

void setup() {
  // put your setup code here, to run once:
servoLeft.attach(13);
servoRight.attach(12);
servoLeft.writeMicroseconds(1500);
servoRight.writeMicroseconds(1500);
}
void moveServosLeft(){
  servoLeft.writeMicroseconds(1300);
  
}
 void moveServosRight(){
  servoRight.writeMicroseconds(1700);
 }
// void moveServosForward(){
//  moveServosLeft()
//  moveServosRight()  
// }

// void moveServosBackwards(){
void loop() {
  // put your main code here, to run repeatedly:
moveServosLeft();
delay(1000);
moveServosRight();
delay (1000);

}
