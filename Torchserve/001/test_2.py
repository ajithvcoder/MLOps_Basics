# Send 100 images and inference time
import requests
import time
# URL where you want to send the POST request
url = 'http://127.0.0.1:8085/detect'

# Path to the file you want to upload
file_path = 'yolo_image.jpg'

num_requests = 100

# List to store response times
response_times = []

for _ in range(num_requests):
    # Open the file in binary mode
    with open(file_path, 'rb') as file:
        # Set up the files dictionary with the file name and contents
        files = {'file': (file_path, file, 'image/jpeg')}

        # Send the POST request with the files dictionary
        start_time = time.time()
        response = requests.post(url, files=files)
        end_time = time.time()
        
        # Calculate response time and add to list
        response_times.append(end_time - start_time)

        # Check the response
        if response.status_code == 200:
            print("File uploaded successfully!")
        else:
            print(f"Error uploading file: {response.status_code} - {response.text}")

print(response_times)
# Calculate average response time
average_response_time = sum(response_times) / num_requests
print(f"Average response time: {average_response_time} seconds")