import io

offset0 = 0x4000
offset1 = 0x5000
offset2 = 0x5f4000
offset3 = 0xBE3000
offset4 = 0x11D2000

outpt = open("logo_new_mi9.img", "wb")

emptyContent =  [0 for i in range(0x17c1000)]

mi9offset = [0x4C, 0x4F, 0x47, 0x4F, 0x21, 0x21, 0x21, 0x21, 0x05, 0x00, 0x00, 0x00,
                0xEf, 0x05, 0x00, 0x00, 0xF4, 0x05, 0x00, 0x00, 0xEF, 0x05, 0x00, 0x00,
                0xE3, 0x0B, 0x00, 0x00, 0xEF, 0x05, 0x00, 0x00, 0xD2, 0x11, 0x00, 0x00,
                0xEf, 0x05]

outpt.write(bytearray(emptyContent))

outpt.seek(offset0)
outpt.write(bytearray(mi9offset))

outpt.seek(offset1)
img = open("pic1.bmp", "rb")
outpt.write(img.read())

outpt.seek(offset2)
img = open("pic2.bmp", "rb")
outpt.write(img.read())

outpt.seek(offset3)
img = open("pic3.bmp", "rb")
outpt.write(img.read())

outpt.seek(offset4)
img = open("pic4.bmp", "rb")
outpt.write(img.read())

outpt.close()
