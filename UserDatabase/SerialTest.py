import communication
import param
import serial

#send
parameters = param.param()
con = communication.Connection("COM5", parameters)

con.connect()
print(con.get_connection())

con.transmit()
con.close_connection()

#test other modes as well
