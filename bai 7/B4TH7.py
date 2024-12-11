print("PHAM VIET TRUONG MSV:235752021610101")
def read_first_n_lines(file_path, n):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            print(f"Đọc {n} dòng đầu tiên của tệp:")
            for i in range(n):
                line = file.readline()
                if not line:
                    break
                print(line, end='')
    except FileNotFoundError:
        print(f"Không tìm thấy file: {file_path}")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

if __name__ == "__main__":
    file_path = input("Nhập đường dẫn tới file cần đọc: ")
    try:
        n = int(input("Nhập số dòng cần đọc: "))
        if n <= 0:
            print("Số dòng phải là một số nguyên dương.")
        else:
            read_first_n_lines(file_path, n)
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ.")

