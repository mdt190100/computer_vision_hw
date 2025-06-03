import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import os

def load_model(path="flower_classifier_model.h5"):
    return tf.keras.models.load_model(path)

def predict_image(model, img_path, class_names):
    img = image.load_img(img_path, target_size=(180,180))
    img_array = image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # tạo batch size 1
    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    print(f"Predicted: {class_names[np.argmax(score)]} ({100 * np.max(score):.2f}%)")

if __name__ == "__main__":
    model = load_model()
    class_names = sorted(os.listdir("../data/flower_photos"))
    test_img = "../data/flower_photos/daisy/123456.jpg"  # đổi thành ảnh test của bạn
    predict_image(model, test_img, class_names)
