# heathack

2022 code for use with our 2015 set of Jeenodes that we've built up to provide room or pipe temperature monitoring and can still use in central Scotland venues when this is useful (for checking for balance and circulation problems, or when we need to monitor lots of locations in the same building at once and don't want to use commercial loggers).

Davist's software works well and throws up a local web server, useful for knowing whether the monitoring is working without waiting to see if data appears on a web service.  However, the required node.js library is no longer maintained to run on the armv6 Pi's that we have.  

This fork just strips down the code for monitoring - nothing else that we did before - and substitutes a very simple python script that sends the data to the web service.


