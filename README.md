# remote_config
This can make you change the configuration on the remote router or switch.

## Need to do
1. Install python3 in your environment
2. Clone this repository on your running machine

## How to run
1. Go to this directory 
2. Put your configuration file to config directory
- There are some example files on config directory, please check these files.
3. Change the telnet-list.csv or Put your original csv file.
- See the example written in telnet-list.csv
- If you don't set the username, telnet password, or enable password, **leave blank the places**
  - Below sentence is the example, if you don't set the username, telnet password, and enable password.
```10.71.134.177,23,,,,./config/20221017-ip.txt```
4. Run the program below
```
source env/bin/activate
python3 maincode.py
```
- Input CSV file and Sleep time after each command input.