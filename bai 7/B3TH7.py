print("PHAM VIET TRUONG MSV:235752021610101")
def read_entire_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            print("Nội dung tệp:")
            print(content)
    except FileNotFoundError:
        print(f"Không tìm thấy file: {file_path}")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
if __name__ == "__main__":
    file_path = input("Nhập đường dẫn tới file cần đọc: ")
    read_entire_file(file_path)

