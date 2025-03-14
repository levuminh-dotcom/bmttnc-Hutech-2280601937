def chia_het_cho_5(so_nhi_phan):
    so_Thap_phan = int(so_nhi_phan, 2)  # Chuyển số nhị phân thành số thập phân
    return so_Thap_phan % 5 == 0  # Trả về True nếu chia hết cho 5

# Nhập danh sách số nhị phân từ người dùng
chuoi_so_nhi_phan = input("Nhập vào chuỗi số nhị phân (phân tách bởi dấu phẩy): ")

# Chia chuỗi thành danh sách các số nhị phân (loại bỏ khoảng trắng dư thừa)
so_nhi_phan_list = [so.strip() for so in chuoi_so_nhi_phan.split(',')]

# Lọc ra các số nhị phân chia hết cho 5
so_chia_cho_5 = [so for so in so_nhi_phan_list if chia_het_cho_5(so)]

# In kết quả
if so_chia_cho_5:  # Kiểm tra list có phần tử không
    ket_qua = ', '.join(so_chia_cho_5)
    print("Các số nhị phân chia hết cho 5 là:", ket_qua)
else:
    print("Không có số nào chia hết cho 5.")
