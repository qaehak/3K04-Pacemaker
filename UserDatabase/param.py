# This program reads and saves relevant parameters for the pacemaker using a local file. The state of the pacemaker is also stored.
#
# Author: Serena Santos
# Date: October 2024
#
# Text file formatting:
# - VOO.txt
#         Line 1 = VOO, Line 2 = Lower Rate Limit (LRL), Line 3 = Upper Rate Limit (URL),
#         Line 4 = Ventricular Amplitude (VA), Line 5 = Ventricular Pulse Width (VPW)
# - AOO.txt
#         Line 1 = AOO, Line 2 = Lower Rate Limit (LRL), Line 3 = Upper Rate Limit (URL),
#         Line 4 = Atrial Amplitude (AA), Line 5 = Atrial Pulse Width (APW), Line 6 = ARP
# - AAI.txt
#         Line 1 = AAI, Line 2 = Lower Rate Limit (LRL), Line 3 = Upper Rate Limit (URL),
#         Line 4 = Atrial Amplitude (AA), Line 5 = Atrial Pulse Width (APW), Line 6 = ARP
# - VVI.txt
#         Line 1 = VVI, Line 2 = Lower Rate Limit (LRL), Line 3 = Upper Rate Limit (URL),
#         Line 4 = Ventricular Amplitude (VA), Line 5 = Ventricular Pulse Width (VPW), Line 6 = ARP
# - AOOR.txt
#         Line 1 = AOOR, Line 2 = Lower Rate Limit (LRL), Line 3 = Upper Rate Limit (URL),
#         Line 4 = Atrial Amplitude (AA), Line 5 = Atrial Pulse Width (APW), Line 6 = Maximum Sensor Rate (MSR),
#         Line 7 = Activity Threshold (AT), Line 8 = Reaction Time (RT),
#         Line 9 = Response Factor (RF), Line 10 = Recovery Time (RECT)
#
# - VOOR.txt
#         Line 1 = AOOR, Line 2 = Lower Rate Limit (LRL), Line 3 = Upper Rate Limit (URL),
#         Line 4 = Ventricular Amplitude (VA), Line 5 = Ventricular Pulse Width (VPW),
#         Line 6 = Maximum Sensor Rate (MSR), Line 7 = Activity Threshold (AT), Line 8 = Reaction Time (RT),
#         Line 9 = Response Factor (RF), Line 10 = Recovery Time (RECT)
# - AAIR.txt
#         Line 1 = AAIR, Line 2 = Lower Rate Limit (LRL), Line 3 = Upper Rate Limit (URL),
#         Line 4 = Atrial Amplitude (AA), Line 5 = Atrial Pulse Width (APW), Line 6 = ARP,
#         Line 7 = Maximum Sensor Rate (MSR), Line 8 = Atrial Sensitivity (AS), Line 9 = PVARP, Line 10 = Hysteresis (H),
#         Line 11 = Rate Smoothing (RS), Line 12 = Activity Threshold (AT), Line 13 = Reaction Time (RT),
#         Line 14 = Response Factor (RF), Line 15 = Recovery Time (RECT)
# - VVIR.txt
#         Line 1 = VVIR, Line 2 = Lower Rate Limit (LRL), Line 3 = Upper Rate Limit (URL),
#         Line 4 = Ventricular Amplitude (VA), Line 5 = Ventricular Pulse Width (VPW), Line 6 = VRP
#         Line 7 = Maximum Sensor Rate (MSR), Line 8 = Ventricular Sensitivity (VS), Line 9 = Hysteresis (H),
#         Line 10 = Rate Smoothing (RS), Line 11 = Activity Threshold (AT), Line 12 = Reaction Time (RT),
#         Line 13 = Response Factor (RF), Line 14 = Recovery Time (RECT)


