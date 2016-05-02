from AFG3252 import * 
import time
from 



print 'Testing AFG'



dev = AFG3252('128.143.196.225')
dev.outputType('square')
dev.setFrequency(1500)
dev.enableOutput(1)



dev.disableOutput(1)
