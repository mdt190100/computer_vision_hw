import numpy as np
import cv2
import matplotlib.pyplot as plt

# ======== 1. Tọa độ thế giới (3D) và ảnh (2D) ========
world_points = np.array([
    [0, 0, 0],
    [0, 100, 0],
    [100, 100, 0],
    [100, 0, 0]
], dtype=np.float32)

image_points = np.array([
    [150, 150],
    [150, 250],
    [250, 250],
    [250, 150]
], dtype=np.float32)

# ======== 2. Ma trận nội suy camera ========
K = np.array([
    [800, 0, 200],
    [0, 800, 150],
    [0,   0,   1]
], dtype=np.float32)

# ======== 3. Tính toán R và t bằng solvePnP ========
success, rvec, tvec = cv2.solvePnP(world_points, image_points, K, None)
R_matrix, _ = cv2.Rodrigues(rvec)

print("=== Rotation Matrix R ===")
print(R_matrix)
print("\n=== Translation Vector t ===")
print(tvec)

# ======== 4. Chiếu lại điểm vào ảnh ========
projected_points, _ = cv2.projectPoints(world_points, rvec, tvec, K, None)

print("\n=== Projected 2D Points ===")
print(projected_points.reshape(-1, 2))

# ======== 5. Vẽ ảnh minh họa kết quả ========
image = np.ones((400, 400, 3), dtype=np.uint8) * 255

for pt in projected_points.reshape(-1, 2):
    cv2.circle(image, tuple(pt.astype(int)), 5, (0, 0, 255), -1)  # đỏ: kết quả chiếu

for pt in image_points:
    cv2.circle(image, tuple(pt.astype(int)), 3, (0, 255, 0), -1)  # xanh: ground truth

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Red: Projected Points | Green: Ground Truth")
plt.axis("off")
plt.show()

