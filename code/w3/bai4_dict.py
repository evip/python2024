# Tạo từ điển
product = {
    "id": "SP001",
    "name": "Bút bi",
    "price": 5000,
    "quantity": 100
}

# Truy cập giá trị
print(product["name"])  # Output: Bút bi

# Thêm giá trị mới
product["category"] = "Dụng cụ học tập"

# Cập nhật giá trị
product["price"] = 5500

# Xóa giá trị
del product["quantity"]

# In từ điển
print(product)
