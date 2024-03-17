# 001 - Serve with Flask

001 - In flask itself you can inference if you have a model why torchserve ?

run the docker earlier itself 

<-- docker build -t flask-001 . --> dont run this instead for this alonge go from next step as its time consumming

docker run -p 8085:8085 -v "<hostpath>":/app -it flask-001  bash

docker run -p 8085:8085 -v "C:\Users\MCW\Documents\Ajith\mcw_interns_3\Torchserve\001":/app -it flask-001  bash

docker exec -it b2948b8e5114 bash

copy files from Torchserve/001/ to docker

Scalability -  TorchServe is designed to handle scalable inference workloads efficiently

Model Lifecycle Management- model versioning, model health monitoring, and automatic scaling

Infrastructure Abstraction - hiding complex underlying details of hardware and software infrastructure to simplify interactions with it.

Performance - lets test
CPU Average response time: 0.2689952802658081 seconds - 1000 runs

# 002 - Torch serve with pytorch

https://github.com/ultralytics/ultralytics/issues/493#issuecomment-1784328169

<!-- docker build -t torchserve-002 . -->

docker run -v "<hostpath>":/usr/app -it torchserve-002 bash
docker run -v "C:\Users\MCW\Documents\Ajith\mcw_interns_3\Torchserve\002":/usr/app -it torchserve-002 bash

mkdir model-store

- torch-model-archiver --model-name yolov8n --version 1.0 --serialized-file yolov8n_torch.pt --handler custom-handler.py

mv yolov8n.mar model-store/

- torchserve --start --model-store model-store --models yolov8n=yolov8n.mar --foreground --no-config-snapshot --ts-config config.yaml

CPU Average response time: 0.22576165080070495 seconds - 1000 runs

The response time is just a sequential run torchserve will perform better than flask if you configure it properly and use it in a proper way like inferencing in GPU, using more workers, allocation of nodes etc..

# 003 - Torch serve with onnx 

<!-- docker build -t torchserve-003 . -->
docker run -v "C:\Users\MCW\Documents\Ajith\mcw_interns_3\Torchserve\003":/usr/app -p 8080:8080 -p 8081:8081 -p 8083:8083 -it torchserve-003 bash

- torch-model-archiver -f --model-name yolov8n --version 1.0 --serialized-file models/yolov8n.onnx --export-path model-store --handler custom-handler.py

- torchserve --start --ncs --model-store model-store --models yolov8n=yolov8n.mar --ts-config config.properties

Average response time: 0.32311110734939574 seconds

Onnx should be faster than torch usually need to check on it.

TODO: show how to access 8081 and 8082
http://localhost:8081/models