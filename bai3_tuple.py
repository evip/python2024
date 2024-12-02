# Tạo tuple
location = (10.762622, 106.660172)

# Truy cập phần tử
latitude = location[0]
longitude = location[1]

# Kiểm tra tuple
print(latitude, longitude)  # Output: 10.762622 106.660172

# Lỗi khi thay đổi giá trị
# location[0] = 11.0  # Sẽ gây lỗi TypeError
print(location[0])