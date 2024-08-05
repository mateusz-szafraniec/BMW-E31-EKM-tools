import sys
import binascii

fin = open(sys.argv[1], "rb")
hexout = open(sys.argv[1]+".trc", "w")
counter = 0
globalcounter = 0
hexout.write("B 00000000,0010,")
while True:
        buf1 = fin.read(1)
        if not buf1:
            break
        if counter == 16:
            counter = 0
            hexout.write("\n")
            hexout.write("B ")
            hexout.write(hex(globalcounter)[2:].upper().zfill(8))
            hexout.write(",0010,")
        hexout.write(binascii.hexlify(buf1).decode("ascii").upper())
        counter +=1
        globalcounter += 1
        if counter < 16:
            hexout.write(",")
fin.close()
hexout.close()
input("Press Enter to continue...")

