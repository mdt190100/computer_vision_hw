import cv2
import numpy as np

# Khởi tạo camera
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
fps = 30  # Định nghĩa FPS
out = cv2.VideoWriter('output.avi', fourcc, fps, (640, 480))

recording = False  # Biến kiểm soát trạng thái ghi hình
blurred = False    # Biến kiểm soát trạng thái làm mờ

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't open camera.")
        break

    # Áp dụng hiệu ứng làm mờ nếu cần
    if blurred:
        frame = cv2.GaussianBlur(frame, (15, 15), 0)

    # Nếu đang ghi ... hiển thị dấu hiệu ghi hình
    if recording:
        cv2.circle(frame, (50, 50), 10, (0, 0, 255), -1)  # Vẽ vòng tròn đỏ

    # Hiển thị video
    cv2.imshow('Video Recorder', frame)

    # Kiểm tra phím nhấn
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC để thoát
        break
    elif key == 32:  # Space để bật/tắt ghi hình
        recording = not recording
        if recording:
            print("Recording...")
        else:
            print("Preview mode")
    elif key == ord('b'):  # Phím b để bật/tắt làm mờ
        blurred = not blurred
        if blurred:
            print("Bật hiệu ứng làm mờ...")
        else:
            print("Tắt hiệu ứng làm mờ...")

    if recording:
        out.write(frame)

# Giải phóng tài nguyên
cap.release()
out.release()
cv2.destroyAllWindows()
