import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from scipy.optimize import curve_fit
import numpy as np

# Bước 1: Nhập dữ liệu
url = 'gdp.csv'
df = pd.read_csv(url)

# Hiển thị thông tin cơ bản
print(df.head())
print(df.info())

# Bước 2: Xử lý dữ liệu
# Chọn dữ liệu từ năm 2000 trở đi
df = df[df['Year'] >= 2000]

# Loại bỏ các hàng có giá trị GDP thiếu
df = df.dropna(subset=['Value'])

# Lựa chọn một số quốc gia để phân tích (ví dụ: Hoa Kỳ, Trung Quốc, Đức, Ấn Độ, Brazil)
countries = ['United States', 'China', 'Germany', 'India', 'Brazil']
df_countries = df[df['Country Name'].isin(countries)]

# Bước 3: Phân tích dữ liệu
# Tính tăng trưởng GDP hàng năm cho từng quốc gia
df_countries['GDP Growth'] = df_countries.groupby('Country Name')['Value'].pct_change() * 100

# Bước 4: Trực quan hóa
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

# Bước 5: Dự báo GDP (ví dụ với hồi quy tuyến tính cho Hoa Kỳ)
usa_data = df_countries[df_countries['Country Name'] == 'United States']

# Xây dựng biến số cho hồi quy
X = usa_data['Year'].values
Y = usa_data['Value'].values

# Hồi quy tuyến tính
slope, intercept, r_value, p_value, std_err = stats.linregress(X, Y)

# Hàm hồi quy
def linear_model(x, slope, intercept):
    return slope * x + intercept

# Dự báo trong 5 năm tới
future_years = np.array([2024, 2025, 2026, 2027, 2028])
future_gdp = linear_model(future_years, slope, intercept)

# Trực quan hóa dự báo
plt.figure(figsize=(12,6))
plt.plot(X, Y, marker='o', label='Thực Tế')
plt.plot(future_years, future_gdp, marker='x', linestyle='--', label='Dự Báo')
plt.title('Dự Báo GDP của Hoa Kỳ (2000 - 2028)')
plt.xlabel('Năm')
plt.ylabel('GDP (USD)')
plt.legend()
plt.grid(True)
plt.show()

# Hiển thị dự báo
forecast_df = pd.DataFrame({
    'Year': future_years,
    'Forecast GDP (USD)': future_gdp
})
print(forecast_df)
