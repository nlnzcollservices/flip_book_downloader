import tkinter as tk
from tkinter import filedialog, messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from PIL import Image

def crop_image(input_path, output_path, top_percent, bottom_percent, left_percent, right_percent):
    """Cropping shapshots by given percentage.
    Parameters:
        input_path(str) - path to image,
        output_path(str) - path to cropped image
        top_percent, bottom_percent, left_percent, right_percent (float or integer) - percent to crop image from each side
    """
    img = Image.open(input_path)
    width, height = img.size
    left = width * left_percent / 100
    top = height * top_percent / 100
    right = width - (width * right_percent / 100)
    bottom = height - (height * bottom_percent / 100)
    img_cropped = img.crop((left, top, right, bottom))
    img_cropped.save(output_path)
    os.remove(input_path)  # Remove the original screenshot

def download_and_crop_pages(url, delay_time, output_folder, page_count, front_top, front_bottom, front_left, front_right, top, bottom, left, right, vertical):
    options = Options()
    # Uncomment next line to run headless
    # options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.set_window_size(1920, 1080)

    try:
        base_url = url.replace(url.split("/")[-1], '#p=')
        for page_number in range(1, page_count + 1):
            print(page_number)
            current_page = int(page_number)  # Treat as integer
            next_page = page_number + 1 if page_number + 1 <= page_count else None
            current_url = base_url + str(current_page)
            time.sleep(delay_time)
            if page_number == 1:
                screenshot_name = f'page_001_temp.png'
                driver.get(current_url)
                driver.execute_script("document.body.style.zoom='150%'")
                WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body")))
                time.sleep(delay_time)
                driver.save_screenshot(os.path.join(output_folder, screenshot_name))
                crop_image(os.path.join(output_folder, screenshot_name), os.path.join(output_folder, screenshot_name.replace("_temp", "")), front_top, front_bottom, front_left, front_right)
                print(f'Screenshot saved: {screenshot_name}')
            else:
                if current_page % 2 == 0:  # even:
                    driver.get(current_url)
                    driver.execute_script("document.body.style.zoom='150%'")
                    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body")))
                    time.sleep(2)

                    if next_page:
                        screenshot_name = f'page_{current_page:03d}_{next_page:03d}_temp.png'
                    else:
                        screenshot_name = f'page_{current_page:03d}_temp.png'
                    driver.save_screenshot(os.path.join(output_folder, screenshot_name))
                    if not vertical:
                        crop_image(os.path.join(output_folder, screenshot_name), os.path.join(output_folder, screenshot_name.replace("_temp", "")), top, bottom, left, right)
                    else:
                        crop_image(os.path.join(output_folder, screenshot_name), os.path.join(output_folder, screenshot_name.replace("_temp", "")), front_top, front_bottom, front_left, front_right)

            print(f'Screenshot saved: {screenshot_name}')
    finally:
        driver.quit()

def browse_folder():
    filename = filedialog.askdirectory()
    folder_path_entry.delete(0, tk.END)
    folder_path_entry.insert(0, filename)

def start_process():
    url = url_entry.get()
    output_folder = folder_path_entry.get()
    page_count = page_count_entry.get()
    
    if not url or not output_folder or not page_count:
        messagebox.showerror("Input Error", "URL, Number of Pages, and Output Folder cannot be empty.")
        return
    
    delay_time = float(delay_time_entry.get())
    front_top = float(front_top_entry.get())
    front_bottom = float(front_bottom_entry.get())
    front_left = float(front_left_entry.get())
    front_right = float(front_right_entry.get())
    top = float(top_entry.get())
    bottom = float(bottom_entry.get())
    left = float(left_entry.get())
    right = float(right_entry.get())
    vertical = vertical_var.get() == 1
    
    try:
        page_count = int(page_count)
    except ValueError:
        messagebox.showerror("Input Error", "Number of Pages must be an integer.")
        return
    
    download_and_crop_pages(url, delay_time, output_folder, page_count, front_top, front_bottom, front_left, front_right, top, bottom, left, right, vertical)

