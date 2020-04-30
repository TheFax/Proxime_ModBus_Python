#MODBUS module.
#
#Exports the function "modbus_generator" that is able to compose a complete ModBus frame
#using the datas passed as arguments.
#For more info:
# help(modbus.modbus_generator)

def crc16(data):
    """Internal use mainly:
    This function calculates the CRC of a ModBus frame.
    Note that this is called CRC but it is not a "real" CRC.
    Returns: 16 bit "CRC"
    """
    crc = 0xFFFF
    for i in range(0,len(data)):
        crc = crc ^ ( data[i] & 0xFF )
        for x in range(1,9):
            if (crc % 2 ) == 0:
                crc = crc >> 1
            else:
                crc = crc >> 1
                crc = crc ^ 0xA001
    return crc

def modbus_add_checksum(data):
    """Internal use only:
    This function add a correct CRC to a frame passed via argument.
    """
    crc = crc16(data)
    final = data + bytes([crc & 0xff]) + bytes([(crc>>8) & 0xff])
    return final

def modbus_generator(node, request, address, words):
    """This is the main function of this module.
    This function calculates a complete frame ModBus, using the datas passed as arguments.
    modbus_generator(node, request, address, words):
       node:    (integer 8 bit) the node number of the receiver
       request: (integer 8 bit) request type (0x03 = read one word)
       address: (integer 16 bit) the address to read (or the first address to read, if you request more than 1 word)
       words:   (integer 16 bit) the number of word you are requesting
    Returns: a complete frame with its checksum, ready to be sent via serial port (or other)
    """
    frame = bytes([node]) + bytes([request]) + bytes([address>>8 & 0xff]) + bytes([address & 0xff]) + bytes([words>>8 & 0xff]) + bytes([words & 0xff])
    frame = modbus_add_checksum(frame)
    return frame

#def main():
#    """This is only a module.
#    Import it and use its functions.
#    Nothing to run here.
#    """
#    print("This is only a module. Nothing to run here.")
#    exit()
#
#if __name__ == "__main__":
#    main()
