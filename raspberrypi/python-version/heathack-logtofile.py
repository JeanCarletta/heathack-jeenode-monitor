# Very simple way of getting stuff off serial port to SD card.
## Possible way to also just send things to ThingSpeak, if hard to get
## the original working.

# whatever arrives on serial port, if it starts with heathack or hhpower, timestamp and log to file.
#
#adapted from code from https://github.com/openenergymonitor/EmoncmsPythonLink 
# website says that's GNU GPL.
import argparse
import serial, sys, string
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument("logfile", help="path and name of file to log the data - new data will be appended to it", type=str)
args = parser.parse_args()
print(args.logfile)

# Set this to the serial port of your Jeelink and baud rate, 9600 is standard emontx baud rate
ser = serial.Serial('/dev/ttyUSB0', 9600)
# or for the Ciseco radio
#ser = serial.Serial('/dev/ttyS0',9600)

while 1:
 # Read in line of readings from Jeelink serial
 ##python2: readline returns a string.  
 ##python3: readline returns binary that needs decoded to a string.
 ## in python3, unlike python2, readline returns binary 
   linestr = ser.readline().decode().rstrip()
   # our data format for temperature and humidity etc. looks like this:
   #heathack 23 4 1 16.6
   #heathack NODENUM SENSORNUM READINGTYPE READING
   # sensor num isn't very useful.  ReadingType is 1 for temperature, 2 for RH
   #print(linestr)
 
   # Split the line at the whitespaces
   array = linestr.split(' ') # python data type: list
   #print(len(array[0]))
   #print(len('heathack'))

   if (array[0] == 'heathack'):
      print("found a reading")
      with open(args.logfile, 'a') as f:
         f.write(linestr)
         f.write(" ")
         f.write(str(datetime.now().strftime('%Y%m%d %H:%M:%S')))
         f.write("\n")
         f.close()
