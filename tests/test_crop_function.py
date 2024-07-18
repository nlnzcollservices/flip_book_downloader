import pytest
from PIL import Image
import shutil
import os

# Define the crop_image function in the test file
def crop_image(input_path, output_path, top_percent, bottom_percent, left_percent, right_percent):
    img = Image.open(input_path)
    width, height = img.size
    left = width * left_percent / 100
    top = height * top_percent / 100
    right = width - (width * right_percent / 100)
    bottom = height - (height * bottom_percent / 100)
    img_cropped = img.crop((left, top, right, bottom))
    img_cropped.save(output_path)

def test_crop_image_vertical(tmp_path):
    # Paths for input and output
    original_image_path = os.path.join(os.getcwd(), 'images', 'single.png')
    input_path = tmp_path / "single_temp.png"
    output_path = tmp_path / "cropped_vertical.png"

    # Copy the original image to a temporary path
    shutil.copyfile(original_image_path, input_path)

    # Crop image with given percentages
    crop_image(input_path, output_path, 10, 10, 10, 10)

    # Load the cropped image
    cropped_img = Image.open(output_path)

    # Expected size (based on cropping 10% from each side)
    img = Image.open(input_path)
    expected_size = (round(img.width * 0.8), round(img.height * 0.8))

    # Verify the size of the cropped image
    assert cropped_img.size == expected_size

def test_crop_image_horizontal(tmp_path):
    # Paths for input and output
    original_image_path = os.path.join(os.getcwd(), 'images', 'double.png')
    input_path = tmp_path / "double_temp.png"
    output_path = tmp_path / "cropped_horizontal.png"

    # Copy the original image to a temporary path
    shutil.copyfile(original_image_path, input_path)

    # Crop image with given percentages
    crop_image(input_path, output_path, 10, 10, 10, 10)

    # Load the cropped image
    cropped_img = Image.open(output_path)

    # Expected size (based on cropping 10% from each side)
    img = Image.open(input_path)
    expected_size = (round(img.width * 0.8), round(img.height * 0.8))

    # Verify the size of the cropped image
    assert cropped_img.size == expected_size

# The following is necessary for running the tests directly
if __name__ == "__main__":
    pytest.main()
