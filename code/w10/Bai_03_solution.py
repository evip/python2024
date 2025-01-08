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
df_countries['GDP Growth'] = df_countries.groupby('Country Name')['Value'].pct_change() * 100

# Bước 4: Trực quan hóa
# Biểu đồ tăng trưởng GDP
plt.figure(figsize=(12, 6))
for country in countries:
    country_data = df_countries[df_countries['Country Name'] == country]
    plt.plot(country_data['Year'], country_data['GDP Growth'], marker='o', label=country)

plt.title('Tỷ Lệ Tăng Trưởng GDP Hàng Năm (2000 - 2023)')
plt.xlabel('Năm')
plt.ylabel('Tỷ Lệ Tăng Trưởng (%)')
plt.legend()
plt.grid(True)
plt.show()

