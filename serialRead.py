import serial, time

ser = serial.Serial('/dev/ttyACM0', 115200)
ser.close()
ser.open()
while True:
	state = raw_input("motor config")
	try:
		ser.write(state)
		time.sleep(2)
		print("Sent commands")
	except:
		pass
	try:
		msg1 = ser.readline()
		msg2 = ser.readline()
		print(msg1 + " " + msg2)
	except:
		pass
