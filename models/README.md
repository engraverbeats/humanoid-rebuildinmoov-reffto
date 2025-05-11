# AI Models

This folder contains AI models optimized using NVIDIA TensorRT.
Include your `.engine` files or ONNX models here.

## Model Examples

- `object_detection.engine` – TensorRT-optimized YOLOv5 model for real-time object detection.
- `face_tracking.onnx` – ONNX model used for facial landmark detection and eye tracking.
- `voice_command.engine` – Optimized deep speech model for command recognition.

Ensure these models are correctly integrated in your ROS nodes using TensorRT or ONNX Runtime.


## How to Get the Real Models

- **object_detection.engine**: Convert YOLOv5 ONNX to TensorRT using `torch2trt` or NVIDIA `trtexec` tool.
- **face_tracking.onnx**: Export from models like MediaPipe Face Mesh or use a pretrained ONNX model.
- **voice_command.engine**: Use DeepSpeech or Whisper model and convert it using NVIDIA TensorRT.

Make sure to place the models here using the exact filenames mentioned above.
