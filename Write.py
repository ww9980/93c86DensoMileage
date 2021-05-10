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

target = 75410

partA = int(target / 1000000)
partB = int((target - partA * 1000000) / 10000)
partC = int((target - partA * 1000000 - partB * 10000) / 100)

targetBytes = [(0xFF).to_bytes(1, byteorder='big'), (partC ^ 0xFF).to_bytes(1, byteorder='big'), 
               (partB ^ 0xFF).to_bytes(1, byteorder='big'), (partA ^ 0xFF).to_bytes(1, byteorder='big')]

barray[98:102] = targetBytes

outfile =  open("out.bin", "wb")
for byteitem in barray:
    outfile.write(bytes(byteitem))
outfile.close()
