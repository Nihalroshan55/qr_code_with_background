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

