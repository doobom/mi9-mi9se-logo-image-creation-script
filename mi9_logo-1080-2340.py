import io

offset0 = 0x4000
offset1 = 0x5000
offset2 = 0x741000
offset3 = 0xE7D000
offset4 = 0x15B9000

outpt = open("logo_new_mi9.img", "wb")

emptyContent =  [0 for i in range(0x1CF5000)]

mi9offset = [0x4C, 0x4F, 0x47, 0x4F, 0x21, 0x21, 0x21, 0x21, 0x05, 0x00, 0x00, 0x00,
                0x3C, 0x07, 0x00, 0x00, 0x41, 0x07, 0x00, 0x00, 0x3C, 0x07, 0x00, 0x00,
                0x7D, 0x0E, 0x00, 0x00, 0x3C, 0x07, 0x00, 0x00, 0xB9, 0x15, 0x00, 0x00,
                0x3C, 0x07]

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
