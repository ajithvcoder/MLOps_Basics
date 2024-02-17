from flask import Flask, request, jsonify
from torchvision import models, transforms
import torchvision.transforms as trans
import numpy as np

import cv2
import torch

model = torch.jit.load('./yolov8n_torch.pt')

app = Flask(__name__)

def detect_objects(image):
    img_size = 640
    transform = trans.Compose([
            trans.ToTensor(),
            trans.Resize((img_size, img_size))
        ])
    image = transform(image).unsqueeze(0)

    inference_output = model(image)
    outputs = np.array([cv2.transpose(inference_output[0].numpy())])
    rows = outputs.shape[1]

    boxes = []
    scores = []
    class_ids = []

    for i in range(rows):
        classes_scores = outputs[0][i][4:]
        (minScore, maxScore, minClassLoc, (x, maxClassIndex)) = cv2.minMaxLoc(classes_scores)
        if maxScore >= 0.25:
            box = [
                outputs[0][i][0] - (0.5 * outputs[0][i][2]), outputs[0][i][1] - (0.5 * outputs[0][i][3]),
                outputs[0][i][2], outputs[0][i][3]]
            boxes.append(box)
            scores.append(maxScore)
            class_ids.append(maxClassIndex)

    result_boxes = cv2.dnn.NMSBoxes(boxes, scores, 0.25, 0.45, 0.5)

    detections = []
    for i in range(len(result_boxes)):
        index = result_boxes[i]
        box = boxes[index]
        detection = {
            'class_id': class_ids[index],
            'class_name': str(class_ids[index]),
            'confidence': scores[index],
            'box': [c.item() for c in box],
            'scale': img_size / 640}
        # print(detection)
        detections.append(detection)

    # format each detection
    return [detections]

@app.route('/detect', methods=['POST'])
def detect():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    try:
        image_stream = file.stream
        image_stream.seek(0)
        image_array = bytearray(image_stream.read())
        image_cv2 = cv2.imdecode(np.asarray(bytearray(image_array), dtype=np.uint8), cv2.IMREAD_COLOR)

        # Convert BGR to RGB (OpenCV uses BGR by default)
        image_rgb = cv2.cvtColor(image_cv2, cv2.COLOR_BGR2RGB)
        results = detect_objects(image_rgb)
        # print("results")
        return results
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/')
def hello_world():
    return 'Hello, World From app1 !'

if __name__ == "__main__":

    app.run(host='0.0.0.0', port=8085) #local host