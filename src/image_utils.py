from PIL import Image
import matplotlib.pyplot as plt
import os

def display_image_info(image_path):
    img = Image.open(image_path)
    print("Image Information:")
    print("Format:", img.format)
    print("Size:", img.size)
    print("Mode:", img.mode)

    file_size_bytes = os.path.getsize(image_path)
    print(f"File Size: {file_size_bytes / 1024:.2f} KB")

def resize_image(image_path, new_size):
    img = Image.open(image_path)
    img = img.resize(new_size)
    img.save("resized_image.jpg")
    print("Image resized and saved as 'resized_image.jpg'")

def crop_image(image_path, crop_box):
    img = Image.open(image_path)
    img = img.crop(crop_box)
    img.save("cropped_image.jpg")
    print("Image cropped and saved as 'cropped_image.jpg'")
