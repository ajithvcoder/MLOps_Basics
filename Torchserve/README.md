001 - In flask itself you can inference if you have a model why torchserve ?
docker run -it flask-torch-001 .
copy files from Torchserve/001/ to docker

Scalability -  TorchServe is designed to handle scalable inference workloads efficiently
Model Lifecycle Management- model versioning, model health monitoring, and automatic scaling
Infrastructure Abstraction - hiding complex underlying details of hardware and software infrastructure to simplify interactions with it.

Performance - lets test
CPU Average response time: 0.2689952802658081 seconds - 1000 runs

002 - Torch serve with pytorch
https://github.com/ultralytics/ultralytics/issues/493#issuecomment-1784328169

docker build -t torchserve-002 .
docker run -it torchserve-002 bash
mkdir model-store
torch-model-archiver --model-name yolov8n --version 1.0 --serialized-file yolov8n_torch.pt --handler custom-handler.py
mv yolov8n.mar model-store/
torchserve --start --model-store model-store --models yolov8n=yolov8n.mar --foreground --no-config-snapshot --ts-config config.yaml
CPU Average response time: 0.22576165080070495 seconds - 1000 runs

The response time is just a sequential run torchserve will perform better than flask if you configure it properly and use it in a proper way like inferencing in GPU, using more workers, allocation of nodes etc..

003 - Torch serve with onnx 

torch-model-archiver -f --model-name yolov8n --version 1.0 --serialized-file models/yolov8n.onnx --export-path model-store --handler custom-handler.py

torchserve --start --ncs --model-store model-store --models yolov8n=yolov8n.mar --ts-config config.properties
Average response time: 0.32311110734939574 seconds

Onnx should be faster than torch usually need to check on it.

Todo: check the output of torchserve 001,002,003
