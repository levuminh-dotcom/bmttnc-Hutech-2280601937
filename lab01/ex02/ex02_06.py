input_str = input("Nhập vào x và y: ")
dimensions = [int(x) for x in input_str.split(',')]
rowNUm = dimensions[0]
colNum = dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNUm)]
for row in range(rowNUm):
    for col in range(colNum):
        multilist[row][col] = row * col
print(multilist)