# Extra Parameters to add possibly Atrial Sensitivity, PVARP, Hysteresis, Rate smoothing,
# Ventricular Sensitivity
#               
# Note that states can be either AOO, VOO, AAI, VVI, AOOR, VOOR, AAIR, and VVIR
#
#
# Function List:
#        - __init__(self): Constructor
#        - save_param(self, param, line): Saves a new parameter to local file using line as index
#        - load_param_VOO(self): Loads parameters from local file for VOO to member variables
#        - load_param_VVI(self): Loads parameters from local file for VVI to member variables
#        - load_param_AOO_AAI(self): Loads parameters from local file for AAO or AAI to member variables
#        - load_param_AOOR(self): Loads parameters from local file for AOOR to member variables
#        - load_param_VOOR(self): Loads parameters from local file for VOOR to member variables
#        - load_param_AAIR(self): Loads parameters from local file for AAIR to member variables
#        - load_param_VVIR(self): Loads parameters from local file for VVIR to member variables
#        - get_file_Name(self): Helper function; Sets member variable file_name to the appropriate path based on state

#        - get_state(self): getter; returns state
#        - get_LowerRateLimit(self): getter; returns LRL
#        - get_UpperRateLimit(self): getter; returns URL
#        - get_AtrialAmplitude(self): getter; returns AA
#        - get_AtrialPulseWidth(self): getter; returns APW
#        - get_VentricularAmplitude(self): getter; returns VA
#        - get_VentricularPulseWidth(self): getter; returns VPW
#        - get_VRP(self): getter; returns VRP
#        - get_ARP(self): getter; returns ARP
#        - get_MaxSensorRate(self): getter; returns MSR
#        - get_AtrialSensitivity(self): getter; returns AS
#        - get_VentricularSensitivity(self): getter; returns VS
#        - get_PVARP(self): getter; returns PVARP
#        - get_Hysteresis(self): getter; returns H
#        - get_RateSmoothing(self): getter; returns RS
#        - get_ActivityThreshold(self): getter; returns AT
#        - get_ReactionTime(self): getter; returns RT
#        - get_ResponseFactor(self): getter; returns RF
#        - get_RecoveryTime(self): getter; returns RECT

