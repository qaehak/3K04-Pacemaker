#   3.2.2 (4) Serial communication back-end (implement visual representation on one of the screens)
#   Author: Fatima Sarfraz (Group 3)
#   Date: October 2024
#   Helpful for this: https://pyserial.readthedocs.io/en/latest/
#   https://docs.python.org/3/library/struct.html
#   https://stackoverflow.com/questions/24956308/how-to-write-integers-to-port-using-pyserial


import serial
import struct
import param

class Connection:

    def __init__(self,com, params):
        self.serPort = com # Adjust com according to unique system setup (e.g. COM3 for Windows)
        self.ser = None
        self.conn = False
        self.status = 0 # disconnected = 0, connected = 1
        self.params = params


    def check_connection(self,serPort):
        try:
            self.ser = serial.Serial(port=self.serPort,baudrate=115200) 
            if self.ser.is_open:
                self.conn = True # DCM and Pacemaker Shield are connected
                self.status = 1
                print("\nConnected")
            else:
                self.conn = False # DCM and Pacemaker Shield are disconnected
                self.status = 0
                print("\nNot Connected")
        except serial.SerialException as e:
            self.conn = False # Connection Failed
    
        
    def get_connection(self):
        return self.status
    
    def pack_AOO(self):
        data = [self.mode, self.params.get_LowerRateLimit(), self.params.get_UpperRateLimit(), self.params.get_AtrialAmplitude(),
                self.params.get_AtrialPulseWidth()]
        
        data_binary = b''
        
        #pack each element
        for p in data:
            data_binary += struct.pack('<B', p) #little endian
        
        print("\n")
        print(data_binary)
        
        #send via UART here:
        self.ser.write(data_binary)
        
    def pack_VOO(self):
        data = [self.params.get_state(), self.params.get_LowerRateLimit(), self.params.get_UpperRateLimit(), self.params.get_VentricularAmplitude(),
                self.params.get_VentricularPulseWidth()]
        
        data_binary = b''
        
        #pack each element
        for p in data:
            data_binary += struct.pack('<B', p) #little endian
            
        #send via UART here:
        self.ser.write(data_binary)
            

    def pack_AAI(self):
        data = [self.params.get_state(), self.params.get_LowerRateLimit(), self.params.get_UpperRateLimit(), self.params.get_AtrialAmplitude(),
                self.params.get_AtrialPulseWidth(), self.params.get_ARP()]
        
        data_binary = b''
        
        #pack each element
        for p in data:
            data_binary += struct.pack('<B', p) #little endian
         
        print("\n")
        print(data_binary)
        
        #send via UART here:
        self.ser.write(data_binary)    
            
    
    def pack_VVI(self):
        data = [self.params.get_state(), self.params.get_LowerRateLimit(), self.params.get_UpperRateLimit(), self.params.get_VentricularAmplitude(),
                self.params.get_VentricularPulseWidth(), self.params.get_VRP()]
        
        data_binary = b''
        
        #pack each element
        for p in data:
            data_binary += struct.pack('<B', p) #little endian
        
        print("\n")
        print(data_binary)
        
        #send via UART here:
        self.ser.write(data_binary)    
            
    def pack_AOOR(self):
        data = [self.params.get_state(), self.params.get_LowerRateLimit(), self.params.get_UpperRateLimit(), self.params.get_AtrialAmplitude(),
                self.params.get_AtrialPulseWidth(), self.params.get_MaxSensorRate(), self.params.get_ActivityThreshold(),
                self.params.get_ReactionTime(), self.params.get_ResponseFactor(), self.params.get_RecoveryTime()]
        
        data_binary = b''
        
        #pack each element
        for p in data:
            data_binary += struct.pack('<B', p) #little endian
        
        print("\n")
        print(data_binary)
        
        #send via UART here:
        self.ser.write(data_binary)    
            
            
    def pack_VOO(self):
        data = [self.params.get_state(), self.params.get_LowerRateLimit(), self.params.get_UpperRateLimit(), self.params.get_VentricularAmplitude(),
                self.params.get_VentricularPulseWidth(), self.params.get_MaxSensorRate(), self.params.get_ActivityThreshold(),
                self.params.get_ReactionTime(), self.params.get_ResponseFactor(), self.params.get_RecoveryTime()]
        
        data_binary = b''
        
        #pack each element
        for p in data:
            data_binary += struct.pack('<B', p) #little endian
        
        print("\n")
        print(data_binary)
        
        #send via UART here:
        self.ser.write(data_binary)      

    def pack_AAIR(self):
        data = [self.params.get_state(), self.params.get_LowerRateLimit(), self.params.get_UpperRateLimit(), self.params.get_AtrialAmplitude(),
                self.params.get_AtrialPulseWidth(), self.params.get_ARP(), self.params.get_MaxSensorRate()
                self.params.get_AtrialSensitivity(), self.params.get_PVARP(), self.params.get_Hysteresis(),
                self.params.get_RateSmoothing(), self.params.get_ActivityThreshold(), self.params.get_ReactionTime(),
                self.params.get_ResponseFactor(), self.params.get_RecoveryTime()]
        
        data_binary = b''
        
        #pack each element
        for p in data:
            data_binary += struct.pack('<B', p) #little endian
            
        print("\n")
        print(data_binary)
        
        #send via UART here:
        self.ser.write(data_binary)      
            
    def pack_VVIR(self):
        data = [self.params.get_state(), self.params.get_LowerRateLimit(), self.params.get_UpperRateLimit(), self.params.get_VentricularAmplitude(),
                self.params.get_VentricularPulseWidth(), self.params.get_VRP(), self.params.get_MaxSensorRate()
                self.params.get_VentricularSensitivity(), self.params.get_Hysteresis(),
                self.params.get_RateSmoothing(), self.params.get_ActivityThreshold(), self.params.get_ReactionTime(),
                self.params.get_ResponseFactor(), self.params.get_RecoveryTime()]
        
        data_binary = b''
        
        #pack each element
        for p in data:
            data_binary += struct.pack('<B', p) #little endian
        
        print("\n")
        print(data_binary)
        
        #send via UART here:
        self.ser.write(data_binary)      
    
    def recieve_data(self):
        print("recieving data")
        # use while loop to wait for data - maybe in WelcomePage.py
        # have some logic for interupting loop when data needs to be sent

    
    def close_connection(self):
        if self.ser and self.ser.is_open:
            self.ser.close() 






    


        