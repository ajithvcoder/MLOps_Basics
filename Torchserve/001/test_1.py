# Single image inference time

import requests
import json
import cv2

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
    outputs = json.loads(response.text)

    img = cv2.imread(file_path)
    # print(outputs)
    # Loop through each bounding box and draw on the image
    for output in outputs[0]:
        # print(output["box"])
        x, y, w, h = map(int, output["box"])
        class_name = output["class_name"]
        confidence = output["confidence"]

        # Draw bounding box on the image
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display class name and confidence
        text = f"{class_name}: {confidence:.2f}"
        cv2.putText(img, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    cv2.imwrite('output.jpg', img)
# Check the response
if response.status_code == 200:
    print("File uploaded successfully!")
else:
    print(f"Error uploading file: {response.status_code} - {response.text}")
