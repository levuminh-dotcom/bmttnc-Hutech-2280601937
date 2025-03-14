def dem_so_lan_xuat_hien(lst):
    dict = {}
    for item in lst:
        if item in dict:
            dict[item] += 1
        else:
            dict[item] = 1
    return dict
input_str=input("Nhập 1 chuỗi: ")
words = input_str.split()
so_lan_xuat_hien = dem_so_lan_xuat_hien(words)
print("Số lần xuất hiện của các ký tự trong chuỗi: ", so_lan_xuat_hien)