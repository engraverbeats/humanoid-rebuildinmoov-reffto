import os
import numpy as np
import cv2

try:
    import onnxruntime as ort
except ImportError:
    ort = None
    print("ONNX Runtime not found. Please install it with: pip install onnxruntime")

def load_onnx_model(model_path):
    if not ort:
        raise ImportError("ONNX Runtime is required but not installed.")
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")
    
    print(f"Loading ONNX model from: {model_path}")
    session = ort.InferenceSession(model_path)
    return session

def run_inference(session, input_data):
    input_name = session.get_inputs()[0].name
    output_name = session.get_outputs()[0].name
    print(f"Running inference on input: {input_name}")
    outputs = session.run([output_name], {input_name: input_data})
    return outputs

if __name__ == "__main__":
    # Example usage
    model_file = "models/face_tracking.onnx"
    session = load_onnx_model(model_file)

    dummy_input = np.random.rand(1, 3, 224, 224).astype(np.float32)  # Simulated input
    results = run_inference(session, dummy_input)

    print("Inference results:", results)
