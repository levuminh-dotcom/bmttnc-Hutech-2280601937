def tao_tupple_tu_list(lst):
    return tuple(lst)
input_list = input("Nhập list so cần chuyển thành tuple (cach bằng dấu [,]): ")
number = list(map(int, input_list.split(',')))
print("List ban đầu là:", number)
print("Tuple sau khi chuyển là:", tao_tupple_tu_list(number))