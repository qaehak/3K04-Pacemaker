# This program reads and saves relevant parameters for the pacemaker using a local file. The state of the pacemaker is also stored.
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
#
# Extra Parameters possibly Atrial Sensitivity, PVARP, Hysteresis, Rate smoothing, Ventricular Sensitivity
#               (Can be added upon request for next sprint)
# Note that states can be either AOO, VOO, AAI,or VVI
#
# Author: Serena Santos
# Date: October 2024
#
# Function List:
#        - __init__(self): Constructor
#        - save_param(self, param, line): Saves a new parameter to local file using line as index
#        - load_param_VOO(self): Loads parameters from local file for VOO to member variables
#        - load_param_VVI(self): Loads parameters from local file for VVI to member variables
#        - load_param_AOO_AAI(self): Loads parameters from local file for AAO or AAI to member variables
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
class param:
    
        
    def __init__(self):
        #initialize member variables
        self.file_name = "AOO.txt"
        self.state = 'AOO'
        self.LRL = '0'
        self.URL = '0'
        self.AA = '0'
        self.APW = '0'
        self.VA = '0'
        self.VPW = '0'
        self.VRP = '0'
        self.ARP = '0'
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
            
        
    def get_file_Name(self):
        #check which file to open based on state
        if (self.state == "VOO"):
            self.file_name = "VOO.txt"  #"VOO.txt"  #os.path.join(os.path.dirname(__file__), "VOO.txt") (Needed this to run on my end - Fatima)
        elif (self.state == "AOO"):
            self.file_name = "AOO.txt"  #"AOO.txt"  #os.path.join(os.path.dirname(__file__), "AOO.txt")
        elif (self.state == "VVI"):
            self.file_name = "VVI.txt"  #"VVI.txt"  #os.path.join(os.path.dirname(__file__), "VVI.txt")
        elif (self.state == "AAI"):
            self.file_name = "AAI.txt"  #"AAI.txt"  #os.path.join(os.path.dirname(__file__), "AAI.txt")
        
        
    
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
        self.save_param(new_state, 1)
        
       # only load paramaters for new state
        if (self.state == "VOO"):
            self.load_param_VOO()
                
        elif (self.state == "VVI"):
            self.load_param_VVI()
                
        elif (self.state == "AOO" or self.state == "AAI"): #AOO and AAI have same file format
            self.load_param_AOO_AAI()
                
    
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
        
