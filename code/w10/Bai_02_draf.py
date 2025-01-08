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


# 4:
# Truc quan hoa du lieu
df_VN = df_countries[df_countries['Country Name'] == 'Viet Nam']
plt.figure(figsize=(12, 6))
plt.plot(df_VN['Year'], df_VN['Value'])
#plt.title("So sanh GDB cac quoc gia")
#plt.xlabel("Nam")
#plt.ylabel("GDP")
#plt.grid(True)
plt.show()
