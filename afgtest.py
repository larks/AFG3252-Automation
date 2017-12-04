from AFG3252 import * 
import time



print 'Testing AFG'



dev = AFG3252('128.141.92.74')
dev.outputType('pulse')
dev.setFrequency(7000)
#dev.setVoltage(1, "50mV")
dev.setVoltageHigh(1,"50mV")
dev.setVoltageLow(1,"0mV")
dev.setLeading(1, "4ns")
dev.setTrailing(1, "55us")

#dev.enableOutput(1)



#dev.disableOutput(1)
