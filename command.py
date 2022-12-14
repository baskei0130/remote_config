import datetime
from multiprocessing.connection import wait
import read_file
import glossary
import time

def output_show(ip,port,show_list,tn):
    log_name = glossary.set_telnet_log_name(ip,port,"show_result")
    
    print("Commands in '", show_list,"' will be issued.")
    command_list = read_file.txt_read(show_list)
    
    tn.write(b"\r\n")
    tn.write(b"\r\n")
    glossary.telnet_log(log_name,tn.read_until(b"#").decode('ascii'))
    tn.write(b"terminal length 0\n")
    glossary.telnet_log(log_name,tn.read_until(b"#").decode('ascii'))
    tn.write(b"\n")

    for com in command_list:
        print("... " + com)
        tn.write(com.encode('ascii') + b"\n")

    tn.write(b"!!!!!! DONE !!!!!!" + b"\n")
    glossary.telnet_log(log_name,tn.read_until(b"!!!!!! DONE !!!!!!").decode('ascii'))
        
    tn.write(b"terminal default length\n")
    #output = tn.read_until(b"!!!!!! DONE !!!!!!").decode('ascii')


    tn.write(b"\n")
    glossary.telnet_log(log_name,tn.read_until(b"#").decode('ascii'))
    
    # Make output file and write output in it
    #dt_now = datetime.datetime.now()
    #log_output = ip + "_" + port + "_" + dt_now.strftime('%Y%m%d-%H%M%S-%f') + "_" + "show_result.txt"
    #f_log = open(log_output,mode="w", newline="", encoding="ms932")
    #f_log.write("\n---- (telnet " + ip + " : " + port +") ----\n")
    #f_log.write(output)
    #f_log.close()

    print("... Done!")
    #print("### ", log_output, "is created.")
    print("### "+ log_name +"is created.")
    

def input_conf(ip,port,config_list,tn, sleep):
    
    print("Commands in '", config_list,"' will be issued.")
    command_list = read_file.txt_read(config_list)

    tn.write(b"\r\n")
    tn.write(b"\r\n")
    tn.read_until(b"#")
    tn.write(b"configure terminal\n")
    tn.read_until(b"#")
    tn.write(b"\n")

    for com in command_list:
        print("... " + com)
        tn.write(com.encode('ascii') + b"\n")
        time.sleep(sleep)

    tn.write(b"end\n")
    tn.write(b"!!!!!! DONE !!!!!!" + b"\n")
    #output = tn.read_until(b"!!!!!! DONE !!!!!!").decode('ascii')

    tn.write(b"\n")
    tn.read_until(b"#")
    
    # Make output file and write output in it
    #dt_now = datetime.datetime.now()
    #log_output = ip + "_" + port + "_" + dt_now.strftime('%Y%m%d-%H%M%S-%f') + "_" + "config_result.txt"
    #f_log = open(log_output,mode="w", newline="", encoding="ms932")
    #f_log.write("\n---- (telnet " + ip + " : " + port +") ----\n")
    #f_log.write(output)
    #f_log.close()

    print("... Done!")
    #print("### ", log_output, "is created.")
