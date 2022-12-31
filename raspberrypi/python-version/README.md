This software for the pi relies only on python 3 with pyserial and requests modules.  You **can't** use the serial module with it.  Python only version - this works and is our preferred option.

Python 3.

We use crontab to run it making sure the user is in the dialout group and the python script is executable.

:TODO: would a service be more reliable?

# To log data from a Current Cost clamp-on electricity monitor using a Pi


1. Create a standard Raspberry Pi OS image on an SD card, boot,
update/upgrade as usual, Attach monitor to electric meter following
the instructions in the box.

2. make sure you have python3 and pip; pip install pyserial and pip install requests.

3.  Ensure user is in dialout group and python script is executable

4. add call to end of user crontab  - choosing the paths you want

@reboot python /home/jeanc/currentcostmonitor/python-only/currentcost-to-thingspeak-standalone.py /home/jeanc/currentcost.csv 2> /home/jeanc/currentcost-error.log

5. Stick a CSV file on the pi that has the jeenode node numbers in the first column and the corresponding ThingSpeak API write keys in the second column - don't put this CSV file in Github.  You'll need the name of the CSV file to use as a command line argument.

6. Jeenode USB attached to pi with HeatHackReceiver flashed to it.

7.  Second Jeenode set up to transmit using a sensor and JeeNodeEnvironMon.

8. Plug in the Pi.  The logging service will start automatically. If
the Pi loses power, the service will restart when it is powered up
again BUT if the Pi has no internet the date and time will be wrong even in the local logs.

# What it does

The service logs to stderr (redirected in the crontab to your choice of file).
It puts csv output in the file you name and also sends data to ThingSpeak.


