import sys
import binascii

fout = open(sys.argv[1]+".virgin.bin", "wb")
fin = open(sys.argv[1], "rb")
counter = 0
while True:
        buf1 = fin.read(1)
        if not buf1:
            break
        if (counter == 0xFC) or (counter == 0xFF):
            if (counter == 0xFC):
                if buf1 == binascii.unhexlify("FF"):
                    print("First byte ok\n")
                else:
                    print("First byte NOK\n")
            if (counter == 0xFF):
                if buf1 == binascii.unhexlify("0F"):
                    print("Second byte ok\n")
                else:
                    print("Second byte NOK\n")
            fout.write(binascii.unhexlify("3F"))
        else:
            fout.write(buf1)
        counter +=1
fin.close()
fout.close()
input("Press Enter to continue...")
