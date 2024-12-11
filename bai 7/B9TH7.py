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

def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            print(f"Số dòng trong tệp: {len(lines)}")
    except FileNotFoundError:
        print(f"Không tìm thấy file: {file_path}")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

def copy_file_content(source_path, destination_path):
    try:
        with open(source_path, 'r', encoding='utf-8') as source_file:
            content = source_file.read()
        with open(destination_path, 'w', encoding='utf-8') as destination_file:
            destination_file.write(content)
        print(f"Đã sao chép nội dung từ {source_path} sang {destination_path} thành công.")
    except FileNotFoundError:
        print(f"Không tìm thấy file: {source_path}")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

if __name__ == "__main__":
    file_path = input("Nhập đường dẫn tới file cần đọc: ")
    try:
        n = int(input("Nhập số dòng cần đọc: "))
        if n <= 0:
            print("Số dòng phải là một số nguyên dương.")
        else:
            choice = input("Bạn muốn đọc dòng đầu (nhập 'dau'), dòng cuối (nhập 'cuoi'), đếm số dòng (nhập 'dem'), hay sao chép file (nhập 'sao chep')? ").strip().lower()
            if choice == 'dau':
                read_first_n_lines(file_path, n)
            elif choice == 'cuoi':
                read_last_n_lines(file_path, n)
            elif choice == 'dem':
                count_lines_in_file(file_path)
            elif choice == 'sao chep':
                destination_path = input("Nhập đường dẫn tới file đích: ")
                copy_file_content(file_path, destination_path)
            else:
                print("Lựa chọn không hợp lệ.")
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ.")

