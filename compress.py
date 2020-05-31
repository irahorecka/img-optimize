"""Python module to compress jpg files in personalWebsite/static/bike_img"""

import os
from PIL import Image, UnidentifiedImageError

ORIG_PATH = "/Users/irahorecka/Desktop/Harddrive_Desktop/Python/ImgCompressor/orig_img"
COMP_PATH = "/Users/irahorecka/Desktop/Harddrive_Desktop/Python/ImgCompressor/comp_img"


def verify_image_extension(method):
    """Wrapper to check appropriate extension of img file"""

    def wrapper(*args, **kwargs):
        allowed_ext = (".jpg", ".png", ".jpeg")
        img_path = args[0]
        _, img_ext = os.path.splitext(img_path)
        if img_ext.lower() not in allowed_ext:
            raise ValueError("Sorry this is not a compatible file type.")

        return method(img_path)

    return wrapper


@verify_image_extension
def open_image(img_path):
    """Open image in pillow"""
    try:
        img = Image.open(img_path)
    except UnidentifiedImageError:
        return
    return img


def save_image(img, save_img_path, img_quality=80):
    """Save pillow img obj"""
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")
    img.save(save_img_path, optimize=True, quality=img_quality)  # change quality here


if __name__ == "__main__":
    bike = os.path.join(ORIG_PATH, "bike.JPEG")
    bike_img = open_image(bike)
    if not bike_img:
        print("whoops, bad image.")
    else:
        save_path = os.path.join(COMP_PATH, "bike.jpg")
        save_image(bike_img, save_path)
