import serial

ser = serial.Serial('/dev/rfcomm0', 9600,timeout=0)


data = "nodetect\r\n"
ser.write(data.encode('utf-8'))

