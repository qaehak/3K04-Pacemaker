import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from param import param

class Modes:

    def __init__(self, root, pacemaker_params):
        self.pacemaker_params = pacemaker_params

        #stores relevant parameters for each mode
        self.mode_params = {
            "AOO": ["Lower Rate Limit", "Upper Rate Limit", "Atrial Amplitude", "Atrial Pulse Width", "ARP"],
            "VOO": ["Lower Rate Limit", "Upper Rate Limit", "Ventricular Amplitude", "Ventricular Pulse Width"],
            "AAI": ["Lower Rate Limit", "Upper Rate Limit", "Atrial Amplitude", "Atrial Pulse Width", "ARP"],
            "VVI": ["Lower Rate Limit", "Upper Rate Limit", "Ventricular Amplitude", "Ventricular Pulse Width", "VRP"]
        }

        #current selected mode (default=AOO)
        self.selected_mode = tk.StringVar(value="AOO")

        #widget creation
        self.widgets(root)
    
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
            #get ride of current widgets (to accomodate new ones)
            widget.destroy()  

        mode = self.selected_mode.get()
        parameters = self.mode_params[mode]

        #create dropdowns for parameters in selected mode
        for i, param in enumerate(parameters):
            tk.Label(self.param_frame, text=f"{param}:").grid(row=i, column=0, padx=10, pady=5)
            combo = ttk.Combobox(self.param_frame, values=self.get_values_for_param(param))
            combo.grid(row=i, column=1)
            current_value = getattr(self.pacemaker_params, f"get_{param.replace(' ', '')}")().strip()
            combo.set(current_value)
            setattr(self, f"{param.replace(' ', '').lower()}_combo", combo)

    def get_values_for_param(self, param):
        #options for parameters
        if "Lower Rate Limit" in param:
            return list(range(30, 176))
        elif "Upper Rate Limit" in param:
            return list(range(50, 176))
        elif "Atrial Amplitude" in param or "Ventricular Amplitude" in param:
            return [round(x * 0.1, 1) for x in range(10, 51)]
        elif "Pulse Width" in param:
            return [round(x * 0.01, 2) for x in range(1, 11)]
        elif "VRP" in param or "ARP" in param:
            return list(range(150, 501, 10))
        else:
            #empty list for unknown params
            return []  
    def submit_parameters(self):
        #save the parameters
        try:
            mode = self.selected_mode.get()
            parameters = self.mode_params[mode]
            with open("param.txt", "w") as file:
                file.write(f"Mode: {mode}\n")
            #get and set the values from dropdowns using param class 
            for param in parameters:
                combo_value = getattr(self, f"{param.replace(' ', '').lower()}_combo").get()
                setter_method = getattr(self.pacemaker_params, f"set_{param.replace(' ', '')}")
                setter_method(combo_value)

            file.write(f"{param}: {combo_value}\n")
            messagebox.showinfo(f"Parameters for {mode} mode have been updated")
        except ValueError as e:
            #handle invalid input
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    #create the main window
    root = tk.Tk()

    #create an instance of param class
    pacemaker_params = param()

    #create the PacemakerUI and pass the pacemaker parameters instance
    app = Modes(root, pacemaker_params)

    #start the application
    root.mainloop()
