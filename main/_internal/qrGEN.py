import qrcode

# taking the desired id's of the people 
n = int(input("Enter the number of people qr code should be generated: "))
lower_bound = int(input("Enter the first id: "))

rollnumbers = []

# making the list of id's
for i in range(n):
    rollnumbers.append(i + lower_bound)

# generating the qrcodes 
for roll in rollnumbers:
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    qr.add_data(roll)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save('QrCodes\\roll_number_{}.png'.format(roll))

print("Qr codes have been generated.")
