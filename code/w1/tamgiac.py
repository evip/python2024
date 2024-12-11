import math

a = float(input("Nhập độ dài cạnh a: "))
b = float(input("Nhập độ dài cạnh b: "))
c = float(input("Nhập độ dài cạnh c: "))

chu_vi = a + b + c

print(chu_vi)

p = chu_vi / 2  # Nửa chu vi
bieu_thuc = p * (p - a) * (p - b) * (p - c)
s = bieu_thuc**(1/2)

print(chu_vi)
print(s)