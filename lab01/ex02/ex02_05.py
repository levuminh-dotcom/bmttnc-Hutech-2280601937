so_gio_lam = float(input("Nhập số giờ làm mỗi tuần: "))
luong_gio = float(input("Nhập thù lao trên mỗi giờ làm tiêu chuẩn: "))
Gio_tieu_chuan = 44
Gio_vuot_chuan = max(0, so_gio_lam - Gio_tieu_chuan)
thuc_tinh = Gio_tieu_chuan * luong_gio + Gio_vuot_chuan * luong_gio * 1.5
print(f"Số tiền thực lĩnh của nhân viên", {thuc_tinh})