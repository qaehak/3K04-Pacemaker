import serial
import struct
import time

class Connection:
    
    def __init__(self, port, params):
        self.serPort = port
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
    
    def transmit(self,mode,ARP,VRP,LRL,URL,MSR,AA,APW,VA,VPW,AVD,AS,VS,RT,AT,RF,RecT,Call):
        
        struc = struct.Struct('<BffffffffffffffffB')
        modes = {'AOO': 0,'VOO': 1,'AAI': 2,'VVI': 3,'AOOR': 4,'VOOR': 5,'AAIR': 6,'VVIR': 7}

        mode_select = modes[mode]
        ARP = float(ARP)
        VRP = float(VRP)
        LRL = float(LRL)
        URL = float(URL)
        MSR = float(MSR)
        AA = float(AA)
        APW = float(APW)
        VA = float(VA)
        VPW = float(VPW)
        AVD = float(AVD)
        AS = float(AS)
        VS = float(VS)
        RT = float(RT)
        AT = float(AT)
        RF = float(RF)
        RecT = float(RecT)
        Call = int(Call)

        packed_data = struc.pack(mode_select,ARP,VRP,LRL,URL,MSR,AA,APW,VA,VPW,AVD,AS,VS,RT,AT,RF,RecT,Call)

        print(packed_data)
        self.ser.write(packed_data)
        data = struc.unpack(packed_data)
        print(data)
        
def close_connection(self):
        if self.ser and self.ser.is_open:
            self.ser.close()
            
#     def transmit(self,mode,ARP,VRP,LRL,URL,MSR,AA,APW,VA,VPW,AVD,AS,VS,RT,AT,RF,RecT,Call,port):
#         
#         ser = serial.Serial(port, baudrate=115200)
#         struc = struct.Struct('<BffffffffffffffffB')
#         modes = {'AOO': 0,'VOO': 1,'AAI': 2,'VVI': 3,'AOOR': 4,'VOOR': 5,'AAIR': 6,'VVIR': 7}
# 
#         mode_select = modes[mode]
#         ARP = float(ARP)
#         VRP = float(VRP)
#         LRL = float(LRL)
#         URL = float(URL)
#         MSR = float(MSR)
#         AA = float(AA)
#         APW = float(APW)
#         VA = float(VA)
#         VPW = float(VPW)
#         AVD = float(AVD)
#         AS = float(AS)
#         VS = float(VS)
#         RT = float(RT)
#         AT = float(AT)
#         RF = float(RF)
#         RecT = float(RecT)
#         Call = int(Call)
# 
#         packed_data = struc.pack(mode,ARP,VRP,LRL,URL,MSR,AA,APW,VA,VPW,AVD,AS,VS,RT,AT,RF,RecT,Call)
# 
#         print(packed_data)
#         ser.write(packed_data)
#         data = struc.unpack(packed_data)
#         print(data)
#         ser.close()

# time.sleep(5)
# #transmit('AOO',0,0,60,120,0,0,0,0,0,0,0,0,0,0,0,0,0,'COM4')
#transmit('VOO',0,0,60,120,0,0,0,3.5,1,0,0,0,0,0,0,0,0,'COM4')
#transmit('VOOR',250,320,60,120,120,2.5,1,3.5,1,150,4,4,30,1.1,8,5,0,'COM4')
# transmit('AOO',0,0,60,120,0,3.5,1,0,0,0,0,0,0,0,0,0,0,'COM4')
# time.sleep(12)
# transmit('VOO',0,0,60,120,0,0,0,3.5,1,0,0,0,0,0,0,0,0,'COM4')
# time.sleep(12)
# transmit('AOOR',250,320,60,120,120,2.5,1,3.5,1,150,4,4,30,1.1,8,5,0,'COM4')
# time.sleep(12)
# transmit('VVIR',250,320,60,120,120,2.5,1,3.5,1,150,4,4,30,1.1,8,5,0,'COM4')
#transmit('AOO',0,0,60,120,0,3.5,1,0,0,0,0,0,0,0,0,0,0,'COM4')
#transmit('VOO',0,0,60,120,0,0,0,3.5,1,0,0,0,0,0,0,0,0,'COM4')
