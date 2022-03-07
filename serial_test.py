import serial


PORT = "COM7"  # change to your port

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port=PORT,
    baudrate=115200,
    stopbits=1,
    timeout=0.1
)

if not ser.isOpen():
    print("Serial open failed, cannot open", PORT)
    print("try to modify line 4 to corresponding port")
    exit()
else:
    print('Enter your commands below. Insert "exit" to leave the application.')

recv = 1
send = ''
while 1:
    # get keyboard input
    recv = input("OUT >> ")

    if recv == 'exit':
        ser.close()
        exit()
    else:
        # send the character to the device
        ser.write(recv.encode('ascii'))

        # while ser.inWaiting() > 0:
        #     print(True)
        send = ser.readline().decode('ascii')

        if send != '':
            print("IN << " + send)
