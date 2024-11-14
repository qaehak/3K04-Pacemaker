# Author: Fatima Sarfraz
# Date: October 2024
#
# This class serves as the User Interface for the reviewing and modifying the Pacemaker modes and their respective parameters through a dropdown menu
#
# Function List:
#        - __init__(self): Constructor + defining mode library which indicates what parameters are relevant for the respective mode
#        - widgets(self,root): Created drop down menu to adjust parameters and submit button
#        - update_parameters_for_mode(self, event=None): Updates parameters based on selected mode
#        - get_values_for_param(self, param): provides value ranges for each parameter
#        - submit_parameters(self): saves values to param.txt ---NEED TO FIX (not saving to file properly)---


import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import ttk
from param import param

class Modes:

    def __init__(self, root, pacemaker_params):
        self.pacemaker_params = pacemaker_params


        #stores relevant parameters for each mode
        self.mode_params = {
            "AOO": ["Lower Rate Limit", "Upper Rate Limit", "Atrial Amplitude", "Atrial Pulse Width"],
            "VOO": ["Lower Rate Limit", "Upper Rate Limit", "Ventricular Amplitude", "Ventricular Pulse Width"],
            "AAI": ["Lower Rate Limit", "Upper Rate Limit", "Atrial Amplitude", "Atrial Pulse Width", "Atrial Sensitivty", "ARP", "PVRP", "Hysteresis", "Rate Smoothing"],
            "VVI": ["Lower Rate Limit", "Upper Rate Limit", "Ventricular Amplitude", "Ventricular Pulse Width", "Ventricular Sensitivity", "VRP", "Hysteresis", "Rate Smoothing"],
            "AOOR": ["Lower Rate Limit", "Upper Rate Limit", "Maximum Sensor Rate", "Atrial Amplitude", "Atrial Pulse Width", "Activity Threshold", "Reaction Time", "Response Factor", "Recovery Time"],
            "VOOR": ["Lower Rate Limit", "Upper Rate Limit", "Maximum Sensor Rate", "Ventricular Amplitude", "Ventricular Pulse Width", "Activity Threshold", "Reaction Time", "Response Factor", "Recovery Time"],
            "AAIR": ["Lower Rate Limit", "Upper Rate Limit", "Maximum Sensor Rate", "Atrial Amplitude", "Atrial Pulse Width", "Atrial Sensitivty", "ARP", "PVRP", "Hysteresis", "Rate Smoothing", "Activity Threshold", "Reaction Time", "Response Factor", "Recovery Time"],
            "VVIR": ["Lower Rate Limit", "Upper Rate Limit", "Maximum Sensor Rate", "Ventricular Amplitude", "Ventricular Pulse Width", "Ventricular Sensitivity", "VRP", "Hysteresis", "Rate Smoothing", "Activity Threshold", "Reaction Time", "Response Factor", "Recovery Time"],
        }

        #current selected mode (default=AOO)
        self.selected_mode = tk.StringVar(value=pacemaker_params.get_state().strip())

        #widget creation
        self.widgets(root)

        self.message_label = tk.Label(root, text="", fg="green")
        self.message_label.grid(row=11, columnspan=2)
    
    def widgets(self,root):
        root.title("Pacemaker Parameters")
        root.geometry("400x600")

        #dropdown menu to select mode
        tk.Label(root, text="Select Mode:").grid(row=0, column=0, padx=10, pady=10)
        mode_dropdown = ttk.Combobox(root, textvariable=self.selected_mode, values=list(self.mode_params.keys()))
        mode_dropdown.grid(row=0, column=1)
        mode_dropdown.bind("<<ComboboxSelected>>", self.update_parameters_for_mode)

        self.param_frame = tk.Frame(root)
        self.param_frame.grid(row=1, column=0, columnspan=2, pady=10)

        #pressing submit button will confirm parameters
        submit_button = tk.Button(root, text="Submit", command=self.submit_parameters)
        submit_button.grid(row=10, columnspan=2, pady=20)

        self.update_parameters_for_mode()

    def update_parameters_for_mode(self, event=None):
        #update parameter options based on selected mode
        for widget in self.param_frame.winfo_children():
            #get rid of current widgets (to accomodate new ones)
            widget.destroy()  

        mode = self.selected_mode.get().strip()
        parameters = self.mode_params.get(mode, [])
        #create dropdowns for parameters in selected mode
        for i, param in enumerate(parameters):
            tk.Label(self.param_frame, text=f"{param}:").grid(row=i, column=0, padx=10, pady=5)
            combo = ttk.Combobox(self.param_frame, values=self.get_values_for_param(param))
            combo.grid(row=i, column=1)
            setattr(self, f"{param.replace(' ', '').lower()}_combo", combo)
        
            self.pacemaker_params.set_state(mode)
            
            if param == "Lower Rate Limit":
                combo.set(self.pacemaker_params.get_LowerRateLimit())
            elif param == "Upper Rate Limit":
                combo.set(self.pacemaker_params.get_UpperRateLimit())
            elif param == "Maximum Sensor Rate":
                combo.set(self.pacemaker_params.get_MaxSensorRate())   
            elif param == "Atrial Amplitude":
                combo.set(self.pacemaker_params.get_AtrialAmplitude())
            elif param == "Atrial Pulse Width":
                combo.set(self.pacemaker_params.get_AtrialPulseWidth())
            elif param == "Ventricular Amplitude":
                combo.set(self.pacemaker_params.get_VentricularAmplitude())
            elif param == "Ventricular Pulse Width":
                combo.set(self.pacemaker_params.get_VentricularPulseWidth())
            elif param == "Atrial Sensitivity":
                combo.set(self.pacemaker_params.get_AtrialSensitivity())
            elif param == "Ventricular Sensitivity":
                combo.set(self.pacemaker_params.get_VentricularSensitivity())
            elif param == "VRP":
                combo.set(self.pacemaker_params.get_VRP())
            elif param == "ARP":
                combo.set(self.pacemaker_params.get_ARP())
            elif param == "PVRP":
                combo.set(self.pacemaker_params.get_PVARP())
            elif param == "Hysteresis":
                combo.set(self.pacemaker_params.get_Hysteresis())
            elif param == "Rate Smoothing":
                combo.set(self.pacemaker_params.get_RateSmoothing())
            elif param == "Activity Threshold":
                combo.set(self.pacemaker_params.get_ActivityThreshold())
            elif param == "Reaction Time":
                combo.set(self.pacemaker_params.get_ReactionTime())
            elif param == "Response Factor":
                combo.set(self.pacemaker_params.get_ResponseFactor())
            elif param == "Recovery Time":
                combo.set(self.pacemaker_params.get_RecoveryTime())
            
            


    def reset_parameters(self):
        #clear previous parameter values from the file
        for param in ["Lower Rate Limit", "Upper Rate Limit", "Maximum Sensor Rate", "Atrial Amplitude", "Atrial Pulse Width", 
                  "Ventricular Amplitude", "Ventricular Pulse Width", "Atrial Sensitivity", "Ventricular Sensitivity", "VRP", 
                  "ARP", "PVRP", "Hysteresis", "Rate Smoothing", "Activity Threshold", "Reaction Time", "Response Factor", "Recovery Time"]:
            getattr(self.pacemaker_params, f'set_{param.replace(" ", "")}')("")

    def get_values_for_param(self, param):
        #options for parameters
        if "Lower Rate Limit" in param:
            return list(range(30, 176))
        elif "Upper Rate Limit" in param:
            return list(range(50, 176))
        elif "Maximum Sensor Rate" in param:
            return list(range(50, 176))
        elif "Atrial Amplitude" in param or "Ventricular Amplitude" in param:
            return [round(x * 0.1, 1) for x in range(5, 71)]
        elif "Pulse Width" in param:
            return [0.5] + [round(x * 0.1, 1) for x in range(1, 20)]
        elif "VRP" in param or "ARP" in param or "PVRP" in param:
            return list(range(150, 501, 10))
        elif "Atrial Sensitivity" in param or "Ventricular Sensitivity" in param:
            return [0.25, 0.50, 0.75] + [float(i) for i in range(1, 10)]
        elif "Hysteresis" in param:
            return ["OFF"] + list(range(50, 176))
        elif "Rate Smoothing" in param:
            return ["OFF"] + list(range(3, 27, 3))
        elif "Activity Threshold" in param:
            return ["V-Low", "Low", "Med-Low", "Med", "Med-High", "High", "V-High"]
        elif "Reaction Time" in param:
            return list(range(10, 51))
        elif "Response Factor" in param:
            return list(range(1, 17))
        elif "Recovery Time" in param:
            return list(range(2, 17))
        else:
            #empty list for unknown params
            return []  
        
    def submit_parameters(self):


        #get and set the values from dropdowns using param class 
        try:
            mode = self.selected_mode.get().strip() #self.selected_mode.get()
            print(f"Selected mode: '{mode}'") #debugging
            parameters = self.mode_params.get(mode, []) #retrieves parameters specific to selected mode
            self.pacemaker_params.set_state(mode) #write new mode into the param
            

            if not parameters:
                for param in ["Lower Rate Limit", "Upper Rate Limit", "Maximum Sensor Rate", "Atrial Amplitude", "Atrial Pulse Width", 
                  "Ventricular Amplitude", "Ventricular Pulse Width", "Atrial Sensitivity", "Ventricular Sensitivity", "VRP", 
                  "ARP", "PVRP", "Hysteresis", "Rate Smoothing", "Activity Threshold", "Reaction Time", "Response Factor", "Recovery Time"]:
                    getattr(self.pacemaker_params, f'set_{param}')( "" )
                self.message_label.config(text=f"Parameters for {mode} mode have been updated.")  
                return

            #saves parameters for those relevant to the selected mode (stored in parameters)
            for param in parameters:
                combo_name = f"{param.replace(' ', '').lower()}_combo"
                if hasattr(self, combo_name):
                    combo_value = combo_value = getattr(self, combo_name).get()
                    print(f"Setting {param} to {combo_value}")  #debugging

                    if param == "Lower Rate Limit":
                        self.pacemaker_params.set_LowerRateLimit(combo_value)

                    elif param == "Upper Rate Limit":
                        self.pacemaker_params.set_UpperRateLimit(combo_value)
                    
                    elif param == "Maximum Sensor Rate":
                        self.pacemaker_params.set_MaxSensorRate(combo_value)

                    elif param == "Atrial Amplitude":
                        self.pacemaker_params.set_AtrialAmplitude(combo_value)

                    elif param == "Atrial Pulse Width":
                        self.pacemaker_params.set_AtrialPulseWidth(combo_value)

                    elif param == "Ventricular Amplitude":
                        self.pacemaker_params.set_VentricularAmplitude(combo_value)

                    elif param == "Ventricular Pulse Width":
                        self.pacemaker_params.set_VentricularPulseWidth(combo_value)
                    
                    elif param == "Atrial Sensitivity":
                        self.pacemaker_params.set_AtrialSensitivity(combo_value)

                    elif param == "VRP":
                        self.pacemaker_params.set_VRP(combo_value)

                    elif param == "ARP":
                        self.pacemaker_params.set_ARP(combo_value)
                    
                    elif param == "PVRP":
                        self.pacemaker_params.set_PVRP(combo_value)
                    
                    elif param == "Hysteresis":
                        self.pacemaker_params.set_Hysteresis(combo_value)

                    elif param == "Rate Smoothing":
                        self.pacemaker_params.set_RateSmoothing(combo_value)
                    
                    elif param == "Activity Threshold":
                        self.pacemaker_params.set_ActivityThreshold(combo_value)
                    
                    elif param == "Reaction Time":
                        self.pacemaker_params.set_ReactionTime(combo_value)
                    
                    elif param == "Response Factor":
                        self.pacemaker_params.set_ResponseFactor(combo_value)
                    
                    elif param == "Recovery Time":
                        self.pacemaker_params.set_RecoveryTime(combo_value)

                     
                    
            self.message_label.config(text=f"Parameters for {mode} mode have been updated.") 

        except KeyError as e:
            self.message_label.config(text=f"Invalid mode selected: {str(e)}", fg="red")
        except ValueError as e:
            #handle invalid input
            self.message_label.config(text=str(e), fg="red")

if __name__ == "__main__":
    #create the main window
    root = tk.Tk()

    #create an instance of param class
    pacemaker_params = param()

    #create the PacemakerUI and pass the pacemaker parameters instance
    app = Modes(root, pacemaker_params)

    #start the application
    root.mainloop()
