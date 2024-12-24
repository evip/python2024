# Đây là bài tập kiểm tra.
# Yêu cầu:
# - đọc dữ liệu từ tệp tin: data_input.txt
# - tính tổng tất cả các số trong tập tin.

with open("data_input.txt", "r") as dl:
    sum_data = 0
    for li in dl:
        li = li.strip()
        li_split = li.split()
        li_int = [int(i) for i in li_split]
        sum_data = sum_data + sum(li_int)
    print("tong la: ", sum_data)