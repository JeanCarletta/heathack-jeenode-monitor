# Very simple way of getting stuff off serial port to SD card.
## Possible way to also just send things to ThingSpeak, if hard to get
## the original working.

# whatever arrives on serial port, if it starts with heathack or hhpower, timestamp and log to file.
#
#adapted from code from https://github.com/openenergymonitor/EmoncmsPythonLink 
# website says that's GNU GPL.
import argparse
import serial, sys, string
import httplib
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument("logfile", help="path and name of file to log the data - new data will be appended to it", type=str)
args = parser.parse_args()
print args.logfile

# Set this to the serial port of your Jeelink and baud rate, 9600 is standard emontx baud rate
#ser = serial.Serial('/dev/ttyUSB0', 9600)
# or for the Ciseco radio
ser = serial.Serial('/dev/ttyS0',9600)

while 1:
 # Read in line of readings from Jeelink serial
 linestr = ser.readline()
 # Remove the new line at the end
 linestr = linestr.rstrip()
 # our data format for temperature and humidity etc. looks like this:
 #heathack 23 4 1 16.6
 #heathack NODENUM SENSORNUM READINGTYPE READING
 # where READINGTYPE is 1 for temp
 # for current sensing, it's still space-delimited:
 # hhpower NUM ...NUM
 print linestr
 
 # Split the line at the whitespaces
 array = linestr.split(' ') # python data type: list

# if (array[0] == ('hhpower' or 'heathack')): 
  
with open(args.logfile, 'a') as f:
   f.write(linestr)
   f.write(" ")
   f.write(str(datetime.now()))
   f.write("\n")
   f.close()
