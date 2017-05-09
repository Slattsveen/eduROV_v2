void motorUpdate(String msg) {
  timing[3] = millis(); // motorfunction called
  // expects a 3 digit string, values 0, 1 or 2

  //Diving/rising motor
  if (msg[1] == '1') {
    //Serial.println("i = 0 -> 1");
    digitalWrite(dive, HIGH);
    digitalWrite(rise, LOW);
  } else if (msg[1] == '2') {
    //Serial.println("i = 0 -> 2");
    digitalWrite(dive, LOW);
    digitalWrite(rise, HIGH);
  } else {
    //Serial.println("i = 0 -> 0");
    digitalWrite(dive, LOW);
    digitalWrite(rise, LOW);
  }

  // port motor
  if (msg[2] == '1') {
    //Serial.println("i = 1 -> 1");
    digitalWrite(portFwd, HIGH);  //the pairs can not be HIGH at the same time! will fry the control board!
    digitalWrite(portRev, LOW);
  } else if (msg[2] == '2') {
    //Serial.println("i = 1 -> 2");
    digitalWrite(portFwd, LOW);
    digitalWrite(portRev, HIGH);
  } else {
    //Serial.println("i = 1 -> 0");
    digitalWrite(portFwd, LOW);
    digitalWrite(portRev, LOW);
  }

  //starboard motor
  if (msg[3] == '1') {
    //Serial.println("i = 2 -> 1");
    digitalWrite(strbdFwd, HIGH);
    digitalWrite(strbdRev, LOW);
  } else if (msg[3] == '2') {
    //Serial.println("i = 2 -> 2");
    digitalWrite(strbdFwd, LOW);
    digitalWrite(strbdRev, HIGH);
  } else {
    //Serial.println("i = 2 -> 0");
    digitalWrite(strbdFwd, LOW);
    digitalWrite(strbdRev, LOW);
  }
  timing[4] = millis(); //motorfunction finished
}


// avoid control mishaps, example: Serial.println(controlAnalyser("110", "120")); returns 100

String controlAnalyser(String msg1, String msg2) {
  String result = "000";
  for (int i = 0; i < 2; i++) { // maybe only run for i= 1, 2. Let diving and rising be overwritten if a new direction is sent
    if (msg1[i] == msg2[i]) {
      result[i] = msg1[i];
    }
  }
  return result;
}

