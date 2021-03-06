import matplotlib
import tensorflow as tf
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# https: // stackoverflow.com/questions/53684971/assertion-failed-flask-server-stops-after-script-is-run
matplotlib.use('Agg')

def get_category(img):
    """Write a Function to Predict the Class Name
    Args:
        img [jpg]: image file
    Returns:
        [str]: Prediction
    """
    # Read an image from a file into a numpy array
    img = mpimg.imread(img)
    # Convert to float32
    img = tf.cast(img, tf.float32)
    # Expand img dimensions from (224, 224, 3) to (1, 224, 224, 3) for set_tensor method call
    img = np.expand_dims(img, axis=0)

    tflite_model_file = 'static/model/converted_model.tflite'

    with open(tflite_model_file, 'rb') as fid:
        tflite_model = fid.read()

    interpreter = tf.lite.Interpreter(model_content=tflite_model)
    interpreter.allocate_tensors()

    input_index = interpreter.get_input_details()[0]["index"]
    output_index = interpreter.get_output_details()[0]["index"]
    
    prediction = []
    interpreter.set_tensor(input_index, img)
    interpreter.invoke()
    prediction.append(interpreter.get_tensor(output_index))

    predicted_label = np.argmax(prediction)
    class_names = ['rock', 'paper', 'scissors']
    
    return class_names[predicted_label]


def plot_category(img):
    """Plot the input image
    Args:
        img [jpg]: image file
    """
    # Read an image from a file into a numpy array
    img = mpimg.imread(img)
    # Remove the plotting ticks
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(img, cmap=plt.cm.binary)
    # matplotlib would not overwrite previous image, so using this work around
    # https://stackoverflow.com/questions/49039581/matplotlib-savefig-will-not-overwrite-old-files
    strFile = 'static/images/output.png'
    if os.path.isfile(strFile):
        os.remove(strFile)
    # Save the image with the file name that result.html is using as its img src
    plt.savefig(strFile)