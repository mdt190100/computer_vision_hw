import cv2
import numpy as np

# Đường dẫn ảnh
image_path = '1.jpg'  # Thay bằng đường dẫn đầy đủ của bạn

# Load ảnh
img = cv2.imread(image_path)
if img is None:
    print(f"Không thể tải ảnh từ đường dẫn: {image_path}")
    exit()

# Resize ảnh
height, width = img.shape[:2]
new_width = 400  # Kích thước bạn muốn
new_height = int(height * new_width / width)
img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)

#  Hthị ảnh gốc
cv2.imshow("Original Image", img)

#  Chuyển sang ảnh xám
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Image", gray)

# Làm mờ để giảm nhiễu
gray_blur = cv2.medianBlur(gray, 5)
cv2.imshow("Blurred Grayscale", gray_blur)

# Phát hiện cạnh
edges = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
cv2.imshow("Edges", edges)

# Làm mịn màu
color = cv2.bilateralFilter(img, 9, 300, 300)
cv2.imshow("Bilateral Filter Color", color)

# Kết hợp ảnh màu với cạnh
cartoon = cv2.bitwise_and(color, color, mask=edges)
cv2.imshow("Cartoon Image", cartoon)

# Lưu ảnh kết quả
cv2.imwrite('cartoon_output.jpg', cartoon)

# Chờ người dùng nhấn phím để đóng tất cả cửa sổ
cv2.waitKey(0)
cv2.destroyAllWindows()