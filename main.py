#This is a DEMO program
#connects to a Proxime via /dev/ttyUSB0 and ask it some information

import time
import proxime_class

print("Starting program")

time.sleep(0.2)

try:
    myprox = proxime_class.proxime("/dev/ttyUSB0")
    while True:
        time.sleep(0.5)
        print(time.time() , " - [main] - Proxime says: " , myprox.input_contact_2(1))
        print(time.time() , " - [main] - Proxime says: " , myprox.voltage(1))
        print(time.time() , " - [main] - Proxime says: " , myprox.current_A(1))
        #  input_contact_1
        #  input_contact_2
        #  firmware
        #  echo
        #  voltage
        #  current_A
        #  current_B
        #  current_C
        #  current_D
        
except KeyboardInterrupt:
    print("Exiting Program")

#except:
#    print("Error Occurs, Exiting Program")

finally:
    pass
