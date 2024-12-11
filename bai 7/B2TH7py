def read_and_reverse_file (file_path) :
    try:
        with open (file_path, 'r') as file:
            lines = file. readlines ()
            reversed_lines - lines[::-1]
            for line in reversed_lines:
                print (line, end='')
    except FileNotFoundError:
         print (f"Không tim thảy file: (file_path)")
    except Exception as e:
         print (f"Đã xảy ra lỗi: (e)")
file_path = input ("Nhập đường dẫn tới file: ")
read_and_reverse_file (file_path)
