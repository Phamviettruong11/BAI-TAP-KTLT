print("PHAM VIET TRUONG MSV:235752021610101")
def write_list_to_file(fname, data):
    with open(fname, 'w', encoding='utf-8') as f:
        f.writelines([item + '\n' for item in data])
data = ["Dòng 1", "Dòng 2", "Dòng 3"]
write_list_to_file('output.txt', data)
''' dùng writelines(): Tạo một danh sách mới với 
mỗi phần tử có thêm ký tự xuống dòng (\n) và ghi tất 
cả vào tệp cùng một lúc. Đây là cách hiệu quả khi muốn 
ghi tất cả phần tử vào tệp trong một thao tác.'''
