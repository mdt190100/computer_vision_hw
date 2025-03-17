import cv2 as cv
import numpy as np

# Cấu hình video
video_source = 0  # 0 là webcam mặc định
video = cv.VideoCapture(video_source)

# Kiểm tra nếu mở được webcam
if not video.isOpened():
    print("Không thể mở webcam!")
    exit()

# Thiết lập thông số ghi video
fourcc = cv.VideoWriter_fourcc(*'XVID')
fps = 20
frame_size = (int(video.get(cv.CAP_PROP_FRAME_WIDTH)), int(video.get(cv.CAP_PROP_FRAME_HEIGHT)))
output = cv.VideoWriter('output.avi', fourcc, fps, frame_size)

# Trạng thái chương trình
recording = False  # Trạng thái quay video
brightness = 0      # Điều chỉnh độ sáng
flip_mode = 1       # 1: Lật ngang, 0: Không lật

while True:
    ret, frame = video.read()
    if not ret:
        break

    # Áp dụng filter (tăng/giảm độ sáng)
    frame = cv.convertScaleAbs(frame, alpha=1, beta=brightness)

    # Lật hình nếu cần
    if flip_mode:
        frame = cv.flip(frame, 1)  # Lật ngang

    # Hiển thị vòng tròn đỏ khi quay
    if recording:
        cv.circle(frame, (50, 50), 20, (0, 0, 255), -1)
        output.write(frame)  # Ghi video

    # Hiển thị chế độ hiện tại
    mode_text = "Record" if recording else "Preview"
    text_color = (0, 0, 255) if recording else (255, 255, 255)  # Đỏ khi ghi, trắng khi xem trước
    cv.putText(frame, f"Mode: {mode_text}", (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, text_color, 2)

    # Hiển thị hình ảnh
    cv.imshow('Video Recorder', frame)

    # Xử lý phím bấm
    key = cv.waitKey(1)
    if key == 27:  # ESC để thoát
        break
    elif key == 32:  # Space để chuyển chế độ
        recording = not recording
    elif key == ord('+'):  # Tăng độ sáng
        brightness += 10
    elif key == ord('-'):  # Giảm độ sáng
        brightness -= 10
    elif key == ord('f'):  # Bật/tắt lật ảnh
        flip_mode = 1 - flip_mode

# Giải phóng tài nguyên
video.release()
output.release()
cv.destroyAllWindows()
