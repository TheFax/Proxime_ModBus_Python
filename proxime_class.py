#PROXIME CLASS
#
#Available functions:
#  input_contact_1
#  input_contact_2
#  firmware
#  echo
#  voltage
#  current_A
#  current_B
#  current_C
#  current_D

import serial
import time
import modbus

class proxime:
    def __init__(self, port):
        """Internal use only
        """
        self.debug = False
        #self.debug = True
        self.port = port
        if (self.debug):
            print ("[proxime] - Opening serial port")
        self.ser = serial.Serial(port,
                                 baudrate=9600,
                                 parity=serial.PARITY_NONE,
                                 stopbits=serial.STOPBITS_TWO,
                                 bytesize=serial.EIGHTBITS
                                )
    
    def send_request(self, data):
        """Internal use only
        """
        self.ser.write(data)
        if (self.debug):
            print ("[proxime] - Request sent")
        time.sleep(0.1)
        answer = "No answer received after the request has been sent: " + str(data)
        while self.ser.inWaiting() > 0:
            if (self.debug):
                print ("[proxime] - Receiving serial data")
            answer = self.ser.read(self.ser.inWaiting())
            if (self.debug):
                #print(data)
                #print(len(data))
                #print(data[0:2])
                if (answer[0:2] == b"\x01\x03"):
                    print ("[proxime] - Received a correct response, lenght %d" % len(answer))
        return answer
    
    def check(self, response):
        """Internal use only
        """
        if (len(response)==7):
            return True
        else:
            return False

    def input_contact_1(self, node):
        """External/cutomer use
        node: the node number of the device you want to query
        Returns: "open" if the contact 1 is open
                 "close" if the contact 1 is closed
        """
        packet = modbus.modbus_generator(node, 3, 0, 1)
        response = self.send_request(packet)
        if (response[4]&16 == 0):
            return "open"
        else:
            return "close"

    def input_contact_2(self, node):
        """External/cutomer use
        node: the node number of the device you want to query
        Returns: "open" if the contact 2 is open
                 "close" if the contact 2 is closed
        """
        packet = modbus.modbus_generator(node, 3, 0, 1)
        response = self.send_request(packet)
        if (response[4]&32 == 0):
            return "open"
        else:
            return "close"
    
    def firmware(self, node):
        """External/cutomer use
        node: the node number of the device you want to query
        Returns: firmware version of the device queried
        """
        packet = modbus.modbus_generator(node, 3, 1, 1)
        response = self.send_request(packet)
        if (self.check(response)):
            return "Version: "+str(response[4])+" - Release: "+str(response[3])
        else:
            return -1
    
    def echo(self, node):
        """External/cutomer use
        node: the node number of the device you want to query
        Returns: echo of the request, e.g. for comunication test.
        """
        packet = modbus.modbus_generator(node, 3, 2, 1)
        response = self.send_request(packet)
        return response
    
    def voltage(self, node):
        """External/cutomer use
        node: the node number of the device you want to query
        Returns: voltage read by proxime
        """
        packet = modbus.modbus_generator(node, 3, 5, 1)
        response = self.send_request(packet)
        if (self.check(response)):
            return response[4]+(response[3]*255)
        else:
            return -1
    
    def current_A(self, node):
        """External/cutomer use
        node: the node number of the device you want to query
        Returns: current read from Hall Probe A (this value is NOT normalized in Ampere)
        """
        packet = modbus.modbus_generator(node, 3, 6, 1)
        response = self.send_request(packet)
        if (self.check(response)):
            return response[4]+(response[3]*255)
        else:
            return -1

    def current_B(self, node):
        """External/cutomer use
        node: the node number of the device you want to query
        Returns: current read from Hall Probe B (this value is NOT normalized in Ampere)
        """
        packet = modbus.modbus_generator(node, 3, 7, 1)
        response = self.send_request(packet)
        if (self.check(response)):
            return response[4]+(response[3]*255)
        else:
            return -1
    
    def current_C(self, node):
        """External/cutomer use
        node: the node number of the device you want to query
        Returns: current read from Hall Probe C (this value is NOT normalized in Ampere)
        """
        packet = modbus.modbus_generator(node, 3, 8, 1)
        response = self.send_request(packet)
        if (self.check(response)):
            return response[4]+(response[3]*255)
        else:
            return -1
    
    def current_D(self, node):
        """External/cutomer use
        node: the node number of the device you want to query
        Returns: current read from Hall Probe D (this value is NOT normalized in Ampere)
        """
        packet = modbus.modbus_generator(node, 3, 9, 1)
        response = self.send_request(packet)
        if (self.check(response)):
            return response[4]+(response[3]*255)
        else:
            return -1

