#Testing for param.
import param

#create instance of the param object
parameters = param.param()

# Testing loading parameters from the file and using the getter functions
print("-----------INITIAL VALUES------------")
print("State: " + parameters.get_state())
print("Lower Rate Limit: " + str(parameters.get_LowerRateLimit()))
print("Upper Rate Limit: " + str(parameters.get_UpperRateLimit()))
print("Atrial Amplitude: " + str(parameters.get_AtrialAmplitude()))
print("Atrial Pulse Width: " + str(parameters.get_AtrialPulseWidth()))
print("Ventricular Amplitude: " + str(parameters.get_VentricularAmplitude()))
print("Ventricular Pulse Width: " + str(parameters.get_VentricularPulseWidth()))
print("VRP: " + str(parameters.get_VRP()))
print("ARP: " + str(parameters.get_ARP()))

#Testing setters and save_param() function(change parameters)
parameters.set_state("AOO")
parameters.set_LowerRateLimit(20)
parameters.set_UpperRateLimit(19)
parameters.set_AtrialAmplitude(18)
parameters.set_AtrialPulseWidth(17)
parameters.set_VentricularAmplitude(16)
parameters.set_VentricularPulseWidth(15)
parameters.set_VRP(14)
parameters.set_ARP(13)

#Print out current values
print("--------AFTER CHANGES------------")
print("State: " + parameters.get_state())
print("Lower Rate Limit: " + str(parameters.get_LowerRateLimit()))
print("Upper Rate Limit: " + str(parameters.get_UpperRateLimit()))
print("Atrial Amplitude: " + str(parameters.get_AtrialAmplitude()))
print("Atrial Pulse Width: " + str(parameters.get_AtrialPulseWidth()))
print("Ventricular Amplitude: " + str(parameters.get_VentricularAmplitude()))
print("Ventricular Pulse Width: " + str(parameters.get_VentricularPulseWidth()))
print("VRP: " + str(parameters.get_VRP()))
print("ARP: " + str(parameters.get_ARP()))

#Reset to default values if running testing shell again
parameters.set_state("VOO")
parameters.set_LowerRateLimit(1)
parameters.set_UpperRateLimit(2)
parameters.set_AtrialAmplitude(3)
parameters.set_AtrialPulseWidth(4)
parameters.set_VentricularAmplitude(5)
parameters.set_VentricularPulseWidth(6)
parameters.set_VRP(7)
parameters.set_ARP(8)