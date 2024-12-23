# Tạo từ điển để lưu thông tin sinh viên
students = {
    "SV001": {"name": "Nguyen Van A", "age": 20, "average_score": 8.5},
    "SV002": {"name": "Tran Thi B", "age": 21, "average_score": 7.8},
    "SV003": {"name": "Le Van C", "age": 19, "average_score": 9.0},
}

# Thêm một sinh viên mới
students["SV004"] = {"name": "Pham Thi D", "age": 22, "average_score": 8.2}

# Cập nhật điểm trung bình của sinh viên "SV002"
students["SV002"]["average_score"] = 8.0

# Xóa thông tin sinh viên "SV001"
del students["SV001"]

# In toàn bộ thông tin sinh viên
print(students)

for item in students:
    print(students[item])