#        - set_state(self, state): setter; sets state and saves to file
#        - set_LowerRateLimit(self, new_LRL): setter; sets LRL and saves to file
#        - set_UpperRateLimit(self, new_URL): setter; sets URL and saves to file
#        - set_AtrialAmplitude(self, new_AA): setter; sets AA and saves to file
#        - set_AtrialPulseWidth(self, new_APW): setter; sets APW and saves to file
#        - set_VentricularAmplitude(self, new_VA): setter; sets VA and saves to file
#        - set_VentricularPulseWidth(self, new_VPW): setter; sets VPW and saves to file
#        - set_VRP(self, new_VRP): setter; sets VRP and saves to file
#        - set_ARP(self, new_ARP): setter; sets ARP and saves to file
#        - set_MaxSensorRate(self, new_ARP): setter; sets MSR and saves to file
#        - set_AtrialSensitivity(self, new_ARP): setter; sets AS and saves to file
#        - set_VentricularSensitivity(self, new_ARP): setter; sets VS and saves to file
#        - set_PVARP(self, new_ARP): setter; sets PVARP and saves to file
#        - set_Hysteresis(self, new_ARP): setter; sets H and saves to file
#        - set_RateSmoothing(self, new_ARP): setter; sets RS and saves to file
#        - set_ActivityThreshold(self, new_ARP): setter; sets AT and saves to file
#        - set_ReactionTime(self, new_ARP): setter; sets RT and saves to file
#        - set_ResponseFactor(self, new_ARP): setter; sets RF and saves to file
#        - set_RecoveryTime(self, new_ARP): setter; sets RECT and saves to file
#
import os
class param:
    
        
    def __init__(self):
        #initialize member variables
        self.file_name = os.path.join(os.path.dirname(__file__),"AOO.txt")
        self.state = "AOO"
        self.LRL = '0'
        self.URL = '0'
        self.AA = '0'
        self.APW = '0'
        self.VA = '0'
        self.VPW = '0'
        self.VRP = '0'
        self.ARP = '0'
        self.AS = '0'
        self.VS = '0'
        self.MSR = '0'
        self.PVARP = '0'
        self.H = '0'
        self.RS = '0'
        self.AT = '0'
        self.RT = '0'
        self.RF = '0'
        self.RECT = '0'
        #load default values for AOO
        self.load_param_AOO_AAI()
        
        
    def save_param(self, param, line):
        self.get_file_Name()
        
        #create file object and read all lines
        with open(self.file_name) as f:
            lines = f.readlines()
            
        #overwrite new param to relevant line
        lines[line-1] = str(param).strip() + "\n"
        
        #save edits to file
        with open(self.file_name, "w") as f:
            for l in lines:
                f.write(l)
                        
 # ------------------- load functions ---------------------------------------               
    def load_param_VOO(self):
        self.get_file_Name()
        #create text file in reading mode
        with open(self.file_name, "r") as f:
            #save each line to its respective variable
            
            #Common to all file
            self.state = f.readline()
            self.LRL = f.readline()
            self.URL = f.readline()
            self.VA = f.readline()
            self.VPW = f.readline()
            
    def load_param_VVI(self):
        self.get_file_Name()
        #create text file in reading mode
        with open(self.file_name, "r") as f:
            #save each line to its respective variable
            
            #Common to all file
            self.state = f.readline()
            self.LRL = f.readline()
            self.URL = f.readline()
            self.VA = f.readline()
            self.VPW = f.readline()
            self.VRP = f.readline()
    
    #break this module down into 2 (AOO and AAI seperatley)
    def load_param_AOO_AAI(self):
        self.get_file_Name()
        #create text file in reading mode
        with open(self.file_name, "r") as f:
            #save each line to its respective variable
            
            #Common to all file
            self.state = f.readline()
            self.LRL = f.readline()
            self.URL = f.readline()
            self.AA = f.readline()
            self.APW = f.readline()
            self.ARP = f.readline()


    #add to function list
    def load_param_AOOR(self):
        self.get_file_Name()
        #create text file in reading mode
        with open(self.file_name, "r") as f:
            #save each line to its respective variable
            
            #Common to all file
            self.state = f.readline()
            self.LRL = f.readline()
            self.URL = f.readline()
            self.AA = f.readline()
            self.APW = f.readline()
            self.MSR = f.readline()
            self.AT = f.readline()
            self.RT = f.readline()
            self.RF = f.readline()
            self.RECT = f.readline()


    #add to function list
    def load_param_VOOR(self):
        self.get_file_Name()
        #create text file in reading mode
        with open(self.file_name, "r") as f:
            #save each line to its respective variable
            
            #Common to all file
            self.state = f.readline()
            self.LRL = f.readline()
            self.URL = f.readline()
            self.VA = f.readline()
            self.VPW = f.readline()
            self.MSR = f.readline()
            self.AT = f.readline()
            self.RT = f.readline()
            self.RF = f.readline()
            self.RECT = f.readline()


    #add to function list
    def load_param_AAIR(self):
        self.get_file_Name()
        #create text file in reading mode
        with open(self.file_name, "r") as f:
            #save each line to its respective variable
            
            #Common to all file
            self.state = f.readline()
            self.LRL = f.readline()
            self.URL = f.readline()
            self.AA = f.readline()
            self.APW = f.readline()
            self.ARP = f.readline()
            self.MSR = f.readline()
            self.AS = f.readline()
            self.PVARP = f.readline()
            self.H = f.readline()
            self.RS = f.readline()
            self.AT = f.readline()
            self.RT = f.readline()
            self.RF = f.readline()
            self.RECT = f.readline()



    #add to function list
    def load_param_VVIR(self):
        self.get_file_Name()
        #create text file in reading mode
        with open(self.file_name, "r") as f:
            #save each line to its respective variable
            
            #Common to all file
            self.state = f.readline()
            self.LRL = f.readline()
            self.URL = f.readline()
            self.VA = f.readline()
            self.VPW = f.readline()
            self.VRP = f.readline()
            self.MSR = f.readline()
            self.VS = f.readline()
            self.H = f.readline()
            self.RS = f.readline()
            self.AT = f.readline()
            self.RT = f.readline()
            self.RF = f.readline()
            self.RECT = f.readline()
            
            
    def get_file_Name(self):
        #check which file to open based on state 
        if (self.state == "VOO"):
            self.file_name = os.path.join(os.path.dirname(__file__),"VOO.txt")  #"VOO.txt"  #os.path.join(os.path.dirname(__file__), "VOO.txt") (Needed this to run on my end - Fatima)
        
        elif (self.state == "AOO"):
            self.file_name = os.path.join(os.path.dirname(__file__),"AOO.txt")  #"AOO.txt"  #os.path.join(os.path.dirname(__file__), "AOO.txt")
        
        elif (self.state == "VVI"):
            self.file_name = os.path.join(os.path.dirname(__file__),"VVI.txt")  #"VVI.txt"  #os.path.join(os.path.dirname(__file__), "VVI.txt")
        
        elif (self.state == "AAI"):
            self.file_name = os.path.join(os.path.dirname(__file__),"AAI.txt")  #"AAI.txt"  #os.path.join(os.path.dirname(__file__), "AAI.txt")
        
        elif (self.state == "AOOR"):
            self.file_name = os.path.join(os.path.dirname(__file__),"AOOR.txt")
        
        elif (self.state == "VOOR"):
            self.file_name = os.path.join(os.path.dirname(__file__),"VOOR.txt")
        
        elif (self.state == "AAIR"):
            self.file_name = os.path.join(os.path.dirname(__file__),"AAIR.txt")
        
        elif (self.state == "VVIR"):
            self.file_name = os.path.join(os.path.dirname(__file__),"VVIR.txt")
        
    
    #-----------------------getter functions ----------------------
    def get_state(self):
        return self.state
    
    def get_LowerRateLimit(self):
        return self.LRL
    
    def get_UpperRateLimit(self):
        return self.URL
    
    def get_AtrialAmplitude(self):
        return self.AA
    
    def get_AtrialPulseWidth(self):
        return self.APW
    
    def get_VentricularAmplitude(self):
        return self.VA
    
    def get_VentricularPulseWidth(self):
        return self.VPW
    
    def get_VRP(self):
        return self.VRP
        
    def get_ARP(self):
        return self.ARP
    
    def get_MaxSensorRate(self): #add to function list from here on
        return self.MSR
    
    def get_AtrialSensitivity(self):
        return self.AS
    
    def get_VentricularSensitivity(self):
        return self.VS
    
    def get_PVARP(self):
        return self.PVARP
    
    def get_Hysteresis(self):
        return self.H
    
    def get_RateSmoothing(self):
        return self.RS
    
    def get_ActivityThreshold(self):
        return self.AT
    
    def get_ReactionTime(self):
        return self.RT
    
    def get_ResponseFactor(self):
        return self.RF
    
    def get_RecoveryTime(self):
        return self.RECT
    
    #-----------------setter functions -----------------------
    #save data to member variables and local file
    def set_state(self, new_state):
        self.state = new_state
        self.save_param(new_state, 1)
        
       # only load paramaters for new state
        if (self.state == "VOO"):
            self.load_param_VOO()
                
        elif (self.state == "VVI"):
            self.load_param_VVI()
                
        elif (self.state == "AOO" or self.state == "AAI"): #AOO and AAI have same file format
            self.load_param_AOO_AAI()
            
        elif (self.state == "AOOR"):
            self.load_param_AOOR()
        
        elif (self.state == "VOOR"):
            self.load_param_VOOR()
            
        elif (self.state == "AAIR"):
            self.load_param_AAIR()
        
        elif (self.state == "VVIR"):
            self.load_param_VVIR()
                
    
    def set_LowerRateLimit(self, new_LRL):
        self.LRL = new_LRL
        self.save_param(new_LRL, 2)
    
    def set_UpperRateLimit(self, new_URL):
        self.URL = new_URL
        self.save_param(new_URL, 3)
    
    def set_AtrialAmplitude(self, new_AA):
        self.AA = new_AA
        self.save_param(new_AA, 4)
    
    def set_AtrialPulseWidth(self, new_APW):
        self.APW = new_APW
        self.save_param(new_APW, 5)
    
    def set_VentricularAmplitude(self, new_VA):
        self.VA = new_VA
        self.save_param(new_VA, 4)
    
    def set_VentricularPulseWidth(self, new_VPW):
        self.VPW = new_VPW
        self.save_param(new_VPW, 5)
    
    def set_VRP(self, new_VRP):
        self.VRP = new_VRP
        self.save_param(new_VRP, 6)
        
    def set_ARP(self, new_ARP):
        self.ARP = new_ARP
        self.save_param(new_ARP, 6)
        
    def set_MaxSensorRate(self, new_MSR): #add to function list from here on
        self.MSR = new_MSR
        
        #save param to line relevant to mode/state
        if (self.state == "AOOR" or self.state == "VOOR"):
            self.save_param(new_MSR, 6)
        elif (self.state == "AAIR" or self.state == "VVAIR"):
            self.save_param(new_MSR, 7)
            
    def set_AtrialSensitivity(self, new_AS):
        self.AS = new_AS
        
        #save param to line relevant to mode/state
        if (self.state == "AAIR"):
            self.save_param(new_AS, 8)
            
            
    def set_VentricularSensitivity(self, new_VS):
        self.VS = new_VS
        
        #save param to line relevant to mode/state
        if (self.state == "VVIR"):
            self.save_param(new_VS, 8)
            
    def set_PVARP(self, new_PVARP):
        self.PVARP = new_PVARP
        
        #save param to line relevant to mode/state
        if (self.state == "AAIR"):
            self.save_param(new_PVARP, 9)
            
    def set_Hysteresis(self, new_H):
        self.H = new_H
        
        #save param to line relevant to mode/state
        if (self.state == "AAIR"):
            self.save_param(new_H, 10)
        elif (self.state == "VVIR"):
            self.save_param(new_H, 9)
            
    
    def set_RateSmoothing(self, new_RS):
        self.RS = new_RS
        
        #save param to line relevant to mode/state
        if (self.state == "AAIR"):
            self.save_param(new_RS, 11)
        elif (self.state == "VVIR"):
            self.save_param(new_RS, 10)
            
    
    def set_ActivityThreshold(self, new_AT):
        self.AT = new_AT
        
        #save param to line relevant to mode/state
        if (self.state == "AOOR" or self.state == "VOOR"):
            self.save_param(new_AT, 7)
        elif (self.state == "AAIR"):
            self.save_param(new_AT, 12)
        elif (self.state == "VVIR"):
            self.save_param(new_AT, 11)
            
    def set_ReactionTime(self, new_RT):
        self.RT = new_RT
        
        #save param to line relevant to mode/state
        if (self.state == "AOOR" or self.state == "VOOR"):
            self.save_param(new_RT, 8)
        elif (self.state == "AAIR"):
            self.save_param(new_RT, 13)
        elif (self.state == "VVIR"):
            self.save_param(new_RT, 12)
            
    def set_ResponseFactor(self, new_RF):
        self.RF = new_RF
        
        #save param to line relevant to mode/state
        if (self.state == "AOOR" or self.state == "VOOR"):
            self.save_param(new_RF, 9)
        elif (self.state == "AAIR"):
            self.save_param(new_RF, 14)
        elif (self.state == "VVIR"):
            self.save_param(new_RF, 13)
            
    def set_RecoveryTime(self, new_RECT):
        self.RECT = new_RECT
        
        #save param to line relevant to mode/state
        if (self.state == "AOOR" or self.state == "VOOR"):
            self.save_param(new_RECT, 10)
        elif (self.state == "AAIR"):
            self.save_param(new_RECT, 15)
        elif (self.state == "VVIR"):
            self.save_param(new_RECT, 14)


