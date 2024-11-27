#   3.2.2 (4) Serial communication back-end (implement visual representation on one of the screens)
#   Author: Fatima Sarfraz (Group 3)
#   Date: October 2024
#   Helpful for this: https://pyserial.readthedocs.io/en/latest/
#   https://docs.python.org/3/library/struct.html
#   https://stackoverflow.com/questions/24956308/how-to-write-integers-to-port-using-pyserial
# ONLY FOR SENDING PACKETS TO PACEMAKER
#
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


    def connect(self):
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
    
    def transmit(self):
        #-----------signal to pacemaker data is coming------------
        sync = 22 # 0x16
        fn_code = 85 #0x55
        state = str.encode(self.params.get_state())
        data_binary = b''
        
        data_binary += struct.pack('>B', sync) #little endian
        data_binary += struct.pack('>B', fn_code)
        data_binary += struct.pack('>3s', state) #3-byte char array (string)
        
        print("\n")
        print(data_binary)   #for debugging
        
        #send via UART
        self.ser.write(data_binary)
        
        #---------------Pack relevant parameters based on mode--------------
        if (state == "AOO"):
            self.pack_AOO()
        elif (state == "VOO"):
            self.pack_VOO()
        elif (state == "AAI"):
            self.pack_AAI()
        elif (state == "VVI"):
            self.pack_VVI()
        elif (state == "AOOR"):
            self.pack_AOOR()
        elif (state == "VOOR"):
            self.pack_VOOR()
        elif (state == "AAIR"):
            self.pack_AAIR()
        elif (state == "VVIR"):
            self.pack_VVIR()
        
    
    
    #-----------------------------Packing functions---------------------------------
    # TRANSMISSION ORDER IS AS FOLLOWS: sync (1byte), fn_code(1byte), mode(3bytes), ARP, VRP, LowerRateLimit, UpperRateLimit,
    # MaxSensorRate, AtrialAmplitude, AtrialPulseWidth, VentricularAmplitude, VentricularPulseWidth,
    # AtrialSensitivity, VentricalSensitivity, ReactionTime, ActivityThreshold, ResponseFactor, RecoveryTime
    
    def pack_AOO(self):
        data = [0,0, float(self.params.get_LowerRateLimit()), float(self.params.get_UpperRateLimit()), 0,  float(self.params.get_AtrialAmplitude()),
                float(self.params.get_AtrialPulseWidth()), 0, 0, 0, 0, 0, 0, 0, 0]
        
        data_binary = b''
        
        #pack each element
        for d in data:
            data_binary += struct.pack('<f', d) #little endian float
        
        print("\n")
        print(data_binary)
        
        #send via UART here:
        self.ser.write(data_binary)
        
        
        
    def pack_VOO(self):
        data = [0,0, float(self.params.get_LowerRateLimit()), float(self.params.get_UpperRateLimit()), 0, 0, 0,
                float(self.params.get_VentricularAmplitude()), float(self.params.get_VentricularPulseWidth()), 0, 0, 0, 0, 0, 0]
        
        data_binary = b''
        
        #pack each element
        for d in data:
            data_binary += struct.pack('<f', d) #little endian float
            
        #send via UART here:
        self.ser.write(data_binary)
        
            

    def pack_AAI(self):
        data = [float(self.params.get_ARP()), 0, float(self.params.get_LowerRateLimit()), float(self.params.get_UpperRateLimit()), 0,  float(self.params.get_AtrialAmplitude()),
                float(self.params.get_AtrialPulseWidth()), 0, 0, 0, 0, 0, 0, 0, 0]
        
        data_binary = b''
        
        #pack each element
        for d in data:
            data_binary += struct.pack('<f', d) #little endian float
         
        print("\n")
        print(data_binary)
        
        #send via UART here:
        self.ser.write(data_binary)    
            
    
    def pack_VVI(self):
        data = [0, float(self.params.get_VRP()), float(self.params.get_LowerRateLimit()), float(self.params.get_UpperRateLimit()), 0, 0, 0,
                float(self.params.get_VentricularAmplitude()), float(self.params.get_VentricularPulseWidth()), 0, 0, 0, 0, 0, 0]
        
        data_binary = b''
        
        #pack each element
        for d in data:
            data_binary += struct.pack('<f', d) #little endian float
        
        print("\n")
        print(data_binary)
        
        #send via UART here:
        self.ser.write(data_binary)    
            
    def pack_AOOR(self):
        data = [0, 0, float(self.params.get_LowerRateLimit()), float(self.params.get_UpperRateLimit()), float(self.params.get_MaxSensorRate()),
                float(self.params.get_AtrialAmplitude()), float(self.params.get_AtrialPulseWidth()), 0, 0, 0, 0, float(self.params.get_ReactionTime()),
                float(self.params.get_ActivityThreshold()), float(self.params.get_ResponseFactor()), float(self.params.get_RecoveryTime())]
        
        data_binary = b''
        
        #pack each element
        for d in data:
            data_binary += struct.pack('<f', d) #little endian float
        
        print("\n")
        print(data_binary)
        
        #send via UART here:
        self.ser.write(data_binary)    
            
            
    def pack_VOO(self):
        data = [0, 0, float(self.params.get_LowerRateLimit()), float(self.params.get_UpperRateLimit()), float(self.params.get_MaxSensorRate()), 0, 0,
                float(self.params.get_VentricularAmplitude()), float(self.params.get_VentricularPulseWidth()), 0, 0, float(self.params.get_ReactionTime()),
                float(self.params.get_ActivityThreshold()), float(self.params.get_ResponseFactor()), float(self.params.get_RecoveryTime())]

        
        data_binary = b''
        
        #pack each element
        for d in data:
            data_binary += struct.pack('<f', d) #little endian float
        
        print("\n")
        print(data_binary)
        
        #send via UART here:
        self.ser.write(data_binary)      

    def pack_AAIR(self):
        # PVARP ???? Hysteresis ????
        data = [float(self.params.get_ARP()), 0, float(self.params.get_LowerRateLimit()), float(self.params.get_UpperRateLimit()), float(self.params.get_MaxSensorRate()),
                float(self.params.get_AtrialAmplitude()), float(self.params.get_AtrialPulseWidth()), 0, 0, float(self.params.get_AtrialSensitivity()), 0,
                float(self.params.get_ReactionTime()), float(self.params.get_ActivityThreshold()), float(self.params.get_ResponseFactor()), float(self.params.get_RecoveryTime())]
        
        data_binary = b''
        
        #pack each element
        for d in data:
            data_binary += struct.pack('<f', d) #little endian float
            
        print("\n")
        print(data_binary)
        
        #send via UART here:
        self.ser.write(data_binary)
        
        
            
    def pack_VVIR(self):
        # RATE SMOOTHING ????
        data = [0, float(self.params.get_VRP()), float(self.params.get_LowerRateLimit()), float(self.params.get_UpperRateLimit()), float(self.params.get_MaxSensorRate()), 0, 0,
                float(self.params.get_VentricularAmplitude()), float(self.params.get_VentricularPulseWidth()), 0, float(self.params.get_VentricularSensitivity()), float(self.params.get_ReactionTime()),
                float(self.params.get_ActivityThreshold()), float(self.params.get_ResponseFactor()), float(self.params.get_RecoveryTime())]
        
        data_binary = b''
        
        #pack each element
        for d in data:
            data_binary += struct.pack('<f', d) #little endian float
        
        print("\n")
        print(data_binary)
        
        #send via UART here:
        self.ser.write(data_binary)      
    
    
    def close_connection(self):
        if self.ser and self.ser.is_open:
            self.ser.close() 






    


        