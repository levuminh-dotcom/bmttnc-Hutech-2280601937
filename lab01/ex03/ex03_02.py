def dao_nguoc_list(lst):
    return lst[::-1]
input_list = input("Nhập list so cần đảo ngược (cacsh bằng dấu [,]): ")
number = list(map(int, input_list.split(',')))
print("List sau khi đảo ngược là:", dao_nguoc_list(number))