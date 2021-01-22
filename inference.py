import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def get_category(img):
    """Write a Function to Predict the Class Name

    Args:
        img [jpg]: image file

    Returns:
        [str]: Prediction
    """
    # open image
    interpreter = tf.lite.Interpreter(model_path="converted_model.tflite")
    interpreter.allocate_tensors()

    # get input and output tensors
    input_index = interpreter.get_input_details()
    output_index = interpreter.get_output_details()

    interpreter.set_tensor(input_index, img)
    interpreter.invoke()
    predictions = interpreter.get_tensor(output_index)
    
    return predictions


def plot_category(img):
    """Plot the input image

    Args:
        img [jpg]: image file
    """
    fig = plt.figure(figsize=(8,8))
    plt.imshow(img)