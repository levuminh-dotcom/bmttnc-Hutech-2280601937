def truy_cap_phan_tu(tuple_data):
    first_element = tuple_data[0]
    last_element = tuple_data[-1]
    return first_element, last_element
input_tuple = input("Nhập tuple (cach bằng dấu ,): ")
first , last = truy_cap_phan_tu(tuple(map(int, input_tuple.split(','))))
print("Phần tử đầu tiên là:", first)
print("Phần tử cuối cùng là:", last)