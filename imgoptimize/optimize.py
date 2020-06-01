import os
from PIL import Image, UnidentifiedImageError


def open_image(img_path):
    """Open image in pillow"""
    try:
        img = Image.open(img_path)
    except UnidentifiedImageError as error:
        print(error)
        return
    return img


def save_image(img, save_img_path, img_quality=80):
    """Save pillow img obj"""
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")
    img.save(save_img_path, optimize=True, quality=img_quality)  # change quality here
