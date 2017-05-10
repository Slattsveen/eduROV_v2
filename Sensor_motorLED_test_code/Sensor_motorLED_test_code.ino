//#include<OneWire.h>
//#include<DallasTemperature.h>

//Pin setup
int pressPin = A0; // read using kPaRead(*pin number*);
int tempPin = A1; // read using getTemp(tempPin);
int battVoltPin = A2; // monitor battery voltage, when motors are idle.
//OneWire tempWire(tempPin);
//DallasTemperature sensors(&tempWire);

//Motor pins, emulated using LED's in this setup
#define dive 7
#define rise 6 //pwm in case of brushless motor use
#define portRev 5 //pwm
#define portFwd 4 
#define strbdRev 3 //pwm
#define strbdFwd 2

// motor flags, use to control motor on/off 
// message format 000 - 111 - 222, "vertical port strbd" 
// 0 - off, 1 - direction A, 2 direction - B
byte vertical = 0;
byte port = 0;
byte strbd = 0;

//sensor variables
double temp = 0;
int atm = 0;
int battVolt = 0;

String input = " ";
String output = " ";
bool stringComplete = false;
//serial message intervals
unsigned int delayTime = 1000;
unsigned long messageTime = 0;

// timing variables
/*
  0 loop start
 1 msg available
 2 msg read
 3 motorfunction called
 4 motorfunction finished
 5 loop finished
 */
unsigned long timing[6] = {
  0, 0, 0, 0, 0, 0};

void setup() {
  Serial.begin(115200);
  //  input.reserve(5);
  //  sensors.begin();
  pinMode(dive, OUTPUT);
  pinMode(rise, OUTPUT);
  pinMode(portRev, OUTPUT);
  pinMode(portFwd, OUTPUT);
  pinMode(strbdRev, OUTPUT);
  pinMode(strbdFwd, OUTPUT);
}

void loop() {
  timing[0] = millis(); // loop start
  if (Serial.available() > 0) {
    input = " ";
    timing[1] = millis(); // message available
    while (Serial.available()) {
      char inChar = (char)Serial.read();
      //input = Serial.readString(); //readString is SLOW!
      input += inChar;
      //Serial.flush();
    }
    timing[2] = millis(); // message received
    Serial.println("Recieved: ");
    Serial.println(input);
    /*for(int i = 1; i < 4; i++){
     Serial.print(input[i]);
     Serial.print(" : ");
     }
     Serial.println(" message printed");*/
  }

  // Read sensor data  
  temp = getTemp(tempPin);    //currently with new sensor tmp36 // 1-wire comm is SLOW! change to analog!
  atm = round(kPaRead(pressPin));
  battVolt = getVolt(); // monitor voltage, given in 10*volt to skip float variable
  //output = String(temp) + ":" + String(atm) + ":" + String(battVolt);

  //Serial.println(getTemp());
  //Serial.println(kPaRead(pressPin));

  // read serial and update motor flags + activate motor mode
  motorUpdate(input);

  if((millis() - messageTime) > delayTime){
       messageTime = millis(); 
      printSensorValues();
  }
  //Serial.println(output);
  output = " ";
  //delay(5);

  timing[5] = millis(); // loop finished
  /*for(int i = 0; i < 6; i++){
   Serial.print(i);
   Serial.print(": ");
   Serial.println(timing[i]);
   }*/
  delay(50);
}




