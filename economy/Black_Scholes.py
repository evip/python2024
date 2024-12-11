import numpy as np
import matplotlib.pyplot as plt

# Tham số ban đầu
S0 = 100      # Giá cổ phiếu ban đầu
T = 20        # Số năm đầu tư
r = 0.07      # Tỷ suất tăng trưởng trung bình (7%/năm)
sigma = 0.2   # Độ biến động giá cổ phiếu (20%)
time_steps = T  # Số bước thời gian (20 năm)

# Khởi tạo danh sách lưu giá cổ phiếu
price_path = [S0]

# Mô phỏng giá cổ phiếu theo từng bước thời gian
for t in range(1, time_steps + 1):
    Z = np.random.normal(0, 1)  # Sinh một số ngẫu nhiên
    next_price = price_path[-1] * np.exp((r - 0.5 * sigma**2) + sigma * Z)
    price_path.append(next_price)

# Vẽ đồ thị
plt.plot(range(time_steps + 1), price_path, color="blue", lw=2)
plt.title("Mô phỏng giá cổ phiếu trong 20 năm (N=1)")
plt.xlabel("Năm")
plt.ylabel("Giá cổ phiếu")
plt.grid(True)
plt.show()

