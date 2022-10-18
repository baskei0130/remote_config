import os
import csv
import sys
import datetime
import telnetlib
import read_file
import prompt
import command

#import prompt
# Check csv file is exist


# Read csv and put into host_list[]
# lineinput = input("Input Telnet list file .csv:")
lineinput = input("input the telnet list file (CSV format)") # 今回専用
telnet_list = read_file.csv_read(lineinput)
print(telnet_list)

# set telnet list to each parameter
for i in range(len(telnet_list)):
  #Import param from telnet_list
  ip = telnet_list[i][0]

  port = telnet_list[i][1]
  Username = telnet_list[i][2]
  tel_password = telnet_list[i][3]
  en_password = telnet_list[i][4]
  config_list = telnet_list[i][5]

  tn = telnetlib.Telnet(ip,port,900)
  prompt.enable(ip,port,Username,tel_password,en_password,tn)
  command.input_conf(ip,port,config_list,tn)

  print("Done:"+ ip +"-"+ port +". Close Telnet port...")
  tn.close()