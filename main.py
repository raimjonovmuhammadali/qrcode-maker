import qrcode

manzil = input("QrCode uchun manzilni kiriting \n>>> ")
qrcode.make(manzil).save('code.jpg')

#Qrcode maker dasturi
#Raimjonov Muhammadali