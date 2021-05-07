def ConvertListToDisplay(listin):
    strout = ''
    for digit in listin:
        strout = strout + str(digit).zfill(2) 
    return strout

file = open("dump.bin", "rb")

barray = []
byte = file.read(1)
barray.append(byte)
while byte:

    #print(byte)
    byte = file.read(1)
    barray.append(byte)

iDisplay = []
for b in barray[98:102]:
    iDisplay.append(int.from_bytes(b, byteorder='big') ^ 0xff)

iDisplay.reverse()
ConvertListToDisplay(iDisplay).lstrip('0')
