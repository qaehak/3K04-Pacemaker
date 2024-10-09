# This program reads and saves relevant parameters for the pacemaker using a local file. The state of the pacemaker is also stored.
# Text file formatting: Line 1 = pacemaker state, Line 2 = Lower Rate Limit (LRL), Line 3 = Upper Rate Limit (URL),
#               Line 4 = Atrial Amplitude (AA), Line 5 = Atrial Pulse Width (APW), Line 6 = Ventricular Amplitude (VA),
#               Line 7 = Ventricular Pulse Width (VPW), Line 8 = VRP, Line 9 = ARP
# Extra Parameters possibly Atrial Sensitivity, PVARP, Hysteresis, Rate smoothing, Ventricular Sensitivity
#               (Can be added upon request for next sprint)
# Note that states can be either AOO, VOO, AAI,or VVI
#
# Author: Serena Santos
# Date: October 2024
#
# Function List:
#        - __init__(self): Constructor
#        - save_param(self): Saves current parameters to local file
#        - load_param(self): Loads parameters from local file to member variables

#        - get_state(self): getter; returns state
#        - get_LowerRateLimit(self): getter; returns LRL
#        - get_UpperRateLimit(self): getter; returns URL
#        - get_AtrialAmplitude(self): getter; returns AA
#        - get_AtrialPulseWidth(self): getter; returns APW
#        - get_VentricularAmplitude(self): getter; returns VA
#        - get_VentricularPulseWidth(self): getter; returns VPW
#        - get_VRP(self): getter; returns VRP
#        - get_ARP(self): getter; returns ARP

#        - set_state(self, state): setter; sets state and saves to file
#        - set_LowerRateLimit(self, new_LRL): setter; sets LRL and saves to file
#        - set_UpperRateLimit(self, new_URL): setter; sets URL and saves to file
#        - set_AtrialAmplitude(self, new_AA): setter; sets AA and saves to file
#        - set_AtrialPulseWidth(self, new_APW): setter; sets APW and saves to file
#        - set_VentricularAmplitude(self, new_VA): setter; sets VA and saves to file
#        - set_VentricularPulseWidth(self, new_VPW): setter; sets VPW and saves to file
#        - set_VRP(self, new_VRP): setter; sets VRP and saves to file
#        - set_ARP(self, new_ARP): setter; sets ARP and saves to file
#
import os
class param:
    #initialize member variables
    file_name = "param.txt"  #os.path.join(os.path.dirname(__file__), "param.txt") (Needed this to run on my end - Fatima)
    state = ''
    LRL = '0'
    URL = '0'
    AA = '0'
    APW = '0'
    VA = '0'
    VPW = '0'
    VRP = '0'
    ARP = '0'
        
    def __init__(self):
        #load current values from the file
        self.load_param()
        
    
    def save_param(self):
        #open text file in writing mode
        f = open(self.file_name, "w")
        f.write(self.state)
        f.write("\n")
        f.write(str(self.LRL))
        f.write("\n")
        f.write(str(self.URL))
        f.write("\n")
        f.write(str(self.AA))
        f.write("\n")
        f.write(str(self.APW))
        f.write("\n")
        f.write(str(self.VA))
        f.write("\n")
        f.write(str(self.VPW))
        f.write("\n")
        f.write(str(self.VRP))
        f.write("\n")
        f.write(str(self.ARP))
        f.write("\n")
        
        f.close()
        
        
    def load_param(self):
        #open text file in reading mode
        f = open(self.file_name, "r")
        
        #save each line to its respective variable
        self.state = f.readline()
        self.LRL = f.readline()
        self.URL = f.readline()
        self.AA = f.readline()
        self.APW = f.readline()
        self.VA = f.readline()
        self.VPW = f.readline()
        self.VRP = f.readline()
        self.ARP = f.readline()
        
        f.close()
        
        
    
    #-----------------------getters----------------------
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
    
    #-----------------setters-----------------------
    #save data to member variables and local file
    def set_state(self, new_state):
        self.state = new_state
        self.save_param()
    
    def set_LowerRateLimit(self, new_LRL):
        self.LRL = new_LRL
        self.save_param()
    
    def set_UpperRateLimit(self, new_URL):
        self.URL = new_URL
        self.save_param()
    
    def set_AtrialAmplitude(self, new_AA):
        self.AA = new_AA
        self.save_param()
    
    def set_AtrialPulseWidth(self, new_APW):
        self.APW = new_APW
        self.save_param()
    
    def set_VentricularAmplitude(self, new_VA):
        self.VA = new_VA
        self.save_param()
    
    def set_VentricularPulseWidth(self, new_VPW):
        self.VPW = new_VPW
        self.save_param()
    
    def set_VRP(self, new_VRP):
        self.VRP = new_VRP
        self.save_param()
        
    def set_ARP(self, new_ARP):
        self.ARP = new_ARP
        self.save_param()
    
    