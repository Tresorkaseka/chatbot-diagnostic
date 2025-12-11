import torch
import tensorflow as tf

print("Checking GPU availability...")

# Check for CUDA availability with PyTorch
print(f"PyTorch CUDA available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"Number of CUDA devices: {torch.cuda.device_count()}")
    for i in range(torch.cuda.device_count()):
        print(f"CUDA device {i}: {torch.cuda.get_device_name(i)}")

# Check for GPU availability with TensorFlow
print(f"TensorFlow GPU available: {tf.config.list_physical_devices('GPU')}")

# Check with TensorFlow 2.x
try:
    print(f"TensorFlow built with CUDA: {tf.test.is_built_with_cuda()}")
    print(f"TensorFlow GPU available: {tf.test.is_gpu_available()}")  # deprecated but still works
except:
    # For newer versions of TensorFlow
    gpus = tf.config.experimental.list_physical_devices('GPU')
    print(f"TensorFlow GPUs available: {gpus}")