from http.client import responses
import requests
import ctypes

def set_desktop_background_image(image_path):
    """"
This function is setting the image as the background with the set parameters

    """
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)

def download_image_from_url(image_url, save_path):
    """
Downloading image from url and commit it to the images folder
    """
    print("Downloading image from URL...", end='')

    response = requests.get(image_url)
    

    if response.status_code == 200:
        print('success')
        img_data = response.content

          
        with open(save_path, 'wb') as file: 
            file.write(img_data)
        print('success')
    else: 
        print('failed. Response code:', response.status_code)
       
    
  