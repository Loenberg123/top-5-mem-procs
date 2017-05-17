# top-5-mem-procs
Scripts to get the top 5 procs in memory usage for Telegraf exec input

The scripts outputs the data in Influx Line Protocol format

## Usage
For use with telegraf exec input, place the scripts in a place accesible to the telegraf user and ensure the telegraf user has permission to run the scripts.

Configure telegraf exec input plugin to use the scripts.

The data will appear on InfluxDB as a measurement named topMemProcs, and a suffix/prefix if configured.

## Example output
This is a example of the script output:

```
topMemProcs pid=4865,mem_perc=9.9,command="/usr/lib/firefox/firefox" 
topMemProcs pid=5583,mem_perc=5.2,command="/usr/lib/virtualbox/VirtualBox" 
topMemProcs pid=5535,mem_perc=5.1,command="/usr/lib/virtualbox/VirtualBox" 
topMemProcs pid=5723,mem_perc=1.5,command="/usr/lib/libreoffice/program/soffice.bin" 
topMemProcs pid=1724,mem_perc=1.3,command="/usr/bin/gnome-software"
```
