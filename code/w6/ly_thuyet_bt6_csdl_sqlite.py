import sqlite3

# Kết nối đến cơ sở dữ liệu (tạo mới nếu chưa tồn tại)
conn = sqlite3.connect('lop_L12.db')
cursor = conn.cursor()

# Tạo bảng
cursor.execute('''CREATE TABLE IF NOT EXISTS sinh_vien_L12 (id INTEGER PRIMARY KEY, ten TEXT, tuoi INTEGER)''')

# Chèn dữ liệu
cursor.execute("INSERT INTO sinh_vien_L12 (ten, tuoi) VALUES (?, ?)", ('Le Thi Son', 21))

# Lưu thay đổi và đóng kết nối
conn.commit()
conn.close()