def gui():
    global url_entry, folder_path_entry, page_count_entry, front_top_entry, front_bottom_entry, front_left_entry, front_right_entry, top_entry, bottom_entry, left_entry, right_entry, delay_time_entry, vertical_var

    app = tk.Tk()
    app.title('Flipbook Downloader and Cropper')

    tk.Label(app, text='Flipbook Base URL:').pack(padx=10, pady=10)
    url_entry = tk.Entry(app, width=50)
    url_entry.pack(padx=10, pady=5)

    tk.Label(app, text='Number of Pages:       Is the last page single?').pack(padx=10, pady=10)
    page_frame = tk.Frame(app)
    page_frame.pack(padx=10, pady=4)

    page_count_entry = tk.Entry(page_frame, width=10)
    page_count_entry.grid(row=0, column=0, padx=5)

    tk.Label(page_frame, text='').grid(row=0, column=1, padx=5)
    vertical_var = tk.IntVar(value=0)
    tk.Radiobutton(page_frame, text='Yes', variable=vertical_var, value=1).grid(row=0, column=2, padx=5)
    tk.Radiobutton(page_frame, text='No', variable=vertical_var, value=0).grid(row=0, column=3, padx=5)

    tk.Label(app, text='Output Folder:').pack(padx=10, pady=10)
    folder_path_entry = tk.Entry(app, width=50)
    folder_path_entry.pack(padx=10, pady=5)

    browse_button = tk.Button(app, text='Browse', command=browse_folder)
    browse_button.pack(padx=10, pady=5)

    tk.Label(app, text='Single Page Crop: (<50%)').pack(padx=10, pady=10)
    page_crop_frame = tk.Frame(app)
    page_crop_frame.pack(padx=10, pady=5)

    tk.Label(page_crop_frame, text='Top:').grid(row=0, column=0)
    front_top_entry = tk.Entry(page_crop_frame, width=10)
    front_top_entry.grid(row=0, column=1)
    front_top_entry.insert(0, "5")

    tk.Label(page_crop_frame, text='Bottom:').grid(row=0, column=2)
    front_bottom_entry = tk.Entry(page_crop_frame, width=10)
    front_bottom_entry.grid(row=0, column=3)
    front_bottom_entry.insert(0, "5")

    tk.Label(page_crop_frame, text='Left:').grid(row=1, column=0)
    front_left_entry = tk.Entry(page_crop_frame, width=10)
    front_left_entry.grid(row=1, column=1)
    front_left_entry.insert(0, "31")

    tk.Label(page_crop_frame, text='Right:').grid(row=1, column=2)
    front_right_entry = tk.Entry(page_crop_frame, width=10)
    front_right_entry.grid(row=1, column=3)
    front_right_entry.insert(0, "31")

    tk.Label(app, text='Double Page Crop: (<50%)').pack(padx=10, pady=10)
    crop_frame = tk.Frame(app)
    crop_frame.pack(padx=10, pady=5)

    tk.Label(crop_frame, text='Top:').grid(row=0, column=0)
    top_entry = tk.Entry(crop_frame, width=10)
    top_entry.grid(row=0, column=1)
    top_entry.insert(0, "5")

    tk.Label(crop_frame, text='Bottom:').grid(row=0, column=2)
    bottom_entry = tk.Entry(crop_frame, width=10)
    bottom_entry.grid(row=0, column=3)
    bottom_entry.insert(0, "5")

    tk.Label(crop_frame, text='Left:').grid(row=1, column=0)
    left_entry = tk.Entry(crop_frame, width=10)
    left_entry.grid(row=1, column=1)
    left_entry.insert(0, "11")

    tk.Label(crop_frame, text='Right:').grid(row=1, column=2)
    right_entry = tk.Entry(crop_frame, width=10)
    right_entry.grid(row=1, column=3)
    right_entry.insert(0, "11")

    tk.Label(app, text='Delay Time (seconds):').pack(padx=10, pady=10)
    delay_time_entry = tk.Entry(app, width=10)
    delay_time_entry.pack(padx=10, pady=5)
    delay_time_entry.insert(0, "2")

    start_button = tk.Button(app, text='Start Download and Crop', command=start_process)
    start_button.pack(padx=10, pady=10)

    app.mainloop()

if __name__ == '__main__':
    gui()
