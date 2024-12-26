# Bài tập: Tính Tổng Lãi Suất Gộp Cho Khoản Đầu Tư Theo Thời Gian

# Nhập dữ liệu từ người dùng
P = float(input("Nhap so tien dau tu ban dau: "))
r = float(input("Nhap lai suat hang nam, vi du 6% thi nhap 0.06: "))
t = int(input("Nhap so nam dau tu: "))
C = float(input("Nhap so tien them vao hang thang: "))
n = int(input("Nhap so lan gop lai moi nam, vi du gop lai hang thang thi nhap 12: "))

# Tính số tháng và lãi suất mỗi kỳ
total_thang = t * n
lai_per_thang = r / n

# Khởi tạo tổng số tiền với số tiền đầu tư ban đầu
A = P

# Vòng lặp tính lãi và thêm tiền mỗi kỳ
for month in range(1, total_thang + 1):
    # Tính lãi cho kỳ hiện tại
    interest = A * lai_per_thang
    A += interest
    # Thêm khoản tiền vào sau khi đã tính lãi
    A += C
    
    # (Tùy chọn) In thông tin từng tháng
    # print(f"Tháng {month}: Số tiền = {A:,.2f} VND")

# In kết quả cuối cùng
print(f"\nTổng số tiền sau {t} năm là: {A:,.2f} VND")
