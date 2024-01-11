from PIL import Image

# Load image
im = Image.open('levine_fix_1.png')                                                                 

# Convert to palette mode and save
im.convert('P').save('levine.png')