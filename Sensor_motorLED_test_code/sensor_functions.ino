double kPaRead(int pin) {
  double val = analogRead(pin);
  double vo = 5.0 * (val / 1023);
  double p = 250 * (vo / 5) + 10;
  return p;
}

double getTemp(int pin) {
  /*for(int i = 0; i < 5; i++){
    analogRead(pin);
  }*/
  //reading tmp36 at analogpin "pin"

  double tempVals = 0;
  for (int i = 0; i < 10; i++) {
    double sensorMilliVolt = analogRead(pin) * (5000.0 / 1024);
    tempVals += (sensorMilliVolt - 500) / 10;
  }
  return (tempVals / 10);
}

int getVolt(){
  double volt = double(analogRead(battVoltPin)) * (5.0 / 1023); // define double variable by using . like 5.0
  return int(2 * volt);
}

void printSensorValues(){
  Serial.print(temp);
  Serial.print(':');
  Serial.print(atm);
  Serial.print(':');
  Serial.println(battVolt);
}

