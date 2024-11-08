#   3.2.2 (4) Serial communication back-end (implement visual representation on one of the screens)
#   Author: Fatima Sarfraz (Group 3)
#   Date: October 2024
#   Helpful for this: https://pyserial.readthedocs.io/en/latest/


import serial
import struct

class Connection:

    def __init__(self,com):
        self.serPort = com # Adjust com according to unique system setup (e.g. COM3 for Windows)
        self.ser = None
        self.conn = False


    def check_connection(self,serPort):
        try:
            self.ser = serial.Serial(port=self.serPort,baudrate=115200) 
            if self.ser.is_open:
                self.conn = True # DCM and Pacemaker Shield are connected
                print("\nConnected")
            else:
                self.conn = False # DCM and Pacemaker Shield are disconnected
                print("\nNot Connected")
        except serial.SerialException as e:
            self.conn = False # Connection Failed

    def close_connection(self):
        if self.ser and self.ser.is_open:
            self.ser.close() 






    


        