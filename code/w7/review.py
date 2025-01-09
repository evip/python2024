class MonHoc:
    def __init__(self, ten, so_tin_chi, hocky, diem=None):
        self.ten = ten
        self.so_tin_chi = so_tin_chi
        self.hocky = hocky
        self.diem = diem

class SinhVien:
    def __init__(self, ten):
        self.ten = ten
        self.danh_sach_mon = {}  # Dictionary: {hocky: [MonHoc, MonHoc, ...]}

    def them_mon_hoc(self, mon):
        self.danh_sach_mon[mon.hocky].append(mon)
        print(f"Đã thêm môn {mon.ten} vào học kỳ {mon.hocky}.")

    def cap_nhat_diem(self, ten_mon, hocky, diem):
        if hocky in self.danh_sach_mon:
            for mon in self.danh_sach_mon[hocky]:
                if mon.ten == ten_mon:
                    mon.diem = diem
                    print(f"Cập nhật điểm cho môn {ten_mon} trong học kỳ {hocky} thành {diem}.")
                    return
        print(f"Không tìm thấy môn {ten_mon} trong học kỳ {hocky} để cập nhật điểm.")

    def in_danh_sach_mon_hoc_trong_hoc_ky(self, hocky):

        if hocky not in self.danh_sach_mon or not self.danh_sach_mon[hocky]:
            print(f"Không có môn học nào trong học kỳ {hocky} của sinh viên {self.ten}.")
            return
        print(f"Danh sách môn học trong học kỳ {hocky} của sinh viên {self.ten}:")
        for mon in self.danh_sach_mon[hocky]:
            print(mon)

    def in_diem_trung_binh_trong_hoc_ky(self, hocky):
        diem_co_dinh = [mon.diem for mon in self.danh_sach_mon[hocky] if mon.diem is not None]
        if not diem_co_dinh:
            print(f"Chưa có điểm nào trong học kỳ {hocky} để tính trung bình.")
            return
        tong = sum(diem_co_dinh)
        tb = tong / len(diem_co_dinh)
        print(f"Điểm trung bình của {self.ten} trong học kỳ {hocky}: {tb:.2f}")
