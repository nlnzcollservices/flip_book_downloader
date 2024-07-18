import pytest
from PIL import Image
import os
import sys
import shutil


# Add the flipbook_downloader directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the functions to be tested
from flip_book_downloader import crop_image

# Test crop_image function
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
    img = Image.open(original_image_path)
    expected_size = (round(img.width * 0.8), round(img.height * 0.8))

    # Verify the size of the cropped image
    assert cropped_img.size == expected_size

    # Verify the input image was removed
    assert not os.path.exists(input_path)

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
    img = Image.open(original_image_path)
    expected_size = (round(img.width * 0.8), round(img.height * 0.8))

    # Verify the size of the cropped image
    assert cropped_img.size == expected_size

    # Verify the input image was removed
    assert not os.path.exists(input_path)

# The following is necessary for running the tests directly
if __name__ == "__main__":
    pytest.main()
