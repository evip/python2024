import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------------------------------
# 1:
# Doc du lieu
url = 'gdp.csv'
df = pd.read_csv(url)

# --------------------------------------------------------------------
# 2:
# Xu ly du lieu
# Chọn dữ liệu từ năm 2000 trở đi
df = df[df['Year'] >= 2000]

# Loại bỏ các hàng có giá trị GDP thiếu
df = df.dropna(subset=['Value'])

# Lựa chọn một số quốc gia để phân tích (ví dụ: Hoa Kỳ, Trung Quốc, Đức, Ấn Độ, Brazil)
#countries = ['United States', 'China', 'Germany', 'India', 'Brazil']
countries = ['United States', 'China', 'Viet Nam']
df_countries = df[df['Country Name'].isin(countries)]


# --------------------------------------------------------------------
# 4:
# Truc quan hoa du lieu
plt.figure(figsize=(12, 6))
for country in countries:
    country_data = df_countries[df_countries['Country Name'] == country]
    plt.plot(country_data['Year'], country_data['Value'], marker='o', label=country)

plt.title('GDP Bình Quân Đầu Người của Một Số Quốc Gia (2000 - 2023)')
plt.xlabel('Năm')
plt.ylabel('GDP (USD)')
plt.legend()
plt.grid(True)
plt.show()
