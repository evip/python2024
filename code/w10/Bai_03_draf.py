import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Bước 1: Nhập dữ liệu
url = 'gdp.csv'
df = pd.read_csv(url)

# Bước 2: Xử lý dữ liệu
# Chọn dữ liệu từ năm 2000 trở đi
df = df[df['Year'] >= 2000]

# Loại bỏ các hàng có giá trị GDP thiếu
df = df.dropna(subset=['Value'])

# Lựa chọn một số quốc gia để phân tích (ví dụ: Hoa Kỳ, Trung Quốc, Đức, Ấn Độ, Brazil)
#countries = ['United States', 'China', 'Germany', 'India', 'Brazil']
countries = ['United States', 'Viet Nam']
df_countries = df[df['Country Name'].isin(countries)]

# Bước 3: Phân tích dữ liệu
# Tính tăng trưởng GDP hàng năm cho từng quốc gia
df_countries = df[df['Country Name']=='United States']
print(df_countries)

# them cot tang giam theo ty le %:
df_countries['Them rate UD'] = df_countries['Value'].pct_change() * 100
print(df_countries)

plt.figure(figsize=(12,6))
plt.plot(df_countries['Year'], df_countries['Them rate UD'])
plt.show()




