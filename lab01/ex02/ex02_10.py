def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]  
input_str = input("Nhập vào chuỗi cần đảo ngược: ")
print("Chuỗi sau khi đảo ngược là:", dao_nguoc_chuoi(input_str))
