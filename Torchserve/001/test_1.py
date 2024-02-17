# Single image inference time

import requests

# URL where you want to send the POST request
url = 'http://127.0.0.1:8085/detect'

# Path to the file you want to upload
file_path = 'yolo_image.jpg'

# Open the file in binary mode
with open(file_path, 'rb') as file:
    # Set up the files dictionary with the file name and contents
    files = {'file': (file_path, file, 'image/jpeg')}

    # Send the POST request with the files dictionary
    response = requests.post(url, files=files)
    print(response.text)

# Check the response
if response.status_code == 200:
    print("File uploaded successfully!")
else:
    print(f"Error uploading file: {response.status_code} - {response.text}")
