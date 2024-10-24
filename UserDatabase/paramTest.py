#Testing for param.
import param

#create instance of the param object
parameters = param.param()

# Testing loading parameters from the file and using the getter functions
print("-----------INITIAL VALUES------------")
#default is AOO
print("State: " + parameters.get_state())
print("Lower Rate Limit: " + str(parameters.get_LowerRateLimit()))
print("Upper Rate Limit: " + str(parameters.get_UpperRateLimit()))
print("Atrial Amplitude: " + str(parameters.get_AtrialAmplitude()))
print("Atrial Pulse Width: " + str(parameters.get_AtrialPulseWidth()))
print("ARP: " + str(parameters.get_ARP()))

parameters.set_state("VOO")
print("\n")
print("State: " + parameters.get_state())
print("Lower Rate Limit: " + str(parameters.get_LowerRateLimit()))
print("Upper Rate Limit: " + str(parameters.get_UpperRateLimit()))
print("Ventricular Amplitude: " + str(parameters.get_VentricularAmplitude()))
print("Ventricular Pulse Width: " + str(parameters.get_VentricularPulseWidth()))

parameters.set_state("VVI")
print("\n")
print("State: " + parameters.get_state())
print("Lower Rate Limit: " + str(parameters.get_LowerRateLimit()))
print("Upper Rate Limit: " + str(parameters.get_UpperRateLimit()))
print("Ventricular Amplitude: " + str(parameters.get_VentricularAmplitude()))
print("Ventricular Pulse Width: " + str(parameters.get_VentricularPulseWidth()))
print("VRP: " + str(parameters.get_VRP()))

parameters.set_state("AAI")
print("\n")
print("State: " + parameters.get_state())
print("Lower Rate Limit: " + str(parameters.get_LowerRateLimit()))
print("Upper Rate Limit: " + str(parameters.get_UpperRateLimit()))
print("Atrial Amplitude: " + str(parameters.get_AtrialAmplitude()))
print("Atrial Pulse Width: " + str(parameters.get_AtrialPulseWidth()))
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
#parameters.save_param()

#Print out current values
print("--------AFTER CHANGES------------")

parameters.set_state("AOO")
parameters.set_LowerRateLimit(1)
parameters.set_UpperRateLimit(2)
parameters.set_AtrialAmplitude(3)
parameters.set_AtrialPulseWidth(4)
parameters.set_ARP(5)

print("\n")
print("State: " + parameters.get_state())
print("Lower Rate Limit: " + str(parameters.get_LowerRateLimit()))
print("Upper Rate Limit: " + str(parameters.get_UpperRateLimit()))
print("Atrial Amplitude: " + str(parameters.get_AtrialAmplitude()))
print("Atrial Pulse Width: " + str(parameters.get_AtrialPulseWidth()))
print("ARP: " + str(parameters.get_ARP()))


parameters.set_state("VOO")
parameters.set_LowerRateLimit(10)
parameters.set_UpperRateLimit(20)
parameters.set_VentricularAmplitude(30)
parameters.set_VentricularPulseWidth(40)
print("\n")
print("State: " + parameters.get_state())
print("Lower Rate Limit: " + str(parameters.get_LowerRateLimit()))
print("Upper Rate Limit: " + str(parameters.get_UpperRateLimit()))
print("Atrial Amplitude: " + str(parameters.get_AtrialAmplitude()))
print("Atrial Pulse Width: " + str(parameters.get_AtrialPulseWidth()))
print("ARP: " + str(parameters.get_ARP()))


parameters.set_state("VVI")
parameters.set_LowerRateLimit(100)
parameters.set_UpperRateLimit(200)
parameters.set_VentricularAmplitude(300)
parameters.set_VentricularPulseWidth(400)
parameters.set_VRP(500)
print("\n")
print("State: " + parameters.get_state())
print("Lower Rate Limit: " + str(parameters.get_LowerRateLimit()))
print("Upper Rate Limit: " + str(parameters.get_UpperRateLimit()))
print("Ventricular Amplitude: " + str(parameters.get_VentricularAmplitude()))
print("Ventricular Pulse Width: " + str(parameters.get_VentricularPulseWidth()))
print("VRP: " + str(parameters.get_VRP()))


parameters.set_state("AAI")
parameters.set_LowerRateLimit(1000)
parameters.set_UpperRateLimit(2000)
parameters.set_AtrialAmplitude(3000)
parameters.set_AtrialPulseWidth(4000)
parameters.set_ARP(5000)
print("\n")
print("State: " + parameters.get_state())
print("Lower Rate Limit: " + str(parameters.get_LowerRateLimit()))
print("Upper Rate Limit: " + str(parameters.get_UpperRateLimit()))
print("Atrial Amplitude: " + str(parameters.get_AtrialAmplitude()))
print("Atrial Pulse Width: " + str(parameters.get_AtrialPulseWidth()))
print("ARP: " + str(parameters.get_ARP()))

#parameters.save_param()