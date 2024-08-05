import sys
import binascii

fout = open(sys.argv[1]+".bin", "wb")
fin = open(sys.argv[1], "r")
counter = 0
while True:
        buf1 = fin.readline()
        if not buf1:
            break
        splitted = buf1.split(",")
        counter = 0
        for data in splitted:
            if counter > 1:
                try:
                    fout.write(binascii.unhexlify(data.strip()))
                except:
                    print("Something went wrong")
            counter +=1
fin.close()
fout.close()
input("Press Enter to continue...")
