print ("Sinh vien:PHAM VIET TRUONG MSV:235752021610101")

binary_numbers = input("Nhập chuỗi các số nhị phân 4 chữ số, phân tách bởi dấu phẩy: ")
binary_list = binary_numbers.split(',')
result = []
for binary in binary_list:
    decimal_value = int(binary, 2)
    if decimal_value % 5 == 0:
        result.append(binary)
print(",".join(result))
