# Very simple way of getting stuff off serial port to SD card.
## Possible way to also just send things to ThingSpeak, if hard to get
## the original working.

# whatever arrives on serial port, if it starts with heathack or hhpower, timestamp and log to file.
#
#adapted from code from https://github.com/openenergymonitor/EmoncmsPythonLink 
# website says that's GNU GPL.
import argparse
import serial, sys, string # serial is pyserial
import httplib
from datetime import datetime

parser = argparse.ArgumentParser(
   prog = "heathack-jeenode-monitor.py",
   description = "Sends data coming from a Jeenode to ThingSpeak, logs it to a file, or both"
   epilog = "Use e.g. --log '/var/log/jeenode.log' to log to a file, specifying the full path; it will append if the file exists. \\n Add --noweb if you only want to log to the SD card. \\n If pi does not have internet access, you should set its date and time manually and expect it to drift, especially in cold spaces."
)
parser.add_argument("--noweb", help="don't attempt to send readings to ThingSpeak (for if you have no internet")
parser.add_argument("--log", help="log readings to file (for if your card has space)", nargs = "?", default="/var/log/jeenode.log", type=str)
parser.add_argument("serialport", help="serial port to use (default: /dev/ttyUSB0)", nargs="?", default="/dev/ttyUSB0" type=str)
parser.add_argument("baudrate",  help="baud rate to use (default: 9600)", nargs="?", default=9600, type=int)
args = parser.parse_args()


sys.stderr.write("Temp and RH Logging: Starting at "+ datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "\n")

# Set this to the serial port of your Jeelink and baud rate, 9600 is standard emontx baud rate
#ser = serial.Serial('/dev/ttyUSB0', 9600) for CISECO radio

ser = serial.Serial(ars.serialport,args.baudrate)


API_KEY         = 'INSERT_KEY_HERE'
API_URL         = 'https://api.thingspeak.com/update'

while True:
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
 sys.stderr.write(linestr)
 
 # Split the line at the whitespaces
 array = linestr.split(' ') # python data type: list

# if (array[0] == ('hhpower' or 'heathack')): 

if (args.log):
   with open(args.outfile, 'a') as f:
      f.write(linestr)
      f.write(" ")
      f.write(str(datetime.now()))
      f.write("\n")
      f.close()

if (not (args.noweb)):

