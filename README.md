# Deprecated - See [Flipbook-Webscraping](https://github.com/nlnzcollservices/Flipbook-Webscraping) instead.

----

# Flip Book Downloader and Cropper

This project contains a Python script `flip_book_downloader.py` designed to download and crop images from an online flipbook. The purpose of this script is to collect pages from the publication available at [this link](https://online.fliphtml5.com/xpldh/hdnh/#p=1).

## Features

- **Download Pages**: Automatically navigate through the pages of the flipbook and download screenshots.
- **Crop Images**: Crop the downloaded images based on specified percentages to remove unwanted margins.
- **User Interface**: A simple GUI built with Tkinter to input the base URL, number of pages, and crop percentages.

## Requirements

- Python 3.x
- Selenium
- Pillow
- Tkinter
- Firefox WebDriver

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/nlnzcollservices/flipbook_downloader.git
    cd flipbook_downloader
    ```

2. **Install the required packages**:
    ```sh
    pip install selenium pillow
    ```

3. **Download the GeckoDriver**:
   - Download the GeckoDriver for Firefox from [here](https://github.com/mozilla/geckodriver/releases).
   - Make sure the GeckoDriver executable is in your PATH.

## Usage

1. **Run the script**:
    ```sh
    python flip_book_downloader.py
    ```

2. **Fill in the details in the GUI**:
   - **Flipbook Base URL**: Enter the base URL of the flipbook.
   - **Number of Pages**: Enter the total number of pages in the flipbook.
   - **Is the last page single?**: Indicate if the last page is single or part of a double-page spread.
   - **Output Folder**: Choose the folder where the downloaded and cropped images will be saved.
   - **Crop Percentages**: Enter the percentages to crop from the top, bottom, left, and right for both single and double pages.
   - **Delay Time**: Enter the delay time between page navigations.

3. **Start the process**:
   - Click the "Start Download and Crop" button to begin downloading and cropping the flipbook pages.

## Example

- **Flipbook Base URL**: ``
- **Number of Pages**: `10`
- **Is the last page single?**: `No`
- **Output Folder**: `./output`
- **Crop Percentages**:
  - **Single Page**: Top: 5%, Bottom: 5%, Left: 31%, Right: 31%
  - **Double Page**: Top: 5%, Bottom: 5%, Left: 11%, Right: 11%
- **Delay Time**: `2` seconds

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for details.

## Contributing

Feel free to submit issues or pull requests if you have any improvements or bug fixes.

## Acknowledgments

- This project uses the Selenium and Pillow libraries.
