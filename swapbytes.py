import sys

fout = open(sys.argv[1]+".out.bin", "wb")
fin = open(sys.argv[1], "rb")
while True:
        buf1 = fin.read(1)
        if not buf1:
            break
        buf2 = fin.read(1)
        if not buf2:
            break
        fout.write(buf2)
        fout.write(buf1)
fin.close()
fout.close()
input("Press Enter to continue...")

