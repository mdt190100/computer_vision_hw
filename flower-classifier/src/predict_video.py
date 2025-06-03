import cv2
import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model("../model/flower_mobilenetv2.h5")
class_names = ['daisy', 'dandelion', 'roses', 'sunflowers', 'tulips']

def preprocess_frame(frame):
    img = cv2.resize(frame, (224,224))
    img = img.astype('float32') / 255.0
    img = np.expand_dims(img, axis=0)
    return img

video_path = r"D:\computer vision\project\flower-classifier\data\flower_videos\test_flower_video.mp4"  # Đổi thành đường dẫn video của bạn
cap = cv2.VideoCapture(video_path)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    input_img = preprocess_frame(frame)
    preds = model.predict(input_img)
    class_idx = np.argmax(preds)
    label = class_names[class_idx]
    confidence = preds[0][class_idx]

    cv2.putText(frame, f"{label}: {confidence:.2f}", (10,30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    cv2.imshow("Flower Classification", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
