import cv2
import matplotlib.pyplot as plt
import numpy as np
import time
from pathlib import Path
from openvino import Core
import os


model_path = Path("computer_vision_model/model/ov_model/")
model = Path(f"{model_path}/model.xml")
weights = Path(f"{model_path}/model.bin")

quantized_model_path = Path("computer_vision_model/model/quantized_model/")
quantized_model = Path(f"{model_path}/model.xml")
quantized_weights = Path(f"{model_path}/model.bin")
print("Model located at {}".format(model_path))
print("Quantized model located at {}".format(quantized_model_path))

core = Core()
read_model = core.read_model(model=model, weights=weights)
compiled_model = core.compile_model(model=model, device_name="CPU")
read_quantized_model = core.read_model(model=quantized_model, weights=quantized_weights)
compiled_quantized_model = core.compile_model(model=quantized_model, device_name="CPU")


def process_image(image_file, quantized=False):
    input_layer = compiled_model.input(0)
    output_layer = compiled_model.output(0)
    quantized_input_layer = compiled_quantized_model.input(0)
    quantized_output_layer = compiled_quantized_model.output(0)
    image = cv2.imread(filename=image_file)
    # Resize image to network input image shape
    resized_image = cv2.resize(src=image, dsize=(224, 224))

    # Transpose image to network input shape
    input_image = np.expand_dims(np.transpose(resized_image, (1, 0, 2)), 0)
    plt.imshow(image)
    result_classes = ["Earthquake", "Drought",
            "Damaged Infrastructure", "Human Damage", "Human", "Land Slide", "Non Damage Buildings and  Street", "Non Damage Wildlife Forest",
            "Sea", "Urban Fire", "Wild Fire", "Water Disaster"]    
    '''
    code below is for dev mode only
    '''
    if os.environ.get("env") == "development":
        pass

    '''  ^^ for dev mode only  '''

    if quantized:
        quantized_result = compiled_quantized_model(inputs={quantized_input_layer: input_image})[quantized_output_layer]
        result_index = np.argmax(quantized_result)
        return f"AI detected {result_classes[result_index]}"
    else:
        normal_result = compiled_model(inputs={input_layer: input_image})[output_layer]
        result_index = np.argmax(normal_result)
        return f"AI detected {result_classes[result_index]}"

    


