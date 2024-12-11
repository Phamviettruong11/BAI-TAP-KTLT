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

def read_last_n_lines(file_path, n):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            print(f"Đọc {n} dòng cuối cùng của tệp:")
            for line in lines[-n:]:
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
            choice = input("Bạn muốn đọc dòng đầu (nhập 'dau') hay dòng cuối (nhập 'cuoi')? ").strip().lower()
            if choice == 'dau':
                read_first_n_lines(file_path, n)
            elif choice == 'cuoi':
                read_last_n_lines(file_path, n)
            else:
                print("Lựa chọn không hợp lệ.")
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ.")
