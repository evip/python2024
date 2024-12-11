# Tạo tập hợp
product_codes = {"SP001", "SP002", "SP003"}

# Thêm phần tử vào tập hợp
product_codes.add("SP004")
print(product_codes)
# Xóa phần tử khỏi tập hợp
product_codes.remove("SP002")

# Kiểm tra phần tử trong tập hợp
print("SP003" in product_codes)  # Output: True
print(product_codes)

# Hợp, giao, hiệu tập hợp
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(set_a | set_b)  # Hợp: {1, 2, 3, 4, 5}
print(set_a & set_b)  # Giao: {3}
print(set_a - set_b)  # Hiệu: {1, 2}
