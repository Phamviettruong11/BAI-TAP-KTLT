print("PHAM VIET TRUONG MSV:235752021610101")
def count_lines(fname):
    with open(fname, 'r', encoding='utf-8') as f:
        line_count = sum(1 for line in f)
    return line_count
print("Số dòng trong tệp là:", count_lines('D:/a.txt'))
#cách này hiệu quả hơn khi với tệp lớn
