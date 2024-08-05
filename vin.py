import sys

fout = open(sys.argv[1]+".vin.txt", "wb")
fin = open(sys.argv[1], "rb")
fin.seek(0xE8)
vin1 = fin.read(7)
vin3 = bytearray()
while True:
    if not vin1:
        break
    fout.write(vin1)
    vin2 = bytearray(fin.read(7))
    if not vin2:
        break
    fout.write(bytes("\n",'ascii'))
    vin3.append(((vin2[0]))^ 0xFF)
    vin3.append(((vin2[1]))^ 0xFF)
    vin3.append(((vin2[2]))^ 0xFF)
    vin3.append(((vin2[3]))^ 0xFF)
    vin3.append(((vin2[4]))^ 0xFF)
    vin3.append(((vin2[5]))^ 0xFF)
    vin3.append(((vin2[6]))^ 0xFF)
    fout.write(vin3)
    fout.write(bytes("\n",'ascii'))
    if vin1 == vin3:
        print("VIN ok\n")
        fout.write(bytes("VIN ok\n",'ascii'))
    else:
        print("VIN NOT OK!\n")
        fout.write(bytes("VIN NOT OK!\n",'ascii'))
    break

fin.close()
fout.close()
input("Press Enter to continue...")

