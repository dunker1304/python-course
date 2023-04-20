# IOPub data rate exceeded

from PIL import Image

nin = Image.open('./z4145695011321_0f084a60a3b78b62fde2e46c0e02d291.jpg')

# nin.show()
# nin.size, attrs

# crop image
crop = nin.crop((0,0,200,200))

# modify image
nin.paste(crop, (0,0,200,200))