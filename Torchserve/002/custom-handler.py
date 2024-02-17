"""Custom TorchServe model handler for YOLOv8 models.
"""
from ts.torch_handler.base_handler import BaseHandler
import numpy as np
import base64
import torch
import torchvision.transforms as trans
import io
import cv2


class ModelHandler(BaseHandler):
    """
    Model handler for YoloV8 bounding box model
    """

    img_size = 640
    """Image size (px). Images will be resized to this resolution before inference.
    """

    def __init__(self):
        # call superclass initializer
        super().__init__()
        self.transform = trans.Compose([
            trans.ToTensor(),
            trans.Resize((640, 640)),  # Assuming you want to resize to 640x640
        ])

    def handle(self, data, context):
        """
        Invoke by TorchServe for prediction request.
        Do pre-processing of data, prediction using model and postprocessing of prediction output
        :param data: Input data for prediction
        :param context: Initial context contains model server system properties.
        :return: prediction output
        """
        model_input = self.preprocess(data)
        model_output = self.inference(model_input)
        return self.postprocess(model_output)


    def preprocess(self, data):
        """Converts input images to float tensors.
        Args:
            data (List): Input data from the request in the form of a list of image tensors.
        Returns:
            Tensor: single Tensor of shape [BATCH_SIZE, 3, IMG_SIZE, IMG_SIZE]
        """

        # print(data)
        # print(data[0].keys())
        # image_data = np.frombuffer(data[0]['file'], dtype=np.uint8)
        # image = cv2.imdecode(image_data, cv2.IMREAD_COLOR)

        # # Convert the image to RGB format (OpenCV reads images in BGR format)
        # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # print("debuggingimage")
        # print(image.shape)
        # image = torch.tensor(image, dtype=torch.float32).permute(2, 0, 1) 
        # images = []
        file = data[0]['file']
        # image_stream = file.stream
        # image_stream.seek(0)
        # image_array = bytearray(image_stream.read())
        image_cv2 = cv2.imdecode(np.asarray(bytearray(file), dtype=np.uint8), cv2.IMREAD_COLOR)

        # Convert BGR to RGB (OpenCV uses BGR by default)
        image_rgb = cv2.cvtColor(image_cv2, cv2.COLOR_BGR2RGB)


        images_tensor = self.transform(image_rgb).unsqueeze(0)
        # images_tensor = images_tensor[:, :3, :, :]
        # print("########## Image tensor #######")
        # print(images_tensor.shape)
        return images_tensor

    def inference(self, data):
        output = self.model(data)
        return output

    def postprocess(self, inference_output):
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
                'scale': self.img_size / 640}
            # print(detection)
            detections.append(detection)

        # format each detection
        return [detections]