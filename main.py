import segno
from urllib.request import urlopen
upi_id = "shalthaf123@okhdfcbank"
qr_data=segno.make_qr(f"upi://pay?pa={upi_id}&pn=ALTHAF&am=100&tn=InvoicePayment&cu=INR")
slts_qrcode = segno.make_qr("https://www.anther.tech")
nirvana_url = urlopen("https://instagram.fccj6-1.fna.fbcdn.net/v/t51.2885-15/186056033_292460802428121_4828455925983876151_n.jpg?stp=dst-jpg_e35&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xMDgweDExNDIuc2RyIn0&_nc_ht=instagram.fccj6-1.fna.fbcdn.net&_nc_cat=109&_nc_ohc=UafScVhKEEgAX_ficQ8&edm=ACWDqb8BAAAA&ccb=7-5&ig_cache_key=MjU3MzkyMjE3NDAyMTQ5NDcxOA%3D%3D.2-ccb7-5&oh=00_AfC0D4AAfcf1G4f0aBOUfSG1HNFVJn8HYWAy6RjQG0I2IA&oe=65C3080C&_nc_sid=ee9879")
# qrcode.save("basic_qrcode.png")
qr_data.to_artistic(
    background=nirvana_url,
    target="qrcode.jpeg",
    scale=50,
)

# import qrcode
# img = qrcode.make('''
# BEGIN:VCALENDAR
# VERSION:2.0
# BEGIN:VEVENT
# SUMMARY:Lunchtime meeting
# DTSTART;TZID=America/New_York:20230420T120000
# DURATION:PT1H
# LOCATION:Meeting Room 1
# END:VEVENT
# END:VCALENDAR
# ''')
# type(img)
# img.save("vcal.png")



# import PIL
# from PIL import Image, ImageDraw

# #Custom function for eye styling. These create the eye masks

# def style_inner_eyes(img):
#   img_size = img.size[0]
#   eye_size = 70 #default
#   quiet_zone = 40 #default
#   mask = Image.new('L', img.size, 0)
#   draw = ImageDraw.Draw(mask)
#   draw.rectangle((60, 60, 90, 90), fill=255) #top left eye
#   draw.rectangle((img_size-90, 60, img_size-60, 90), fill=255) #top right eye
#   draw.rectangle((60, img_size-90, 90, img_size-60), fill=255) #bottom left eye
#   return mask

# def style_outer_eyes(img):
#   img_size = img.size[0]
#   eye_size = 70 #default
#   quiet_zone = 40 #default
#   mask = Image.new('L', img.size, 0)
#   draw = ImageDraw.Draw(mask)
#   draw.rectangle((40, 40, 110, 110), fill=255) #top left eye
#   draw.rectangle((img_size-110, 40, img_size-40, 110), fill=255) #top right eye
#   draw.rectangle((40, img_size-110, 110, img_size-40), fill=255) #bottom left eye
#   draw.rectangle((60, 60, 90, 90), fill=0) #top left eye
#   draw.rectangle((img_size-90, 60, img_size-60, 90), fill=0) #top right eye
#   draw.rectangle((60, img_size-90, 90, img_size-60), fill=0) #bottom left eye  
#   return mask  

# # Useage of the custom functions
# import qrcode
# from qrcode.image.styledpil import StyledPilImage
# from qrcode.image.styles.moduledrawers import RoundedModuleDrawer,VerticalBarsDrawer,SquareModuleDrawer
# from  qrcode.image.styles.colormasks import SolidFillColorMask

# if not hasattr(PIL.Image, 'Resampling'):
#   PIL.Image.Resampling = PIL.Image
# # Now PIL.Image.Resampling.BICUBIC is always recognized.


# qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)

# qr.add_data('http://www.medium.com')

# qr_inner_eyes_img = qr.make_image(image_factory=StyledPilImage,
#                             eye_drawer=RoundedModuleDrawer(radius_ratio=1.2),
#                             color_mask=SolidFillColorMask(back_color=(255, 255, 255), front_color=(63, 42, 86)))

# qr_outer_eyes_img = qr.make_image(image_factory=StyledPilImage,
#                             eye_drawer=VerticalBarsDrawer(),
#                             color_mask=SolidFillColorMask(front_color=(255, 128, 0)))                            

# qr_img = qr.make_image(image_factory=StyledPilImage,
#                        module_drawer=SquareModuleDrawer())

# inner_eye_mask = style_inner_eyes(qr_img)
# outer_eye_mask = style_outer_eyes(qr_img)
# intermediate_img = Image.composite(qr_inner_eyes_img, qr_img, inner_eye_mask)
# final_image = Image.composite(qr_outer_eyes_img, intermediate_img, outer_eye_mask)
# final_image.save('final_image.png')
