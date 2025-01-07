class TaiKhoan:
    def __init__(self, ten, so_du_ban_dau):
        self.ten_tk = ten
        self.so_du = so_du_ban_dau

    def nap(self, so_tien):
        self.so_du = self.so_du + so_tien

    def rut(self, so_tien):
        self.so_du = self.so_du - so_tien

    def thong_tin(self):
        print(f"Tai khoan: {self.ten_tk}, so du hien tai: {self.so_du}")

    def tinh_phi(self):
        pass

    def tinh_lai(self):
        pass

class ThanhToan(TaiKhoan):
    def __init__(self, ten, so_du_ban_dau, p_thang=5):
        super().__init__(ten, so_du_ban_dau)
        self.phi_thang = p_thang

    def tinh_phi(self):
        self.so_du = self.so_du - self.phi_thang
        print(f"Tai khoan: {self.ten_tk} vua tru phi: {self.phi_thang}")
                
    def tinh_lai(self):
        pass

class TietKiem(TaiKhoan):
    def __init__(self, ten, so_du_ban_dau, lai_nam):
        super().__init__(ten, so_du_ban_dau)
        self.lai = lai_nam

    def tinh_phi(self):
        pass

    def tinh_lai(self):
        them = self.so_du * ((self.lai / 100)/12)
        self.so_du = self.so_du + them
        print(f"Tai khoan: {self.ten_tk}, vua cong don lai: {them}")


tk_tt = ThanhToan("Thanh toan", 2000, 5)
tk_tt.rut(500)
tk_tt.nap(100)
tk_tt.nap(100)
tk_tt.tinh_phi()
tk_tt.thong_tin()


tk_tk = TietKiem("Tiet kiem", 2000, 8)
tk_tk.nap(1000)
tk_tk.tinh_lai()
tk_tk.thong_tin()