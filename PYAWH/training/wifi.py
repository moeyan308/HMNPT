#!/usr/bin/python 3
#Wi-Fi Hotspot Enabler

import os
os.system("cls")
print("\n\n\n\n")
cmd= "0"
while cmd != "3":

    print("type 1 to start program")
    print("type 2 to stop program")
    print("type 3 to end program")
    cmd = input("Please enter your Choice....")
    if cmd == "1":
        ssid = input("Please enter Hotspot name....")
        password = input("Please enter Password....")
        print("netsh wlan set hostednetwork mode=allow ssid="+ ssid +" key="+password)
        os.system("netsh wlan set hostednetwork mode=allow ssid="+ ssid +" key="+password)
        os.system("netsh wlan start hostednetwork")
        print("Wifi Hotspot Enable........")
    elif cmd == "2":
        os.system("netsh wlan stop hostednetwork")
        print("Hotspot Disable")
    elif cmd == "3":
        print("Program exit.")
        quit()
    else:
        print("Bad input, Please try again.")


