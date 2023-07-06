from PIL import Image

# resizing image

length = 30

with Image.open("check_mark.png") as old_check_mark:
    resized_check_mark = old_check_mark.resize((length, length))
    resized_check_mark.save("resized_check_mark.png")

with Image.open("x.png") as old_x_mark:
    resized_x_mark = old_x_mark.resize((length, length))
    resized_x_mark.save("resized_x_mark.png")
